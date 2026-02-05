import json
with open("util/land.json", "r") as f:
    data = json.load(f)

lands = [row["Column2"] for row in data['data']]
print(lands)
print(len(lands))