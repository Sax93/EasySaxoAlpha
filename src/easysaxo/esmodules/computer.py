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
from rich import print

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

        print(f"Processor Model: [blue]{platform.processor() or 'Unknown'}[/blue]")
        if cpuinfo:
            try:
                info = cpuinfo.get_cpu_info()
                print(f"Brand: [cyan]{info.get('brand_raw', 'N/A')}[/cyan]")
                print(f"Architecture: [cyan]{info.get('arch', 'N/A')}[/cyan]")
                print(f"L2 Cache: [cyan]{info.get('l2_cache_size', 'N/A')}[/cyan]")
                print(f"L3 Cache: [cyan]{info.get('l3_cache_size', 'N/A')}[/cyan]")
            except (AttributeError, TypeError, ValueError, KeyboardInterrupt) as e: return e

        print(f"Cores: [blue]{psutil.cpu_count(logical=False)}[/blue] Physical | [blue]{psutil.cpu_count(logical=True)}[/blue] Logical")
        try:
            freq = psutil.cpu_freq()
            if freq: print(f"Speed: [blue]{freq.current:.2f} MHz (Min: {freq.min:.2f} MHz, Max: {freq.max:.2f} MHz)[/blue]")
        except (AttributeError, TypeError, ValueError, KeyboardInterrupt) as e: return e

        print(f"Total CPU Usage: [blue]{psutil.cpu_percent(interval=0.0)}[/blue]%")
        print(f"Core Usage: [blue]{psutil.cpu_percent(interval=0.2, percpu=True)}[/blue]%")

    @staticmethod
    def getarch():
        print(f"Architecture: [blue][bold]{platform.architecture()[0]} ({platform.machine()})[/bold][/blue]")
        print(f"Byte Order: [blue]{sys.byteorder.upper()}-endian[/blue]")

    @staticmethod
    def getram():
        try:
            mem = psutil.virtual_memory()
            print(f"Total RAM: [green]{mem.total / (1024**3):.2f} GB[/green]")
            print(f"Available RAM: [green]{mem.available / (1024**3):.2f} GB[/green]")
            print(f"Used RAM: [green]{mem.used / (1024**3):.2f} GB ([/green][blue]{mem.percent}%[/blue][green])[/green]")
            try:
                swap = psutil.swap_memory()
                print(f"Swap Total: [green]{swap.total / (1024**3):.2f} GB[/green]")
                print(f"Swap Used: [green]{swap.used / (1024**3):.2f} GB ([/green][blue]{swap.percent}%[/blue][green])[/green]")
            except RuntimeError: 
                easysaxo.k_log("10")
                print("Swap Memory: [yellow]Unavailable[/yellow]")
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
                        print(f"GPU Name: [red]{gpu.name}[/red]")
                        print(f"  VRAM Total: [red]{gpu.memoryTotal} MB[/red]")
                        print(f"  VRAM Used: [red]{gpu.memoryUsed} MB ([/red][blue]{gpu.memoryUtil*100:.1f}%[/blue][red])[/red]")
                        print(f"  Temperature: [red]{gpu.temperature} °C[/red]")
                    return
            except (ImportError, ValueError, AttributeError, KeyboardInterrupt) as e: return e

        try:
            if os.name == "nt":
                result = subprocess.run(
                    ["powershell", "-Command", "Get-CimInstance Win32_VideoController | Select-Object Name, AdapterRAM, DriverVersion"],
                    capture_output=True, text=True, timeout=5, check=True
                    )
                output = result.stdout.strip()
                if output: print(f"\nGPU Details:\n[red]{output}[/red]\n")
                else: print("GPU: [red]No GPU detected[/red]")
            else:
                result = subprocess.run(["lspci", "-v", "-mm"], capture_output=True, text=True, timeout=5,check=True)
                for line in result.stdout.split("\n"):
                    if "VGA" in line or "Display" in line:
                        print(f"GPU: [red]{line.strip()}[/red]")
                        break
                else: print("GPU: [red]No GPU detected[/red]")
        except (PermissionError, subprocess.CalledProcessError, KeyboardInterrupt): 
            easysaxo.k_log("4")
            print("GPU: [red]Unable to detect GPU[/red]")

    @staticmethod
    def getmotherboard():
        try:
            if os.name == "nt":
                result = subprocess.run(
                    ["powershell", "-Command", "Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product, SerialNumber"],
                    capture_output=True, text=True, timeout=5, check=True)
                print(f"\nMotherboard Info:\n"
                      f"[red]{result.stdout.strip()}[/red]\n")
            else: print("Motherboard: [cyan]Requires root permissions (dmidecode) on Linux/Unix[/cyan]\n")
        except (PermissionError, AttributeError, subprocess.CalledProcessError, KeyboardInterrupt) as e: 
            easysaxo.k_log("4" if isinstance(e, PermissionError) else "11" if isinstance(e, KeyboardInterrupt) else "10")
            print(f"Motherboard: [red]Error fetching motherboard data:\n{e}[/red]")

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

                for p in partitions:
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
                        print(f"Drive [yellow]{partition.mountpoint}[/yellow] ({partition.fstype}): [yellow]{usage.total / (1024**3):.2f} GB[/yellow] Total, [yellow]{usage.free / (1024**3):.2f} GB[/yellow] Free ([magenta]{usage.percent}%[/magenta] Used)")
                    except PermissionError:
                        easysaxo.k_log("4")
                        print(f"Drive [yellow]{partition.mountpoint}[/yellow]: Access denied.")

            try:
                io = psutil.disk_io_counters()
                if io:
                    print(f"\n--- Disk I/O Metrics ---\nRead: [yellow]{io.read_bytes / (1024**2):.2f} MB[/yellow] | Written: [yellow]{io.write_bytes / (1024**2):.2f} MB[/yellow]")
            except (AttributeError, TypeError, ValueError, PermissionError) as e: 
                easysaxo.k_log("10" if not isinstance(e, ValueError or TypeError) else "6" if not isinstance(e, PermissionError) else "4")
                print("[red]Could not fetch disk data.[/red]")
            print("[red]Cancelled disk data fetching.[/red]")
        except (PermissionError, AttributeError, TypeError, ValueError, KeyboardInterrupt) as e: 
            easysaxo.k_log("10" if not isinstance(e, ValueError or TypeError) else "6" if not isinstance(e, PermissionError) else "4")
            print(f"[red]Could not fetch disk data: {e}[/red]")
    
    @staticmethod
    def getbattery():
        try:
            battery = psutil.sensors_battery()
            if battery:
                plugged = "Plugged In" if battery.power_plugged else "On Battery"
                print(f"Battery Charge: [cyan]{battery.percent}%[/cyan] ({plugged})")
                if battery.secsleft not in [psutil.POWER_TIME_UNLIMITED, psutil.POWER_TIME_UNKNOWN]:
                    mins = battery.secsleft // 60
                    print(f"Time Remaining: [cyan]{mins // 60}h {mins % 60}m[/cyan]")
            else: print("Battery: [cyan]No battery detected[/cyan]")
        except (ValueError, AttributeError, KeyboardInterrupt) as e:
            easysaxo.k_log("10" if not isinstance(e, ValueError) else "11" if not isinstance(e, PermissionError) else "4")
            print("Battery: [red]Unable to detect battery status[/red]") # poor

    @staticmethod
    def getos():
        print(f"Operating System: [blue]{platform.system()} {platform.release()}[/blue]")
        print(f"OS Version: [blue]{platform.version()}[/blue]")
        print(f"Full Platform Tag: [blue]{platform.platform()}[/blue]")

    @staticmethod
    def getpythoninfo():
        import locale
        print(f"Python Version: [green]{platform.python_version()} ([green]{platform.python_compiler()})[/green]")
        print(f"Executable Path: [green]{sys.executable}[/green]")
        print(f"Virtual Environment: [green]{'Active' if sys.prefix != sys.base_prefix else 'Inactive'}[/green]")
        loc, enc = locale.getlocale()
        print(f"System Locale: [green]{loc or 'Default'} | Encoding: {enc or 'UTF-8'}[/green]")

    @staticmethod
    def getuserinfo():
        import getpass
        import socket
        print(f"Logged User: [cyan]{getpass.getuser()}[/cyan]")
        print(f"Device Name (Hostname): [cyan]{socket.gethostname()}[/cyan]")

    @staticmethod
    def getenvvars():
        print("\n--- Environment Variables ---")
        for key, value in list(os.environ.items())[:15]: print(f"[magenta]{key}[/magenta]: {value}")
        print(f"... total {len(os.environ)} variables loaded.")

    @staticmethod
    def getinstalledpackages():
        try:
            reqs = subprocess.check_output([sys.executable, "-m", "uv", "pip", "list"])
            print(f"\n[cyan]--- Installed Pip Packages ---[/cyan]\n{reqs.decode('utf-8')}")
        except (PermissionError, AttributeError, subprocess.CalledProcessError, KeyboardInterrupt) as e: 
            easysaxo.k_log("10" if not isinstance(e, PermissionError or KeyboardInterrupt) else "4" if isinstance(e, PermissionError) else "11")
            print(f"[red]Error retrieving installed packages:\n{e}[/red]")

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
                print(f"  PID: {p.info['pid']} | Name: [cyan]{p.info['name']}[/cyan] | CPU: {p.info['cpu_percent']}% | RAM: {p.info['memory_percent']:.2f}%")

