# file=open("student.txt","r")
# data=file.read()
# print(data)
# file.close()

# #readline:it reads only one line
# file=open("student.txt","r")
# data=file.readlines()
# print(data)
# file.close()

# #read lines- read all the lines and returns those as a list
# file=open("student.txt","r")
# data=file.readlines()
# print(data)
# file.close()

# #writing a file
# file=open("student.txt","w")
# file.write("ajay\n")
# file.close()

# #append mode
# file=open("student.txt","a")
# file.write("\nkiran")
# file.close()

#with open():
# with open("student.txt","r") as file:
#     data=file.read()
#     print(data)

# #writing using withopen
# with open("student.txt","w") as file
#     file.write("rahul\n")


# #reading line by line
# with open("student.txt","w") as file:
#     for line in file:
#         print(line.strip())



#real time exmpale
# name=input("enter student name:")
# age=input("enter age:")
# course=input("enter course:")
# with open("student.txt","a") as file:
#     file.write(f"Name:{name}\n")
#     file.write(f"Age:{age}\n")
#     file.write(f"Course:{course}\n")
# print("student details saved succesfully.")

#atm
balance = 10000

try:
    amount = int(input("Enter withdraw amount: "))

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount

        with open("transactions.txt", "a") as file:
            file.write(f"Withdrawn: {amount}\n")
            file.write(f"Rem bal: {balance}\n")

        print("Success")
        print("Rem bal:", balance)

except ValueError as e:
    print("Error:", e)