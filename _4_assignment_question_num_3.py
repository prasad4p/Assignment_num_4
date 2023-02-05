# Assignment_number_4
# Question_number_3 = Write a Python program to square the elements of a list using map() function.



def square_num(n):
  return n ** 2

size  = int(input("enter the size : "))
lst = []
for i in range (size):
    element = int(input("enter the element : "))
    lst.append(element)

print("Original list : ",lst)

data = map(square_num, lst)

print("Square of elements in a list :" , list(data))