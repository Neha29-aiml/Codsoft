import random
print("----------Welcome to Rock Paper Scissor----------")
user_score = 0
comp_score = 0
ties = 0
name = input("Enter your name here: ")
print('''Winning Rules:
1. Paper vs Rock---> Paper
2. Rock vs Scissors---> Rock
3. Scissors vs Paper---> Scissors''')
print()
print ( '''Choices are:
1. Rock
2. Paper
3. Scissors''')
choice = int(input("enter your choice from 1-3: "))
print()
while choice >3 or choice < 1:
       choice = int(input("enter valid input"))
if choice == 1:
      user_choice = "Rock"
elif choice==2:
      user_choice ="Paper"
else:
       user_choice ="Scissors"
print("The user's choice is", user_choice)
print("Now it is computer's turn")

computer = random.randint(1,3)
if computer == 1:
       comp_choice = "Rock"
elif computer == 2:
       comp_choice = "Paper"
else:
       comp_choice = "Scissors"

print("The computer choice is",comp_choice)   

if ((user_choice =="Paper"  and comp_choice == "Rock") or (user_choice =="Rock" or comp_choice == "Paper")):
       print("Paper wins")
       result = "Paper"
elif((user_choice =="Scissors"  and comp_choice == "Rock") or (user_choice =="Rock" or comp_choice == "Scissors")):
       print("Rock wins")
       result = "Rock"
else:
       print("Scissors wins")
       resul = "Scissors"
print("Play Again")