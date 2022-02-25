from flask import Flask, request
from GetCoordinates import get_coordinates_from_address
from CsvLoader import load_csv
from CellAvailability import get_cell_availability_from_coord
from Formatter import format_response


app = Flask(__name__)

path_to_csv = "data/2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv"

operator_table = {20801: "Orange", 20810: "SFR", 20815: "Free", 20820: "Bouygue"}

operator_data = load_csv(path_to_csv)

precision = 500


@app.route("/api", methods=['GET'])
def api_endpoint():
    args = request.args
    address = args.get('q')
    if not address:
        return 'bad request!', 400
    coords = get_coordinates_from_address(address)
    if not coords:
        return 'bad request!', 400
    cell_service = get_cell_availability_from_coord(coords, precision, operator_data)
    if not cell_service:
        return 'bad request!', 400
    response = format_response(cell_service, operator_table)
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
