#array
#data structure
#collections of elements
#we store values in array by using index
#index only store single value
#index start from 0 to n-1 whwre n =length of array
#left to right -> positive index
#right to left -> negative index (-1 to -n)

array=[10,20,30]
print(array)
print(len(array))
print(array[0])
print(array[1])
print(array[2])
print(array[-1])
print(array[-2])
print(array[-3])
array.append(40)
array.insert(3,35)
print(array)
array.remove(35)
array.pop()
array.pop(2)
print(array)

#access by value
for x in array:
    print(x)

#access by index
for i in range(len(array)):
    print(array[i])

#reverse access
#access by value
for i in reversed(array):
    print(i)

#access by index
for i in range(len(array) -1,-1,-1):
    print(i)