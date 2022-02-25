import json


def format_response(cell_service, operator_table):
    res = {}
    for x in cell_service.keys():
        res[operator_table[int(x)]] = {"2G": bool(int(cell_service[x][0])), "3G": bool(int(cell_service[x][1])), "4G": bool(int(cell_service[x][2]))}
    return json.dumps(res)
