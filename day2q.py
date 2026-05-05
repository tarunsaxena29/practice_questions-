# 1. wap to input user's first name and print its length ?

first_name = input("enter your first name")
print("length of your name is", len(first_name))

# 2. wap to find the occurence of '$' in the given string ?

str1 = "this i$ a $tring with$ a lot$ of $ymbols"
print("the number of occurence of $ is ",str1.count("$"))

#3. wap to check if a number is entered by user is even or odd ?

num = int(input("enter a number"))
if(num%2==0):
    print("the number is even")
else:
    print("the number is odd ")

#4. wap to find gretest of three numbers entered by user ?

num1= int(input("enter first number"))
num2= int(input("enter second number"))
num3= int(input("enter third number"))

if(num1>num2 and num1>num3):
    print("the gretest number is ",num1)
elif(num2>num1 and num2>num3):
    print("the gretest number is ",num2)
else:
    print("the gretest number is ",num3)

#5. wap to find greatest of four numbers entered by user ?

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))
num4 = int(input("enter fourth number"))

if(num1>num2 and num1>num3 and num1>num4):
    print("the greatest number is ",num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print("the greatest number is ",num2)
elif(num3>num1 and num3>num2 and num3>num4):
    print("the greatest number is ",num3)
else:
    print("the greatest number is ",num4)
    