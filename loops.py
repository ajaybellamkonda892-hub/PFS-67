#loops :doing same task repetition
#for,while
#for:if we know no of iterations we can use ex:cooking food for family
#while:we dont no of iterations  ex: cooking food in hotel

# #for 
# for i in range(1,11):
#     print("hello")

# #by using list datetype and index
# nums=[10,20,30,40,50]
# for i in range(0,5):
#     print(nums[i])

# #by using values
# nums=[2,3,5,6]
# for num in nums:
#     print(num*2)

#while
# i=1
# while i<=5:
#     print(i)
#     i+=1

# #print even numbers 1 to 10
# for i in range(1,11):
#     if i%2==0:
#         print(i)          

# for i in range(10,0,-1):
#     print(i)


# # sum of numbers
# total=0
# for i in range(1,11):
#     total+=i
# print(total)

#multplication table
# num=int(intput("enter a value:")
# for i in range(1,11):
#     print(num*i)

#finding largest number
# nums=[10,20,30,40]
# largest=nums[0]
# for num in nums:
#     if num>largest:
#         largest=num
# print(largest)

#palindrome
# num=int(input("enter a value:"))
# original=num
# reverse=0
# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num//=10
# if original==reverse:
#     print("palindrome")
# else:
#     print("Not palindrome")

#factorial
# num=5
# fact=1
# while num>0:
#     fact=fact*num
#     num-=1
# print(fact)

# #fibonacci series
# n=10
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     a,b=b, a+b

# #finding duplicates
# numbers=[1,2,3,3,4,5,4,5]
# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i]==numbers[j]:
#             print(numbers[i])