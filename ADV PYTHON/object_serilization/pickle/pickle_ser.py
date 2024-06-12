import pickle
class Student:
    def __init__(self,sname,sno,sgrade,sadd):
        self.sname=sname
        self.sno=sno
        self.sgrade=sgrade
        self.sadd=sadd
    def display(self):
        print("the student details are:")
        print("student name:{}\nstudent roll no:{}\nstudent grade:{}\nstudent address:{}".format(self.sname,self.sno,self.sgrade,self.sadd))
s1=Student("Ravi",20,"A","HYD")
with open("data.pickle","wb") as f:
    pickle.dump(s1,f)
