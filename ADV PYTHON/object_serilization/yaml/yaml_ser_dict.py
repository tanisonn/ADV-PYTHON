import yaml
emp={
    "name":"shravani",
    "age":35,
    "salary":40000,
    "ismarried":False
}
yaml_str=yaml.dump(emp)
print(yaml_str)
with open("yaml_dict","w") as f:
    yaml.dump(emp,f)
