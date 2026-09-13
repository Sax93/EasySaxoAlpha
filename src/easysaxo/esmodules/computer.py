"""Computer data getter for EasySaxo.

Includes:
- ComputerData class
- ComputerOper class
"""

# dark magic, only watching

import ctypes
import os
import platform
import subprocess
import sys

import psutil
from colorama import Fore, Style

from ..config import easysaxo

try:
    from rich.console import Console
    from rich.table import Table
    console = Console()
    RICH_AVAILABLE = True
except ImportError: RICH_AVAILABLE = False

class ComputerData:
    """Computer data/metadata handler."""
    @staticmethod
    def getcpu():
        try:
            import cpuinfo
        except ImportError: cpuinfo = None

        print(f"Processor Model: {Fore.BLUE}{platform.processor() or 'Unknown'}{Style.RESET_ALL}")
        if cpuinfo:
            try:
                info = cpuinfo.get_cpu_info()
                print(f"Brand: {Fore.CYAN}{info.get('brand_raw', 'N/A')}{Style.RESET_ALL}")
                print(f"Architecture: {Fore.CYAN}{info.get('arch', 'N/A')}{Style.RESET_ALL}")
                print(f"L2 Cache: {Fore.CYAN}{info.get('l2_cache_size', 'N/A')}{Style.RESET_ALL}")
                print(f"L3 Cache: {Fore.CYAN}{info.get('l3_cache_size', 'N/A')}{Style.RESET_ALL}")
            except (AttributeError, TypeError, ValueError, KeyboardInterrupt) as e: return e

        print(f"Cores: {Fore.BLUE}{psutil.cpu_count(logical=False)} Physical | {psutil.cpu_count(logical=True)} Logical{Style.RESET_ALL}")
        try:
            freq = psutil.cpu_freq()
            if freq: print(f"Speed: {Fore.BLUE}{freq.current:.2f} MHz (Min: {freq.min:.2f} MHz, Max: {freq.max:.2f} MHz){Style.RESET_ALL}")
        except (AttributeError, TypeError, ValueError, KeyboardInterrupt) as e: return e

        print(f"Total CPU Usage: {Fore.BLUE}{psutil.cpu_percent(interval=0.0)}{Style.RESET_ALL}%")
        print(f"Core Usage: {Fore.BLUE}{psutil.cpu_percent(interval=0.2, percpu=True)}{Style.RESET_ALL}%")

    @staticmethod
    def getarch():
        print(f"Architecture: {Fore.BLUE}{Style.BRIGHT}{platform.architecture()[0]} ({platform.machine()}){Style.RESET_ALL}")
        print(f"Byte Order: {Fore.BLUE}{sys.byteorder.upper()}-endian{Style.RESET_ALL}")

    @staticmethod
    def getram():
        try:
            mem = psutil.virtual_memory()
            print(f"Total RAM: {Fore.GREEN}{mem.total / (1024**3):.2f} GB{Style.RESET_ALL}")
            print(f"Available RAM: {Fore.GREEN}{mem.available / (1024**3):.2f} GB{Style.RESET_ALL}")
            print(f"Used RAM: {Fore.GREEN}{mem.used / (1024**3):.2f} GB ({mem.percent}%){Style.RESET_ALL}")
            try:
                swap = psutil.swap_memory()
                print(f"Swap Total: {Fore.GREEN}{swap.total / (1024**3):.2f} GB{Style.RESET_ALL}")
                print(f"Swap Used: {Fore.GREEN}{swap.used / (1024**3):.2f} GB ({swap.percent}%){Style.RESET_ALL}")
            except RuntimeError: 
                easysaxo.k_log("10")
                print(f"Swap Memory: {Fore.YELLOW}Unavailable{Style.RESET_ALL}")
        except KeyboardInterrupt: 
            easysaxo.k_log("a0")
            return
        
    @staticmethod
    def getgpu():
        try:
            import GPUtil
        except ImportError: GPUtil = None

        if GPUtil:
            try:
                gpus = GPUtil.getGPUs()
                if gpus:
                    for gpu in gpus:
                        print(f"GPU Name: {Fore.RED}{gpu.name}{Style.RESET_ALL}")
                        print(f"  VRAM Total: {Fore.RED}{gpu.memoryTotal} MB{Style.RESET_ALL}")
                        print(f"  VRAM Used: {Fore.RED}{gpu.memoryUsed} MB ({gpu.memoryUtil*100:.1f}%){Style.RESET_ALL}")
                        print(f"  Temperature: {Fore.RED}{gpu.temperature} °C{Style.RESET_ALL}")
                    return
            except (ImportError, ValueError, AttributeError, KeyboardInterrupt) as e: return e

        try:
            if os.name == "nt":
                result = subprocess.run(
                    ["powershell", "-Command", "Get-CimInstance Win32_VideoController | Select-Object Name, AdapterRAM, DriverVersion"],
                    capture_output=True, text=True, timeout=5, check=True
                    )
                output = result.stdout.strip()
                if output: print(f"\nGPU Details:\n{Fore.RED}{output}{Style.RESET_ALL}\n")
                else: print(f"GPU: {Fore.RED}No GPU detected{Style.RESET_ALL}")
            else:
                result = subprocess.run(["lspci", "-v", "-mm"], capture_output=True, text=True, timeout=5,check=True)
                for line in result.stdout.split("\n"):
                    if "VGA" in line or "Display" in line:
                        print(f"GPU: {Fore.RED}{Style.BRIGHT}{line.strip()}{Style.RESET_ALL}")
                        break
                else: print(f"GPU: {Fore.RED}No GPU detected{Style.RESET_ALL}")
        except (PermissionError, subprocess.CalledProcessError, KeyboardInterrupt): 
            easysaxo.k_log("4")
            print(f"GPU: {Fore.RED}Unable to detect GPU{Style.RESET_ALL}")

    @staticmethod
    def getmotherboard():
        try:
            if os.name == "nt":
                result = subprocess.run(
                    ["powershell", "-Command", "Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product, SerialNumber"],
                    capture_output=True, text=True, timeout=5, check=True)
                print(f"\nMotherboard Info:\n"
                      f"{Fore.CYAN}{result.stdout.strip()}{Style.RESET_ALL}\n")
            else: print(f"Motherboard: {Fore.CYAN}Requires root permissions (dmidecode) on Linux/Unix{Style.RESET_ALL}\n")
        except (PermissionError, AttributeError, subprocess.CalledProcessError, KeyboardInterrupt) as e: 
            easysaxo.k_log("4" if isinstance(e, PermissionError) else "11" if isinstance(e, KeyboardInterrupt) else "10")
            print(f"Motherboard: {Fore.RED}Error fetching motherboard data:\n{e}{Style.RESET_ALL}")

    @staticmethod
    def getdisk():
        try:
            partitions = psutil.disk_partitions()

            if RICH_AVAILABLE:
                table = Table(title="Disk Partitions & Usage")
                table.add_column("Drive", style="yellow")
                table.add_column("Type", style="cyan")
                table.add_column("Total", style="green")
                table.add_column("Free", style="green")
                table.add_column("Usage", style="magenta")

                for p in partitions: # bad joke here 
                    try:
                        u = psutil.disk_usage(p.mountpoint)
                        table.add_row(p.mountpoint, p.fstype, f"{u.total / (1024**3):.2f} GB", f"{u.free / (1024**3):.2f} GB", f"{u.percent}%")
                    except PermissionError:
                        table.add_row(p.mountpoint, p.fstype, "Access Denied", "-", "-")
                console.print(table)
            else:
                print("\n--- Disk Partitions & Usage ---")
                for partition in partitions:
                    try:
                        usage = psutil.disk_usage(partition.mountpoint)
                        print(f"Drive {Fore.YELLOW}{partition.mountpoint}{Style.RESET_ALL} ({partition.fstype}): {Fore.YELLOW}{usage.total / (1024**3):.2f} GB{Style.RESET_ALL} Total, {Fore.YELLOW}{usage.free / (1024**3):.2f} GB{Style.RESET_ALL} Free ({usage.percent}% Used)")
                    except PermissionError: 
                        
                        easysaxo.k_log("4")
                        print(f"Drive {Fore.YELLOW}{partition.mountpoint}{Style.RESET_ALL}: Access denied.")

            try:
                io = psutil.disk_io_counters()
                if io:
                    print(f"\n--- Disk I/O Metrics ---\nRead: {Fore.YELLOW}{io.read_bytes / (1024**2):.2f} MB{Style.RESET_ALL} | Written: {Fore.YELLOW}{io.write_bytes / (1024**2):.2f} MB{Style.RESET_ALL}")
            except (AttributeError, TypeError, ValueError, PermissionError) as e: 
                easysaxo.k_log("10" if not isinstance(e, ValueError or TypeError) else "6" if not isinstance(e, PermissionError) else "4")
                print(f"{Fore.RED}Could not fetch disk data.{Style.RESET_ALL}")
        except KeyboardInterrupt: 
            easysaxo.k_log("11")
            print(f"{Fore.RED}Cancelled disk data fetching.{Style.RESET_ALL}")
            
    @staticmethod
    def getbattery():
        try:
            battery = psutil.sensors_battery()
            if battery:
                plugged = "Plugged In" if battery.power_plugged else "On Battery"
                print(f"Battery Charge: {Fore.CYAN}{battery.percent}%{Style.RESET_ALL} ({plugged})")
                if battery.secsleft not in [psutil.POWER_TIME_UNLIMITED, psutil.POWER_TIME_UNKNOWN]:
                    mins = battery.secsleft // 60
                    print(f"Time Remaining: {Fore.CYAN}{mins // 60}h {mins % 60}m{Style.RESET_ALL}")
            else:
                print(f"Battery: {Fore.CYAN}No battery detected{Style.RESET_ALL}")
        except (ValueError, AttributeError, KeyboardInterrupt) as e:
            easysaxo.k_log("10" if not isinstance(e, ValueError) else "11" if not isinstance(e, PermissionError) else "4")
            print(f"Battery: {Fore.RED}Unable to detect battery status{Style.RESET_ALL}") # poor

    @staticmethod
    def getos():
        print(f"Operating System: {Fore.BLUE}{platform.system()} {platform.release()}{Style.RESET_ALL}")
        print(f"OS Version: {Fore.BLUE}{platform.version()}{Style.RESET_ALL}")
        print(f"Full Platform Tag: {Fore.BLUE}{platform.platform()}{Style.RESET_ALL}")
        # unless you barely have a kboard

    @staticmethod
    def getpythoninfo():
        import locale
        print(f"Python Version: {Fore.GREEN}{platform.python_version()} ({platform.python_compiler()}){Style.RESET_ALL}")
        print(f"Executable Path: {Fore.GREEN}{sys.executable}{Style.RESET_ALL}")
        print(f"Virtual Environment: {Fore.GREEN}{'Active' if sys.prefix != sys.base_prefix else 'Inactive'}{Style.RESET_ALL}")
        loc, enc = locale.getlocale()
        print(f"System Locale: {Fore.GREEN}{loc or 'Default'} | Encoding: {enc or 'UTF-8'}{Style.RESET_ALL}")

    @staticmethod
    def getuserinfo():
        import getpass
        import socket
        print(f"Logged User: {Fore.CYAN}{getpass.getuser()}{Style.RESET_ALL}")
        print(f"Device Name (Hostname): {Fore.CYAN}{socket.gethostname()}{Style.RESET_ALL}")

    @staticmethod
    def getenvvars():
        print("\n--- Environment Variables ---")
        for key, value in list(os.environ.items())[:15]:
            print(f"{Fore.MAGENTA}{key}{Style.RESET_ALL}: {value}")
        print(f"... total {len(os.environ)} variables loaded.")

    @staticmethod
    def getinstalledpackages():
        try:
            reqs = subprocess.check_output([sys.executable, "-m", "uv", "pip", "list"])
            print(f"\n{Fore.CYAN}--- Installed Pip Packages ---{Style.RESET_ALL}\n{reqs.decode('utf-8')}")
        except (PermissionError, AttributeError, subprocess.CalledProcessError, KeyboardInterrupt) as e: 
            easysaxo.k_log("10" if not isinstance(e, PermissionError or KeyboardInterrupt) else "4" if isinstance(e, PermissionError) else "11")
            print(f"{Fore.RED}Error retrieving installed packages:\n{e}{Style.RESET_ALL}")

    @staticmethod
    def getprocesses():
        processes = sorted(psutil.process_iter(
            ["pid", "name", "cpu_percent", "memory_percent"]),
                key=lambda p: p.info["cpu_percent"] or 0,
                reverse=True)[:5]

        if RICH_AVAILABLE:
            print()
            table = Table(title="Top 5 CPU Processes")
            table.add_column("PID", style="magenta")
            table.add_column("Name", style="cyan")
            table.add_column("CPU %", style="yellow")
            table.add_column("RAM %", style="green")
            for p in processes:
                table.add_row(str(p.info['pid']), p.info['name'], str(p.info['cpu_percent']), f"{p.info['memory_percent']:.2f}")
            console.print(table)
        else:
            print("\nTop 5 CPU-Consuming Processes:")
            for p in processes:
                print(f"  PID: {p.info['pid']} | Name: {Fore.CYAN}{p.info['name']}{Style.RESET_ALL} | CPU: {p.info['cpu_percent']}% | RAM: {p.info['memory_percent']:.2f}%")

