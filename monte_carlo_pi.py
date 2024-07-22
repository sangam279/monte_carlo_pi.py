import random
import matplotlib.pyplot as plt

def monte_carlo_pi(num_points):
    inside_circle = 0
    points_inside = []
    points_outside = []

    for _ in range(num_points):
        # we are generating Random point (x, y) inside the square
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Checking if point (x, y) inside the circle
        if x**2 + y**2 <= 1:
            inside_circle += 1
            points_inside.append((x, y))
        else:
            points_outside.append((x, y))

    # the ratio of points that are inside the circle to the total points
    # the area of the circle divided by the area of square approximates (π/4).
    # we can approximate π by multiplying by 4.
    pi_estimate = (inside_circle / num_points) * 4
    return pi_estimate, points_inside, points_outside

# for generating Number of random points
num_points = 100000

# run Simulation
pi_estimate, points_inside, points_outside = monte_carlo_pi(num_points)
print(f"{num_points} points ke baad π ki estimated value: {pi_estimate}")

# plotting the Points
points_inside_x, points_inside_y = zip(*points_inside)
points_outside_x, points_outside_y = zip(*points_outside)

plt.figure(figsize=(8, 8))
plt.scatter(points_inside_x, points_inside_y, color='blue', s=1, label='Inside Circle')
plt.scatter(points_outside_x, points_outside_y, color='red', s=1, label='Outside Circle')

# for Reference draw the circle boundary
circle = plt.Circle((0, 0), 1, color='green', fill=False)
plt.gca().add_patch(circle)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f"Monte Carlo Simulation for Estimating π\nEstimated π = {pi_estimate}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
