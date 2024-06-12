import yaml
with open("yaml_dict","r") as f:
    z=yaml.safe_load(f)
print(z)