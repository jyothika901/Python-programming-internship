
print("simple calculator")
a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
print("choose operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice=input("enter your choice(1-4)")
if choice=="1":
        print("result=",a+b)
elif choice=="2":
        print("result=",a-b)
elif choice=="3":
        print("result=",a*b)
elif choice=="4":
        if b!=0:
                print("result=",a/b)
        else:
                print("division by zero is not possible!")
                print("Invalid choice")