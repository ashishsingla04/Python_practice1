def check(func):
    def inside (a,b):
        if b == 0:
            print("can not divide by 0")
            return
        func(a,b)
    return inside

@check
def div( a, b):
    print (a//b)

div(100,10)