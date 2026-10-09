# #identify number either positive or negative or zero

# num=int(input("Enter a number:"))
# if num>0:
#     print("positive")
# elif num<0:
#     print("Negative")
# else:
#     print("zero")

# # even or odd
# num=int(input("Enter a number:"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

#largest of two numbers
# a=int(input("Enter a value:"))
# b=int(input("Enter a value:"))
# if a>b:
#     print("a is big")
# elif a<b:
#     print("b is big")
# else:
#     print("both are equal")

#collegs adimission

# marks=int(input("Enter marks:"))
# entrance=input("did you pass entrance exam? (yes/no):")
# if marks>=60 and entrance=="yes":
#     print("eligible")
# else:
#     print("not eligible")

#login 

# username=input("Enter a string:")
# password=input("enter a password:")
# if username=="ajay" and password=="password":
#     print("login")
# else:
# #     print("invalid username or passwod")

#diving license

# age=int(input())
# license_valid=input("yes/no:")
# if age>=18:
#     if license_valid=="yes":
#         print("you can drive")
#     else:
#         print("valid license required")
# else:
#     print("too young to drive")

#movie ticket
# age=int(input())
# if age<5:
#     print("free")
# elif 5<=age<=12:
#     print(100)
# elif 13<=age<=59:
#     print(200)
# else:
#     print(120)

#leap year
year=int(input())
if year%400==0:
    print("leap year")
elif year%4==0 and year%100!=0:
    print("leap year")
else:
    print("not a leap year")
