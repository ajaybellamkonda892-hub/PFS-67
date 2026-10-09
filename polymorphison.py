#polymorphism:one name,many forms
#poly - many
#morphism - forms
#in python ,polymorphism means the same method, function or operator can behave differently depending on the object or data being used

# class dog:
#     def sound(self):
#         print("dog barks")
# class cat:
#     def sound(self):
#         print("cat meow")
# d=dog()
# c=cat()
# d.sound()
# c.sound()

#types of polymorphism
#method overloading
#method overriding
#operator overloading


#method overriding : it occurs when a class provides it's own implementation of a method
#that already exists in parent class

# class animal:
#     def sound(self):
#         print("animal make sound")
# class dog(animal):
#     def sound(self):
#         print("dog barks")
# class cat(animal):
#     def sound(self):
#         print("cat meow")
# d=dog()
# c=cat()
# d.sound()
# c.sound()


#method overloading:having multiple methods with same and different parameters

# class calculator:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
# calc=calculator()
# calc.add(10,20)
# calc.add(10,20,30)


#default arguments
# class calculator:
#     def add(self,a,b,c=0):
#         return a+b+c
# calc=calculator()
# print(calc.add(10,20))
# print(calc.add(10,20,30))


# #using *args
# class calc:
#     def add(self,*args):
#         return sum(args)
# c=calc()
# print(c.add(10,20,30))
# print(c.add(10,20,30,40))


#operator overloadinging : it means giving operators such as +,-,l*, etc special behaviour 
#for our own objects

# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self, other):
#         return point(
#             self.x+other.x,
#             self.y+other.y
#         )
# p1=point(10,20)
# p2=point(30,40)
# p3=p2+p1
# print(p3.x)
# print(p3.y)


# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __eq__(self, other):
#         return self.marks==other.marks
# s1=student("a",10)
# s2=student("b",10)
# print(s1==s2)


#Absraction :it means hiding unneccesary data and show the useful daea

from abc import ABC,abstractmethod   #ABC CALLED AS ABSTRACT BASE CLASS
# class animal(ABC):
#     #abstract method
#     def sound(self):
#         pass
# #animal says that every animal must privide sound() method
# class dog(animal):
#     def sound(self):
#         print("dog barks")
# class cat(animal):
#     def sound(self):
#         print("cat meow")
# Dog=dog()
# Dog.sound()
# Cat=cat()
# Cat.sound()

# class payment(ABC):
#     def pay(self,amount):
#         pass
# class UPI(payment):
#     def pay(self,amount):
#         print("paid",amount,"using UPI")
# class creditcard(payment):
#     def pay(self,amount):
#         print("paid",amount,"using creditcard")
# upi=UPI()
# card=creditcard()
# upi.pay(1000)
# card.pay(2000)

        





