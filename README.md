# Cloud-Native Telemetry & System Monitoring Engine

A lightweight, production-minded telemetry monitor built to interface directly with host operating system kernels. This engine captures real-time hardware performance logs, stream-buffers data points in an memory cache, executes vectorized rolling mathematical averages, and throws real-time bottleneck alerts.

## 🚀 Key Architectural Features
* **Real-Time Data Streaming**: Leverages kernel-level event listener hooks (`psutil`) to continuously ingest accurate hardware performance parameters without CPU overhead.
* **In-Memory Data Structures**: Dynamically structures unstructured raw system logs inside a dedicated collection array buffer to completely bypass disk latency bottlenecks.
* **Vectorized Streaming Math**: Computes sliding rolling calculation averages on the fly over live streaming analytics windows.
* **Automated Alert Routing**: Integrates threshold evaluation logic to identify anomalous performance levels and instantly log resource utilization spikes.

---

## 💻 Tech Stack & Dependencies
* **Engine Environment**: Optimized for Python 3.12 / 3.14 Development
* **Telemetry Library**: `psutil 7.x` (Direct kernel-level hardware reporting)
* **Core Structures**: Native In-Memory Dynamic Caching Arrays

---

## ⚙️ Installation & Runtime Quickstart

### 1. Initialize System Dependencies
Deploy the hardware abstraction library directly inside your terminal cluster workspace:
```bash
pip install psutil
```

### 2. Execute the Telemetry Pipeline
Launch the real-time engine to begin streaming analytics packets, tracking metrics, and processing mathematical history windows:
```bash
python3 app.py
```

---

## 📊 Live Console Execution Feed
```text
--- ADVANCED TELEMETRY ENGINE ONLINE ---
Packet 01/10 | Current CPU: 20.2% | Rolling Avg: 20.2%
Packet 02/10 | Current CPU: 24.9% | Rolling Avg: 22.5%
Packet 03/10 | Current CPU: 28.6% | Rolling Avg: 24.5%
Packet 04/10 | Current CPU: 25.1% | Rolling Avg: 24.7%
Packet 05/10 | Current CPU: 20.1% | Rolling Avg: 23.7%
...
```

---

## 🛠️ Version Control & Production Workflow
Changes are staged, snapshotted, and automatically published upstream using standardized repository command structures:

```bash
# Stage updated program logic
git add app.py

# Record version checkpoint message
git commit -m "Upgrade pipeline architecture to support in-memory caching buffers"

# Deploy codebase changes to GitHub main pipeline
git push origin main
```
