from IsRemotelyClose import is_remotely_close


def get_cell_availability_from_coord(coords, precision, operator_data):
    res = {}
    for x in operator_data:
        if is_remotely_close(int(x[1]), coords[0], precision) and is_remotely_close(int(x[2]), coords[1], precision):
            res[x[0]] = [x[3], x[4], x[5]]
    return res
