# Progect1
numbers = [1,2,3,4,5,6,7,8,9,10]
for x in numbers:
   if x%2 ==0:
       print(f"\n{x}")
print("Finished the loop successfully" )

#Project 2
tasks = input("Enter your tasks for today separated by commas:\n").split(", ")
comleted = []
uncompleted =[]
for task in tasks:
    Q = input(f"Did you finish {task} alredy\n")
    if Q.lower()=="yes":
      comleted.append(task)
      print("Nice job\n----------")
    elif Q.upper()=="NO":
       uncompleted.append(task)
       print("Try not to put it off\n-----------")
    else:
       print("Invalid entaring")
prog = input("Do you want to see your today's progress?(Yes, no)\n")
if prog.lower() == "yes" :
   print(f"***** Done Tasks *******\n{comleted}\n******* Ongoing Tasks *******\n{uncompleted}")
else:
   input("Please hit enter to exit")
     
#Project3
print("*** Welcome to the multiplication table ***")
num =int(input("Enter a number:\n"))
print(f"Multiplication table for {num} :")
for number in range(1,11):
    val =number*num
    print(f"{num} x {number} = {val}")
  
      

#6 Project4
print("*** Welcome to iShop calculator ***")
many= int(input("How many items are there in your basket today?\n"))
basket = []
prices = []

if many > 0 :
   print("let's get to counting them ...\n")
   for  ip in range(1,many+1):
    names = input(f"please tell me the name of item number {ip}\n")
    basket.append(names)
    price = float(input(f"What is the price of {names}\n"))
    prices.append(price)
   know_basket=input("Would you like to see entire basket items? \n").lower()
   if  know_basket  =="yes" :
    print(basket)
    know_price=input("Would you like to see how much it'll cost?\n")
    if know_price.lower()=="yes":
       print(f"Buying these items will cost:\n{sum(prices)}")
    else:
      input("Prress enter to exit")
   else :
    input("Press Enter to exit")
  
else :
  print("Seems like you're not in the mood for shopping today")
  
#P5 , my solution
names = input("Enter the names\n")
names_list = names.split(", ")
abbreveted_name = []
for name in names_list :
   names_part = name.split()
   print( names_part)
print("Abbrrevted Names")
for name in names_list :
   names_part = name.split()    
   print(f"{ names_part[0][0]}.{ names_part[1][0]}.")


#P5 , The teacher's solution
names_list=input("Enter the name seperated by a comma:\n").split(", ")
Abbreviated_names = []
for name in names_list:
   names_part = name.split()
   print(names_part)
   first_name = names_part[0]
   last_name = names_part[1]
   first_initial = first_name[0]
   last_initial = last_name[0]
   Abbreviation = f"{first_initial}.{last_initial}."
   Abbreviated_names.append(Abbreviation)
print("Abbreviated names")
x = f"{first_initial}.{last_initial}."
for x in Abbreviated_names:
   print(x)
sentence = input("Enter a sentence:\n").split()
Reverced_list=sentence[::-1]
Reverced_sentence=" ".join(Reverced_list)
print(Reverced_sentence)
import string
sentence = input("Please type a sentence:\n")
new_sentence=""
for x in sentence:
    if x not in string.punctuation:
     new_sentence +=x
print(new_sentence)



#Unit 6 main project
import string
import random
print("Welcome to the Password Generator! ")
length=[]
Pass_random=[]

char=int(input("Enter the totlal numbers of characters in the password:\n"))




let =int(input("Enter the total numbers of letters in the password:\n"))
length.append(let)


num=int(input("Enter the total numbers of numbers in the password:\n"))
length.append(num)


sym=int(input("Enter the total numbers of symbols in the password:\n"))
length.append(sym)



if sum(length) == char:
 rand_let = random.choices(string.ascii_letters, k=let)
 Pass_random.extend(rand_let)
 rand_num = random.choices(string.digits, k=num)
 Pass_random.extend(rand_num)
 rand_sym = random.choices(string.punctuation, k=sym)
 Pass_random.extend(rand_sym)
 random.shuffle(Pass_random)
 print(f"Generated Password " + "".join(Pass_random))
else:
  print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password")