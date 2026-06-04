import time
import psutil

print("--- SYSTEM ENGINE ONLINE ---")

for i in range(1, 6):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    print(f"Packet {i} | CPU: {cpu}% | RAM: {memory}%")

