# import pandas as pd 
# mydataset = {
#     'cars': ["BMW", "Volvo", "Ford"],
#     'passings': [3, 7, 2]   
# }
# myvar = pd.DataFrame(mydataset)
# print(myvar)



import pandas as pd

data ={
    "students": ["Amandaz","benadict","Clementine","rayan","michael","margaret","james","john","mary","susan"],
    "marks": [100, 105, 45, 80, 90, 75, 85, 95, 70, 80]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
print(df.loc[1:4])