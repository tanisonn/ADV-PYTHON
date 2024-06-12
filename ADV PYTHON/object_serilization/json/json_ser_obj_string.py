import json
class vech:
    def __init__(self,vechno,vechname,vechid,vechadd):
        self.vechno=vechno
        self.vechname=vechname
        self.vechid=vechid
        self.vechadd=vechadd
    def display(self):
        print("The information about the vechicle is:")
        print("vechno:{}\nvechname:{}\nvechid:{}\nvechadd:{}".format(self.vechno,self.vechname,self.vechid,self.vechadd))
motor=vech(9059,"activa",100,"HYD")
e=motor.__dict__
json_str=json.dumps(e)
print(json_str)
    