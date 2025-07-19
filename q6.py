import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
def calc_cosine_similarity(file, sheet):
    data = pd.read_excel(file, sheet=sheet)
    for col in data.columns:
        for i in range(len(data[col])):
            value = data.at[i, col]
            if isinstance(value, str): #binary vectors
                lval = value.lower()
                if lval == 't':
                    data.at[i, col] = 1 
                elif lval == 'f':
                    data.at[i, col] = 0
    catcol = data.select_dtypes(include='object').columns
    encode = pd.get_dummies(data, columns=catcol, drop_first=False)
    scale = StandardScaler()
    fit = pd.DataFrame(scale.fit_transform(encode), columns=encode.columns)
    vector1 = fit.iloc[0].values.reshape(1, -1)
    vector2 = fit.iloc[1].values.reshape(1, -1)
    sim = cosine_similarity(vector1, vector2)[0][0]
    return sim
result = calc_cosine_similarity(r"lab2/Copy of Lab Session Data.xlsx", "thyroid0387_UCI")
print(f"Cosine similarity:",result)
