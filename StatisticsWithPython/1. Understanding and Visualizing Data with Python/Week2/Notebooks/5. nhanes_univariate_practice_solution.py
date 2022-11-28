
# coding: utf-8

# # Practice notebook for univariate analysis using NHANES data
#
# This notebook will give you the opportunity to perform some univariate analyses on your own using the
# NHANES.  These analyses are similar to what was done in the week 2 NHANES case study notebook.
#
# You can enter your code into the cells that say "enter your code here", and you can type responses to
# the questions into the cells that say "Type Markdown and Latex".
#
# Note that most of the code that you will need to write below is very similar to code that appears in
# the case study notebook.  You will need to edit code from that notebook in small ways to adapt it to
# the prompts below.
#
# To get started, we will use the same module imports and read the data in the same way as we did in the
# case study:

# In[2]:

DATA_DIR = "/Users/wel51x/Box/MyBox/Courses/Coursera/UMich/StatisticsWithPython/data/"

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pd.set_option('mode.chained_assignment', None)

da = pd.read_csv(DATA_DIR + "nhanes_2015_2016.csv")
print(da.columns)

# ## Question 1
#
# Relabel the marital status variable [DMDMARTL](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#DMDMARTL)
# to have brief but informative character labels.  Then construct a frequency table of these values for all
# people, then for women only, and for men only.  Then construct these three frequency tables using only
# people whose age is between 30 and 40.

# Q1 solutions using both groupby and where

da["DMDMARTLx"]=da.DMDMARTL.replace({1:"Married", 2:"Widowed",3:"Divorced",4:"Separated",5:"Never Married",
                                     6:"Living with Partner",77:"Refused",99:"Dont know"})
da["RIAGENDRx"] = da.RIAGENDR.replace({1: 'Male', 2: 'Female'})
# recode the educational variable
da["DMDEDUC2x"] = da.DMDEDUC2.replace({1: "A:<9", 2: "B:9-11", 3: "C:HS/GED", 4: "D:Some college/AA",
                                       5: "E:College", 7: "F:Refused", 9: "G:Don't know"})

# check age interval - should be between 30 and 40 (not inclusive) for both methods

print("AGE INTERVAL CHECK\n")

da["agegroup"]=pd.cut(da.RIDAGEYR, bins=[31, 40], right=False)
print("GROUPBY METHOD")
print(da.groupby(["agegroup"])["RIDAGEYR"].min())
print(da.groupby(["agegroup"])["RIDAGEYR"].max())
print("")

selections = (da.RIDAGEYR < 40) & (da.RIDAGEYR > 30)
print("WHERE METHOD")
print(da.where(selections).RIDAGEYR.min())
print(da.where(selections).RIDAGEYR.max())
print("")

# print frequencies

print("EVERYONE")
print(da.DMDMARTLx.value_counts())
print("")

print("USING PD.CUT and GROUPBY\n")

print("GENDER ONLY")
print(da.groupby(["RIAGENDRx"])["DMDMARTLx"].value_counts())
print("")

print("AGE ONLY")
print(da.groupby(["agegroup"])["DMDMARTLx"].value_counts())
print("")

print("AGE AND GENDER")
print(da.groupby(["agegroup", "RIAGENDRx"])["DMDMARTLx"].value_counts())
print("")

print("USING WHERE\n")

selections = (da.RIAGENDRx == "Male")
print("MALES ONLY")
print(da.where(selections).DMDMARTLx.value_counts())
print("")

selections = (da.RIAGENDRx == "Female")
print("FEMALES ONLY")
print(da.where(selections).DMDMARTLx.value_counts())
print("")

selections = (da.RIDAGEYR < 40) & (da.RIDAGEYR > 30)
print("EVERYONE BETWEEN 30 AND 40")
print(da.where(selections).DMDMARTLx.value_counts())
print("")

selections = (da.RIAGENDRx == "Male") & (da.RIDAGEYR < 40) & (da.RIDAGEYR > 30)
print("MALES ONLY BETWEEN 30 AND 40")
print(da.where(selections).DMDMARTLx.value_counts())
print("")

selections = (da.RIAGENDRx == "Female") & (da.RIDAGEYR < 40) & (da.RIDAGEYR > 30)
print("FEMALES ONLY BETWEEN 30 AND 40")
print(da.where(selections).DMDMARTLx.value_counts())

