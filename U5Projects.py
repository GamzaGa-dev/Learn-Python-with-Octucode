# First projects, my solution 
print("Welcome to the 'who's wallet'?")
print("You will give me a list of names , and I will pick a person to pay")
names =input("If you're ready , enter the names separated by comma ")
names_LIST = names.split(", ")
import random
payer = random.randint(0,len(names_LIST)-1)
chosen = names_LIST[payer]
print(f"please ask {chosen} to pay ")
#First project, the teacher's solution
import random
print("Welcome to the 'whse wallet'?")
print("You will give me a list of names , and I will pick a person to pay")
print(f"please ask {random.choice(input("If you're ready , enter the names separated by comma ").split(", "))} to take out his wallet, dinner is on him")
#Third project
basket = [["Apples", "Bananas"], ["Milk", "Water"]]
print(basket)
input("Press enter to change the content ......")
basket[0].insert(0,"Oranges")
basket[0].append("Kiwis")
basket[1].remove("Water")
basket[1].insert(0,"Coffee")
basket[1].append("Tea")
basket.append([1,2,3])
print(basket)
#fourth My solution
print("Welcome to the palace rabbit\n")
t1 =["tree","tree","tree"]
t2 =["tree","tree","tree"]
t3 =["tree","tree","tree"] 

enter = input("Where the rabbit go?\n Please choose a arow and a colum \n")
en=int(enter[0])
en1=int(enter[1])
num=int(enter)
if (num ==11) or (num ==12) or (num == 13) or (num == 21) or (num == 22) or (num == 23) or (num == 31) or (num == 32) or (num == 33): #brakets is not important
 if en== (1) :
    if en1==1:
        t1.remove("tree")
        t1.insert(0,"rabbit")
    elif en1==2 :
        t1.remove("tree")
        t1.insert(1,"rabbit")
    elif en1== 3:
        t1.remove("tree")
        t1.append("rabbit")
 elif en==2 :
    if en1 == 1:
        t2.remove("tree")
        t2.insert(0,"rabbit")
    elif en1== 2 :
        t2.remove("tree")
        t2.insert(1,"rabbit")
    elif en1 ==3:
        t2.remove("tree")
        t2.append("rabbit")
 elif en ==3:
    if en1== 1:
        t3.remove("tree")
        t3.insert(0,"rabbit")
    elif en1==2:
        t3.remove("tree")
        t3.insert(1,"rabbit")
    elif en1==3:
        t3.remove("tree")
        t3.append("rabbit")
 print(f"{t1}\n{t2}\n{t3}")        

else:
    print("Eror value!!!")


#Fourth the teacher's solution        
print("Welcome to the place the rabbit")
feiled = [["tree","tree", "tree"],["tree", "tree", "tree"],["tree", "tree","tree"]]
print(f"{feiled[0]}\n{feiled[1]}\n{feiled[2]}\n")
print("Where should the rabbit go? rabbit")
enter =input("please chose a row and a colum\n")
if len(enter)==2:
 row = int(enter[0])-1
 colum = int(enter[1])-1
 feiled[row][colum]= "rabbit"
 print("Success....\n\n") 
else:
 print("feild, Enter correct data")
print(f"{feiled[0]}\n{feiled[1]}\n{feiled[2]}\n")
#project of Unit
import random
print("Welcome to the Rock, Paper, Scissors game:")
hel = input("Press Enter to continue or type (Help) for the rules\n")
if hel.lower() =="help":
    print("         *********  RULES  *********")
    print("         1) You chose and the computer chosees\n         2) Rock smashes Scissors -> Rock win\n         3) Scissor cut Paper -> Scissor win\n         4) Paper covers Rock -> Paper wins\n")
game = ["Rock", "Paper", "Scissors"]
en  = input("Enter your choise (Rock, Paper, Scissors):").capitalize()
co = random.choice(game)

if en in game :
    if co == en :
        print("Draw")
    elif (
    
    
    (en == game[0] and co == game[2]) 
     or
    (en == game[1] and co == game[0])    
     or
    (en == game[2] and co == game[1])
    ):
     print("You win")
          
    else :
         print("you lose")
else :
 print("Wrong choise?")




