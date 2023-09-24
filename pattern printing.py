n=4
for i in range(4):
    print("*" * (i+1))

# print pyramid pattern
for i in range(4):
      print(" " * (n-i-1),end=" ")
      print("*" * (2*i+1),end=" ")
      print(" " * (n-i-1))

#  printing hollow star square
n=4
for i in range(4):
    for j in range(4):
        if(i==0 or i==3 or 
        j==0 or j==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# print reverse of the first one
n=6
for i in range(6):
    print("*"*(n-i))