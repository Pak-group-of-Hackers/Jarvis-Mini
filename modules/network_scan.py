import nmap
from rich.console import Console
from rich.table import Table

console = Console()


def network_scan():
    target = input("Enter IP or Domain: ")

    scanner = nmap.PortScanner()

    try:
        console.print("[cyan][Jarvis]: Scanning target...[/cyan]")

        scanner.scan(target, '1-1000')

        table = Table(title=f"Scan Results - {target}")
        table.add_column("Port")
        table.add_column("State")
        table.add_column("Service")

        for host in scanner.all_hosts():
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()

                for port in ports:
                    state = scanner[host][proto][port]['state']
                    service = scanner[host][proto][port]['name']

                    table.add_row(str(port), state, service)

        console.print(table)

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")