import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def classification(file):
    df = pd.read_excel(file, sheet_name="Purchase data",usecols="A:E")  #loading the first 5 columns
    payment=df[['Payment (Rs)']].to_numpy()
    label=[]
    for spend in payment: 
        if spend>200:
            label.append("RICH")
        else:
            label.append("POOR")
    df['labelling'] = label #labelling and storing the data back to the file
    labelling=df[['Payment (Rs)']].to_numpy() #accessing the label
    customers=df[['Customer']].to_numpy() #accessing the customer field
    le=LabelEncoder()
    encoded_data=le.fit_transform(label) #fitting the label
    field=df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].to_numpy() 
    trainx,testx,trainy,testy,traincust,testcust = train_test_split(field,encoded_data,customers,test_size=0.2,random_state=42) # 80% for training and 20% for testing 
    knn_model = KNeighborsClassifier(n_neighbors=3) # classifier initialized
    knn_model.fit(trainx,trainy)
    prediction = knn_model.predict(testx) #knn prediction
    decoding = le.inverse_transform(prediction) #decoding
    return decoding,testx,testcust 
file=r"lab2/Copy of Lab Session Data.xlsx"
prediction,testx,testcust = classification(file)
print("Prediction:",prediction)

for i in range(len(testx)):
        print(f"Test Customer",i+1,"- Features:",testcust[i][0],"Prediction:",prediction[i])
        


