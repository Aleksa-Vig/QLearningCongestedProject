import numpy as np

# This function maps a cbr, vehicle_density tuple to a number from 0-6999 (7000 possibilites)
def map_tuple_to_integer(cbr, vehicle_density):
    density_range = 50
    cbr_range = 1.5

    # Vehicle denisty already mapped
    density_normalized = int(vehicle_density)
    # Map cbr to 1-140 values
    cbr_normalized = int((cbr + 0.01 - 0.11) / 0.01)

    unique_integer = density_normalized * cbr_normalized

    return unique_integer-1

def main():
    # Create a numpy array of size 5000x140 with tuple columns
   print(map_tuple_to_integer( 0.11, 1))

if __name__ == '__main__':
    main()