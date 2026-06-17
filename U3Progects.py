#المشروع الاول
print("welcome to my app")
age = int(input ("How old are you\n"))
if age >= 12 :
    print("you can use the app")
else : 
    print("you can not use the app")
# المشروع الثاني
num = float (input ("enter your number\n"))
if num > 0 :
    print("your number is possitive")
elif num < 0 :
    print (" your number is negative")
else :
    print("your number is zero")
#المشروع الثالث
score = float(input("What is your degree?\n"))
if score >= 90 :
    print("privilege")
elif score >=75 :
    print("good")
elif score >= 50 :
    print("accepted")
else  :
    print("failed")
#المشروع الرابع
password = input("enter the password\n" )
if password == "welcom" :
 print("your welcom")
else :
 print( " Sorry , the pass word is wrong")
#المشروع االخامس
word = input("write 'yes . no . maybe \n")
if word == "yes" :
    print(f"[word]")
elif word == "maybe" :
    print("f[word]")
elif word == "no" :
    print("f[word]")
else :
    print("that is wrong")
#المشروع الخامس
gussed = int(input("Guess the number\n"))
num = 7
if gussed ==num :
    print(f" You are right the number is{gussed}")
else :
    print(f"Wrong number you entered {gussed} but the right number is {num}") 
#المشروع السابع
area = input("Chose an area : (Gaza) , (Rafah) , (Khanyouness) \n ")
if area.lower() == "gaza" :
 print("You chose Gaza")
elif area.upper() == "RAFAH" :
 print("You chose Rafah")
elif area.lower() == "khanyouness" :
 print("You chose Khanyouness")
else :
 print("Wrong choise ")
 #المشروع الثامن
area = input("Choose an area (Rafah) , (Khanyouness) , (Gaza)\n")
if area.lower() == "gaza" or area.lower() == "rafah" or area.lower() == "khanyouness" :
    print( " your welcome")
else:
    print("that is not on our list")
#المشروع التاسع
print("Welcome\n")
age = int(input("How old are you?\n"))
lin = input("Do you have a linces\n")
if age >= 18 and lin.lower() == "yes" :
    print(" you can drive")
elif age < 18 or lin.lower() == "no" :
 print("You can not drive")
else:
   print("Wrong entery")
#المشروع العاشر
is_pal = input("Are you palesteenian?\n").lower()
if is_pal == "yes" :
    print("Ok , to the next step")
    age_18 = input("are you above 18 years old? (yes) or (no)\n")
    if age_18.lower() == "yes" :
     print("You can have ID ")
    elif age_18 == "no" :
       print("Please try again when you are 18")
    else:
       print(" wrong entery")
elif  is_pal == "no" :
   print("Sorry , this ID is given only to palesteenian")
else :
   print("wrong entery")
#المشروع الحادي عشر
print(""" 
Welcome to my island
There are tow doors in front of you . a red door and a blue door  """)
door = input("Which door do you want to open ?\n").lower()
if door == "red" :
    print("Great , you now entered the room")
    box = input("You found three boxes green , black , white Which box do you want to open? \n").lower()
    if box == "green" :
        print("Congratulations! You found the trasure!")
    elif  box == "white":
        print("Oops! you entered a box filled with snakes")
    elif box == ("black") :
        print("Oops! You opened a box filled with spiders")
    else:
        print("Wrong choise")
elif door == "blue":
  print("Oops! You chose the crocodile door\nGame over")
else : 
    print(" Wrong choise")

