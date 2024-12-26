import noise
import numpy as np

# Perlin parameters
scale = 30.0
octaves = 8
persistance = 0.5
lacunarity = 2.0

# threshold
threshold = 0.0

def generate_random_map(width: int, height: int):

    map_matrix = np.zeros((height,width), dtype=int)
    base = np.random.randint(1,40)
    for y in range(height):
        for x in range (width):
            noise_val = noise.pnoise2(
                    x/scale,
                    y/scale,
                    octaves,
                    persistance,
                    lacunarity,
                    repeatx=1024,
                    repeaty=1024,
                    base = base
                    )
            if noise_val > threshold:
                map_matrix[y,x] = 1 
            else:
                map_matrix[y,x] = 0
    return map_matrix
