
def add (n, m, *z,  **a):
    print (type(a))
    print(type(z))
    print (a)
    print(z)

    sum = a["x"] + a['y']
    return sum

print (add (1,2, 55,33,55, x=10, y=20))


#setting default values
def test (a=0, b=0):
    return a + b

print (test ())
