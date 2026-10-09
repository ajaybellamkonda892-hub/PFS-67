# #syntax
# for i in range(0,2):
#     for j in range(0,2):
#         print(i,j)

#star pattern
# incresing triangle
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

# #decresing patten
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# #sqaure
# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print()

#rectangular
# rows=4
# col=8
# for i in range(rows):
#     for j in range(col):
#         print("*",end="")
#     print()


# #give space for print
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
    # print()

#pyramid
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):

#         print("*",end="")
#     print()


# #numbers triangle
# 1
# 12
# 123
# 1234
# 12345
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# # #repeting number
# 1
# 22
# 333
# 4444
# 55555
# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print()


#reverse printing numbers
# 5
# 54
# 543
# 5432
# # 54321
# for i in range(1,6):
#     for j in range(5,5-i,-1):
#         print(j,end="")
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# num=1
# for i in range(1,5):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
    # print()

# 54321
# 54321
# 54321
#  54321
# for i in range(5):
#     for j in range(5,0,-1):
#         print(j,end="")
#     print()

# 54321
# 5432
# 543
# 54
# 5
# for i in range(5,0,-1):
#     for j in range(5,5-i,-1):
#         print(j,end="")
#     print()

# 1
# 21
# 321
# 4321
# # 54321 
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print() 

#pyramid
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print(j,end="")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print(i,end="")
#     print()

#reverse star
# n=5
# for i in range(5,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()

# n=5
# for i in range(1,n+1):  # upper pyramid
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()
# for i in range(n-1,0,-1):  #lower pyramid
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()



#name pattern
#CODE
#C
#CO
#COD
#CODE
# name="CODE"
# for i in range(1,len(name)+1):
#     for j in range(i):
#         print(name[j],end="")
#     print()

# #reverse
# name="CODE"
# for i in range(len(name),0,-1):
#     for j in range(i):
#         print(name[j],end="")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         if i==n:
#             print("*",end="")
# elif j==1 or j==2*i-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
    

