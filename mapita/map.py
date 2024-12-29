import noise
import numpy as np

# Perlin parameters
scale = 120.0
octaves = 3
persistance = 0.5
lacunarity = 2.0


w = 25 
h = 50


def map(width = 25, height= 50, number_rivers=3, debug=False):
    w = width
    h = height
    return detail(quantize(rivers(number_rivers, randmap(width, height, debug), debug)))


def randmap(width: int, height: int, debug):
    map_matrix = np.zeros((width, height), dtype=float)
    base = np.random.randint(1, 2040)
    for y in range(height):
        for x in range(width):
            noise_val = noise.pnoise2(
                    x/scale,
                    y/scale,
                    octaves,
                    persistance,
                    lacunarity,
                    repeatx=1024,
                    repeaty=1024,
                    base=base
                    )
            val = (noise_val/(0.1))
            map_matrix[x, y] = val
    ##  Debug
    if debug:
        print("Debug: ")
        print(f"Base: {base}")
        print(f"Mapa: {width} x {height}")
        print(f"Scale: {scale}")
        print(f"OPL: {octaves}, {persistance}, {lacunarity}")

    return map_matrix


def access(index, shape, matrix):
    # Check bounds
    if index[0] < 0 or index[1] < 0 or index[0] >= shape[0] or index[1] >= shape[1]:
        return np.inf  # Use np.inf for out-of-bounds values so it won't be chosen
    return matrix[index]


def min_nearby(max, index, matrix):
    values = []
    valid = []
    shape = matrix.shape  #size (i,j)
    list_index = list(index)


    # Upside
    list_index[0] += 1
    values.append(access(tuple(list_index), shape, matrix))
    # Downside
    list_index[0] -= 2
    values.append(access(tuple(list_index), shape, matrix))
    # Rightside
    list_index[0] += 1
    list_index[1] += 1
    values.append(access(tuple(list_index), shape, matrix))
    # Leftside
    list_index[1] -= 2
    values.append(access(tuple(list_index), shape, matrix))
    for i in range(4):
        if values[i] != np.inf:
            valid.append(i)

    values = np.array(values)
    if np.random.random() < 0.5:
        return valid[np.random.randint(0, np.size(valid))]
    return np.argmin(values)

def rivers(cuantity: int, matrix, debug):
    new = np.copy(matrix)
    first = True
    for _ in range(cuantity):
        if first:
            flat_index = np.argmax(matrix)
            first = False
        else:
            flat_index = np.random.randint(1, np.size(matrix))

        #print(flat_index)# indice flat del max
        index = np.unravel_index(flat_index, matrix.shape)  # coords
        new_index = list(index)
        max = matrix[index]
        #new[tuple(index)] = -1

        i = 0
        while (max > -2):
            i +=1
            if i>150: break

            min = min_nearby(flat_index, index, matrix)

            if(min == 0):
                new_index[0] += 1
            elif (min == 1):
                new_index[0] -= 1
            elif (min == 2):
                new_index[1] += 1
            else:
                new_index[1] -= 1

            index = tuple(new_index)        
            max = matrix[index]
            if max >= -1:
                new[index] = -1
    

    ## Debug

    if debug:
      print(f"Rivers: {cuantity}")
    

    return new

def quantize(matrix):
    for i in range(len(matrix)):  # Iterate through rows
        for j in range(len(matrix[i])):  # Iterate through columns
            if matrix[i][j] <= -2:
                matrix[i][j] = -2
            elif matrix[i][j] <= -1:
                matrix[i][j] = -1
            elif matrix[i][j] <= -0.7:
                matrix[i][j] = 0 
            elif matrix[i][j] <= 1.5:
                matrix[i][j] = 1
            elif matrix[i][j] <= 2.5:
                matrix[i][j] = 2
            elif matrix[i][j] <= 3.5:
                matrix[i][j] = 3
            else:
                matrix[i][j] = 4
    return matrix


def detail(matrix):
    details = 10
    for _ in range(details):
        i = np.random.randint(0, w)
        j = np.random.randint(0, h)
        if matrix[i][j] == 1:
            matrix[i][j] = 11
        elif matrix[i][j] == 11:
            matrix[i][j] = 10
            #matrix[i][j+1] = 10
    return matrix
