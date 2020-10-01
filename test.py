import json

with open("member_list.json", "r", encoding="utf8") as f:
    data=f.read()
    obj = json.loads(data)
    print(obj["members"])
