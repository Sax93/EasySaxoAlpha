"""Telemetry/Network data getter for EasySaxo"""
# dont worry, this is only shown to ur terminal and not publicly

import re
import socket
import time
import urllib.request
import uuid

from rich import print

from ..config import easysaxo


class TelemetryData:
    """Telemetry/Network information displayer."""
    @staticmethod
    def getnet():
        try:
            import psutil
            net_io = psutil.net_io_counters()
            print("\n--- Network Traffic Statistics ---")
            print(f"Bytes Sent/Recv: [cyan]{net_io.bytes_sent / (1024**2):.2f} MB[/cyan] / [cyan]{net_io.bytes_recv / (1024**2):.2f} MB[/cyan]")
            print(f"Packets Sent/Recv: [cyan]{net_io.packets_sent}[/cyan] / [cyan]{net_io.packets_recv}[/cyan]")
        except (ImportError, KeyboardInterrupt) as e:
            easysaxo.k_log("11" if isinstance(e, KeyboardInterrupt) else "9")
            print(f"[red]Unable to get network stats: {e}[/red]")

    @staticmethod
    def getupt():
        try:
            import psutil
            uptime = time.time() - psutil.boot_time()
            hrs_val, remainder = divmod(int(uptime), 3600)
            mins, secs = divmod(remainder, 60)
            days, hrs_val = divmod(hrs_val, 24)
            print(f"System Uptime: [magenta]{days}d {hrs_val}h {mins}m {secs}s[/magenta]")
        except (ImportError, KeyboardInterrupt) as e: 
            easysaxo.k_log("11" if isinstance(e, KeyboardInterrupt) else "9")
            print(f"[red]Unable to get uptime: {e}[/red]")

    @staticmethod
    def getip():
        try:
            import psutil
            print("\n--- Network Interfaces & IP Addresses ---")
            for interface, addrs in psutil.net_if_addrs().items():
                print(f"Interface: [yellow]{interface}[/yellow]")
                for addr in addrs:
                    if addr.family == socket.AF_INET: print(f"  IPv4: [green]{addr.address}[/green]")
                    elif addr.family == socket.AF_INET6: print(f"  IPv6: [cyan]{addr.address}[/cyan]")
        except (ImportError, KeyboardInterrupt) as e: 
            easysaxo.k_log("11" if isinstance(e, KeyboardInterrupt) else "9")
            print(f"[red]Unable to get IP address: {e}[/red]")

    @staticmethod
    def getmac():
        mac = ":".join(re.findall("..", f"{uuid.getnode():012x}"))
        print(f"Primary MAC Address: [blue]{mac.upper()}[/blue]")

    @staticmethod
    def getpublicip():
        print("Fetching public IP address...")
        try:
            pub_ip = urllib.request.urlopen("https://api.ipify.org", timeout=4).read().decode("utf-8")
            print(f"Public IP Address: [green]{pub_ip}[/green]")
        except Exception:  # noqa: BLE001
            easysaxo.k_log("10")
            print("Public IP: [red]Unable to fetch public IP.[/red]")

    @staticmethod
    def getnetstats():
        try:
            import psutil
            stats = psutil.net_if_stats()
            print("\n--- Network Adapter Hardware Status ---")
            for nic, stat in stats.items():
                status = "[green]UP[/green]" if stat.isup else "[red]DOWN[/red]"
                print(f"Adapter [yellow]{nic}[/yellow]: Status [{status}] | Speed: {stat.speed}MB | MTU: {stat.mtu}")
        except (ImportError, KeyboardInterrupt) as e: 
            easysaxo.k_log("11" if isinstance(e, KeyboardInterrupt) else "9")
            print(f"[red]Unable to get network status: {e}[/red]")

    @staticmethod
    def getconnections():
        import psutil
        print("\n--- Active Connections (Sample) ---")
        try:
            conns = psutil.net_connections(kind="inet")
            for conn in conns[:10]:
                laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                print(f"Proto: {conn.type.name} | Local: [green]{laddr:<20}[/green] -> Remote: [cyan]{raddr:<20}[/cyan] Status: {conn.status}")
        except (AttributeError, ValueError, KeyboardInterrupt) as e: 
            easysaxo.k_log("11" if isinstance(e, KeyboardInterrupt) else "6")
            print(f"[red]Could not fetch active connections: {e}[/red]")

    @staticmethod
    def speedtest_network():
        try:
            import speedtest
        except ImportError: speedtest = None

        if not speedtest:
            easysaxo.k_log("9")
            print("[yellow]Speedtest package not installed.[/yellow]")
            return
        print("Testing network speed (this may take a few seconds)...")
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            print(f"Download Speed: [green]{st.download() / (1024**2):.2f} Mbps[/green]")
            print(f"Upload Speed: [green]{st.upload() / (1024**2):.2f} Mbps[/green]")
            print(f"Ping: [cyan]{st.results.ping} ms[/cyan]")
        except (ValueError, AttributeError, KeyboardInterrupt) as e: 
            easysaxo.k_log("11" if isinstance(e, KeyboardInterrupt) else "6")
            print(f"[red]Speed test failed: {e}[/red]")

# broo chill i aint stealing ur shi

