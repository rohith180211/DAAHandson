def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


# Debugging fibonacci(5)
def fibonacci_debug(num):
    trace_calls = []

    def helper_fib(x):
        trace_calls.append(f'fibonacci({x})')
        if x == 0:
            return 0
        if x == 1:
            return 1
        return helper_fib(x - 1) + helper_fib(x - 2)

    final_result = helper_fib(num)
    return trace_calls, final_result


trace_calls, final_result = fibonacci_debug(5)
print("Trace of Calls:", " -> ".join(trace_calls))
print("Final Result:", final_result)
