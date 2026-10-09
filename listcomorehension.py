# #list comprehension
# numbers=[i for i in range(1,6)]
# print(numbers)
# one line representation
#syntax: [expression for variable in iterable]
#[x for x in range(1,5)]


# squares=[i*i for i in range(1,6)]
# print(squares)

# names=["ajay","ram","srinu"]
# result=[name.upper() for name in names]
# print(result)

# #list comprehension using if
numbers=[i for i in range(1,11) if i%2==0]
print(numbers)

#filtering values
# nums=[10,20,30,40,50]
# result=[i for i in nums if i>20]
# print(nums)

# nested list comprehension
# it means having more than one for loop inside list comprehension
# result=[(i,j) for i in range(1,4) for j in range(1,4)]
# print(result) 

# matrix=[
#     (1,2,3),
#     (4,5,6),
#     (7,8,9)
# ]
# result=[x for row in matrix for x in row]
# print(result)

