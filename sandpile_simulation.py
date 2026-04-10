import numpy as np
import matplotlib.pyplot as plt

# Grid size
L = 30

# Threshold for toppling
threshold = 4

# Number of grains added
steps = 10000

# Initialize grid
grid = np.zeros((L, L), dtype=int)

# Store avalanche sizes
avalanches = []

for step in range(steps):

    # Add grain randomly (noise)
    x, y = np.random.randint(0, L, 2)
    grid[x, y] += 1

    avalanche_size = 0
    unstable = True

    # Avalanche process
    while unstable:
        unstable = False

        for i in range(L):
            for j in range(L):

                if grid[i, j] >= threshold:

                    avalanche_size += 1
                    grid[i, j] -= 4

                    if i > 0:
                        grid[i-1, j] += 1
                    if i < L-1:
                        grid[i+1, j] += 1
                    if j > 0:
                        grid[i, j-1] += 1
                    if j < L-1:
                        grid[i, j+1] += 1

                    unstable = True

    if avalanche_size > 0:
        avalanches.append(avalanche_size)

# Plot avalanche distribution
plt.hist(avalanches, bins=50)
plt.xlabel("Avalanche Size")
plt.ylabel("Frequency")
plt.title("Avalanche Size Distribution in Sandpile Model")
plt.show()

# Save avalanche data
np.savetxt("avalanche_data.txt", avalanches)