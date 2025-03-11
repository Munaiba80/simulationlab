import numpy as np
import matplotlib.pyplot as plt

# The function we want to integrate: f(x) = x^3
def f(x):
    return x ** 3

# Simple Monte Carlo integration function
def monte_carlo_integration(num_points, x_min, x_max, y_max):
    # Random points in the rectangle
    x_random = np.random.uniform(x_min, x_max, num_points)
    y_random = np.random.uniform(0, y_max, num_points)

    # Count how many points are below the curve
    points_under_curve = y_random <= f(x_random)

    # Estimate the integral based on the ratio of points under the curve
    integral_estimate = (x_max - x_min) * y_max * np.sum(points_under_curve) / num_points
    return integral_estimate, x_random, y_random, points_under_curve

# Get user input for the number of random points (multiple points allowed)
num_points_input = input("Enter the number of random points (separate by commas): ")
num_points_list = [int(x) for x in num_points_input.split(',')]  # Convert input to list of integers

# Get user input for the range of x and y
x_min = float(input("Enter the minimum x value: "))
x_max = float(input("Enter the maximum x value: "))
y_max = float(input("Enter the maximum y value: "))

# The exact value of the integral
exact_integral = 152.25

# Run Monte Carlo integration for each set of random points entered by the user
for num_points in num_points_list:
    integral_estimate, x_random, y_random, points_under_curve = monte_carlo_integration(num_points, x_min, x_max, y_max)

    # Print the results
    print(f"\nFor {num_points} points:")
    print(f"Estimated integral: {integral_estimate:.2f}")
    print(f"Exact integral: {exact_integral}")
    print(f"Error: {abs(integral_estimate - exact_integral):.2f}")

    # Plot the results
    plt.figure(figsize=(8, 6))

    # Plot the function f(x) = x³
    x_curve = np.linspace(x_min, x_max, 1000)
    y_curve = f(x_curve)
    plt.plot(x_curve, y_curve, label="f(x) = x³", color='green')

    # Plot random points: blue for under the curve, red for above the curve
    plt.scatter(x_random[points_under_curve], y_random[points_under_curve], color="blue", label="Under the curve")
    plt.scatter(x_random[~points_under_curve], y_random[~points_under_curve], color="red", label="Above the curve")

    # Labels and title
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Monte Carlo Integration of f(x) = x³")
    plt.legend()
    plt.grid(True)
    plt.show()
