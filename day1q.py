print("hello world")
print("welcome to python programming")
print("my name is tarun")
print("i am learning python programing")
print (29)
print (29+29)
name ="tarun"
age=18
iq =999.9 
#vairable are used to store data in memory and we can use that data later in our program
print("my name is",name)
print("my age is:",age)
print("my iq is:",iq)

# datatypes in python 
print(type(name))
print(type(age))
print(type(iq))

A=None
print(type(A))

#ARETHMETIC OPERATORS
a=50
b=30
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)


#relational operators

x=80
y=70
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

# assignment operator 
z=10
z+=5
print(z)
z-=5
print(z)
z*=5
print(z)
z/=5
print(z)
z//=5
print(z)
z%=5
print(z)
z**=5
print(z)

#logical operators
t=60 
T=70
print (not(t>T))
print("and operator:",T and t)
print("or operator:",T or t)

#type casting
q= "100"
print(type(q))
q=int(q)
print(type(q))

#input function
name = input("enter your name:")
age = input("enter your age :")
print("welcome",name)
print("your age is:",age)
    

# question practice

# 1.write program to input 2 number and print their sum ?

first = input("enter first number:")
second = input("enter second number:")
sum = int(first) + int(second)
print ("sum is",sum)

# 2.write a program to input side of square and print area of square?
side = input("enter side of square:")
area = int(side) * int(side)
print("area of square is:",area)

# 3.write a program to input length and breadth of rectangle and print area of rectangle?
length = input("enter length of rectangle:")
breadth = input("enter breadth of rectangle:")
area = int(length) * int(breadth)
print("area of rectangle is:",area)
 
 # 4.write to input 2 floats points and print their average?
first = input("enter first number:")
second = input("enter second number:")
average = (float(first) + float(second)) / 2
print("average is:",average)
 
# 5.write a program to input 2 integers numbers, A and B. print true if A is greater than or equal to B, otherwise print false?
A = int(input("enter first number:"))
B = int(input("enter second number:"))
print(A >= B)
