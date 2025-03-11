import random
import math

# Function to check if a point is inside a unit circle (radius = 1)
def is_point_in_circle(x, y, r=1):
    return x**2 + y**2 <= r**2

# Monte Carlo method to estimate the area of the circle
def monte_carlo_area(num_points):
    inside_count = 0  # Counter for points inside the circle
    
    for _ in range(num_points):
        # Generate random points between 0 and 1 for both x and y
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        # Check if the point is inside the circle
        if is_point_in_circle(x, y):
            inside_count += 1
    
    # Area of the square is 1 * 1 (since x and y are between 0 and 1)
    area_of_square = 1 * 1
    
    # Estimation of the circle's area
    estimated_area = (inside_count / num_points) * area_of_square
    return estimated_area

# Input: number of random points
num_points = int(input("Enter the number of random points: "))

# Estimate the area of the circle
estimated_area = monte_carlo_area(num_points)
exact_area = math.pi * 1**2  # Exact area of the unit circle (π * r^2), radius is 1

# Output results
print(f"Estimated area: {estimated_area:.4f}")
print(f"Exact area: {exact_area:.4f}")
