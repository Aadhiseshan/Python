repeat='Y'
print("\n\t\t\t\t  Basic Calculator")
print("\n\t\t **********************************************************")


while repeat =='Y':
    num1=float(input("Eneter the No: "))
    operator=input("Enter your operators +,-,*,/,%,^ : ")
    num2=float(input("Enter the no: "))

    if operator =="+":
        ans=num1+num2
        print(num1," + ",num2," = ",ans)
        
    elif operator =='-':
        ans=num1-num2
        print(num1," - ",num2," = ",ans)

    elif operator =='*':
        ans=num1*num2
        print(num1," x ",num2," = ",ans)

    elif operator =='/':
        ans=num1/num2
        print(num1," / ",num2," = ",ans)

    elif operator =='%':
        ans=num1%num2
        print(num1," % ",num2," = ",ans)

    elif operator =='^':
        ans=num1**num2
        print(num1," x^ ",num2," = ",ans)

    else:
        print("Sorry! Please Check Your Operator")

    choice=input("Enter Y or N for continue the calculation: ")

    repeat=choice.upper()

    if repeat!='Y':
        print("Thank You")

