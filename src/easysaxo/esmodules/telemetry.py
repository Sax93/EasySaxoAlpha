"""Telemetry Network data getter for EasySaxo"""
# dont worry, this is only shown to ur terminal and not publicly

import re
import socket
import time
import urllib.request
import uuid

from colorama import Fore, Style


class TelemetryData:
    @staticmethod
    def getnet():
        try:
            import psutil
            net_io = psutil.net_io_counters()
            print("\n--- Network Traffic Statistics ---")
            print(f"Bytes Sent/Recv: {Fore.CYAN}{net_io.bytes_sent / (1024**2):.2f} MB{Style.RESET_ALL} / {Fore.CYAN}{net_io.bytes_recv / (1024**2):.2f} MB{Style.RESET_ALL}")
            print(f"Packets Sent/Recv: {Fore.CYAN}{net_io.packets_sent}{Style.RESET_ALL} / {Fore.CYAN}{net_io.packets_recv}{Style.RESET_ALL}")
        except (ImportError, KeyboardInterrupt) as e:
            print(f"{Fore.RED}Unable to get network stats: {e}{Style.RESET_ALL}")

    @staticmethod
    def getupt():
        try:
            import psutil
            uptime = time.time() - psutil.boot_time()
            hrs_val, remainder = divmod(int(uptime), 3600)
            mins, secs = divmod(remainder, 60)
            days, hrs_val = divmod(hrs_val, 24)
            print(f"System Uptime: {Fore.MAGENTA}{days}d {hrs_val}h {mins}m {secs}s{Style.RESET_ALL}")
        except (ImportError, KeyboardInterrupt) as e:
            print(f"{Fore.RED}Unable to get uptime: {e}{Style.RESET_ALL}")

    @staticmethod
    def getip():
        try:
            import psutil
            print("\n--- Network Interfaces & IP Addresses ---")
            for interface, addrs in psutil.net_if_addrs().items():
                print(f"Interface: {Fore.YELLOW}{interface}{Style.RESET_ALL}")
                for addr in addrs:
                    if addr.family == socket.AF_INET: print(f"  IPv4: {Fore.GREEN}{addr.address}{Style.RESET_ALL}")
                    elif addr.family == socket.AF_INET6: print(f"  IPv6: {Fore.CYAN}{addr.address}{Style.RESET_ALL}")
        except (ImportError, KeyboardInterrupt) as e:
            print(f"{Fore.RED}Unable to get IP address: {e}{Style.RESET_ALL}")

    @staticmethod
    def getmac():
        mac = ":".join(re.findall("..", f"{uuid.getnode():012x}"))
        print(f"Primary MAC Address: {Fore.BLUE}{mac.upper()}{Style.RESET_ALL}")

    @staticmethod
    def getpublicip():
        print("Fetching public IP address...")
        try:
            pub_ip = urllib.request.urlopen("https://api.ipify.org", timeout=4).read().decode("utf-8")
            print(f"Public IP Address: {Fore.GREEN}{pub_ip}{Style.RESET_ALL}")
        except (PermissionError, KeyboardInterrupt):
            print(f"Public IP: {Fore.RED}Unable to fetch public IP (Offline or Timeout){Style.RESET_ALL}")

    @staticmethod
    def getnetstats():
        try:
            import psutil
            stats = psutil.net_if_stats()
            print("\n--- Network Adapter Hardware Status ---")
            for nic, stat in stats.items():
                status = f"{Fore.GREEN}UP{Style.RESET_ALL}" if stat.isup else f"{Fore.RED}DOWN{Style.RESET_ALL}"
                print(f"Adapter {Fore.YELLOW}{nic}{Style.RESET_ALL}: Status [{status}] | Speed: {stat.speed}MB | MTU: {stat.mtu}")
        except (ImportError, KeyboardInterrupt) as e:
            print(f"{Fore.RED}Unable to get network status: {e}{Style.RESET_ALL}")

    @staticmethod
    def getconnections():
        import psutil
        print("\n--- Active Connections (Sample) ---")
        try:
            conns = psutil.net_connections(kind="inet")
            for conn in conns[:10]:
                laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                print(f"Proto: {conn.type.name} | Local: {Fore.GREEN}{laddr:<20}{Style.RESET_ALL} -> Remote: {Fore.CYAN}{raddr:<20}{Style.RESET_ALL} Status: {conn.status}")
        except (AttributeError, ValueError, KeyboardInterrupt) as e:
            print(f"{Fore.RED}Could not fetch active connections: {e}{Style.RESET_ALL}")

    @staticmethod
    def speedtest_network():
        try:
            import speedtest
        except ImportError: speedtest = None

        if not speedtest:
            print(f"{Fore.YELLOW}Speedtest package not installed.{Style.RESET_ALL}")
            return
        print("Testing network speed (this may take a few seconds)...")
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            print(f"Download Speed: {Fore.GREEN}{st.download() / (1024**2):.2f} Mbps{Style.RESET_ALL}")
            print(f"Upload Speed: {Fore.GREEN}{st.upload() / (1024**2):.2f} Mbps{Style.RESET_ALL}")
            print(f"Ping: {Fore.CYAN}{st.results.ping} ms{Style.RESET_ALL}")
        except (ValueError, AttributeError, KeyboardInterrupt) as e:
            print(f"{Fore.RED}Speed test failed: {e}{Style.RESET_ALL}")

