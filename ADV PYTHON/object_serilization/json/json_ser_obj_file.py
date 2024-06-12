import json
class pendrives:
    def __init__(self,pendrivename,pendrivespace,pendrivedate,pendriveerasable):
        self.pendrivename=pendrivename
        self.pendrivespace=pendrivespace
        self.pendrivedate=pendrivedate
        self.pendriveerasable=pendriveerasable
    def display(self):
        print("The information about pendrive is:")
        print("Pendrive Name:{}\npendrive Space:{}\n pendrive Date:{}".format(self.pendrivename,self.pendrivespace,self.pendrivedate))
pen=pendrives("sandisk","4GB","June",True)
data=pen.__dict__
with open("json_dict_1","w") as f:
    json.dump(data,f,indent=1)

