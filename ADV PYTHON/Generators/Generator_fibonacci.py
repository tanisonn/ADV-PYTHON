def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
g=fib()
for i in g:
    if i<=100:
        print(i) 
    else:
        break