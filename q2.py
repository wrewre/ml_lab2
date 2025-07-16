import pandas as pd
import numpy as np
df = pd.read_excel(r"lab2/Copy of Lab Session Data.xlsx", sheet_name="Purchase data",usecols="A:E")  
print(df.columns)
A=df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].to_numpy()
C=df[['Payment (Rs)']].to_numpy()