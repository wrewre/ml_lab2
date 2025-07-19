import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Function to compute Jaccard, SMC, and Cosine Similarity using original logic
def compute(file, sheet):
    # load data
    data = pd.read_excel(file, sheet_name=sheet)
    part = data.iloc[:20].copy()
    part = part.replace({'t': 1, 'f': 0})
    
    # get binary cols
    bins = [c for c in part.columns if set(part[c].dropna().unique()).issubset({0, 1})]
    bindata = part[bins].astype(int)

    size = bindata.shape[0]
    jac = np.zeros((size, size))
    smc = np.zeros((size, size))

    # calc jc and smc
    for i in range(size):
        for j in range(size):
            v1 = bindata.iloc[i]
            v2 = bindata.iloc[j]
            f11 = ((v1 == 1) & (v2 == 1)).sum()
            f00 = ((v1 == 0) & (v2 == 0)).sum()
            f10 = ((v1 == 1) & (v2 == 0)).sum()
            f01 = ((v1 == 0) & (v2 == 1)).sum()
            jac[i][j] = f11 / (f11 + f10 + f01) if (f11 + f10 + f01) != 0 else 0
            smc[i][j] = (f11 + f00) / (f11 + f10 + f01 + f00)

    
    done = pd.get_dummies(part, drop_first=True)
    scale = StandardScaler()
    done = pd.DataFrame(scale.fit_transform(done), columns=done.columns)

    # cosine calculation
    cos = cosine_similarity(done)
    
    return jac, smc, cos


def plot(mat, head):
    plt.figure(figsize=(10, 8))
    sns.heatmap(mat, annot=False, cmap='coolwarm', xticklabels=False, yticklabels=False)
    plt.title(head)
    plt.show()


file = "lab2/Copy of Lab Session Data.xlsx"
sheet = "thyroid0387_UCI"

jac, smc, cos = compute(file, sheet)
plot(jac, "Jaccard Coefficient Heatmap of 20 Vectors.")
plot(smc, "Simple Matching Coefficient Heatmap of  20 Vectors.")
plot(cos, "Cosine Similarity Heatmap of 20 Vectors.")
