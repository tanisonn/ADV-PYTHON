def solve(n):
    i=1
    while(i<=n):
        yield i
        i+=1
a=solve(10)
for x in a:
    print(x)