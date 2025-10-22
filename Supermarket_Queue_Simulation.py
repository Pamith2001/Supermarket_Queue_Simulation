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

# --- 3. Setup (Customer Generator) ---
def setup(env, num_cashiers, avg_service_time, avg_arrival_interval):
    """
    This process sets up the environment and generates customers.
    """
    # cashier resource represents the group of checkout counters
    cashiers = simpy.Resource(env, capacity=num_cashiers)

    customer_id = 0
    # Keep generating customers while the simulation runs
    while True:
        # Simulate realistic arrival intervals 
        # We use an exponential distribution (Poisson process)
        yield env.timeout(random.expovariate(1.0 / avg_arrival_interval))
        
        customer_id += 1
        # Start the 'customer' process for the new arrival
        env.process(customer(env, f'Customer {customer_id}', cashiers))

# --- 4. Run the Simulation ---
print(f'--- Supermarket Queue Simulation ---')
print(f'Parameters:')
print(f'  Cashiers: {NUM_CASHIERS}')
print(f'  Avg. Arrival Interval: {AVG_ARRIVAL_INTERVAL} min')
print(f'  Avg. Service Time: {AVG_SERVICE_TIME} min')
print(f'  Simulation Time: {SIM_TIME} min')
print('--------------------------------------')
print('Running simulation...')

# Set the random seed
random.seed(RANDOM_SEED)

# Create a SimPy environment
env = simpy.Environment()

# Start the setup process
env.process(setup(env, NUM_CASHIERS, AVG_SERVICE_TIME, AVG_ARRIVAL_INTERVAL))

# Run the simulation
env.run(until=SIM_TIME)

# --- 5. Analyze and Print Results ---
print('--------------------------------------')
print(f'Simulation finished at {env.now:.2f} minutes.')

if wait_times:
    avg_wait = statistics.mean(wait_times)
    max_wait = max(wait_times)
    total_customers = len(wait_times)
    
    print(f'Total customers served: {total_customers}')
    print(f'Average wait time: {avg_wait:.2f} minutes')
    print(f'Maximum wait time: {max_wait:.2f} minutes')
else:
    print('No customers were served in the simulation time.')