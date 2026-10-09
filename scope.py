# #local scope
# def display():
#     name="ajay"
#     age=22
#     print(name)
#     print(age)
# # display()

# # #global scope
# name="ajay"
# age=22
# def diplay():
#     print(name)
#     print(age)
# diplay()

# x=100
# def display():
#     global x   #gobal is used for change the value
#     x=200
# display()
# print(x)

# #pass by value and pass by reference
# def diplay(x):
#     x=20
# a=10
# diplay(a)
# print(a)

# pass by Value
def change(x):
    x=20
    print("inside func:",x)
a=10
change(a)
print("outside func:",a)

#pass by reference
def add_element(data):
    data.append(40)
values=[10,20,30]
add_element(values)
print(values)

#recursion :fuction calling itself
# def count_down(n):
#     #base case
#     if n==0:
#         return
#     #recursive case
#     print(n)
#     count_down(n-1)
# count_down(5)

#factorial
# def fact(n):
#     #base case
#     if n<=1:
#         return 1
#     #recursive case
#     return n*fact(n-1)
# print(fact(5))

#fibanacii
# def fib(n):
#     a=0
#     b=1
#     if n<=0:
#         return
#     for i in range(n):
#         print(a,end=" ")
#         a,b=b,a+b
# fib(10)