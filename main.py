import requests


def get_info(IP):
    print("Information about IP-adress: ")
    try:
        r = requests.get(url=f"http://ip-api.com/json/{IP}").json()
        data = {
            "IP": r.get("query"),
            "Provider": r.get("isp"),
            "Organisation": r.get("org"),
            "Country": r.get("country"),
            "Region": r.get("regionName"),
            "City": r.get("city"),
            "ZIP": r.get("zip"),
            "Lat": r.get('lat'),
            "Lon": r.get('lon')
        }
        for k, v in data.items():
            print(f"{k}: {v}")
    except requests.exceptions.ConnectionError:
        print("ERROR! CAN NOT CONNECT")


def main():
    ip = input()
    get_info(ip)


main()
