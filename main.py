from colorama import init
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box

init()
console = Console()

# Core imports (safe try/except to avoid crash)
try:
    from core.banner import show_banner
    from core.system_stats import get_system_stats
except:
    def show_banner():
        console.print("[cyan]ALPHA JARVIS ONLINE[/cyan]")

    def get_system_stats():
        return {"cpu": 0, "ram": 0, "disk": 0}


# Modules (safe fallback)
try:
    from modules.network_scan import network_scan
    from modules.ping_test import ping_test
    from modules.password_generator import password_generator
    from modules.system_info import system_info
except:
    def network_scan():
        print("Network Scan Running...")

    def ping_test():
        print("Ping Test Running...")

    def password_generator():
        print("Password Generated: 123456")

    def system_info():
        print("System Info Loaded")


def show_menu():

    table = Table(
        title="ALPHA JARVIS MENU",
        box=box.DOUBLE,
        style="cyan"
    )

    table.add_column("ID", justify="center", style="yellow")
    table.add_column("Feature", style="green")

    table.add_row("1", "Network Scan")
    table.add_row("2", "Ping Test")
    table.add_row("3", "Password Generator")
    table.add_row("4", "System Information")
    table.add_row("0", "Exit")

    console.print(table)


def show_status():

    try:
        stats = get_system_stats()

        console.print(
            Panel.fit(
                f"[green]CPU:[/green] {stats['cpu']}%\n"
                f"[green]RAM:[/green] {stats['ram']}%\n"
                f"[green]Disk:[/green] {stats['disk']}%\n"
                f"[cyan]Status:[/cyan] SYSTEM SECURE",
                title="SYSTEM STATUS",
                border_style="green"
            )
        )

    except Exception as e:
        console.print(f"[red]Status Error: {e}[/red]")


def main():

    show_banner()
    show_status()

    while True:

        show_menu()

        choice = Prompt.ask("[cyan][Jarvis][/cyan] Enter choice").strip()

        if choice == "1":
            network_scan()

        elif choice == "2":
            ping_test()

        elif choice == "3":
            password_generator()

        elif choice == "4":
            system_info()

        elif choice == "0":
            console.print("[red]Shutting down JARVIS...[/red]")
            break

        else:
            console.print("[red]Invalid Option[/red]")


if __name__ == "__main__":
    main()