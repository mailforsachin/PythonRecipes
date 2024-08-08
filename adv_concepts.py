
#July 27th 2024
""" i="outside class"
class test:
    i="inside class"
    def display(self):
        i="inside method"
        print("inside display method:",i)
    def put(self):
        print("inside put method:",i)
t=test()
t.display()
t.put()
print(i)
print("class variable from outside class:",t.i)


# nothing, inside display method: inside method, inside put method:outside class, outside class, class variable from outside class: inside class """

""" 
class test:
    val=10
    def display(self):
        print("val=", self.val);
t=test()
print(test.val)
t.display()


class test:
    val=10
    def display(self,other):
        print("val=", other, test.val);
t=test()
print(test.val)
t.display(100) """

#6th August
class test:
    def _new_(cls):
        print("creating object")
    def test(self, val=8):
        self.val=val;
        print(f"initialisation{val}")
test.test(8)
t=test()