# ## Question 2
#
# Restricting to the female population, stratify the subjects into age bands no wider than ten years, and
# construct the distribution of marital status within each age band.  Within each age band, present the
# distribution in terms of proportions that must sum to 1.

# recode marital status and gender so that they're treated as categorical
da1 = da.copy()
da1['DMDMARTL'] = da1.DMDMARTL.replace({1: 'Married', 2: 'Widowed', 3: 'Divorced', 4: 'Separated', 5: 'Never Married', 6: 'Living with Partner', 77: 'Refused', 99: 'Don\'t Know'})
da1['RIAGENDR'] = da1.RIAGENDR.replace({1: 'Male', 2: 'Female'})

# subset the data to include only females
da1 = da.where(da1.RIAGENDR == 'Female')

# cut age into bands no wider than 10 years
da1['AGEGRP'] = pd.cut(da1.RIDAGEYR, [20, 30, 40, 50, 60, 70, 80])

# Eliminate rare/missing values
dx = da1.loc[~da1.DMDMARTLx.isin(["Don't know", "Missing"]), :]

# group marital status by age group band
dx = dx.groupby(["AGEGRP"])["DMDMARTLx"]

# obtain the counts for marital status within each age group band
dx = dx.value_counts()

dx = dx.unstack() # Restructure the results from 'long' to 'wide'
dx = dx.apply(lambda x: x/x.sum(), axis=1) # Normalize within each stratum to get proportions
print("\nFemale Marital Status by Age Group")
print(dx.to_string(float_format="%.3f"))  # Limit display to 3 decimal places


# recode marital status and gender so that they're treated as categorical
da2 = da.copy()
da2['DMDMARTL'] = da2.DMDMARTL.replace({1: 'Married', 2: 'Widowed', 3: 'Divorced', 4: 'Separated', 5: 'Never Married', 6: 'Living with Partner', 77: 'Refused', 99: 'Don\'t Know'})
da2['RIAGENDR'] = da2.RIAGENDR.replace({1: 'Male', 2: 'Female'})

# subset the data to include only females
da2 = da.where(da2.RIAGENDR == 'Male')

# cut age into bands no wider than 10 years
da2['AGEGRP'] = pd.cut(da2.RIDAGEYR, [20, 30, 40, 50, 60, 70, 80])

# Eliminate rare/missing values
dx = da2.loc[~da2.DMDMARTLx.isin(["Don't know", "Missing"]), :]

# group marital status by age group band
dx = dx.groupby(["AGEGRP"])["DMDMARTLx"]

# obtain the counts for marital status within each age group band
dx = dx.value_counts()

dx = dx.unstack() # Restructure the results from 'long' to 'wide'
dx = dx.apply(lambda x: x/x.sum(), axis=1) # Normalize within each stratum to get proportions
print("\nMale Marital Status by Age Group")
print(dx.to_string(float_format="%.3f"), '\n')  # Limit display to 3 decimal places

# __Q3a.__ Use the `bins` argument to [distplot](https://seaborn.pydata.org/generated/seaborn.distplot.html)
# to produce histograms with different numbers of bins.  Assess whether the default value for this argument
# gives a meaningful result, and comment on what happens as the number of bins grows excessively large or
# excessively small.

# In[73]:

#da["HEIGHTGRP"] = pd.cut(da.BMXHT, [135, 145, 155, 165, 175, 185, 200]) # Create height strata based on these cuts
#sns.distplot(da.BMXHT.dropna(), bins=[135, 145, 155, 165, 175, 185, 200]).set_title('Body Height (cm) Distribution Plot')
df = da.loc[da.RIAGENDRx.isin(["Female"]), :]
dm = da.loc[da.RIAGENDRx.isin(["Male"]), :]

sns.distplot(df.BMXHT.dropna(), label='Female')
sns.distplot(dm.BMXHT.dropna(), label='Male').set_title("Distribution plot of Height by Gender")
plt.legend()
plt.show()

# __Q3b.__ Make separate histograms for the heights of women and men, then make a side-by-side boxplot showing
# the heights of women and men.

sns.boxplot(x="RIAGENDRx", y="BMXHT", data=da).set_title("Box plot of Height by Gender")
plt.show()

# __Q4a.__ What proportion of the subjects have a lower SBP on the second reading compared to the first?

sns.boxplot(data=(da['BPXSY1'] - da['BPXSY2'])).set_title('Systolic Difference Boxplot')
plt.show()

