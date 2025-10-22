import simpy
import random
import statistics

# --- 1. Simulation Parameters (Input Variation) ---
# These are the "input variations"

RANDOM_SEED = 42          # For reproducible results
NUM_CASHIERS = int(input("Enter number of cashiers: "))          # Number of workers (servers) 
AVG_SERVICE_TIME = 5      # Avg. time a cashier spends with a customer (minutes)
AVG_ARRIVAL_INTERVAL = 2  # Avg. time between customer arrivals (minutes) 
SIM_TIME = 120            # Total simulation time (e.g., 120 minutes = 2 hours)

# This list will store metrics for later analysis 
wait_times = []

