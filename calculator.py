print("<<<<  SIMPLE CALCULATOR >>>>")

print ("Select an operation from the following : ")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Division (/)")
print("4. Multiplication (*)")
while True:
    try:
        
            num1=float(input("Enter the first Number : "))
            num2=float(input("Enter the second Number : "))
            break
    except ValueError:
        print("Please enter a valid input.")
while True:
    try:
        choice= int(input("Enter your choice : "))
        if 1<= choice <=4:
            break
        else:
            print("Please enter a valid choice(1-4).")

    except ValueError :
        print("The choice should be integers(1-4) only .")
    
if choice==1:
    result=num1+num2
    print("The sum of these two numbers is : ",result)
elif choice==2:
    result=num1-num2
    print("The difference of these two numbers is : ",result)
elif choice==3:
    if  num2==0:
        print("Division  by zero is not possible.")
    else:
        result=num1/num2
        print("The division of these numbers is : ",result)
elif choice == 4:
    result=num1*num2
    print("The product of these numbers is : ",result)
