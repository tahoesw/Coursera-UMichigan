# coding: utf-8

# In[30]:

import math

# ## Data Types in Python 

# The following data types can be used in base python:
# * **boolean**
# * **integer**
# * **float**
# * **string**
# * **list**
# * **None**
# * complex
# * object
# * set
# * dictionary
# 
# We will only focus on the **bolded** ones

# Let's connect these data types to the the variable types we learned from the
# [Variable Types video](https://www.coursera.org/learn/understanding-visualization-data/lecture/iDodZ/variable-types).

# ###  Numerical or Quantitative (taking the mean makes sense)
# * Discrete
#     * Integer (int) #Stored exactly
# * Continuous
#     * Float (float) #Stored similarly to scientific notation. Allows for decimal places but loses precision.

# In[31]:

print("type(4):", type(4))

# In[32]:

print("type(0):", type(0))

# In[33]:

print("type(-3):", type(-3),'\n')

# In[34]:

#try taking the mean
numbers = [2, 3, 4, 5]
print("sum([2, 3, 4, 5])/len([2, 3, 4, 5]):", sum(numbers)/len(numbers))
print(type(sum(numbers)/len(numbers))) #In Python 3 returns float, but in Python 2 would return int

# **Floats**

# In[35]:

print("type(3/5):", type(3/5))

# In[36]:

print("type(6*10**(-1)):", type(6*10**(-1)))

# In[38]:

print("type(math.pi):", type(math.pi))

# In[39]:

print("type(4.0):", type(4.0),'\n')

# In[40]:

# Try taking the mean
numbers = [math.pi, 3/5, 4.1]
print("sum([math.pi, 3/5, 4.1])/len([math.pi, 3/5, 4.1]):", sum(numbers)/len(numbers))
print(type(sum(numbers)/len(numbers)))

# ### Categorical or Qualitative
# * Nominal
#     * Boolean (bool)
#     * String (str)
#     * None (NoneType)
# * Ordinal
#     * Only defined by how you use the data
#     * Often important when creating visuals
#     * Lists can hold ordinal information because they have indices

# **Boolean**

# In[41]:

# Boolean

print("type(True):", type(True), '\n')

# In[42]:

# Boolean
if 6 < 5:
    print("Yes!")

# In[43]:

myList = [True, 6<5, 1==3, None is None]
print("myList:", myList)
for element in myList:
    print(element, type(element))

# In[44]:

print("\nsum(myList)/len(myList):", sum(myList)/len(myList))
print("type:", type(sum(myList)/len(myList)),'\n')

# **String**

# In[45]:

print('"This sentence makes sense" is of type:', type("This sentence makes sense"))

# In[46]:

print('"Makes sentense this sense" is of type:', type("Makes sentense this sense"))

# In[47]:

type("math.pi")

# In[48]:

strList = ['dog', 'koala', 'goose']
print("strList =", strList)
try:
    print("sum(strList)/len(strList)", sum(strList)/len(strList))
except Exception as error:
    print("sum(strList)/len(strList): An exception occurred:", error)
# **Nonetype**

# In[49]:

# None

print("\ntype(None):", type(None))

# In[50]:

# None
x = None
type(x)

# In[51]:

noneList = [None]*5
print("noneList =", noneList)
try:
    print("sum(noneList)/len(noneList)", sum(noneList)/len(noneList))
except Exception as error:
    print("sum(noneList)/len(noneList): An exception occurred:", error)

# **Lists**
# 
# A list can hold many types and can also be used to store ordinal information.

# In[52]:


# List
myList = [1, 1.1, "This is a sentence", None]
print('\nmyList =', myList)
for element in myList:
    print(element, "is of", type(element))

# In[53]:

try:
    print("sum(myList)/len(myList)", sum(myList)/len(myList))
except Exception as error:
    print("sum(myList)/len(myList): An exception occurred:", error)

# In[54]:


# List
myList = [1, 2, 3]
print('\nmyList =', myList)
for element in myList:
    print(element, "is of", type(element))
print("sum(myList)/len(myList)", sum(myList)/len(myList), '\n') # note that this outputs a float


# In[55]:


myList = ['third', 'first', 'medium', 'small', 'large']
print("myList =", myList)
print("myList[0] =", myList[0])

# In[56]:


myList.sort()
print("myList sorted =", myList)
print("myList[0] =", myList[0])

# There are more datatypes available when using different libraries such as Pandas and Numpy, which we will introduce to you as we use them.
