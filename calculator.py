print ("------calculator------")

num1 = float(input("enter a number : "))
num2 = float(input("enter second number here: "))

print ("press 1 for addition\n press 2 for subtraction\n press 3 for multiply\n press 4 for division")

choice = int (input("enter your choice 1-4: "))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else:
    print("Invalid Input")
    


