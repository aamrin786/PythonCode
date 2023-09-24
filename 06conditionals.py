# if-elif-else lader(in this case you can print only the first true statement)
a=45
if(a>3):
    print("The value is greater than 3")
elif(a>7):
    print("The value is greater than 7")
else:
    print("The value is greater than 3,7")

 # multiple if cases(in this case you can print multiple true conditions)
if(a>3):
    print("The value is greater than 3")
if(a>7):
    print("The value is greater than 7")
else:
    print("The value is greater than 3,7")

# Q| print yes if user given age is greater than or equal to 18
age=int(input("Enter age: "))
if(age>=18):
    print("yes")
else:
    print("no")