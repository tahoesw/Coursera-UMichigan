
# coding: utf-8

# ## Unit Testing
# While we will not cover the [unit testing library](https://docs.python.org/3/library/unittest.html) that python has, we wanted to introduce you to a simple way that you can test your code.
# 
# Unit testing is important because it the only way you can be sure that your code is do what you think it is doing. 
# 
# Remember, just because ther are no errors does not mean your code is correct.

# In[ ]:

DATA_DIR = "/Users/wel51x/Box/MyBox/Courses/Coursera/UMich/StatisticsWithPython/data/"

import numpy as np
import pandas as pd
import matplotlib as plt
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe
pd.set_option('display.width', 155) # Show all columns when looking at dataframe

# In[ ]:

# Download NHANES 2015-2016 data
#df = pd.read_csv(DATA_DIR + "nhanes_2015_2016.csv", index_col = "SEQN")
df = pd.read_csv(DATA_DIR + "nhanes_2015_2016.csv")
df.index = range(1,df.shape[0]+1)
df.columns = df.columns.to_series().apply(lambda x: x.strip())

# In[ ]:

print(df.shape)
print(df.head())

# ### Goal
# We want to find the mean of first 100 rows of 'BPXSY1' when 'RIDAGEYR' > 60

# In[ ]:

# One possible way of doing this is:
#df1 = df[df.RIDAGEYR > 60].iloc[:100]
print(pd.Series.mean(df[df.RIDAGEYR > 60].iloc[:100]['BPXSY1']))
#print(pd.Series.mean(df[df.RIDAGEYR > 60].loc[range(0,100), 'BPXSY1']))
# Current version of python will include this warning, older versions will not

# In[ ]:

# test our code on only ten rows so we can easily check
test = pd.DataFrame({'col1': np.repeat([3,1],5), 'col2': range(3,13)}, index=range(1,11))
print(test)

# In[ ]:

# pd.Series.mean(df[df.RIDAGEYR > 60].loc[range(0,5), 'BPXSY1'])
# should return 5

print(pd.Series.mean(test[test.col1 > 2].iloc[:5]['col2']))
#print(pd.Series.mean(test[test.col1 > 2].loc[range(0,5), 'col2']))

# What went wrong?

# In[ ]:

print(test[test.col1 > 2].iloc[:5]['col2'])
#print(test[test.col1 > 2].loc[range(0,5), 'col2'])
# 0 is not in the row index labels because the second row's value is < 2. For now, pandas defaults to filling this
# with NaN


# In[ ]:

# Using the .iloc method instead, we are correctly choosing the first 5 rows, regardless of their row labels
print(test[test.col1 >2].iloc[range(0,5), 1])

# In[ ]:

print(pd.Series.mean(test[test.col1 >2].iloc[range(0,5), 1]))

# In[ ]:

# We can compare what our real dataframe looks like with the incorrect and correct methods
#print(df[df.RIDAGEYR > 60].loc[range(0,5), :]) # Filled with NaN whenever a row label does not meet the condition

# In[ ]:

print(df[df.RIDAGEYR > 60].iloc[range(0,5), :]) # Correct picks the first five rows such that 'RIDAGEYR" > 60

# In[ ]:

# Applying the correct method to the original question about BPXSY1
print(pd.Series.mean(df[df.RIDAGEYR > 60].iloc[range(0,100), 16]))

# Another way to reference the BPXSY1 variable
print(pd.Series.mean(df[df.RIDAGEYR > 60].iloc[range(0,100), df.columns.get_loc('BPXSY1')]))

