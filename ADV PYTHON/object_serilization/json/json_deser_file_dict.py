import json
with open("json_dict_1","r") as f:
    access=json.load(f)
print(type(access))
print(access)
