marks=[94.5,87.5,95.4,66.4,44.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

#student details
student = ["karan",97.5,17,"delhi"]
print(student[0])
student[0] = "tarun"
print(student)

#slicing list

marks = [86,98,56,78]
print(marks[1:])
print(marks[:4])
print(marks[-3:-1])

#list method 
list = [3,5,7,8]

list.append(6)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.insert(1,6)
print(list)

list.pop(3)
print(list)

#tuples in python

tup = (2,4,7,8,9)
print(type(tup))

print(tup[2])

tup = ()
print(tup)
print(type(tup))

#method in tuples 

tup1=(2,5,7,9,8)
print(tup1.index(7))

print(tup1.count(9))
