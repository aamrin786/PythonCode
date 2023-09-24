num=int(input("Enter a number: "))
for i in range(1,11):
    print(str(num) + "X" + str(i) +"="+str(i*num) )

    # or use f-string
    print(f"{num} X {i} = {num*i}")

#  reverse the multiplication orde:-
num=int(input("Enter a number: "))
for i in range(10,0,-1):
    print(str(num) + "X" + str(i) +"="+str(i*num) )
