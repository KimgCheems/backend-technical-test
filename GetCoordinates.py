import requests


def get_coordinates_from_address(address):
    query = {'q': address}
    r = requests.get("https://api-adresse.data.gouv.fr/search/", params=query)
    parsed_res = r.json()
    if not parsed_res["features"]:
        return
    return int(parsed_res["features"][0]["properties"]["x"]), int(parsed_res["features"][0]["properties"]["y"])
