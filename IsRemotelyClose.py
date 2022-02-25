

def is_remotely_close(coord1, coord2, precision):
    return coord2 - precision <= coord1 <= coord2 or coord2 <= coord1 <= coord2 + precision