import json
import os
import platform
import subprocess
import textwrap
import urllib.parse


class TelemetryOperations:
    """Web operator handler set for web operations."""
    @staticmethod
    def resolve_github_url(url: str) -> tuple[str, str]:
        clean_url = url.rstrip("/")
        
        # for std repo: https://github.com/user/repo -> main.zip
        repo_match = re.match(r"^https?://github\.com/([^/]+)/([^/]+)/?$", clean_url)
        if repo_match:
            user, repo = repo_match.groups()
            return f"https://github.com/{user}/{repo}/archive/refs/heads/main.zip", f"{repo}-main.zip"

        # for blob file -> raw contents
        if "/blob/" in clean_url:
            download_url = clean_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            return download_url, download_url.split("/")[-1]

        return url, clean_url.split("/")[-1] or "downloaded_file"  # link fallback

    @staticmethod
    def w_request(url: str, method: str = "GET", payload: dict | None = None, timeout: int = 10, download_path: str | None = None):
        import requests

        if not urllib.parse.urlparse(url).scheme: url = f"https://{url}"

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        
        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                json=payload,
                headers=headers,
                timeout=timeout,
                stream=True  # to handle large files
            )

            status_color = "[green]" if response.ok else "[red]"
            print(f"\n--- Request: [yellow]{method.upper()} {url}[/yellow] ---")
            print(f"Status Code: {status_color}{response.status_code} {response.reason}[/color]")
            
            if not response.ok: return response

            # handle fd mode (file download)
            if download_path:
                print(f"Downloading file to: [cyan]{download_path}[/cyan]...")
                print("[lightblack]Make sure your internet conection is stable.[/lightblack]")
                total_size = int(response.headers.get("content-length", 0))
                downloaded = 0

                with open(download_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)

                if total_size > 0: print(f"[green]Download complete! ({downloaded / (1024**2):.2f} MB)[/green] (check \\downloads)")
                else: print("[green]Download complete! (check \\easysaxo\\downloads)[/green]")
                return response

            # parse text output
            content_type = response.headers.get('content-type', '')
            print(f"Content-Type: [cyan]{content_type}[/cyan]")

            if "application/json" in content_type:
                print("\n[blue]=== JSON Response ===[/blue]")
                try:
                    formatted_json = json.dumps(response.json(), indent=2)
                    print(formatted_json[:1500] + ("\n..." if len(formatted_json) > 1500 else ""))
                except ValueError: 
                    easysaxo.k_log("6")
                    print(response.text[:500])

            elif "text/html" in content_type:
                from bs4 import BeautifulSoup

                soup = BeautifulSoup(response.text, "html.parser")
                title = soup.title.string.strip() if soup.title and soup.title.string else "No Title"
                print(f"Page Title: [lightmagenta]{title}[/lightmagenta]")

                for element in soup(["script", "style", "head", "noscript", "meta", "nav", "footer", "header"]): element.decompose()

                readme_container = soup.find("article", class_="markdown-body")
                target_container = readme_container or soup.find("main") or soup.find("article") or soup.body

                blocks = []
                if target_container:
                    for elem in target_container.find_all(["h1", "h2", "h3", "p", "li"]):
                        text = elem.get_text(strip=True)
                        if not text: continue
                        
                        if elem.name in ["h1", "h2", "h3"]:
                            blocks.append(f"\n[yellow]# {text}[/yellow]")
                        elif elem.name == "li": blocks.append(f"  * {text}")
                        else: blocks.append(textwrap.fill(text, width=80))

                clean_output = "\n".join(blocks) if blocks else soup.get_text(separator="\n", strip=True)
                print("\n[blue]=== Content Preview ===[/blue]\n")
                print(clean_output[:1200] + ("\n..." if len(clean_output) > 1200 else ""))

            else:
                preview = response.text[:500] + ("..." if len(response.text) > 500 else "")
                print(f"\nResponse Preview:\n{preview}")
            
            return response

        except requests.exceptions.Timeout: 
            easysaxo.k_log("7")
            print(f"[red]Request timed out after {timeout} seconds.[/red]")
        except requests.exceptions.ConnectionError: 
            easysaxo.k_log("7")
            print("[red]Failed to connect to host.[/red]")
        except requests.exceptions.RequestException as e: 
            easysaxo.k_log("8")
            print(f"[red]Request failed: {e}. Check if there are any typos in the prompt.[/red]")
        except KeyboardInterrupt: 
            easysaxo.k_log("11")
            print("\n[yellow]Request cancelled.[/yellow]")
            
        return None

    @staticmethod
    def flush_dns():
        try:
            if os.name == 'nt': subprocess.run(["ipconfig", "/flushdns"], check=True, capture_output=True)
            elif platform.system() == 'Darwin':
                subprocess.run(["dscacheutil", "-flushcache"], check=True)
                subprocess.run(["killall", "-HUP", "mDNSResponder"], check=True)
            else: subprocess.run(["resolvectl", "flush-caches"], check=True)
            print("[green]DNS cache flushed successfully.[/green]")
        except Exception as e:  # noqa: BLE001
            easysaxo.k_log("10")
            print(f"[red]Could not flush DNS cache: {e}[/red]")