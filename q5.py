from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

thyroid_df = pd.read_excel(r"lab2/Copy of Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")  # file read

df_encoded = thyroid_df.copy()  # copy data
object_columns = df_encoded.select_dtypes(include='object').columns  
for col in object_columns:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))  

binary_columns = df_encoded.columns[df_encoded.nunique() == 2]  # get binary
binary_df = df_encoded[binary_columns]  # fetch only binary

vec1 = binary_df.iloc[0].values  # first vector
vec2 = binary_df.iloc[1].values  # second vector

print("Vector 1:", vec1)
print("Vector 2:", vec2)

def jaccard_smc(v1, v2):
    ones_match = np.logical_and(v1 == 1, v2 == 1).sum()  # both one
    zeros_match = np.logical_and(v1 == 0, v2 == 0).sum()  # both zero
    one_zero = np.logical_and(v1 == 1, v2 == 0).sum()  # first one
    zero_one = np.logical_and(v1 == 0, v2 == 1).sum()  # second one

    total = ones_match + zeros_match + one_zero + zero_one
    if (ones_match + one_zero + zero_one):
        jaccard = ones_match / (ones_match + one_zero + zero_one) 
    else:
        jacard = 0
    if total:
        smc = (ones_match + zeros_match) / total    
    else:
        smc = 0
    return jaccard, smc  # return values

jc, smc = jaccard_smc(vec1, vec2)

print(f"Jaccard Coefficient (JC):",jc)
print(f"Simple Matching Coefficient (SMC):",smc)
