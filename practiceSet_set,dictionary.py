# find meaning of hindi word from a dictionary
myDict={"Pankha":"Fan","Dabba":"Box","Vastu":"Item"}
print("Options are:",myDict.keys())
a = input("Enter the Hindi word: ")
print("The meaning of the word is :",myDict[a])
print("The meaning of the word is :",myDict.get(a))

# print unique numbers
num1=input("Enter no 1;")
num2=input("Enter no 2;")
num3=input("Enter no 3;")
num4=input("Enter no 4;")
num5=input("Enter no 5;")
num6=input("Enter no 6;")
S = {num1,num2,num3,num4,num5,num6}
print(S)

# printing len of a set
S = set()
S.add(20)
S.add(20.0)
S.add("20")
print(S)
print(len(S))

             # **************************************
# in a input dictionary input 4 languages as values and name as keys
favLang={}
a=input("Enter your favourite language Riya:\n")
b=input("Enter your favourite language Raj:\n")
c=input("Enter your favourite language Ram:\n")
d=input("Enter your favourite language Jerry:\n")
favLang["Riya"]=a
favLang["Raj"]=b
favLang["Ram"]=c
favLang["Jerry"]=d
print(favLang)