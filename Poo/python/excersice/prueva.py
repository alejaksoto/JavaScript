n = 0
def f():
    global n
    n = 9
    print("Dentro de f :",n)
f()
print("Fuera de f:",n)
