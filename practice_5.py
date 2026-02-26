import pandas as pd

employees = {
    "Employees_ID": [1,2,3,4,5],
    "name": ["Ali","Ahmad","Ahsan","Huzaifa","Daniyal"],
    "department": ["IT","HR","IT","Finance","HR"],
    "age": [28,32,25,30,29],
    "salary": [60000, 55000, 70000, 65000, 50000],
    "Joining_Year": [2019, 2018, 2020, 2017, 2019],
    "Performance_Score": [8,7,9,6,7]
}

experience_values = {
    1:6,
    2:7,
    3:8,
    4:9,
    5:10
}

df = pd.DataFrame(employees)

df["Experience"] = df["Employees_ID"].map(experience_values)

print(df)