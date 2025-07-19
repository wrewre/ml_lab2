import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def scale_numeric_columns(filepath, sheetname):
    df = pd.read_excel(filepath, sheet_name=sheetname)  
    minmax = MinMaxScaler()  # initialize minmax
    standard = StandardScaler()  # initialize standard
    cols = df.select_dtypes(include=['int64', 'float64']).columns  # pick number columns
    df_minmax = pd.DataFrame(minmax.fit_transform(df[cols]), columns=cols)  # minmax scale
    df_standard = pd.DataFrame(standard.fit_transform(df[cols]), columns=cols)  # standard scale
    return df[cols], df_minmax, df_standard  # return result

original, minmax, standard = scale_numeric_columns(r"lab2/Copy of Lab Session Data.xlsx", "thyroid0387_UCI")
print("Original numeric data:", original.head())
print("Min-Max Scaled data:", minmax.head())
print("Z-Score Standardized data:", standard.head())

