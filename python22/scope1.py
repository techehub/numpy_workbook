x= 10

def outer ():
    global x
    x= x+10
    print (x)

    def inner ():
        global x
        x= x+3
        print (x)


    inner ()

print (x)
outer ()
print (x)