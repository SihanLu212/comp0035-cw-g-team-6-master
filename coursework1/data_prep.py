import pandas as pd
from pathlib import Path
import os
#  create some functions
def DataDisplay(dataset):
    # Get the size of data
    print("size of dataset:", dataset.shape)
    # Get the columns' name
    print("columns' name:", list(dataset.columns))
    # Observe the data distribution of each column (Only numeric columns can be observed)
    dataset.describe()
def DeleteColumns(dataset, delete_columns):
    # Delete some columns
    for each in delete_columns:
        del dataset[each]
    return dataset
def ReplaceZeroValue(dataset, zero_columns):
    # Replace the data with the value of 0
    for each in zero_columns:
        dataset[each].replace(0,20,inplace = True)
    return dataset
def GetZeroColumnNames(dataset):
    # The values 0 are considered to be missing values
    zero_columns = []
    for i in dataset.columns:
        print(f"{i}'s missing values:",(dataset[i] == 0).sum())
        if (dataset[i] == 0).sum() > 0:
            zero_columns.append(i)
    return zero_columns
def one_hot(dataset, object_columns):
    return pd.get_dummies(dataset,columns = object_columns)
# Open the data file
path = Path(".\\").parent.joinpath('County0010.xlsx')
print(path)
# Load the excel file into a pandas DataFrame
dataset = pd.read_excel(path)
#First, check whether there is NULL value. Obviously, there is no NULL value
dataset.info()
# data display
DataDisplay(dataset)
# remove unnecessary columns
dataset = DeleteColumns(dataset, ['Prov_CH', 'City_CH', 'County_CH'])
# data display again
DataDisplay(dataset)
# Observe the data distribution of each column (Only numeric columns can be observed)
dataset.describe()
# Get the names of the column containing 0
zero_columns = GetZeroColumnNames(dataset)
print("Zero columns:", zero_columns)
dataset = ReplaceZeroValue(dataset, zero_columns)
# Get the names of the column containing 0
zero_columns = GetZeroColumnNames(dataset)
print("Zero columns:", zero_columns)
dataset.head()
# The one-hot based on the county will result in too many column features
# object_columns = ["Prov_CH","Prov_EN","City_CH","City_EN","County_EN","County_EN"]
# Therefore, the selection is based on the province and city
object_columns = ["Prov_EN", "City_EN"]
dataset = one_hot(dataset, object_columns)
print("The dataset has",dataset.shape[0],"rows")
print("The dataset has",dataset.shape[1],"features")
dataset
dataset.to_excel("out.xlsx")
