def convert_json_of_mongo(data):

    for item in data:
        item["_id"] = str(item["_id"])
        item["updatedAt"] = str(item["updatedAt"])
        item["createdAt"] = str(item["createdAt"])

    return data
