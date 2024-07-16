import requests
from requests import HTTPError


def get_weather_in_city(url: str, city: str,
                        params: dict) -> str:
    """
    :param url: адрес на который осуществляется запрос
    :param city: название города
    :param params: параметры запроса
    :return: прогноз в юникоде
    """
    response = requests.get(
        url.format(city_name=city),
        params=params
    )
    response.raise_for_status()

    return response.text


if __name__ == "__main__":

    cities = ['Лондон', 'Шереметьево', 'Череповeц']
    url = "http://wttr.in/{city_name}"
    params = {
        'n': '',
        'T': '',
        'q': '',
        'm': '',
        'lang': 'ru'
    }

    for city in cities:
        try:
            print(get_weather_in_city(url, city, params))
        except HTTPError:
            print(f'Погода в {city} недоступна')
