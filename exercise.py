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