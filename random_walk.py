import random
import matplotlib.pyplot as plt

# Number of steps
steps = 20

# Starting coordinates
x, y = 0, 0

# Lists to store the x and y positions for plotting
x_positions = [x]
y_positions = [y]

# Probability ranges for each direction
# Forward (F): 0 to 4 (50%) -> 0,1,2,3,4
# Left (L): 5 to 6 (20%) -> 5,6
# Right (R): 7 to 8 (20%) -> 7,8
# Backward (B): 9 (10%) -> 9

print("Step-by-step positions of the drunkard:")

for step in range(steps):
    rand_num = random.randint(0, 9)  # Generate a random number between 0 and 9

    if 0 <= rand_num <= 4:  # Forward
        y += 1
        direction = "F"
    elif 5 <= rand_num <= 6:  # Left
        x -= 1
        direction = "L"
    elif 7 <= rand_num <= 8:  # Right
        x += 1
        direction = "R"
    elif rand_num == 9:  # Backward
        y -= 1
        direction = "B"

    # Print the random number, direction, and the current position
    print(f"Step {step + 1}: Random number = {rand_num}, Direction = {direction}, Position = ({x}, {y})")

    # Append the current position to the lists for plotting
    x_positions.append(x)
    y_positions.append(y)

# Final position after 50 steps
print(f"\nThe drunkard's final position is: ({x}, {y})")

# Plotting the drunkard's path
plt.plot(x_positions, y_positions, marker='o', linestyle='-', color='b', markersize=5)
plt.scatter(x_positions[0], y_positions[0], color='green', label='Start (0, 0)', s=100)  # Starting point
plt.scatter(x_positions[-1], y_positions[-1], color='red', label=f'End ({x}, {y})', s=100)  # End point
plt.title("Drunkard's Walk")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)
plt.legend()
plt.show()