# broo chill i aint stealing ur shi

import json
import textwrap
import urllib.parse

import requests
from bs4 import BeautifulSoup


class TelemetryOperations:
    @staticmethod
    def w_request(url: str, method: str = "GET", payload: dict | None = None, timeout: int = 5):
        if not urllib.parse.urlparse(url).scheme:
            url = f"https://{url}"

        # Browser-like headers to reduce blocking
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                json=payload,
                headers=headers,
                timeout=timeout
            )

            status_color = Fore.GREEN if response.ok else Fore.RED
            print(f"\n--- Request: {Fore.YELLOW}{method.upper()} {url}{Style.RESET_ALL} ---")
            print(f"Status Code: {status_color}{response.status_code} {response.reason}{Style.RESET_ALL}")
            print(f"Content-Type: {Fore.CYAN}{response.headers.get('content-type', 'N/A')}{Style.RESET_ALL}")

            content_type = response.headers.get('content-type', '')

            if "application/json" in content_type:
                print(f"\n{Fore.BLUE}=== JSON Response ==={Style.RESET_ALL}")
                try:
                    formatted_json = json.dumps(response.json(), indent=2)
                    print(formatted_json[:1500] + ("\n..." if len(formatted_json) > 1500 else ""))
                except ValueError:
                    print(response.text[:500])

            elif "text/html" in content_type:
                soup = BeautifulSoup(response.text, "html.parser")
                
                title = soup.title.string.strip() if soup.title and soup.title.string else "No Title"
                print(f"Page Title: {Fore.LIGHTMAGENTA_EX}{title}{Style.RESET_ALL}")

                # Remove non-content elements
                for element in soup(["script", "style", "head", "noscript", "meta", "nav", "footer", "header"]):
                    element.decompose()

                # Prioritize GitHub README container -> main tag -> article tag -> body
                readme_container = soup.find("article", class_="markdown-body")
                target_container = readme_container or soup.find("main") or soup.find("article") or soup.body

                blocks = []
                if target_container:
                    for elem in target_container.find_all(["h1", "h2", "h3", "p", "li"]):
                        text = elem.get_text(strip=True)
                        if not text:
                            continue
                        
                        # Preserve document structure visually
                        if elem.name in ["h1", "h2", "h3"]:
                            blocks.append(f"\n{Fore.YELLOW}# {text}{Style.RESET_ALL}")
                        elif elem.name == "li":
                            blocks.append(f"  * {text}")
                        else:
                            blocks.append(textwrap.fill(text, width=80))

                clean_output = "\n".join(blocks) if blocks else soup.get_text(separator="\n", strip=True)
                
                print(f"\n{Fore.BLUE}=== Content Preview ==={Style.RESET_ALL}\n")
                print(clean_output[:1200] + ("\n..." if len(clean_output) > 1200 else ""))

            else:
                preview = response.text[:500] + ("..." if len(response.text) > 500 else "")
                print(f"\nResponse Preview:\n{preview}")
            
            return response

        except requests.exceptions.Timeout:
            print(f"{Fore.RED}Request timed out after {timeout} seconds.{Style.RESET_ALL}")
        except requests.exceptions.ConnectionError:
            print(f"{Fore.RED}Failed to connect to host.{Style.RESET_ALL}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}Request failed: {e}{Style.RESET_ALL}")
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Request cancelled.{Style.RESET_ALL}")
            
        return None