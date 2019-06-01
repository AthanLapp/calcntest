from calc import *
import numpy as np
highint=99999999999999
breaknumber=2000
c=0
while(np.random.random()!=0):
    c=c+1
    a = np.random.random()*np.random.randint(-highint,highint)
    b = np.random.random()*np.random.randint(-highint,highint)
    print(a, b)
    assert add(a,b) == a+b
    assert substract(a,b) == a-b
    assert multiply(a,b) == a*b
    assert divide(a,b) == a/b
    if(c==breaknumber):
        print("test passed")
        break

