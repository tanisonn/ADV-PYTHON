import jsonpickle
class mob:
    def __init__(self,mobilecompany,mobilemodel,mobileemino):
        self.mobilecompany=mobilecompany
        self.mobilemodel=mobilemodel
        self.mobileemino=mobileemino
    def display(self):
        print("The mobile details are:")
        print("mobilecompany:{}\nmoiblemodel:{}\nmobileemino:{}".format(self.mobilecompany,self.mobilemodel,self.mobileemino))
with open("json_pick_obj_file","r")as f:
    obj=f.readline()
z=jsonpickle.decode(obj)
z.display()
