import jsonpickle
class mob:
    def __init__(self,mobilecompany,mobilemodel,mobileemino):
        self.mobilecompany=mobilecompany
        self.mobilemodel=mobilemodel
        self.mobileemino=mobileemino
    def display(self):
        print("The mobile details are:")
        print("mobilecompany:{}\nmoiblemodel:{}\nmobileemino:{}".format(self.mobilecompany,self.mobilemodel,self.mobileemino))
m=mob("samsung","s24","9800")
str=jsonpickle.encode(m)
with open("json_pick_obj_file","w") as f:
    f.write(str)
