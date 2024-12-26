import random


def generate_random_map(width: int, height: int, wall_probability: float = 0.3):
    map_matrix = []

    for y in range(height):
        row = []
        for x in range(width):
            # Ensure borders are walls
            #if x == 0 or x == width - 1 or y == 0 or y == height - 1:
            #    row.append('#')
            #else:
                # Randomly decide if the cell should be a wall or floor
                if random.random() < wall_probability:
                    row.append('a')  # Wall
                else:
                    row.append('b')  # Floor
        map_matrix.append(row)
    
    return map_matrix
