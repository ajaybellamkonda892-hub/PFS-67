#generators
#generators produce a value one after another

# yield : it passes the function and remebers its current state
# def numbers():
#     yield 1
#     yield 2
#     yield 3
# result=numbers()
# print(next(result))
# print(next(result))
# print(next(result))

# def numbers():
#     for i in range(1,6):
#         yield i
# result=numbers()
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

#yeild vs return
# def demo():
#     return 10
#     return 20
# print(demo())
# print(demo())

# def demo():
#     yield 10
#     yield 20
#     yield 30
# result =demo()
# print(next(result))
# print(next(result))
# print(next(result))


#using generator with for loop
# def numbers():
#     for i in range(1,6):
#         yield i
# for x in numbers():
#     print(x)

# we need  to use generators when we want to generate values at a time

#medium level problem 
# #even numbers 1 to 20
# def even():
#     for i in range(1,21):
#         if i%2==0:
#             yield i
# for x in even():
#     print(x)