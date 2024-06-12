import json
d={
    "laptopname":"Lenovo",
    "Model":980025,
    "RAM":"8Gb",
    "Processor":"i5",
    "fingerprint option":False
}
with open("json_dict","w") as f:
    json.dump(d,f,indent=1)
