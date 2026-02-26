import pandas as pd
import requests

df = pd.read_csv("data.csv")

df= df.fillna(0)

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

params= {
    "coins":["bitcoin","ethereum","dogecoin","litecoin"],
    "amount_held":[0.5,2,1000,5],
    "Buy_price":[20000,1500,0.05,50]
}

response = requests.get(url,params=params)

print(response.status_code)

data = response.json()

df= pd.DataFrame(data)

print(df[[""]])

filename = "project.csv"
df.to_csv(filename,index=False)
print("File_saved",filename)