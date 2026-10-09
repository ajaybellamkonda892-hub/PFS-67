#DATA ANLYTICS
# it is the process of collecting,cleaning,transforming,analyzing,
# and interpreting data to find useful info and make decisions

#importants steps
#1.data collections
#excel,CSV,databases,APIS,websites,applications

#2.data cleaning
#missing values,duplicate records,incorrect values,wrong formats

#3.data processing
#converts the data into useful format

#data analysis
#finding patterns and relationships

#5.visualization:
# representing data using bar,line,pie,histograms

#numpy: numerical python
# it is a python library used for numerical calculations, working with 
#array,mathematical operations,matrix operations




# import numpy as np
# marks=np.array([80,90,70,60])
# marks=marks+5
# print(marks)

# #2d matrix
# import numpy as np
# marks=np.array([
#     [80, 90, 70],
#     [85, 95, 75],
#     [70, 80, 90]
# ])
# print(marks)
# print(marks.ndim)
# print(marks.shape)
# print(marks.size)
# print(marks.dtype)
# print(marks[0][0])
# print(marks[0][1])
# print(marks[0][2])
# print(marks[1][0])
# print(marks[1][1])
# print(marks[1][2])
# print(marks[2][0])
# print(marks[2][1])
# print(marks[2][2])
# print(marks[0:2,1:3])

#[0:2] -> rows 0 and 1
#[1:3] -> columns 1 and 2

#creating special arrays
#1.np.zeroes()- creates an array filled with zeroes
# import numpy as np
# a=np.zeros(5)
# print(a)

# b=np.zeros((2,3))
# print(b)

#2 np.ones : filled with ones
# import numpy as np
# a=np.ones(5)
# print(a)

# b=np.ones((2,3))
# print(b)

#3.np.arrange()
# #similar to python
# import numpy as np
# a=np.arange(1,10)
# print(a)


#array operations
# import numpy as np
# a=np.array([10,20,30])
# b=np.array([1,2,3])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)


#comparision operator
# import numpy as np
# a=np.array([10,20,30])
# print(a>20)

#mathematical functions
# import numpy as np
# marks=np.array([70,80,80,60])
# #sum
# print(np.sum(marks))
# #average
# print(np.mean(marks))
# #maximum
# print(np.max(marks))
# #minimum
# print(np.min(marks))

# import numpy as np
# marks=np.array([
#     [80,70,90],
#     [85,75,95],
#     [70,60,50]
# ])
# #column wise
# print(np.sum(marks,axis=0))
# #row wise
# print(np.sum(marks,axis=1))


#pandas:
#pandas is a python library used for working with structured data.
#pandas works on a data that looks like a table
#EG : CSV FILES, excel files,databases,,data analytics projects

# import pandas as pd
#pandas series -1D labled data structure
# marks=pd.Series([80,90,70,75])
# print(marks)
# print(marks.iloc[1])  #iloc : position

# marks=pd.Series(
#     [80,90,70],
#     index=["A", "B", "C"]
# )
# print(marks.loc["B"])   #loc : label representation


# #series operations
# import pandas as pd
# marks=pd.Series([80,90,70])
# print(marks+10)
# print(marks-10)
# print(marks*10)


#data frame : 2d labeled data structure
#series : one column
#dataframe: multiple column +rows
# import pandas as pd
# data={
#     "Name":["A","B","C"],
#     "Age":[21,22,23],
#     "Marks":[85,95,89]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df[["Name","Marks"]])
# print(df.iloc[0])  #accessing the index wise data
# print(df.iloc[1])
# print(df.iloc[2])
# #accessing specific data
# print(df.loc[1,"Marks"])
# print(df.shape)
# print(df.size)

# #reading CSV files
# import pandas as pd
# df=pd.read_csv("annual.csv")
# print(df)
# print(df.head(10))  #head it will give first ten row
# print(df.tail(10)) # tail it will give last ten row
# print(df.info())
# print(df.describe())#describe used for values maens,averge etc

#datacleaning
#finding missing values
import pandas as pd
df = pd.read_csv("annual.csv")
# print(df.isnull()) # isnull used for verfiying missing values
# print(df.isnull().sum())  #isnull().sum() is used for no of missing values

#removing missing rows
# df=df.dropna()
# print(df)

#filling missing values
# df["year"]=df["year"].fillna(2026)
# df["height"]=df["height"].fillna(df["height"].mean()) # it will fill with mean which are missing

#duplicate data
# print(df.duplicated()) #to identify duplicate

#remove duplicates
# df=df.drop_duplicates() # it will remove duplicates

#changing column 
# df=df.rename(columns={                      #it will change column naqme
#     "industry_code_ANZSIC":"ANZ"
# })
# print(df.head())

#filter
result=df[df["year"]>2011]
print(result)

