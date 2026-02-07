import json
with open("util/land.json", "r") as f:
    data = json.load(f)

lands = [row["Column2"] for row in data['data']]
print(lands)
print(len(lands))

with open("util/land.json", "r") as f:
    data = json.load(f)["data"]

land = [row for row in data if isinstance(row.get('※ 매월 말일자 통계 현황'), str) and row['※ 매월 말일자 통계 현황'].isdigit() and len(row['※ 매월 말일자 통계 현황']) == 10 and row['※ 매월 말일자 통계 현황'].endswith('000000') and not row['※ 매월 말일자 통계 현황'].endswith('00000000')]
lands = [row["Column2"] for row in land]
print(len(lands))