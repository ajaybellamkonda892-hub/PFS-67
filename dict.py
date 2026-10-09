#dictonary
student = {
    "name": "ajay",
    "age": 20,
    "course":"python",
    "addr":"nrt"
}
print(student)
print(student["name"])
print(student["age"])
print(student["course"])
print(student["addr"])
print(type("name"))
print(type("age"))
print(student.get("salary")) #get - get is used for if dont have key it will print as none

#adding a new key
#sytax =dict_name["new key"]=value
student["contact"]=6301413151
print(student)

#updating :chaning a value
student["contact"]=9603623595
print(student)

#i need to print keys
print(student.keys())

#items()
for key,value in student.items():
    print(key,value)



#updatinf multiple values
student.update({
    "name":"arya",
    "age":21
})
print(student)

#pop
student.pop("age")
print(student)

student.clear()
print(student)

data ={
    2:"a",
    3:"b",
    4:"c"
}
print(max(data))
print(min(data))