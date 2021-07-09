def get_result_data(result: dict):
    data = {}

    if 'name' in result:
        data['title'] = result['name']
    if 'weather' in result:
        data['weather_data'] = result['weather'][0]
    if 'main' in result:
        data['main_data'] = result['main']
    if 'wind' in result:
        data['wind_data'] = result['wind']
    if 'sys' in result:
        data['sun_data'] = result['sys']
    if 'dt' in result:
        data['updated_on'] = result['dt']

    return data
