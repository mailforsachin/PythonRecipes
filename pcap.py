import random as r

print(dir(r))
mystr="Sachin"
print(type(mystr));
if type(mystr)==str:
    try:
        name= input("what is your name");


    except TypeError:
        print("some error")
    


class A:
    A = 0
    def __init__(self,v = 0):
        self.Y = v
        print(v)

        A.A += v
print (__name__)

a = A()
print(a)

# A= 0,v=0, Y=0, A.A=A.A+V (0.0=0+0)
b = A(1)
#v=0,V=0, A.A=A.A+V , A.A=
c = A(2)

print(c.A)


print(chr(ord('a') + 5))
print(ord('a'))
    


from random import randint

for i in range(2):
          print(randint(0, 1), end='**')


class A:
    def __init__(self, a = 1):
        self.a = a
    def swap(self, a):
        self.a *= a
        return a


a = A(2)
print(a.swap(a.a + 1))

# A(2), a=2
#a.swap , a=a+1, a=3