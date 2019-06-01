def add(a,b):
    c = a + b
    print(c)
    return c

def substract(a,b):
    c = a - b
    print(c)
    return c

def multiply(a,b):
    c = a * b
    print(c)
    return c

def divide(a,b):
    if b!=0:
        c = a / b
        print(c)
        return c
    else:
        print("division by zero")
        if (a>0):
            return 9223372036854775807
        else:
            return -9223372036854775806
