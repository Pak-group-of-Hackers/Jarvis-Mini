import psutil
import os

def get_system_stats():
    path = "C:\\" if os.name == "nt" else "/"

    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage(path).percent
    }