
# coding: utf-8

# ### Visualizing Data in Python
# #### Tables, Histograms, Boxplots, and Slicing for Statistics
# 
# When working with a new dataset, one of the most useful things to do is to begin to visualize the data.
# By using tables, histograms, box plots, and other visual tools, we can get a better idea of what the data
# may be trying to tell us, and we can gain insights into the data that we may have not discovered otherwise.
# 
# Today, we will be going over how to perform some basic visualisations in Python, and, most importantly,
# we will learn how to begin exploring data from a graphical perspective.

# In[ ]:

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# We first need to import the packages that we will be using
import seaborn as sns # For plotting
import matplotlib.pyplot as plt # For showing plots

# Load in the data set
tips_data = sns.load_dataset("tips")


# #### Visualizing the Data - Tables
# When you begin working with a new data set,  it is often best to print out the first few rows before you
# begin other analysis. This will show you what kind of data is in the dataset, what data types you are
# working with, and will serve as a reference for the other plots that we are about to make.

# In[ ]:


# Print out the first few rows of the data
print(tips_data.head(), '\n')


# #### Describing Data
# Summary statistics, which include things like the mean, min, and max of the data, can be useful to get
# a feel for how large some of the variables are and what variables may be the most important.

# In[ ]:


# Print out the summary statistics for the quantitative variables
print(tips_data.describe())


# #### Creating a Histogram
# 
# After we have a general 'feel' for the data, it is often good to get a feel for the shape of the
# distribution of the data.

# In[ ]:


# Plot a histogram of the total bill
sns.distplot(tips_data["total_bill"], kde = False).set_title("Histogram of Total Bill")
plt.show()


# In[ ]:


# Plot a histogram of the Tips only
sns.distplot(tips_data["tip"], kde = False).set_title("Histogram of Total Tip")
plt.show()


# In[ ]:


# Plot a histogram of both the total bill and the tips'
sns.distplot(tips_data["total_bill"], kde = False)
sns.distplot(tips_data["tip"], kde = False).set_title("Histogram of Both Tip Size and Total Bill")
plt.show()


# #### Creating a Boxplot
# 
# Boxplots do not show the shape of the distribution, but they can give us a better idea about the center
# and spread of the distribution as well as any potential outliers that may exist. Boxplots and Histograms
# often complement each other and help an analyst get more information about the data

# In[ ]:


# Create a boxplot of the total bill amounts
sns.boxplot(tips_data["total_bill"]).set_title("Box plot of the Total Bill")
plt.show()


# In[ ]:


# Create a boxplot of the tips amounts
sns.boxplot(tips_data["tip"]).set_title("Box plot of the Tip")
plt.show()


# In[ ]:


# Create a boxplot of the tips and total bill amounts - do not do it like this
sns.boxplot(tips_data["total_bill"])
sns.boxplot(tips_data["tip"]).set_title("Box plot of the Total Bill and Tips")
plt.show()


# #### Creating Histograms and Boxplots Plotted by Groups
# 
# While looking at a single variable is interesting, it is often useful to see how a variable changes
# in response to another. Using graphs, we can see if there is a difference between the tipping amounts
# of smokers vs. non-smokers, if tipping varies according to the time of the day, or we can explore
# other trends in the data as well.

# In[ ]:


# Create a boxplot and histogram of the tips grouped by smoking status
sns.boxplot(x = tips_data["tip"], y = tips_data["smoker"]).set_title("Box plot of Tips by smoking status")
plt.show()


# In[ ]:


# Create a boxplot and histogram of the tips grouped by time of day
sns.boxplot(x = tips_data["tip"], y = tips_data["time"]).set_title("Box plot of Tips by time of day")

g = sns.FacetGrid(tips_data, row = "time")
g = g.map(plt.hist, "tip")
plt.show()


# In[ ]:


# Create a boxplot and histogram of the tips grouped by the day
sns.boxplot(x = tips_data["tip"], y = tips_data["day"]).set_title("Box plot & Histogram of Tips by Day")

g = sns.FacetGrid(tips_data, row = "day")
g = g.map(plt.hist, "tip")
plt.show()

