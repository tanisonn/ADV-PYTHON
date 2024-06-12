import time
import random
#list
student=["ravi","kiran","surya","charan"]
subject=["science","social","gk","maths"]
def listgen(n):
    res=[]
    for i in range(n):
        stud={"id":i,"name":random.choice(student),"subject":random.choice(subject)}
        res.append(stud)
    return res
t1=time.perf_counter()
listgen(10000)
t2=time.perf_counter()
print("the time taken to generate 100 lists are",t2-t1)
def gene(n):
    for i in range(n):
        stud={"id":i,"name":random.choice(student),"subject":random.choice(subject)}
        yield stud
t3=time.perf_counter()
gene(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
t4=time.perf_counter()
print("The time required to generate 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 generators are",t4-t3)

"""the time taken to generate 100 lists are 0.014520287048071623
The time required to generate 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 generators are 6.53101596981287e-06"""