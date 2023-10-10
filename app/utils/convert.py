def convert_json_of_mongo(data):
    for item in data:
        for key, value in item.items():
            if not isinstance(value, (str, int, float, bool, list, dict)):
                item[key] = str(value)
    return data
