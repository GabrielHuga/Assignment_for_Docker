import requests
import pandas as pd

url = 'https://api.opencagedata.com/geocode/v1/json'
api_key = 'a34768ccd55d49cfa29fb5753e2d1486'

df = pd.DataFrame({'country': ['Country1', 'Country2', 'Country3']})
country = df[['country']]

countries = df['country'].tolist()

components_list = []

for country in countries:
    params = {'q': country, 'key': api_key}

    response = requests.get(url, params=params)

    json_data = response.json()

    components = json_data['results'][0]['components']

    country_components = {'country': country,
                          'country_code': components.get('country_code', ''),
                          'latitude': json_data['results'][0]['geometry']['lat'],
                          'longitude': json_data['results'][0]['geometry']['lng']}

    components_list.append(country_components)

components_df = pd.DataFrame(components_list)
