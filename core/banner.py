from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel

console = Console()


def show_banner():
    banner = Figlet(font="slant")
    text = banner.renderText("ALPHA JARVIS")

    console.print(
        Panel.fit(
            f"[green]{text}[/green]\n"
            f"[cyan]OFFLINE AI CYBER ASSISTANT[/cyan]",
            border_style="cyan"
        )
    )