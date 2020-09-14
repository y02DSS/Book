import requests


class Map():
    def get_address(address):
        URL = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}&format=json&sco=latlong&kind=house&results=1&lang=ru_RU"
        result = requests.get(URL).json()
        a = (result['response']['GeoObjectCollection']['featureMember']
             [0]['GeoObject']['boundedBy']['Envelope']['lowerCorner']).split()
        b = (result['response']['GeoObjectCollection']['featureMember']
             [0]['GeoObject']['boundedBy']['Envelope']['upperCorner']).split()
        return((float(a[1]) + float(b[1])) / 2, (float(a[0]) + float(b[0])) / 2)
