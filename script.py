import requests
from requests import HTTPError


def get_weather_in_city(url: str, city: str) -> str:
    """
    :param url: адрес на который осуществляется запрос
    :param city: название города
    :return: прогноз в юникоде
    """
    response = requests.get(
        url.format(city_name=city)
    )
    response.raise_for_status()

    return response.text


if __name__ == "__main__":

    cities = ['Лондон', 'Шереметьево', 'Череповeц']
    url = "http://wttr.in/{city_name}?nTqm&lang=ru"

    for city in cities:
        try:
            print(get_weather_in_city(url, city))
        except HTTPError:
            print(f'Погода в {city} недоступна')
