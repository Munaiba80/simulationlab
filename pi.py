import numpy as np
import matplotlib.pyplot as plt

# Take user input for N (number of points)
N = int(input("Enter the number of random points: "))

# Choose manual input or random generation
choice = input("Do you want to enter x, y manually? (yes/no): ").strip().lower()

x_values, y_values = [], []

if choice == "yes":
    # Manually input x and y values
    for i in range(N):
        x = float(input(f"Enter x[{i+1}]: "))
        y = float(input(f"Enter y[{i+1}]: "))
        x_values.append(x)
        y_values.append(y)
else:
    # Auto-generate random x and y values
    x_values = np.random.rand(N)
    y_values = np.random.rand(N)

# Convert lists to NumPy arrays
x_values = np.array(x_values)
y_values = np.array(y_values)

# Check if points are inside the quarter-circle (x² + y² ≤ 1)
inside_circle = x_values**2 + y_values**2 <= 1
M = np.sum(inside_circle)  # Count points inside

# Estimate π
pi_estimate = 4 * (M / N)

# Print results
print(f"\nEstimated π: {pi_estimate}")
print(f"Actual π: {np.pi}")
print(f"Error: {abs(pi_estimate - np.pi)}")

# Simple Graph
plt.figure(figsize=(6, 6))
plt.scatter(x_values, y_values, s=5, color="blue", alpha=0.3, label="Random Points") 
plt.scatter(x_values[inside_circle], y_values[inside_circle], s=5, color="green", alpha=0.5, label="Inside Circle")

# Draw quarter-circle
theta = np.linspace(0, np.pi/2, 100)
plt.plot(np.cos(theta), np.sin(theta), color="red", linewidth=2, label="Quarter Circle")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Estimation of π")
plt.legend()
plt.show()