# __Q4b.__ Make side-by-side boxplots of the two systolic blood pressure variables.
sns.boxplot(data=da.loc[:,["BPXSY1","BPXSY2"]])
plt.show()

# Question 5
# Construct a frequency table of household sizes for people within each educational attainment category
# (the relevant variable is DMDEDUC2). Convert the frequencies to proportions.

print(da.DMDEDUC2x.value_counts() / da.DMDEDUC2x.value_counts().sum())

dx = da.groupby(["DMDEDUC2x"])["DMDHHSIZ"].value_counts()

# what datatype was returned?
#print(type(dx))

# what do the results look like?
print("\nBefore Unstack")
print(dx)

# restructure the results from 'long' to 'wide'
dx = dx.unstack()

# what datatype was returned?
#print(type(dx))

# how did .unstack() change the results?
print("\nAfter Unstack")
print(dx, '\n')

# normalize within each stratum to get proportions that sum to 1
dx = dx.apply(lambda x: x/x.sum(), axis=1)

# print the results and format to three decimal points
print(dx.to_string(float_format="%.3f"), '\n')

# __Q5b.__ Restrict the sample to people between 30 and 40 years of age.  Then calculate the median
# household size for women and men within each level of educational attainment.

daHH = da[['RIDAGEYR', 'RIAGENDRx', 'DMDEDUC2x', 'DMDHHSIZ']] #create new data frame with needed columns

daHH30 = daHH[(daHH.RIDAGEYR >= 30) & (daHH.RIDAGEYR <= 40)] # limit new df to ages 30-40

daHH30M = daHH30.groupby(['RIAGENDRx', 'DMDEDUC2x'])['DMDHHSIZ'].median()#calc the median on new df
print("Median Household size by Gender, Educ. Level for population between 30 & 40")
print(daHH30M, '\n')

# ## Question 6
#
# The participants can be clustered into "masked variance units" (MVU) based on every combination of the
# variables [SDMVSTRA](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#SDMVSTRA) and
# [SDMVPSU](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#SDMVPSU).  Calculate the mean age
# ([RIDAGEYR](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#RIDAGEYR)),
# height ([BMXHT](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.htm#BMXHT)),
# and BMI ([BMXBMI](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.htm#BMXBMI)) for each gender
# ([RIAGENDR](https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm#RIAGENDR)), within each MVU,
# and report the ratio between the largest and smallest mean (e.g. for height) across the MVUs.

# create new dataframes for Males and Females
dam = da.where(da.RIAGENDR == 1)
daf = da.where(da.RIAGENDR == 2)

# get max mean for age across every combo of SDMVPSU and SDMVSTRA
agemaxm = dam.groupby(['SDMVPSU', 'SDMVSTRA'])["RIDAGEYR"].mean().max()

# get min mean for age across every combo of SDMVPSU and SDMVSTRA
ageminm = dam.groupby(['SDMVPSU', 'SDMVSTRA'])["RIDAGEYR"].mean().min()

# print max, min and ratio
print("Male Age Max:", agemaxm)

print("Male Age Min:", ageminm)

print("Male Age Ratio:", agemaxm/ageminm, '\n')

# get max mean for age across every combo of SDMVPSU and SDMVSTRA
agemaxf = daf.groupby(['SDMVPSU', 'SDMVSTRA'])["RIDAGEYR"].mean().max()

# get min mean for age across every combo of SDMVPSU and SDMVSTRA
ageminf = daf.groupby(['SDMVPSU', 'SDMVSTRA'])["RIDAGEYR"].mean().min()

# print max, min and ratio
print("Female Age Max:", agemaxf)

print("Female Age Min:", ageminf)

print("Female Age Ratio:", agemaxf/ageminf, '\n')

# get max mean for height across every combo of SDMVPSU and SDMVSTRA
htmaxm = dam.groupby(['SDMVPSU', 'SDMVSTRA'])["BMXHT"].mean().max()

# get min mean for height across every combo of SDMVPSU and SDMVSTRA
htminm = dam.groupby(['SDMVPSU', 'SDMVSTRA'])["BMXHT"].mean().min()

# print max, min and ratio
print("Male Height Max:", htmaxm)

print("Male Height Min:", htminm)

print("Male Height Ratio:", htmaxm/htminm, '\n')

