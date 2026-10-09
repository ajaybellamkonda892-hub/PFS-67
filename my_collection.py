#collections : specialized data structures
# co0unter,deque,named tuple,default dict

#counter : counter is used to count how many times it occurs

# from collections import Counter
# nums=[1,1,1,2,2,2,3,3,3]
# count=Counter(nums)
# # print(count)
# text="bananas"
# count=Counter(text)
# print(count)

# #default dict
# from collections import defaultdict
# students=defaultdict(int)
# print(students["python"])

# from collections import defaultdict
# students=defaultdict(list)
# students["CSE"].append("RAHUL")
# students["CSE"].append("f")
# students["ECE"].append("y")
# print(students)

#deque
# from collections import deque
# nums=deque([10,20,30])
# nums.append(40)
# print(nums)

# #add at beginning
# nums.appendleft(5)
# print(nums)

# #delete for t
# nums.pop()
# print(nums)

# #delete at first
# nums.popleft()
# print(nums)


# #named tuple : a named tuple is like a tuple whose values can aslo be accessed by names
# from collections import namedtuple
# student=namedtuple("student",["name","age","branch"])
# Student=student("rahul",22,"CSE")
# print(Student.name)
# print(Student.age)
# print(Student.branch)


