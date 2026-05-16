import subprocess
import platform
from rich.console import Console

console = Console()

def ping_test():
    target = input("Enter IP or Domain: ")

    param = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        result = subprocess.run(
            ["ping", param, "4", target],
            capture_output=True,
            text=True
        )

        console.print(result.stdout)

    except Exception as e:
        console.print(f"[red]{e}[/red]")