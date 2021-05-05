#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to print &quot;Hello Python&quot;?
# 2. Write a Python program to do arithmetical operations addition and division.?
# 3. Write a Python program to find the area of a triangle?
# 4. Write a Python program to swap two variables?
# 5. Write a Python program to generate a random number?

# In[1]:


print("Hello Python") # printing the text 


# In[6]:


x = 2 # variable 1
y = 3 # variable 2
print("Aditiion of x and y :",x + y) # printing the addition result
print("Division of x and y :", round(x/y,2)) # printing the division result


# In[36]:


def area_of_traingle(b,h): # where b is breadth and h is height of traingle
    print('Calculated area of traingle is {}'.format((b*h)/2))


# In[37]:


area_of_traingle(2,4)


# In[29]:


def swap(a,b):
    print('The value of a before swapping is {} and the value of b before swapping is {}'.format(a,b))
    c = a # c is a temp variable
    a = b
    b = c
    print('The value of a after swapping is {} and the value of b after swapping is {}'.format(a,b))


# In[30]:


swap(2,4) # swapping a = 2, b =4


# In[26]:


import random # importing a rando module
print(random.random()) # printing a one random value


# In[ ]:




