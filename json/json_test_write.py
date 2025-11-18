import json

data = {"name": "Vlad", "age": 26}

with open("user.json", "w") as file:
    json.dump(data, file)