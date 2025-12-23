def hill_climbing(start, step_size, max_iterations):
    current = start

    for _ in range(max_iterations):
        # Evaluate neighbors
        left = current - step_size
        right = current + step_size

        # Choose the best neighbor
        if f(left) > f(current):
            current = left
        elif f(right) > f(current):
            current = right
        else:
            break  # no better neighbor found

    return current


def f(x):
    return -x**2 + 10


# Run the algorithm
start_point = 0.001
step = 0.1
iterations = 100

best_solution = hill_climbing(start_point, step, iterations)
print("Best solution:", best_solution)
print("Maximum value:", f(best_solution))
