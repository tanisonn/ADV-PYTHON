import yaml
class toothpaste:
    def __init__(self,paste1,paste2,paste3):
        self.paste1=paste1
        self.paste2=paste2
        self.paste3=paste3
    def display(self):
        print("The toothpastes are :{},{},{}".format(self.paste1,self.paste2,self.paste3))
m=toothpaste("colgate","close-Up","pepsident")
yaml_str=yaml.dump(m)
print(yaml_str)
with open("obj.yaml","w") as f:
    yaml.dump(m,f)
