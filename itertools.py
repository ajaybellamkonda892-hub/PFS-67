#itertools :it provides tools to work with iterators
#it will work on
#1.combinations
#2.permutations
#3.cartesian products
#4.grouping


#count
# import itertools
# numbers=itertools.count(1)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))


# #cycle
# import itertools
# colors=itertools.cycle(["red","green"])
# print(next(colors))
# print(next(colors))
# print(next(colors))



# #permutations
# from itertools import permutations
# nums=[1,2,3]
# result=permutations(nums)
# for item in result:
#     print(item)



#combinations: it selects items where order doestnt matter
# from itertools import combinations
# nums=[1,2,3,4,5,6,7]
# result=combinations(nums,2)
# for item in result:
#     print(item)

#chain 
# from itertools import chain
# a=[1,2,3]
# b=[4,5,6]
# result=chain(a,b)
# for x in result:
#     print(x)

# #datetime module
# from datetime import date
# today=date.today()
# print(today)
# print(today.year)
# print(today.month)

# from datetime import datetime
# now=datetime.now()
# print(now)


#creating specific date
# from datetime import date
# birthday=date(2004,8,23)
# print(birthday)

# #creating date and time
# from datetime import datetime
# dt=datetime(2026,9,26,15,30)
# print(dt)

#represent difference between date and timedelta
# from datetime import date,timedelta
# today=date.today()
# future=today+timedelta(days=10)
# print(today)
# print(future)

# #date difference
# from datetime import date
# date1=date(2004,8,23)
# date2=date(2026,9,26)
# diff=date2-date1
# print(diff)
# print(diff.days)



# #formatting date-strftime()
# from datetime import datetime
# now=datetime.now()
# formatted=now.strftime("%d-%m-%Y")
# print(formatted)

# from datetime import datetime
# date_string="26-09-2026"
# date_object=datetime.strptime(date_string,"%d-%m-%Y")
# print(date_object)


# #Random password generator
# import random
# characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# password=""
# for i in range(53):
#     password+=random.choice(characters) #it will give random password
# print("password",password)



# #including special characters for random password generator
# import random
# characters="@#%^&*()?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# password=""
# for i in range(8):
#     password+=random.choice(characters) #it will give random password
# print("password",password)


#password generator using string

# import random
# import string

# import random
# characters=string.ascii_letters+string.digits+string.punctuation
# password=""
# for i in range(8):
#     password+=random.choice(characters) #it will give random password
# # print("password",password)


# #ATM EXAMPLE :IF,ELIF,ELSE,VARIBLES,INPUT,ARTHEMATIC OPERATION,LOGICAL

# #check pin
# correct_pin=1234
# pin=int(input("enter pin:"))
# if pin==correct_pin:
#     print("access granted")
# else:
#     print("invalid pin")

# #add balance
# balance=10000
# deposit=5000
# pin=int(input("enter pin:"))
# if pin==1234:
#     print("access granted")
#     balance+=deposit
#     print(balance)
# else:
#     print("invalid pin")
    
# #withdraw amount
# balance=10000
# pin=int(input("enter a pin:"))
# if pin==1234:
#     amount=int(input("enter withdraw amount:"))
#     if amount<=balance:
#         balance-=amount
#         print("withdraw succefull")
#         print("remaining balance",balance)
#     else:
#         print("insufficient balance")
# else:
#     print("invalid pin")


#complete atm program
balance=10000
pin=int(input("enter a pin:"))
if pin==1234:
    print("\n1.check balance")
    print("2.withdraw")
    print("3.deposit")
    choice=int(input("enter a choice:"))
    if choice==1:
        print("balance:",balance)
    elif choice==2:
        amount=int(input("enter a amount:"))
        if amount<=balance:
            balance-=amount
            print("Withdraw successfull")
            print("remaining balance:",balance)
        else:
            print("insufficient balance")
    elif choice==3:
        amount=int(input("enter amount:"))
        balance+=amount
        print("deposit sucessfull")
        print("updated balance",balance)
    else:
        print("invalid choice")
else:
    print("invalid pin")