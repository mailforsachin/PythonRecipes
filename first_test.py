#July 20th-July 21 2024

'''
print("### Test 1 ### 1. Basic Syntax, Print and Comments. Print \"Hello, World!\" to the console. \n Write comments explaining what the code does. ")
print ("Hello, World")
#Printing Hello World
# Printing Hello World
print("\n### Test 2 Create variables of different data types (integer, float, string, boolean) and print them. \n Swap the values of two variables without using a third variable.")
my_boolean= True;
print(type(my_boolean), my_boolean);

my_integer= 1;
print(type(my_integer), my_integer);

my_float=0.1;
print(type(my_float), my_float);

my_string= "Sachin"
print(type(my_string), my_string);

my_integer,my_float= my_float, my_integer;
print(my_integer, my_float)

print("""\nTest 3. **Basic Input/Output** Write a program that takes input from the user for their name and prints \"Hello, [name]\". 
Write a program that takes input for two numbers and prints their sum.""")

#user_name= input("Enter your name: ")
#print (f"Hello, {user_name}");

#try:
    #number_1= input("Enter the 1st number: ");
    #number_2= input("Enter the 2nd number: ");
    #print(int(number_1)+int(number_2));

#except NameError:
#    print("It has to be a number");

#except ValueError:
#    print("It has to be a number");

user_number= input("Enter the number. ")

if int(user_number) in range(21):
    print ("Yes")
else:
    print ("No")

'''

""" my_counter= 0;
while (int(my_counter) <=10):
    print(my_counter);
    my_counter=my_counter+1; """

""" for i in range(10):
    print(i+1) """

""" for i in range(10):
    if i == 3:
        continue;
    else:
        print(i+1); """

""" for i in range(10):
    if i == 4:
        break;
    else:
        print(i+1); """

