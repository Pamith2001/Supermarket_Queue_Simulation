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

# --- 2. Customer Process ---
def customer(env, name, cashiers):
   
    arrival_time = env.now
    # print(f'{name} arrives at {arrival_time:.2f}')

    # Request a cashier (a resource)
    with cashiers.request() as req:
        # Wait in the queue until a cashier is free
        yield req
        
        # We have a cashier! Record wait time.
        service_start_time = env.now
        wait = service_start_time - arrival_time
        wait_times.append(wait)
        # print(f'{name} starts service at {service_start_time:.2f} (waited {wait:.2f})')

        # Simulate realistic service time 
        # We use an exponential distribution for service time
        service_duration = random.expovariate(1.0 / AVG_SERVICE_TIME)
        yield env.timeout(service_duration)
        
        # print(f'{name} leaves at {env.now:.2f}')


