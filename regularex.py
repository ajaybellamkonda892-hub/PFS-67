#regular expression -search looks for a pattern anywhere inside
# #string
#re.search
# import re
# text="i am learning python"
# result=re.search("python",text)
# print(result)

#we need to use search when we want to know as "does this pattern occur somewhere in text"

# #re.match() : it checks the pattern only at begining
# import re
# text="i am learning python"
# result=re.match("python",text)
# print(result)

# #re.fullmatch() : it requires entire string to match the pattern
# import re
# text="python"
# result=re.fullmatch("python",text)
# print(result)

#re.findall(): it finds all occurences of a pattern and return then as  a list
#\d=digits(0to9)
#\d+ = combination of one or more digits
# import re
# text="i have 10 apples and 20 oranges"
# result=re.findall(r"\d+",text)
# print(result)

#\w - word characters
#letters,digits,underscores
# import re
# text="python_123"
# result=re.findall(r"\w",text)
# print(result)

# ^ - start of string
# # the pattern must start at beginning

# import re
# pattern=r"^python"
# print(re.search(pattern,"python is easy"))

# $ - dollarm - it represent pattern must end at the end of string
# import re
# pattern=r"python$"
# print(re.search(pattern," is easy python")
# 
# #quatifiers - it tells regex how many times something can occur
# '* ,+,?,{}

#* - zero or more
#r"ab*" - a,ab,abb,abbbb,abbbbb......

#+ -one or more
#r"ab+" - ab,abb,abbb,abbbb,abbbb.....

#? - zero or more
# r"colou?r"-color,colour

# {} - exact number
# r"^\d{4}$"-means exctaly 4 digits

#digits validations
# import re
# value=input()
# pattern =r"^\d+$"
# if re.fullmatch(pattern,value):
#     print("only digits")
# else:
#     print("invalid")


#phone number validations
# import re
# phone=input("Enter number: ")
# pattern =r"^[6-9]\d{9}$"
# if re.fullmatch(pattern,phone):
#     print("valid")
# else:
#     print("invalid")

#email validations
# import re
# email=input("enter mail: ")
# pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
# if re.fullmatch(pattern,email):
#     print("valid")
# else:
#     print("invalid")

# import re 
# name=input("enter name: ")
# password=input("enter password: ")
#name
# if re.fullmatch(r"[A-Za-z]+",name):
#     print("valid")
# else:
#     print("invalid")
# #password
# pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
# if re.fullmatch(pattern,password):
#     print("valid")
# else:
#     print("invalid")
