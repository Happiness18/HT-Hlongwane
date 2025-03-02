#importing necessary libraries to use within the code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading the cleaned dataset using pandas
data = pd.read_csv("C:/Users/KB.com/OneDrive/Pictures/Mabonono/Internship Tasks/technohacks internship/Cleaned_Housing_Prices.csv")

#outputting the first five rows of the cleaned dataset
print("------------------------------------------------------------------------")
print("-------------------------ORIGINAL DATASET-------------------------------")
print("------------------------------------------------------------------------")
print(data.head())
print("------------------------------------------------------------------------")

#finding the description of the dataset using the describe() method
data_description = data.describe()
print("----------------------------DESCRIPTION---------------------------------")
print("------------------------------------------------------------------------")
print(data_description)
print("------------------------------------------------------------------------")

#checking for missing values
missing_values = data.isnull().sum()
#outputting the number of missing values
print("------------------------MISSING VALUES----------------------------------") 
print("------------------------------------------------------------------------")
print(missing_values[missing_values > 0])
print("------------------------------------------------------------------------")

#plotting the distribution of SalePrice using the histograph
plt.figure(figsize = (10,6))
sns.histplot(data['SalePrice'], kde=True, bins = 30, color = "blue")
plt.title('Distrinution of SalePrice')
plt.xlabel('SalesPrice')
plt.ylabel('Frequency')
plt.show()

##selecting the columns with numerical values
numeric_data = data.select_dtypes(include = ['float64', 'int64'])
#calculating the correlation matrix
corr_matrix = numeric_data.corr()
#plotting the heatmap of the correlation matrix 
plt.figure(figsize = (12,8))
sns.heatmap(corr_matrix, annot = True, cmap = 'viridis', fmt = '.2f', linewidths = 0.5)
plt.title('Correlation Heatmap')
plt.show()

#scatter plot between GrLivarea and SalePrice
plt.figure(figsize = (10, 6))
sns.scatterplot(x = 'GrLivArea', y = 'SalePrice', data = numeric_data)
plt.title('GrLivArea vs SalePrice')
plt.xlabel('Above Grade Living Area (GrLivArea)')
plt.ylabel('SalePrice')
plt.show()

#Boxplot for Neighborhood and SalePrice
plt.figure(figsize = (12, 6))
sns.boxplot(x = 'Neighborhood', y = 'SalePrice', data = data)
plt.xticks(rotation = 90)
plt.title('Neighnorhood vs SalesPrice')
plt.xlabel('Neighborhood')
plt.ylabel('SalePrice')
plt.show()

#Pairplot for a subset of features
subset_columns = ['SalePrice', 'GrLivArea', 'OverallQual', 'TotRmsAbvGrd']
sns.pairplot(data[subset_columns])
plt.show()

#Identifying outliers using Z-score or simple threshold
outliers = data[(data['GrLivArea'] > 4000) & (data['SalePrice'] < 300000)]
#outputting the outliers which indicates home with very high GrLivArea but low SalePrice
print("----------HOMES WITH VERY HIGH (GrLivArea) BUT LOW (SalePrice)----------") 
print("------------------------------------------------------------------------")
print(outliers)
print("------------------------------------------------------------------------")