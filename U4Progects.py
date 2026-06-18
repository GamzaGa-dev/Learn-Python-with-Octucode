#[first project
import random
print("Welcome to the Coin Guessing Game!")
cho = int(input("Chose a method to guess the coin\n1. Using random.random\n2.Using random.randint\n Enter your choise\n"))
if cho == 1 :
    
    guess1 =input("Enter your Guess (Heads or Tails):\n")
    pchois = random.random()
    if  pchois>=.5 :
      if  guess1.lower() == "heads" :
        print("Congratulations! You won\nThe computer choise was : Heads" )
      elif guess1.lower() == "tails":
        print("Sorry You lost! \nthe computer choise was : Heads" )
      else:
        print("Incorrect choise , Only (Heads or Tails) ")
    elif pchois <.5 :         
       if  guess1.lower() =="tails":
         print("Congratulations! You won\n The computer choise was : Tails" )
       elif guess1.lower() == "heads":
         print("Sorry You lost! \n the computer's choise was : Tails" )
       else:
         print("Incorrect choise , Only (Heads or Tails) ")
elif cho ==2 :
    pchois =random.randint(1,2)
    guess2 =input("Enter your Guess (Heads or Tails):\n")
    if  pchois==1:
      
     if  guess2.lower() == "heads" :
        print("Congratulations! You won\n The computer choise was : Heads " )
     elif guess2.lower() == "tails":
        print("Sorry You lost! \n the computer's choise was : Heads" )
     else:
        print("Incorrect choise , Only (Heads or Tails) ")
    elif pchois ==2 :
      
     if  guess2.lower() == "tails" :
        print("Congratulations! You won\n The computer choise was : Tails " )
     elif guess2.lower() == "heads":
        print("Sorry You lost! \n the computer's choise wae : Tails")
    else:
        print("Incorrect choise , Only (Heads or Tails) " \
        "" \
        "")
else :
 print("""Incorrect choise
   
       """)

  #second project    
st = input("press Enter to start the second project")
libown = []
own_book = input("Enter the name of a book you own:\n")
libown.append(own_book)
own_book2 = input("Enter a name of another book you own (or press Enter to skip)\n")
if own_book2 :   
 libown.append(own_book2)
 print(f"Yuor library is {libown} ")
else :
 print(f"Yor library is {libown}")
libwish = []
wish_book = input("Enter the wish of a book you wish to have in the future\n")
libwish.append(wish_book)
wish_book2 = input("Enter the name of another book you wish to have (or press Enter to skip)\n")
if wish_book2 :
 libwish.append(wish_book2)
 print(f"Your list wish is {libwish}")
else :
 print(f"Your list wish is {libwish}")
wishown = input("Enter a book from your Wishlist that you've owned (or press 'Enter' to skip)\n")
if wishown in libwish :
 libwish.remove(wishown)
 libown.append(wishown)
 print(f"Update library: {libown} \nUpdate wish list: {libwish} ")
else:
  print("The book is not in your library\n")
  print(f"Update library: {libown} \nUpdate wish list: {libwish} ")


don = input("Enter the of a book from your library you wish to donate (or press Enter to skip)\n")
if don in libown :
 libown.remove(don)
 print(f"Final library after Donations: {libown}")
else:
  print("The book is not in your library")
  print(f"Final library after Donations: {libown}")

 


    
    