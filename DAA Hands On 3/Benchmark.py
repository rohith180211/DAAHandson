import time
import numpy as np
import matplotlib.pyplot as plt

# Original function f(n)
def compute_function(size):
    counter = 1
    for outer_loop in range(size):
        for inner_loop in range(size):
            counter += 1
    return counter

# Range of input sizes
input_sizes = list(range(1, 1000))
execution_times = []

# Measure time for different input sizes
for size in input_sizes:
    start = time.time()
    compute_function(size)
    end = time.time()
    
    duration = end - start
    execution_times.append(duration)

# Convert to numpy arrays for curve fitting
input_sizes_np = np.array(input_sizes)
execution_times_np = np.array(execution_times)

# Fit a polynomial (quadratic) curve to the measured times
poly_coeffs = np.polyfit(input_sizes_np, execution_times_np, 2)
fitted_curve = np.polyval(poly_coeffs, input_sizes)

# Plot the actual times vs fitted quadratic curve
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, label="Measured Time")
plt.plot(input_sizes, fitted_curve, label="Quadratic Fit", color='r')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Measured Execution Time vs Input Size')
plt.legend()
plt.grid(True)
plt.show()

# Display polynomial coefficients
# print("Quadratic coefficients for the fitted curve:", poly_coeffs)

# Calculate upper and lower bounds for time complexity
upper_limit = poly_coeffs[0] * input_sizes_np**2
lower_limit = poly_coeffs[0] * input_sizes_np**2 * 0.8  # Arbitrary example for lower bound

# Plot the measured times along with upper and lower bounds
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, label="Measured Time")
plt.plot(input_sizes, fitted_curve, label="Quadratic Fit", color='r')
plt.plot(input_sizes, upper_limit, label="Upper Bound", color='g')
plt.plot(input_sizes, lower_limit, label="Lower Bound", color='orange')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Upper and Lower Bounds for Execution Time')
plt.legend()
plt.grid(True)
plt.show()

# Estimate n_0 (point where time exceeds the fitted curve)
n0_index = np.where(execution_times_np > fitted_curve)[0][0]

# Plot highlighting n_0
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, label="Measured Time")
plt.plot(input_sizes, fitted_curve, label="Quadratic Fit", color='r')
plt.axvline(x=input_sizes[n0_index], color='k', linestyle='--', label=f"n_0 ~ {input_sizes[n0_index]}")
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Estimating n_0 (Divergence Point)')
plt.legend()
plt.grid(True)
plt.show()

print(f"Estimated n_0: {input_sizes[n0_index]}")
