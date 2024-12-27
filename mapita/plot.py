import noise
import numpy as np
import matplotlib.pyplot as plt

# Define grid size
width, height = 40, 20

# Perlin parameters
scale = 30.0
octaves = 8
persistance = 0.5
lacunarity = 2.0


grid = np.zeros((width, height))

# Generate 2D Perlin noise
for y in range(height):
    for x in range(width):
        grid[x][y] = noise.pnoise2(x/scale, y/scale, octaves, persistance, lacunarity, repeatx = 1024, repeaty = 1024, base = 40)

# Display the noise pattern as an image
plt.imshow(grid, cmap='gray')
plt.colorbar()
plt.savefig('plot.png')
plt.close()

