# #fuction creations
# def greet():
#     print("hello") #function body
# greet()   #function calling

# # type1:no parameter,no return value
# def greet():
#      print("hello") #function body
# greet()  

# #typr2: parameter,no return value
# def greet(name):
#     print("hello",name)
# greet("ajay")

# #type3:no parameter,with return value
# def get_number():
#     return 100
# result=get_number()
# print(result)

# #type4: parameter,return value
# def add(a,b):
#     return a+b
# print(add(2,3))

# #retuning multiple values
# def cal(a,b):
#     add=a+b
#     sub=a-b
#     return add,sub
# x,y=cal(2,3)
# print(x)
# print(y)

#positional aruguments
# aruguments are matched based on their position
#oredered is very important
# def student(name,age):
#     print("Name:",name)
#     print("Age:",age)
# student("ajay",22)

#keyword arugments
# def student(name,age):
#     print(name)
#     print(age)
# student(age=22,name="ajay")

# # default aruguments
# def greet(name="student"):
#     print("hello",name)
# greet("codegnan")

# #varible-length og aruguments(*args)
# def add(*numbers):
#     total=0
#     for number in numbers:
#         total +=number
#     return total
# print(add(10,20))
# print(add(10,20,30,40,50))

#keyword variable length aruguments(**kwargs)
#accept multiple key words
# def student_details(**details):
#     print(details)
# student_details(
#     name="ajay",
#     age=22,
#     city="nrt"
# )

def example(*args,**kwargs):
    print(args)
    print(kwargs)
example(10,20,30,name="ajay",age=22)