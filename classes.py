""" The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks. """


#Round tuple, square list, curly dict

""" myList=["test","best","rest","nest"];
myTuple=("this", "test");
myStr="banana"

for x in myList, myTuple, myStr:
        print(x)
 """
#July 20TH
# Classes and Inheritence
#Create a class named Person, with firstname and lastname properties, and a printname method:#

# class person:

#     def __init__(self, firstname, lastname):
#         self.firstname=firstname;
#         self.lastname=lastname;

#     def printname(self):
#         print (self.firstname+self.lastname);

# class child(person):
#     def __init__(self, firstname, lastname, year):
#         super().__init__(firstname, lastname);
#         self.year=year;
#     def printname(self):
#         print (self.firstname+self.lastname+str(self.year));

# newPerson=person("abhijeet", "kumar")
# newPerson.printname();
# newChild=child("bonzo","nganau",19)
# newChild.printname();


""" class Animal:
    def __init__(self,name,age):
       self.name=name;
       self.age=age;
    

dog=Animal("Max",5);
cat=Animal("Puss",5);
print(dog.name) """