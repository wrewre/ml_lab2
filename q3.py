import pandas as pd
import numpy as np
from statistics import *
import matplotlib.pyplot as plt
import seaborn as sns
def stock_market(file):
    df = pd.read_excel(file, sheet_name="IRCTC Stock Price") #loading dataset
    days=df[['Day']].to_numpy()  #extracting columns
    price=df[['Price']].to_numpy()
    chg=df[['Chg%']].to_numpy()
    days_count = len(df['Day'])
    mean_of_dataset=mean(price.flatten())
    variance_of_dataset=variance(price.flatten())
    
    wednesday = df[df['Day'] == 'Wed']['Price'].to_numpy() #condition such that the day is wednesday
    april = df[df['Month'] == 'Apr']['Price'].to_numpy() #condition such that the day is april
    wed = (df['Day'] == 'Wed').sum()
    loss_chg = (df['Chg%']<0).sum() #condition such that the chg should be negative
    total_chg = df[['Chg%']].count()
    prob_loss=loss_chg/total_chg
    profit_chg = ((df['Chg%']>0) & (df['Day'] == "Wed")).sum() #condition such that the chg is positive and the day is wednesday
    prob_profit = profit_chg/total_chg
    cond_prof = profit_chg / wed
    


    mean_of_dataset_wednesday = mean(wednesday)
    mean_of_dataset_april = mean(april)
    return mean_of_dataset,variance_of_dataset,prob_loss,prob_profit,mean_of_dataset_wednesday,mean_of_dataset_april

def plotting(file):
    df = pd.read_excel(file, sheet_name="IRCTC Stock Price") #loading dataset
    df1 = df.dropna(subset=["Chg%", "Day"])
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="Day", y="Chg%", data=df1, color="blue", s=80, alpha=0.7)
    plt.title("Change % across Weekdays")
    plt.xlabel("Day")
    plt.ylabel("Chg%")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

mean_of_dataset,variance_of_dataset,prob_loss,prob_profit,mean_of_dataset_wednesday,mean_of_dataset_april=stock_market(r"lab2/Copy of Lab Session Data.xlsx")
print("Total Mean:",mean_of_dataset)
print("Variance:",variance_of_dataset)
print("Probabiltiy of loss in stock:",prob_loss.iloc[0])
print("Probabiltiy of profit in stock on wednesday:",prob_profit.iloc[0])
print("Probabiltiy of profit in stock given that it is on wednesday:",prob_profit.iloc[0])
print("Mean(Wednesday):",mean_of_dataset_wednesday)
print("Mean(Total)/Mean(Wednesday):",mean_of_dataset/mean_of_dataset_wednesday)
print("Mean(April):",mean_of_dataset_april)
print("Mean(Total)/Mean(April):",mean_of_dataset/mean_of_dataset_april)
print("The mean of the price in april was greater than the total mean whereas the mean of the price on wednesdays was lesser than the total mean.")
plotting(r"lab2/Copy of Lab Session Data.xlsx")