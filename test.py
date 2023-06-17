import numpy as np

def create_numpy_array(rows, cols):
    array = np.random.rand(rows, cols)
    return array

# Example usage
rows = 3
cols = 4
my_array = create_numpy_array(rows, cols)
print(my_array)