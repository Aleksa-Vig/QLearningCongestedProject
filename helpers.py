def convert_to_unique_integer(cbr, vehicle_density):
    cbr_range = 0.01
    density_range = 1

    cbr_normalized = int((cbr - 0.01) / cbr_range * 250)
    density_normalized = int((vehicle_density - 1) / density_range * 250)

    unique_integer = cbr_normalized + density_normalized * 50

    return unique_integer