class ComputerOper:
    """Computer internal operation handler."""
    @staticmethod
    def shut_down(waittime: int | str | None = None):
        try:
            if isinstance(waittime, str) and waittime.lower() in ["/a", "-c", "cancel", "abort"]:
                if os.name == 'nt': os.system("shutdown /a")
                else: os.system("sudo shutdown -c")
                print(f"{Fore.GREEN}Scheduled shutdown action canceled.{Style.RESET_ALL}")
                return

            if isinstance(waittime, str) and waittime.isdigit(): waittime = int(waittime)

            print("Shutting down the system...")
            if os.name == 'nt':
                delay = waittime if isinstance(waittime, int) else 0
                os.system(f"shutdown /s /t {delay}")
            else:
                time_arg = f"+{waittime}" if isinstance(waittime, int) and waittime > 0 else "now"
                os.system(f"sudo shutdown -h {time_arg}")

        except (PermissionError, ValueError, KeyboardInterrupt, OSError) as e: 
            easysaxo.k_log("9" if not isinstance(e, KeyboardInterrupt) else "11")
            print(f"Cannot operate over shut down: {e}")

    @staticmethod
    def restart(waittime: int | str | None = None):
        try:
            if isinstance(waittime, str) and waittime.lower() in ["/a", "-c", "cancel", "abort"]: 
                if os.name == 'nt': os.system("shutdown /a")
                else: os.system("sudo shutdown -c")
                print(f"{Fore.GREEN}Scheduled restart action canceled.{Style.RESET_ALL}")
                return
            print("Restarting the system...")
            if os.name == 'nt': os.system(f"shutdown /r /t {waittime if waittime is not None else 0}")
            else:
                try: subprocess.run(["sudo", "reboot"], check=True)
                except subprocess.CalledProcessError: os.system("reboot")
        except (PermissionError, ValueError, KeyboardInterrupt, OSError) as e: 
            easysaxo.k_log("9" if not isinstance(e, KeyboardInterrupt) else "11")
            print(f"Cannot restart: {e}")

    @staticmethod
    def suspend():
        try:
            print("Suspending computer...")
            current_os = platform.system().lower()

            if "windows" in current_os: subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0", "1", "0"], check=True)

            elif "linux" in current_os: subprocess.run(["systemctl", "suspend"], check=True)

            elif "darwin" in current_os: subprocess.run(["pmset", "sleepnow"], check=True)

            else: print(f"Unsupported Operating System: {platform.system()}")
                
        except (subprocess.CalledProcessError, OSError) as e: 
            easysaxo.k_log("9" if not isinstance(e, KeyboardInterrupt) else "11")
            print(f"Failed to suspend the device: {e}")
        except PermissionError: 
            easysaxo.k_log("4")
            print("You may need administrative or root privileges to suspend this device.")
        except KeyboardInterrupt:
            easysaxo.k_log("11")
            print("Suspend cancelled.")

    @staticmethod
    def lock_screen():
        try:
            print("Locking screen...")
            if os.name == 'nt': ctypes.windll.user32.LockWorkStation()
            elif platform.system() == 'Darwin': subprocess.run(["pmset", "displaysleepnow"], check=False)
            else: os.system("xdg-screensaver lock || loginctl lock-session")
        except (PermissionError, KeyboardInterrupt, OSError) as e: 
            easysaxo.k_log("4" if not isinstance(e, KeyboardInterrupt) else "11")
            print(f"{Fore.RED}Could not lock screen: {e}{Style.RESET_ALL}")

    @staticmethod
    def clean_temp():
        try:
            temp_dir = os.environ.get("TEMP") if os.name == "nt" else "/tmp"
            if not temp_dir or not os.path.exists(temp_dir):
                easysaxo.k_log("5")
                print(f"{Fore.YELLOW}Temp directory path not found.{Style.RESET_ALL}")
                return

            deleted_files = 0
            deleted_size = 0

            for root, dirs, files in os.walk(temp_dir):
                for f in files:
                    filepath = os.path.join(root, f)
                    try:
                        size = os.path.getsize(filepath)
                        os.remove(filepath)
                        deleted_files += 1
                        deleted_size += size
                    except (PermissionError, OSError): continue

            mb_freed = deleted_size / (1024 ** 2)
            print(f"{Fore.GREEN}Temp Cleanup Done: Cleared {deleted_files} files ({mb_freed:.2f} MB freed).{Style.RESET_ALL}")
        except KeyboardInterrupt:
            easysaxo.k_log("11")
            print("Flush interrupted.")

    @staticmethod
    def requirements():
        from .lister import SystemList
        print(f"{Fore.CYAN}{easysaxo.name} {easysaxo.ver} Requirements:{Style.RESET_ALL}\n")
        print(f"Minimum requirements:\n{SystemList.min_req}\n")
        print(f"Reccomended requirements:\n{SystemList.rec_req}")
 
                
# note: 8 out of 10 intel celeron inside cpus crash here