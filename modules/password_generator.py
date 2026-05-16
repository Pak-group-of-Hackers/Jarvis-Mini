import secrets
import string
from rich.console import Console

console = Console()


def password_generator():
    length = int(input("Password Length: "))

    chars = string.ascii_letters + string.digits + "!@#$%^&*()"

    password = ''.join(secrets.choice(chars) for _ in range(length))

    console.print(f"[green][Jarvis]: Generated Password:[/green] {password}")