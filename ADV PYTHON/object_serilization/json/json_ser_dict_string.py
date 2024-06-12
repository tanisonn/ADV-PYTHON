import json
d={
    "laptopname":"Lenovo",
    "Model":980025,
    "RAM":"8Gb",
    "Processor":"i5",
    "fingerprint option":False
}
json_str=json.dumps(d)
print(json_str)
