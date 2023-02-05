# Assignment_number_4
# Question_number_2 = Write a Python program to triple all numbers of a given list of integers. Use Python map.



size  = int(input("enter the size : "))
lst = []
for i in range (size):
    element = int(input("enter the element : "))
    lst.append(element)

print("original list : ", lst)

data = map(lambda x: x * 3, lst)

print("Triple of all number in a list :", list(data))