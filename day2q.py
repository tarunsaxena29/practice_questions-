str1="this is a string"
str2="this is another string"
str3="this is another string"
 
#escape sequences
#1. \n 
str = "this is a string\nthis is another string"
print(str)
#2. \t
str5 = "this is a string\tthis is another string"
print(str5)

#basic string operations
#1. concatenation
print(str1+str2)

#2. length of string
print(len(str1))

#3. indexing 
print(str5[5])

#4. slicing
print(str5[2:9])

## string functions 
str7="i am a coder"

#1. endwith
print(str7.endswith("der"))

#2. startwith
print(str7.startswith("i am"))

#3. capatalize
print(str7.capitalize())

#4. rerplace
print(str7.replace("coder","programmer"))

#5. find
print(str7.find("a"))

#6. count 
print(str7.count("a"))

# conditional statements
 
light = "yellow"

if (light == "red"):
    print("stop")
elif(light=="yellow"):
    print("get ready")
elif(light=="green"):
    print("go")
else:
    print("light is not working")


marks = int(input("enter your marks"))
if(marks>=90):
   print("grade A")
elif(marks>=80 and marks<90):
    print("grade B")
elif(marks>=70 and marks<80):
    print("grade C")
else:
    print("grade D")

# question practice 

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
    
