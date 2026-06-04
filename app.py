import time
import psutil

# An in-memory storage array to hold our streaming performance telemetry data
cpu_history = []

print("--- ADVANCED TELEMETRY ENGINE ONLINE ---")

# Running an extended 10-packet loop window to process data statistics
for i in range(1, 11):
    cpu = psutil.cpu_percent(interval=1)
    cpu_history.append(cpu)
    
    # Calculate a rolling mathematical average of our streaming history cache
    average_load = sum(cpu_history) / len(cpu_history)
    print(f"Packet {i:02d}/10 | Current CPU: {cpu:04.1f}% | Rolling Avg: {average_load:04.1f}%")
    
    # Algorithmic check to flag heavy performance bottlenecks on the cloud server
    if cpu > 50.0:
        print("⚠️ ALERT: High System Resource Utilization Detected!")
