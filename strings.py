place ="hyderabad"
spcl ='hyderabad'
print(place==spcl)

#indexing
lang = "python"
print(lang[0])
print(lang[-1])
print(lang[-2])

#string slicing
#variable_name[start:stop:step]
word ="python"
print(word[0:6])
print(word[0:6:2])

#reversing
print(word[::-2])

#replace
result = word.replace("h","")
print(result)

#concatination joinin of two strings
firstname = "ajay"
lastname = "bellam"
name = firstname+lastname
print(name)

#repetation
print("word"*3)

#membership -in()
message = "python is easy"
print("python" in message)

#METHODS
word = "python"
print(word.upper())
print(word.isupper())
print(word.lower())
print(word.islower())
word2 ="python is easy"
print(word2.title()) #it will first charater of every word in the sentence capital
print(word2.capitalize()) # it will print first character of the sentence print capital
print(word.strip()) # it removes spaces
print(word.rstrip()) #it is a right SPACES9O9
print(word.lstrip()) # it is a left SPACES

#count
company ="codegnan"
print(company.count("n"))

#startswith
company = "codegnan is a best"
print(company.startswith("codegnan"))
print(company.startswith("best"))
print(company.endswith("best"))

#split()
company="python,java,sql"
print(company.split())

#join
list=['python','java','sql']
result = " ".join(list)
print(result)

#isalpha()-alphabetics, isalnum()-alphabetics,numbersa,isdigit()-numbers
school="mbbs1"
print(school.isalpha())
print(school.isalnum())
print(school.isdigit())
