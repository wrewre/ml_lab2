import pandas as pd
import numpy as np
def purchase_data(file):
    df = pd.read_excel(file, sheet_name="Purchase data",usecols="A:E")  
    first=df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].to_numpy() #first matrix
    second=df[['Payment (Rs)']].to_numpy()   #second matrix
    dim1 = first.shape[1] #first column
    dim2 = first.shape[0] #first row
    dim3 = second.shape[1] #second column
    dim4 = second.shape[0] #second row
    X=np.linalg.pinv(first) @ second #solving for X
    return dim2,dim1,dim4,dim3,first,X 
dim2,dim1,dim4,dim3,rank,cost= purchase_data(r"lab2/Copy of Lab Session Data.xlsx")
print("dimensions of matrix A is:",dim2,"X",dim1," and C is:",dim4,"X",dim3)
print("Rank of A:",np.linalg.matrix_rank(rank))
print("Cost of each product available for sale is: ",cost)