class ComputerOper:
    """Computer internal operation handler."""
    @staticmethod
    def shut_down(waittime: int | str | None = None):
        try:
            if isinstance(waittime, str) and waittime.lower() in ["/a", "-c", "cancel", "abort"]:
                if os.name == 'nt': os.system("shutdown /a")
                else: os.system("sudo shutdown -c")
                print("[green]Scheduled shutdown action canceled.[/green]")
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
                print("[green]Scheduled restart action canceled.[/green]")
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
            print(f"[red]Could not lock screen: {e}[/red]")

    @staticmethod
    def clean_temp():
        try:
            temp_dir = os.environ.get("TEMP") if os.name == "nt" else "/tmp"
            if not temp_dir or not os.path.exists(temp_dir):
                easysaxo.k_log("5")
                print("[yellow]Temp directory path not found.[/yellow]")
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
            print(f"[green]Temp Cleanup Done: Cleared {deleted_files} files ({mb_freed:.2f} MB freed).[/green]")
        except KeyboardInterrupt:
            easysaxo.k_log("11")
            print("Flush interrupted.")

    @staticmethod
    def requirements():
        from .lister import SystemList
        print(f"[cyan]{easysaxo.name} {easysaxo.ver} Requirements:[/cyan]\n")
        print(f"Minimum requirements:\n{SystemList.min_req}\n")
        print(f"Recommended requirements:\n{SystemList.rec_req}")
