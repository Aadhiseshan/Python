choice ='Y'
while choice =='Y':
    from random import randint 
    min=1
    max=6
    print("Your Dice Value is:",randint(min,max))

    another_You = input("Enter Yes or No for Continue:")

    choice=another_You.upper()
    if choice != 'Y':
        print("Thank You")
