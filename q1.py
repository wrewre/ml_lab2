import pandas as pd
import numpy as np
df = pd.read_excel(r"lab2/Copy of Lab Session Data.xlsx", sheet_name="Purchase data",usecols="A:E")  
print(df.columns)
A=df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].to_numpy()
C=df[['Payment (Rs)']].to_numpy()
print(A)
print(C)
dim1 = A.shape[1]
dim2 = A.shape[0]
dim3 = C.shape[1]
dim4 = C.shape[0]
print("dimensions of matrix A is:",dim2,"X",dim1," and C is:",dim4,"X",dim3)
A_t=A.T
print("Rank of A:",np.linalg.matrix_rank(A))
X=np.linalg.pinv(A) @ C
print("Cost of each product available for sale is: ",X)
