# #expectionhandling
# try:                                  #try block thar any cause of erroe
#     num=int(input("enter a value:"))
#     print("you entered:",num)
# except ValueError:                     #except block code handle the error 
#     print("please enter valid no.")


#zero division error
# try:
#     a=10
#     b=0
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divide by zero")



# try:
#     a=int(input())
#     b=int(input())
#     result=a/b
#     print("result:",result)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("valid number")
# finally:                             #it will give output when error may occur
#     print("done")        





# try:
#     a=int(input())
#     b=int(input())
#     result=a/b
#     print("result:",result)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("valid number")
# else:
#     print("done with calculations")
# finally:                             #it will give output when error may occur
#     print("done") 

try:
    age=int(input("enter a age:"))
    if age<0:
        raise ValueError("age cant be negative")
    print("age",age)
except ValueError as g:
    print("value")