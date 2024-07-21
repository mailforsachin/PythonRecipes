'July 20'
'Classes'
""" class calculator:
    def __init__(self, number1, number2):
        self.number1=number1;
        self.number2=number2;

    def add(number1, number2):
        return number1+number2;

addresult=calculator.add(10,10)
print(addresult)
 """ """ """

'July 19'
'List Comparison'
""" 
countList1= input("How many numbers for List 1? ")
countList2= input("How many numbers for List 2? ")

myList1=[];
myList2=[];

try:
    for x in range(int(countList1)):
        addNoToList1= int(input("List 1: Enter the number. "));
        myList1.append(addNoToList1)
    for x in range(int(countList2)):
        addNoToList2= int(input("List 2: Enter the number. "));
        myList2.append(addNoToList2)
    print(myList1, myList2)

    for element in myList1:
        if element in myList2:
            print(f"Common element found: {element}")

    myList1=set(myList1)
    myList2=set(myList2)
    commonElements =myList1.intersection(myList2)
    print(f"Common elements is {commonElements}")

except ValueError:
    print("Value should be numbers. ")

except TypeError:
    print("Type should be numbers. ")


 """

'July 19'
'Avg Min Max'
""" import numpy as n
myNum=input("How many numbers? ")
count=1;
try:
    myList =[];
    for i in range(int(myNum)):
        popNumber=int(input("Enter number. "))
        myList.append(int(popNumber))
        print(myList)
    mySum = sum(myList)
    myAvg = n.average(myList)
    myMax = n.max(myList)
    myMin= n.min(myList)
    print(f"Sum is {mySum}")
    print(f"Average is {myAvg}, Minimum is {myMin} and Maximum is {myMax}")
except ValueError:
    print("Values are not numbers")

except TypeError:
    print("Values are not numbers");

except:
    print("Invalid Input. ")
 """


""" 

'July 19th'
'List Ops'

myNum = [1,2,3]
myNumSq = [x*x for x in myNum]
print(myNumSq)

'July 19th'
'Map functions'

x=[1,2,3,4]

def add(myNum):
    return myNum*2;

y=list(map(add,x));
print (y)
 """
'July 19th'
'Using lambda and Map'

' x=[1,2,4,5,6]'
' squareX= list(map(lambda x:x*x,x));'
' print(squareX)'



'July 18th'
'Lambda Functions'

""" x=10;y=10;
mySum= lambda x,y:x+y;
print(f"Sum is {mySum(x,y)}")
 """

""" 'July 18th'
'Even Odd Calculator'

def EvenOdd(userInput):
    if (userInput%2==0):
        return "Even";
    else:
        return "Odd";

userInput=input("Welcome to Even Odd Program. Do you want to proceed?(y/n)");

while userInput.lower()=="y":
    try:
        UserNumber=input("Enter the number. ");
        EvenOddAns=EvenOdd(int(UserNumber));
        print(f"The number is {EvenOddAns} ");
    
    except TypeError:
        print("Should be a number. ");
    except ValueError:
        print("Should be a number. ");
    userInput=input("Do you want to continue(y/n)?");
 """
'July 18th'
'Perimeter of a Rectangle'
""" 

def calc_perimeter(rectBr,rectHt):
    return 2*float(rectBr)+2*float(rectHt);

userInput=input("Welcome to the calculator game! Do you want to continue(y/n): ")

while userInput.lower()=="y":
    try:
        rectBr=input("Enter the breadth: ");
        rectHt=input("Enter the height: ");
        print(f"Perimeter is {calc_perimeter(rectBr,rectHt)}");
    except TypeError:
        print(" Values must be number. ");
        continue;
    except ValueError:
        print(" Values must be number.");
        continue;
    userInput=input("Do you want to continue?(y/n)  "); 

 """
'July 17th'

""" userInput ="Y"
while(userInput=="y" or userInput =="Y"):
    
    rectLen= input("Enter the length of a rectangle. ");
    rectBdth= input("Enter the bdth of a rectangle. ")

    if (type(rectLen)!=int and float(rectLen) < 0.1) or (type(rectBdth)!=int and float(rectBdth)<0.1):
        print("Invalid length or breadth.")
        userInput=input("Try again, y/n: ");
        if (userInput =="y" or userInput=="Y"):
            continue;
        else:
            print("Thank you for using the calculator!");
            exit;
    else:
        if (type(rectBdth)!=int or type(rectLen)!=int):
            print(f"Perimeter is {2*(float(rectBdth)+float(rectLen))}");    
        else:
            print(f"Perimeter is {2*(int(rectBdth)+int(rectLen))}");
        userInput=input("Try again, y/n: ");
        if (userInput =="y" or userInput=="Y"):
            continue;
        else:
            print("Thank you for using the calculator");
            exit;

 """
