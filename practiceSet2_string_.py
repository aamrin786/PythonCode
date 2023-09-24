# write a python program to display a user control name followed by the word "Good Afternoon"
name = input("Enter your name: ")
print("Good Afternoon,",name,"!!")

#making a letter(question->check copy)
letter = '''Dear <|Name|>
You are selected!

Date: <|Date|>'''
name = input("Enter Name:")
date = input("Enter date:")
letter = letter.replace("<|Name|>",name)
letter = letter.replace(" <|Date|>",date)
print(letter)

#find double spaces
a = "I am  Aamrin"
print(a.find("  "))