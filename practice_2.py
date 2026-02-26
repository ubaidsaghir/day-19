import pandas as pd

data = {
    "name": ["Ali", "Sara", "Ahmed", "Ahsan", "Hina"],
    "department": ["IT", "HR", "IT", "Finance", "HR"],
    "salary": [60000, 50000, 70000, 80000, 55000]
}

df = pd.DataFrame(data)

print(df)

avg_salary = df.groupby("department")["salary"].mean()
print(avg_salary)