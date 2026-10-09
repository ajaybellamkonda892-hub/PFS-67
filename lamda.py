#Lambda Functions
#Anonymous - Without name
#Small anonymous functions
#Single line functiond

#Lambda syntax:
#lambda arguments : expression

#def square(x):
#   print(x*x)
#square(5)

#Lambda:
#square = lambda x : x * x
#print(square(6))

#Lambda with Multiple Parameters
#add = lambda x, y, z : x + y + z
#print(add(27, 30, 13))

#Lambda with if-else

#check = lambda x : "Even" if x % 2 == 0 else "odd"
#print(check(7))
#print(check(10))

#When should we use Lambda 

#Small functions temporaily, especially with:
#map(), filter(), sorted(), reduce()

#Map() - It applies function to every element
#of an iterable
#Syntax: map(function, iterable)

# nums= [1, 2, 3, 4, 5]
# squares = list(map(lambda x : x * x, nums))
# print(squares)

#Map without lambda
# def square(x):
#   return x * x
# numbers = [1, 2, 3, 4, 5]
# result = map(square, numbers)
# print(list(result))

#filter() - It is used when we want to select only elements that satisfy a condition

#syntax: filter(function, iteration)

#nums = [1, 2, 3, 4, 5, 6]
#result =filter(lambda x: x % 2 == 0, nums)
#print(list(result))

#reduce() - It repeatedly applies a function to elements and reduces entire sequence to one final value.

#from functools import reduce

#from functools import reduce

#numbers = [1, 2, 3, 4]
#result = reduce(lambda a, b : a * b, numbers)
#print(result)

#Sorted():

#nums = [10, 40, 20, 30]
#result = sorted(nums, reverse=True)
#print(result)

#names = ["ram", "shyam", "srijay"]
#result = sorted(names, key=len)
#print(result)

#Sorting numbers according to Absolute number

#nums = [-10, -8, 2, 7, -13, 21]
#result = sorted(nums, key=abs)
#print(result)

#LIST

#number = []

#for i in range(1, 6):
#   number.append(i)
#print(number)

#number = [i for i in range(1, 6)]
#print(number)
#one line representation of loop
#Syntax: [expression for variable in iterable]
#[x for x in range(1, 5)]

#squares = [i*i for i in range(1, 6)]
#print(squares)

#names = ["sam", "ram", "jim"]
#result = [name.upper() for name in names]
#print(result)

#List Comprehension With If

#numbers = []
#for i in range(1, 11):
#   if i % 2 == 0:
#        numbers.append(i)
#print(numbers)

#numbers = [i for i in range(1, 11) if i % 2 == 0]
#print(numbers)

#Filtering Values
#nums = [10, 15, 20, 25, 30, 35, 40]
#result = [i for i in nums if i > 20]
#print(result)

#Nested List Comprhension:
# It means having more than one for loop inside list comprhension.

#result = []
#for i in range(1, 4):
#  for j in range(1, 4):
#       result.append((i, j))
#print(result)

#result = [(i, j) for i in range(1, 4) for j in range(1, 4)]
#print(result)

#matrix = [
#  [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
#]

#result = [x for row in matrix for x in row]
#print(result)

#Generators 
#Generators produces values one at a time when required.

#def numbers2():
#  for i in range(1, 6):
#       yield i
#result = number2()
#print(result)
#print(next(result))
#print(next(result))
#print(next(result))

#yield passes the function and remembre its current state.

#def numbers():
#  yield 1
#   yield 2
#   yield 3
#result = numbers()
#print(next(result))
#print(next(result))
#print(next(result))

#Demo:

#def demo():
# yield 10
#  yield 20
#   yield 30
#result = demo()
#print(next(result))
#print(next(result))
#print(next(result))

#def demo():
#  return 10
#   return 20
#print(demo())
#print(demo())

#Understanding Generator Execution.
#def demo():
#print("start")
#yield 10
#print("middle")
# yield 20
#  print("end")
#   yield 30
#result = demo()
#print(next(result))
#print(next(result))
#print(next(result))

#Using Generator with for loop.

#def numbers():
#    for i in range(1, 6):
#        yield i
#for x in numbers():
#    print(x)

#Generator Expression

#List Comp = []
#Generator Exp = ()

#nums = (x * x for x in range(1, 6))
#print(next(nums))
#print(next(nums))
#print(next(nums))
#print(next(nums))
#print(next(nums))

#We need to use Generators when we want to generate values at a time.

#Medium:
#Create a generator that produces even no.s from 1 to 20.

#def even():
# for i in range (1, 20):
#      if i % 2 == 0:
#           yield i
#for x in range: