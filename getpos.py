import requests


def geodata(ip_list):
    info = []
    for ip in ip_list:
        geo = requests.get("https://get.geojs.io/v1/ip/geo/{}.json".format(ip)).json()
        ptr = requests.get("https://get.geojs.io/v1/dns/ptr/{}.json".format(ip)).json()
        geo[list(ptr.items())[0][0]] = list(ptr.items())[0][1]

        info.append(geo)

    return tuple(info)
