#importing pndas library
import pandas as pd

#loading a dataset called drinks using pandas library
data = pd.read_csv("C:/Users/KB.com/OneDrive/Pictures/Mabonono/Internship Tasks/technohacks internship/train.csv")

#outputting or showing the first 5 rows of the dataset
print("------------------------------------------------------------------------")
print("-------------------------ORIGINAL DATASET-------------------------------")
print("------------------------------------------------------------------------")
print(data.head())
print("------------------------------------------------------------------------")

#checking for missing values
missing_values = data.isnull().sum()
#finding the percentage of the missing values
missingValues_percentage = (missing_values / len(data)) * 100
#outputting the missing values and their percentages
print("------------------------MISSING VALUES----------------------------------") 
print("------------------------------------------------------------------------")
print(missing_values[missing_values > 0])
print("------------------------------------------------------------------------")
print("------------------MISSING VALUES PERCENTAGES----------------------------") 
print("------------------------------------------------------------------------")
print(missingValues_percentage[missingValues_percentage > 0])
print("------------------------------------------------------------------------")

#selecting the columns with numerical values
numerical_cols = data.select_dtypes(include = ['float64, int64']).columns
#Filling the missing numerical values with the median 
data[numerical_cols] = data[numerical_cols].apply(lambda x : x.fillna(x.median()))

#selecting the columns with categorical values
categorical_cols = data.select_dtypes(include = ['object']).columns
#Filling the missing categorical values with the mode
data[categorical_cols] = data[categorical_cols].apply(lambda x : x.fillna(x.mode()))

data[numerical_cols] = data[numerical_cols].apply(lambda x : (x - x.min()) / (x.max() - x.min()))

#saving the cleaned dataset to the new file
data.to_csv('Cleaned_Housing_Prices.csv', index = False)
print("DATASET CLEANED AND SAVED AS 'Cleaned_Housing_Prices.csv'.")