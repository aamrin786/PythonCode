num = int(input("Enter a number"))
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
print("Factorial is: ",factorial)

# using recursion
def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    return n*factorial_recursive(n-1) #recursion
num = int(input("Enter a no. :"))
f = factorial_recursive(num)
print(f,"is the factorial of",num)