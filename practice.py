import pandas as pd 

# Students = {
#     "name":["ubaid","Ali","Ahmad","Raheel"],
#     "age":[21,22,23,24],
#     "salary":[30000,40000,50000,60000]
# }

# df = pd.DataFrame(Students)
# print(df)

df = pd.read_csv("data.csv")
# print(df.head(10))

# print(df.info())
# print(df.describe())

df.rename(columns={"Hours_Studied":"Hello_World"},inplace=True)
print(df[df.columns[:5]])

df=df.fillna(0)