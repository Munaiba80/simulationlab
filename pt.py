import numpy as np
import matplotlib.pyplot as plt

# Step 1: Take user input for N (number of points)
while True:
    try:
        N = int(input("Enter the number of random points: "))  # User enters N
        if N > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Enter a whole number (e.g., 10000).")

# Step 2: Ask user if they want to manually enter (x, y) or auto-generate them
choice = input("Do you want to enter x, y manually? (yes/no): ").strip().lower()

if choice == "yes":
    x_random = []
    y_random = []
    print("\nEnter x and y values (between 0 and 1):")
    for i in range(N):
        while True:
            try:
                x = float(input(f"Enter x[{i+1}]: "))  # Take x input
                y = float(input(f"Enter y[{i+1}]: "))  # Take y input
                if 0 <= x <= 1 and 0 <= y <= 1:
                    x_random.append(x)
                    y_random.append(y)
                    break
                else:
                    print("Please enter values between 0 and 1.")
            except ValueError:
                print("Invalid input. Enter numbers between 0 and 1.")
    
    x_random = np.array(x_random)
    y_random = np.array(y_random)

else:
    # Step 3: Auto-generate x and y if user chooses 'no'
    x_random = np.random.rand(N)  # Random x values between 0 and 1
    y_random = np.random.rand(N)  # Random y values between 0 and 1

# Step 4: Count points inside the quarter-circle (x^2 + y^2 ≤ 1)
inside_circle = x_random**2 + y_random**2 <= 1  # Boolean array
M = np.sum(inside_circle)  # Count how many points are inside

# Step 5: Estimate π
pi_estimate = 4 * (M / N)

# Step 6: Print results
print(f"\nEstimated π: {pi_estimate}")
print(f"Actual π: {np.pi}")
print(f"Error: {abs(pi_estimate - np.pi)}")

# Step 7: Visualization
plt.figure(figsize=(6, 6))
plt.scatter(x_random, y_random, color='blue', s=1, alpha=0.3, label="Random Points")
plt.scatter(x_random[inside_circle], y_random[inside_circle], color='green', s=1, alpha=0.3, label="Inside Circle")

# Draw quarter-circle boundary
circle = plt.Circle((0, 0), 1, color='red', fill=False, linewidth=2)
plt.gca().add_patch(circle)

# Draw square boundary
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=0, color='black', linewidth=1)
plt.axhline(y=1, color='black', linestyle='dashed', linewidth=1)
plt.axvline(x=1, color='black', linestyle='dashed', linewidth=1)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Estimation of π")
plt.legend()
plt.show()
