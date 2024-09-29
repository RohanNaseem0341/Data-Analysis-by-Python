import pandas as pd
# Read file
data=pd.read_csv("data.csv")
# print(data)

# #Head and Tail Function
# #Head ---> Top values
# print(data.head()) #default 5 top values
# print(data.head(10)) 

# #Tail ---> Bottom values
# print(data.tail())  #default Bottom 5 values
# print(data.tail(10))  # Bottom 10 values

# Info Function
# print(data.info())

# Drop na function delete the row which have any null value
# data1=data.dropna()
# print(data1)

# Fill na function fill all the values in dataset
# data2=data.fillna(1000)
# print(data2)

#Drop Duplicate function to remove duplicate values
# df=data.drop_duplicates()
# df=data.drop_duplicates(subset='Pulse')

# print(df)

data['Duration'].replace({60:100},inplace=True)
# above function will replace the all 60 into 100 present in Duration coulumn
print(data)
