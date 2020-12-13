# Importing pandas
# 1. Import pandas under the alias pd
from numpy.core.numeric import NaN
import pandas as pd
import numpy as np

# 2. Print the version of pandas that has been imported
# print(pd.__version__)

# 3. Print out all the version information of the libraries that are required by the pandas library
# print(pd.show_versions())

# DataFrame basics
# 4. Create a DataFrame df from this dictionary data which has the index labels
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)

# 5. Display a summary of the basic information about this DataFrame and its data (hint: there is a single method that can be called on the DataFrame)
print(df.describe())

# 6. Return the first 3 rows of the DataFrame df
print(df.iloc[:3,:])

# 7. Select just the 'animal' and 'age' columns from the DataFrame df
#print(df.loc[:,['animal','age']])
print(df[['animal','age']]) 

# 8. Select the data in rows [3, 4, 8] and in columns ['animal', 'age']
#print(df.iloc[[3,4,8],[0,1]])
print(df[['animal', 'age']].iloc[[3,4,8]])

# 9. Select only the rows where the number of visits is greater than 3
print(df[df['visits']>=3])

# 10. Select the rows where the age is missing, i.e. it is NaN
print(df[df['age'].isna()==True])

# 11. Select the rows where the animal is a cat and the age is less than 3
print(df[(df.animal=='cat') & (df.age<3)])

# 12. Select the rows the age is between 2 and 4 (inclusive)
print(df[(df.age<2) & (df.age<=4)])

# 13. Change the age in row 'f' to 1.5
print(df.loc['f','age']) # =2.0
df.loc['f','age']=1.5
print(df.loc['f','age'])

# 14. Calculate the sum of all visits in df (i.e. find the total number of visits)
print(df['visits'].sum())

# 15. Calculate the mean age for each different animal in df
print(df['age'].groupby(df['animal']).mean())

# 16. Append a new row 'k' to df with your choice of values for each column. 
# Then delete that row to return the original DataFrame.

df.loc['k']=['elephant',50,10,'no']
print(df)
df = df.drop('k',axis=0)
print(df)

# 17. Count the number of each type of animal in df
print(df['animal'].value_counts())

# 18. Sort df first by the values in the 'age' in decending order, 
# then by the value in the 'visits' column in ascending order (so 
# row i should be first, and row d should be last)