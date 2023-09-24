fruits = ["Apple","Banana","Grapes","Pineapple"]
for item in fruits:
    print(item)

for i in range(0,8):
    print(i)
# using step_size
for i in range(0,8,2):
    print(i)
#even no print
for i in range(11):
    if i%2==0:
         continue
    print(i)