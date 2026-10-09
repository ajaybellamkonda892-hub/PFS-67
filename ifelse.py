#conditional statements :exceute or works based on conditions
#if elif else

#if:exceute the code when condition is true
age=22
if age>=18:
    print("eligible")

#else
age=17
if age>=18:
    print("eligible")
else:
    print("not eligible")


marks=int(input())
if marks>=90:
    print("O")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks<70:
    print("F")

#NESTEDIF

age =25
has_id=True
if age>=22:
    print("Age satisfied")
    if has_id:
        print("you can enter")

#atm program : i have did my own this program
card=int(input()) 
if card==123456789012345:
    print("card valid")
    pin=int(input())
    if pin==1234:
        print("valid pin")
        amount=int(input())
        if amount>=1000:
            print("withdraw")
        else:
            print("insufficient balance")
    else:
        print("invalid pin")
else:
    print(" invalid card")


#