# get max mean for height across every combo of SDMVPSU and SDMVSTRA
htmaxf = daf.groupby(['SDMVPSU', 'SDMVSTRA'])["BMXHT"].mean().max()

# get min mean for height across every combo of SDMVPSU and SDMVSTRA
htminf = daf.groupby(['SDMVPSU', 'SDMVSTRA'])["BMXHT"].mean().min()

# print max, min and ratio
print("Female Height Max:", htmaxf)

print("Female Height Min:", htminf)

print("Female Height Ratio:", htmaxf/htminf, '\n')

# get max mean for BMI across every combo of SDMVPSU and SDMVSTRA
bmimaxm = dam.groupby(['SDMVPSU', 'SDMVSTRA'])["BMXBMI"].mean().max()

# get min mean for BMI across every combo of SDMVPSU and SDMVSTRA
bmiminm = dam.groupby(['SDMVPSU', 'SDMVSTRA'])["BMXBMI"].mean().min()

# print max, min and ratio
print("Male BMI Max:", bmimaxm)

print("Male BMI Min:", bmiminm)

print("Male BMI Ratio:", bmimaxm/bmiminm, '\n')

# get max mean for BMI across every combo of SDMVPSU and SDMVSTRA
bmimaxf = daf.groupby(['SDMVPSU', 'SDMVSTRA'])["BMXBMI"].mean().max()

# get min mean for BMI across every combo of SDMVPSU and SDMVSTRA
bmiminf = daf.groupby(['SDMVPSU', 'SDMVSTRA'])["BMXBMI"].mean().min()

# print max, min and ratio
print("Female BMI Max:", bmimaxf)

print("Female BMI Min:", bmiminf)

print("Female BMI Ratio:", bmimaxf/bmiminf, '\n')

# __Q6b.__ Calculate the inter-quartile range (IQR) for age, height, and BMI for each gender and
# each MVU.  Report the ratio between the largest and smallest IQR across the MVUs.

dam_mod = dam[['SDMVSTRA', 'SDMVPSU', 'RIDAGEYR', 'BMXHT', 'BMXBMI', 'RIAGENDR']]

dam_q3 = dam_mod.groupby(['SDMVPSU', 'SDMVSTRA', 'RIAGENDR'], axis=0).quantile(.75)
dam_q1 = dam_mod.groupby(['SDMVPSU', 'SDMVSTRA', 'RIAGENDR'], axis=0).quantile(.25)

dam_iqr = dam_q3 - dam_q3
dam_iqr.rename_axis('IQR', axis=1, inplace=True)

ratiom_age_iqr = dam_q3['RIDAGEYR'].max()/dam_q3['RIDAGEYR'].min()
print("Males' IQR Ratio for Age", round(ratiom_age_iqr, 3))

ratiom_height_iqr = dam_q3['BMXHT'].max()/dam_q3['BMXHT'].min()
print("Males' IQR Ratio for Height", round(ratiom_height_iqr, 3))

ratiom_bmi_iqr = dam_q3['BMXBMI'].max()/dam_q3['BMXBMI'].min()
print("Males' IQR Ratio for BMI", round(ratiom_bmi_iqr, 3), '\n')

daf_mod = daf[['SDMVSTRA', 'SDMVPSU', 'RIDAGEYR', 'BMXHT', 'BMXBMI', 'RIAGENDR']]

daf_q3 = daf_mod.groupby(['SDMVPSU', 'SDMVSTRA', 'RIAGENDR'], axis=0).quantile(.75)
daf_q1 = daf_mod.groupby(['SDMVPSU', 'SDMVSTRA', 'RIAGENDR'], axis=0).quantile(.25)

daf_iqr = daf_q3 - daf_q3
daf_iqr.rename_axis('IQR', axis=1, inplace=True)

ratiof_age_iqr = daf_q3['RIDAGEYR'].max()/daf_q3['RIDAGEYR'].min()
print("Female IQR Ratio for Age", round(ratiof_age_iqr, 3))

ratiof_height_iqr = daf_q3['BMXHT'].max()/daf_q3['BMXHT'].min()
print("Female IQR Ratio for Height", round(ratiof_height_iqr, 3))

ratiof_bmi_iqr = daf_q3['BMXBMI'].max()/daf_q3['BMXBMI'].min()
print("Female IQR Ratio for BMI", round(ratiof_bmi_iqr, 3), '\n')
