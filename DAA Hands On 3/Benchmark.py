import time
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Initial version of the function
def initial_function(limit):
    result = 1
    for outer in range(limit):
        for inner in range(limit):
            result += 1
    return result

# Modified version of the function
def revised_function(limit):
    result_x = 1
    result_y = 1
    for outer in range(limit):
        for inner in range(limit):
            result_x += 1
            result_y = outer + inner
    return result_x

# Collect execution times for various input sizes
input_sizes = list(range(1, 10001, 500))  # Test for larger input values
initial_times = []
revised_times = []

# Time measurement loop
for limit in input_sizes:
    # Measure time for the initial function
    start_time = time.time()
    initial_function(limit)
    finish_time = time.time()
    initial_times.append(finish_time - start_time)

    # Measure time for the revised function
    start_time = time.time()
    revised_function(limit)
    finish_time = time.time()
    revised_times.append(finish_time - start_time)

# Fit a quadratic polynomial to model time complexity of the initial function
fit_coeffs = np.polyfit(input_sizes, initial_times, 2)  # Quadratic curve
time_polynomial = Polynomial(fit_coeffs[::-1])  # Polynomial for better plotting

# Establish upper and lower bounds
upper_estimate = lambda limit: 1.2 * time_polynomial(limit)  # Multipliers for bounds
lower_estimate = lambda limit: 0.8 * time_polynomial(limit)

# Plotting results
plt.figure(figsize=(18, 6))

# Plot 1: Time vs input size for the initial function
plt.subplot(1, 3, 1)
plt.plot(input_sizes, initial_times, 'ro-', label='Initial Function')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Time Complexity of Initial Function')
plt.grid(True)

# Plot 2: Time vs input size with bounds and fitted curve
plt.subplot(1, 3, 2)
plt.plot(input_sizes, initial_times, 'ro-', label='Execution Time')
plt.plot(input_sizes, time_polynomial(input_sizes), 'b-', label='Quadratic Fit')
plt.plot(input_sizes, upper_estimate(input_sizes), 'g--', label='Upper Bound')
plt.plot(input_sizes, lower_estimate(input_sizes), 'y--', label='Lower Bound')
plt.axvline(x=1800, color='gray', linestyle='--', label='n_0 = 1800')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Fitted Curve with Bounds for Initial Function')
plt.legend()
plt.grid(True)

# Plot 3: Comparison of revised function with bounds and n0
plt.subplot(1, 3, 3)
plt.plot(input_sizes, revised_times, 'ro-', label='Revised Function')
plt.plot(input_sizes, time_polynomial(input_sizes), 'b-', label='Quadratic Fit')
plt.plot(input_sizes, upper_estimate(input_sizes), 'g--', label='Upper Bound')
plt.plot(input_sizes, lower_estimate(input_sizes), 'y--', label='Lower Bound')
plt.axvline(x=1800, color='gray', linestyle='--', label='n_0 = 1800')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Revised Function with Fit and n_0')
plt.legend()
plt.grid(True)

# Adjust layout and display plots
plt.tight_layout()
plt.show()
