import timeit
import sys
import cProfile
import numpy as np
from prettytable import PrettyTable
import memory_profiler
import psutil

print(f"System Recursion Limit: {sys.getrecursionlimit()}")

# Define the functions
def for_loop(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

def list_comprehension(n):
    return [i * i for i in range(n)]

def using_map(n):
    return list(map(lambda i: i * i, range(n)))

def generator_expression(n):
    return list(i * i for i in range(n))

def using_numpy(n):
    return (np.arange(n) * np.arange(n)).tolist()

def set_comprehension(n):
    return {i * i for i in range(n)}

def dict_comprehension(n):
    return {i: i * i for i in range(n)}

def recursive_function(n, i=0, acc=None):
    if acc is None:
        acc = []
    if i == n:
        return acc
    return recursive_function(n, i + 1, acc + [i * i])

def using_zip(n):
    return [x * y for x, y in zip(range(n), range(n))]

# Define methods with recursive flag
methods = {
    'For Loop': {'func': for_loop, 'recursive': False},
    'List Comprehension': {'func': list_comprehension, 'recursive': False},
    'Using Map': {'func': using_map, 'recursive': False},
    'Generator Expression': {'func': generator_expression, 'recursive': False},
    'Using NumPy': {'func': using_numpy, 'recursive': False},
    'Set Comprehension': {'func': set_comprehension, 'recursive': False},
    'Dictionary Comprehension': {'func': dict_comprehension, 'recursive': False},
    'Recursive Function': {'func': recursive_function, 'recursive': True},
    'Using Zip': {'func': using_zip, 'recursive': False},
}

# Initialize table
table = PrettyTable()
table.field_names = ["Method", "Samples", "Repeats", "Time (ms)", "Memory (Bytes)", "Avg CPU (%)", "Recursive"]

# Define sample sizes and repeat counts to test
sample_sizes = [10000]
repeat_counts = [100,1000]

results = []

recursion_limit = sys.getrecursionlimit()
safety_margin = recursion_limit - 50

# Initialize a list to hold the string representations of the tables
tables = []

# Compare methods and store tables' string representations for each sample size
for n in sample_sizes:
    for r in repeat_counts:
        for name, method_info in methods.items():
            method = method_info['func']
            is_recursive = method_info['recursive']
            
            if is_recursive and n > (recursion_limit - safety_margin):
                print(f"Skipped {name} with {n} samples and {r} repeats due to recursion limit.")
                continue  # Skip recursive function for large n
                
            profiler = cProfile.Profile()
            profiler.enable()
            
            cpu_percentages = []
            for _ in range(r):
                start_time = timeit.default_timer()
                _ = method(n)
                elapsed = (timeit.default_timer() - start_time) * 1e3  # Convert to milliseconds
                cpu_percent = psutil.cpu_percent(interval=elapsed / 1e3)  # Convert back to seconds for interval
                cpu_percentages.append(cpu_percent)
            
            avg_cpu_percent = sum(cpu_percentages) / len(cpu_percentages)
            
            profiler.disable()
            profiler.print_stats(sort='cumtime')
            
            mem_before = memory_profiler.memory_usage()[0] * (2**20)  # Convert to Bytes
            _ = method(n)
            mem_after = memory_profiler.memory_usage()[0] * (2**20)  # Convert to Bytes
            mem_usage = mem_after - mem_before
            
            total_time = sum(cpu_percentages) / 100 * r * 1e3  # Calculate total time in milliseconds
            results.append([name, n, r, total_time, mem_usage, avg_cpu_percent, is_recursive])
            print(f"Completed {name} with {n} samples and {r} repeats.")
    
    results.sort(key=lambda x: x[3])
    for result in results:
        table.add_row([result[0], result[1], result[2], f"{result[3]:.6f}", f"{result[4]:.6f}", f"{result[5]:.2f}", result[6]])
    
    # Store the string representation of the table
    tables.append(f"\nSummary for Sample Size: {n}\n{table}")

# Print all the tables together after all computations are done
print("\nAll Summaries:")
for table_str in tables:
    print(table_str)