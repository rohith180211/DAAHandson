import time
import random
import platform
import psutil
import matplotlib.pyplot as plt


# System Information
def fetch_system_details():
    sys_details = {
        "Host Name": platform.node(),
        "CPU": platform.processor(),
        "Memory": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "Total Cores": psutil.cpu_count(logical=True),
        "Python Version": platform.python_version()
    }
    return sys_details


# Insertion Sort
def perform_insertion_sort(data):
    length = len(data)
    for index in range(1, length):
        current_value = data[index]
        position = index - 1
        while position >= 0 and current_value < data[position]:
            data[position + 1] = data[position]
            position -= 1
        data[position + 1] = current_value
    return data


# Selection Sort
def perform_selection_sort(data):
    length = len(data)
    for index in range(length):
        minimum_index = index
        for j in range(index + 1, length):
            if data[j] < data[minimum_index]:
                minimum_index = j
        data[index], data[minimum_index] = data[minimum_index], data[index]
    return data


# Bubble Sort
def perform_bubble_sort(data):
    length = len(data)
    for index in range(length):
        for j in range(0, length - index - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


# Benchmarking
def evaluate_sorting_algorithms():
    test_sizes = [3, 15, 25, 75, 150, 250, 600, 1200, 2500, 6000]
    sorting_algorithms = {
        "Insertion Sort": perform_insertion_sort,
        "Selection Sort": perform_selection_sort,
        "Bubble Sort": perform_bubble_sort
    }

    benchmark_results = {alg: [] for alg in sorting_algorithms}

    for size in test_sizes:
        random_data = random.sample(range(size * 10), size)  # Generate a random array of the given size
        for algo_name, sorting_func in sorting_algorithms.items():
            start_time = time.time()
            sorting_func(random_data.copy())  # Run the sorting algorithm
            time_taken = time.time() - start_time
            benchmark_results[algo_name].append(time_taken)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    for algo_name, times in benchmark_results.items():
        plt.plot(test_sizes, times, label=algo_name, marker='o')

    plt.title("Runtime Benchmark of Sorting Algorithms")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.yscale("log")
    plt.legend()
    plt.grid(True)
    plt.show()


# Main execution
if _name_ == "_main_":
    # Display system details
    system_details = fetch_system_details()
    print("System Details:")
    for key, value in system_details.items():
        print(f"{key}: {value}")
    print("\nExecuting benchmarks...\n")

    # Run the benchmark
    evaluate_sorting_algorithms()
