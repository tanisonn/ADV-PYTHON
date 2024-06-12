def sol():
    yield "a"
    yield "b"
    yield "c"
a=sol()
for x in a:
    print(x)