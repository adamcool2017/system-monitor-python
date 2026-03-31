import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    print(f"CPU Usage: {cpu}% | RAM Usage: {ram}%")