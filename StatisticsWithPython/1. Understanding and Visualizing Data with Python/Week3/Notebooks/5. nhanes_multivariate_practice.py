
# coding: utf-8

# # Practice notebook for multivariate analysis using NHANES data
# 
# This notebook will give you the opportunity to perform some multivariate analyses on your own using the
# NHANES study data.  These analyses are similar to what was done in the week 3 NHANES case study notebook.
# 
# You can enter your code into the cells that say "enter your code here", and you can type responses to the
# questions into the cells that say "Type Markdown and Latex".
# 
# Note that most of the code that you will need to write below is very similar to code that appears in the case
# study notebook.  You will need to edit code from that notebook in small ways to adapt it to the prompts below.
# 
# To get started, we will use the same module imports and read the data in the same way as we did in the case study:

# In[ ]:

DATA_DIR = "/Users/wel51x/Box/MyBox/Courses/Coursera/UMich/StatisticsWithPython/data/"

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import numpy as np

pd.set_option('mode.chained_assignment', None)

da = pd.read_csv(DATA_DIR + "nhanes_2015_2016.csv")
print(da.columns)

# ## Question 1
# 
# Make a scatterplot showing the relationship between the first and second measurements of diastolic blood
# pressure ([BPXDI1](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.htm#BPXDI1) and
# [BPXDI2](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.htm#BPXDI2)).  Also obtain the 4x4 matrix of
# correlation coefficients among the first two systolic and the first two diastolic blood pressure measures.

# In[ ]:

# enter your code here
plt.figure(figsize=(10,10))
plt.scatter(x = da.BPXDI1, y = da.BPXDI2)
plt.title("Scatter Plot of BPXDI1 vs BPXDI2")
plt.show()
#sy_corr = da.corr(method="pearson").BPXSY1.BPXSY2
#print(sy_corr)
#print(da.corr(method="pearson").BPXDI1.BPXDI2)
print("\nCorrelation Matrix of BPXSY1, BPXSY2, BPXDI1, BPXDI2")
df = da[['BPXSY1', 'BPXSY2', 'BPXDI1', 'BPXDI2']] #create new data frame with needed columns
print(df.corr(), '\n')
# __Q1a.__ How does the correlation between repeated measurements of diastolic blood pressure relate to
# the correlation between repeated measurements of systolic blood pressure?
# Slightly less correleated
# __Q2a.__ Are the second systolic and second diastolic blood pressure measure more correlated or less
# correlated than the first systolic and first diastolic blood pressure measure?
# First slightly more correlated
# ## Question 2
#
# Construct a grid of scatterplots between the first systolic and the first diastolic blood pressure
# measurement.  Stratify the plots by gender (rows) and by race/ethnicity groups (columns).

# In[ ]:

# insert your code here

df = da[['BPXSY1', 'BPXDI1', 'BPXSY2', 'BPXDI2', 'RIAGENDR', 'RIDRETH1']]
df["RIAGENDR"] = df.RIAGENDR.replace({1: 'Male', 2: 'Female'})
# recode the educational variable
df["RIDRETH1"] = df.RIDRETH1.replace({1: "Mexican Amer", 2: "Other Hispanic",
                                      3: "White", 4: "Black",
                                      5: "Other Race"})
df.rename(columns={"RIAGENDR": "Sex", "RIDRETH1": "Race"}, inplace = True)

plt.figure(figsize=(20,10))
graph = sns.FacetGrid(df, 'Sex', 'Race')
graph.map(sns.regplot, 'BPXSY1', 'BPXDI1', line_kws={"color": "red"})
plt.show()

# __Q2a.__ Comment on the extent to which these two blood pressure variables are correlated to different
# degrees in different demographic subgroups.

# ## Question 3
# 
# Use "violin plots" to compare the distributions of ages within groups defined by gender and educational
# attainment.

# In[ ]:


# insert your code here
plt.figure(figsize=(14, 8))
da["DMDEDUC2x"] = da.DMDEDUC2.replace({1: "<9", 2: "9-11", 3: "HS/GED", 4: "Some college/AA", 5: "College", 7: "Refused", 9: "Don't know"})

da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
da["AGEGRP"] = pd.cut(da.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])

df = da[da.DMDEDUC2 <= 5]
sns.violinplot("DMDEDUC2x", "RIDAGEYR", hue = "RIAGENDRx" , data = df, palette="husl")
plt.show()

# __Q3a.__ Comment on any evident differences among the age distributions in the different demographic groups.

# ## Question 4
# 
# Use violin plots to compare the distributions of BMI within a series of 10-year age bands.  Also stratify
# these plots by gender.

# In[ ]:

# insert your code here
plt.figure(figsize=(20,10))
#graph = sns.FacetGrid(da, 'RIAGENDRx', 'AGEGRP')

sns.violinplot("AGEGRP", "BMXBMI", hue="RIAGENDRx", data=df)
plt.show()

# __Q5a.__ Comment on the trends in BMI across the demographic groups.

# ## Question 5
# 
# Construct a frequency table for the joint distribution of ethnicity groups
# ([RIDRETH1](https://www.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#RIDRETH1)) and health-insurance status
# ([HIQ210](https://www.cdc.gov/Nchs/Nhanes/2015-2016/HIQ_I.htm#HIQ210)).  Normalize the results so that
# the values within each ethnic group are proportions that sum to 1.

# In[ ]:


# insert your code here
df = da[['HIQ210', 'RIDRETH1']]
df["RIDRETH1"] = df.RIDRETH1.replace({1: "Mexican Amer", 2: "Other Hispanic",
                                      3: "White", 4: "Black",
                                      5: "Other Race"})
df["HIQ210"] = df.HIQ210.replace({1: "Yes", 2: "No", 9:"Unknown"})

print("Uninsured in past year by Race")
dx = df.groupby(["RIDRETH1"])["HIQ210"].value_counts()
dx = dx.unstack()
dx = dx.apply(lambda x: x/x.sum(), axis=1)
print(dx.to_string(float_format="%.3f"), '\n')

# __Q6a.__ Which ethnic group has the highest rate of being uninsured in the past year?
