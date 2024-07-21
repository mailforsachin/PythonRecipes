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


""" def whats_my_name(name):
    print(f"Hello {name}");

enter_your_name = input("Whats your name? ")
whats_my_name(enter_your_name);
 """

""" def sum(a,b):
    return print(a+b);

try:
    enter_your_two_numbers = input ("Enter two numbers followed by spaces. ")
    enter_your_two_numbers = enter_your_two_numbers.split();
    sum(int(enter_your_two_numbers[0]), int(enter_your_two_numbers[1]));
except NameError:
    print("Enter numbers please")

except ValueError:
    print("Enter numeric value please") """

""" 
try:
    x=input("Enter your number. ")
    final_number= lambda x:x+10;
    print(final_number(int(x)));
except NameError:
    print("Incorrect Identifier");
except ValueError:
    print("Incorrect Value") """


""" my_list = [1,2,3,4,5]

my_new_list=list(map(lambda x:x+1,my_list))

print(my_new_list) """
""" 
my_list =[];

def add_to_list(new_num):
    my_list.append(new_num);
    print(my_list)

def remove_from_list():
    my_list.pop()
    print(my_list)

def sort_the_list():
    my_list.sort();
    print(my_list)

def find_max_from_list():
    return print (max(my_list))

your_ans="y"
while (your_ans.lower()=="y"):

    
    my_task= input("What do you wana do? add-1,remove-2,find_max-3, sort-4")

    if (int(my_task)==1):
        my_num=input("Enter the number. ")
        add_to_list(my_num)
    elif (int(my_task)==2):
        remove_from_list()
    elif (int(my_task)==3):
        find_max_from_list();
    else:
        sort_the_list()
    
    your_ans=input("Do you want to continue?(Y/N)") """


""" #List comprehension

my_list=[1,2,3,4,5]
my_new_list=[num*2 for num in my_list]
print(my_new_list) """

""" my_list=["sachin", "tewari"]
my_new_list=[my_list[::-1] for my_list in my_list]
print(my_new_list) """

""" my_list =[1,2,3,4,5]
my_new_list = [num for num in my_list if num %2==0 ]
print(my_new_list) """

#curly dict, rountuple, squarelist

""" my_dict = ("this", 1, "is", True);
print(type(my_dict))
print(list(my_dict));
print(type(my_dict)) """

""" 
#set doesnt allow duplicates
my_set=set(["1","1","1"])
print(my_set) """

#dictionary
""" 
my_dictionary = {"Leader":{"name": "John", "age": 28, "occupation": "teacher"}, "Doctor" :{"name": "Jane", "age": 32, "occupation": "doctor"}, 
"Engineer": {"name": "Bob", "age": 25, "occupation": "engineer"}}

print(type(my_dictionary));
#print(my_dictionary["Leader"]["name"]);

for key, value in my_dictionary.items():
    print (value["name"])
 """
#vowel or not

""" my_string = "aerious"

my_vowel_count=0;
my_vowel_list =[];
for strings in my_string:
    if strings in {"a","e", "i", "o", "u"}:
        if strings not in my_vowel_list:
           my_vowel_count=my_vowel_count+1;
           my_vowel_list.append(strings)
print(my_vowel_count)
print(my_vowel_list) """

#palindrome
""" 
input_str="saippuakivikauppias"
check_str=input_str[::-1]
if (input_str==check_str):
   print("Palindrome")
else:
    print("Not a palindrome")

#Alt
input_str="saippuakivikauppias"
print("Palindrome" if input_str == input_str[::-1] else "Not a palindrome")  """