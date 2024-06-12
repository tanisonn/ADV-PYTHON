import json
json_string='''{"vechno": 9059, "vechname": "activa", "vechid": 100, "vechadd": "HYD"}'''
a=json.loads(json_string)
print(type(a))
print(a)
