num1=int(input("Enter first number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))
num4=int(input("Enter 4th number: "))

if(num1>num2 and num1>num3 and num1>num4):
    print("The greatest no is:",num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print("The greatest no is: ",num2)
elif(num3>num1 and num3>num2 and num3>num4):
    print("The greatest no is: ",num3)
else:
    print("The greatest no is: ",num4)

# or this method
if(num1>num2):
    f1=num1
else:
    f1=num2
if(num3>num4):
    f2=num3
else:
    f2=num4
if(f1>f2):
    print(f1,"is the greatest")
else:
    print(f2,"is the greatest")
 