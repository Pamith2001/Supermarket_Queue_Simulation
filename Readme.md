# Supermarket Queue Simulation

A simple **event-driven simulation** using the **SimPy** library to model customer arrivals, queueing, and service at multiple cashiers.

---

# Features

- Event-driven simulation using the **SimPy** library  
- Realistic random arrivals and service durations using **exponential distributions**  
- Tracks:
  - Total customers served  
  - Average waiting time  
  - Maximum waiting time  

---

# How It Works

1. **Customers arrive** at random intervals (based on `AVG_ARRIVAL_INTERVAL`).  
2. Each customer **waits in a queue** until a cashier becomes available.  
3. When served, the **service time** is also random (based on `AVG_SERVICE_TIME`).  
4. The simulation runs for a fixed duration (`SIM_TIME`).  
5. After completion, the program prints **key performance metrics**.

---

# How to Run

1. **Install Python 3**  
   Download from [python.org](https://www.python.org/downloads/)

2. **Install SimPy**  
   ```bash
   pip install simpy
