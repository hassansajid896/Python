
# coding: utf-8

# # Primitive Types
# ### Integer 
# ### Floats
# ### Boolean
# 
# # Strings
# ### slicing
# ### Strings indexing
# ### Strings Class Method
# 

# ## Integer

# In[21]:


x= int(input("Enter first num: "))
y = int(input("Enter second num: "))
sum = x + y
print("Your Answer is: ",sum)


# ## Float

# In[23]:


x = float(input("enter first NUmber: "))
y = float(input("enter Sec NUmber: "))
z = x*x +y
print("your answer is:",z )


# In[2]:


import math
x = float(input("Enter the value of x: "))
SqRoot = math.sqrt(x)
print("Sq of the given number is: ",SqRoot)


# ## Boolean

# In[13]:


birth_year = int(input("please enter your birthyear: "))
age = 2024 - birth_year
criteria = 18
eligiblity = age >= criteria
print("your eligiblity to vote is?", eligiblity)


# ## Strings Indexing

# In[15]:


text = ("My name is hassan")
x = text.index("is")
print(x)


# ## Strings Class Method

# In[24]:


name = "hassan Sajid"
print(name.capitalize())


# In[1]:


fruits = ['Banana' , 'Mango' , 'Apple']
x = fruits.count("Apple")
print(x)


# In[13]:


name = "hassan Sajid"
print(name.find("Sajid"))
print(name.isalpha())
print(name.isdecimal())
print(name.isnumeric())
print(name.title())
print(name.replace("hassan" , "Hassan"))


# ## Slicing

# In[12]:


name = "My name is Hassan Sajid"
print(name[5])

