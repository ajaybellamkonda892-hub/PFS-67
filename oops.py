#oops :object oriented programiming
# it is programming approach where we organize our program around object rather than only function and varibl

# student:
# data:
#     name,age,marks,roll_no
# Behaviour:
#     study(),attend_classes(),write_exam(),display()

#in oops we combine data+behaviour into object

#1.class  :blueprint template to create objects
#
# 2.object: instance of class 
#class:blueprint
# #object:actual thing created from blueprint

# # class student:
# #     passs
# # student1=student() #object
# # student2=student()

# #attributes : attributes are the data/properties associated with an object

# class student:
#     pass
# student1=student()
# student1.name="ajay"
# student1.age=22
# student1.marks=92
# print(student1.name)
# print(student1.age)
# print(student1.marks)

# #methods : functions created insides class
# class student:
#     def study(self):
#         print("student is studying")
# student1=student()
# student1.study()

#method vs function
#method:method only belongs to class

#constructors:it is a special method that autumatically called when an object is created
# _init
# class student:
#     def __init__(self):
#         print("student is studying")
# student1=student()

#attributes with constructor
# class student:
#     def __init__(self,name,age,marks):    #self represent current object
#         self.name=name
#         self.age=age
#         self.marks=marks
# student1=student("ajay",22,92)
# print(student1.name)
# print(student1.age)
# print(student1.marks)

#crating multiple methods with class ang object
# class student:
#     def __init__(self,name,age,marks):    #self represent current object
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print(self.name,self.age,self.marks)
# student1=student("ajay",22,92)
# student1.display()

#encapsulation: binding  data and methods in to single unit

# class bankaccount:
    # def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#     def withdraw(self,amount):
#         self.__balance-=amount
#     def get_balance(self):
#         return self.__balance
# ba=bankaccount(50000)
# ba.deposit(10000)
# # ba.withdraw(5000)
# # print(ba.get_balance())

# #double underscore indicates a private-like attributes in python through  name managing 


# #Getter and setter used in private data
# #getter : read data
# #setter :modify data safely

# class student:
#     def __init__(self,marks):
#         self.__marks=marks
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self,marks):
#         if 0<=marks<=100:
#             self.__marks=marks
#         else:
#             print("invalid marks")
# student=student(80)
# print(student.get_marks())
# student.set_marks(90)
# print(student.get_marks())


#inheritance :acquiring properties from one class to annother class
#parent to child class

#types of inheritance
# #1.single inheritance :one parent to one child
# class animal:
#     def eat(self):
#         print("animal eats")
# class lion(animal):
#     def roar(self):
#         print("lion roars")
# l=lion()
# l.eat()
# l.roar()


#multiple inheritance:one child inherits to multiple parents
# class father:
#     def father_properties(self):
#         print("fathers's properites")
# class mother:
#     def mother_properties(self):
#         print("mothers propertoes")
# class child(father,mother):
#     def child_properties(self):
#         print("childs properties")
# c=child()
# c.father_properties()
# c.mother_properties()
# c.child_properties()

#multi-level inheritance
#grandparent -> parent -> child
# class grandparent:
#     def house(self):
#         print("grandsparents house")
# class parent(grandparent):
#     def car(self):
#         print("parents car")
# class child(parent):
#     def bike(self):
#         print("childs bike")
# c=child()
# c.house()
# c.car()
# c.bike()

# 4.hierarchial inheritance:one parent to multiple child
# class animal:
#     def eat(self):
#         print("animal eats")
# class dog(animal):
#     def bark(self):
#         print("dark barks")
# class cat(animal):
#     def meow(self):
#         print("cat meow")
# d=dog()
# c=cat()
# d.eat()
# d.bark()
# c.eat()
# c.meow()

# #5 hybrid inheritance
# class a:
#     def method_a(self):
#         print("a")
# class b(a):
#     def method_b(self):
#         print("b")
# class c(a):
#     def method_c(self):
#         print("c")
# class d(b,c):
#     def method_d(self):
#         print("d")
# obj=d()
# obj.method_a()
# obj.method_b()
# obj.method_c()
# obj.method_d()


#super keyword:in python super() is used to access functionlity from parent class=

# class parent:
#     def show(self):
#         print("parent method")
# class child(parent):
#     def show(self):
#         super().show()
#         print("child method")
# c=child()
# c.show()


# #super with constructor
# class person:
#     def __init__(self,name):
#         self.name=name
# class student(person):
#     def __init__(self, name,marks):
#         super().__init__(name)
#         self.marks=marks
# s=student("rahul",95)
# print(s.name)
# print(s.marks)

#vehical and car
#vehicle - start(),stop()
#car -drive
# class vehicle:
#     def start(self):
#         print("vehicle start")
#     def stop(self):
#         print("vehicle stop")
# class car(vehicle):
#     def drive(self):
#         print("car drives")
# c=car()
# c.start()
# c.stop()
# c.drive()

#person and student
#person - name,age,display_person()
#student-roll_n0,course,display_student()
#output:name,age,roll_no,course


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_person(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# class Student(Person):
#     def __init__(self, name, age, roll_no, course):
#         super().__init__(name, age)
#         self.roll_no = roll_no
#         self.course = course

#     def display_student(self):
#         self.display_person()
#         print("Roll No:", self.roll_no)
#         print("Course:", self.course)


# s = Student("Ajay", 20, 101, "Python")
# s.display_student()