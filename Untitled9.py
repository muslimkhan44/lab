
# coding: utf-8

# In[1]:

name=(input("Enter name:"))
print(name)


# In[4]:

cities=["karachi","lahore","islamabad","multan"]
print(cities)


# In[6]:

cities=["karachi","lahore","islamabad","multan"]
del cities[0]
print(cities)


# In[7]:

cities=["karachi","lahore","islamabad","multan"]
cities.append("canada")
print(cities)


# In[9]:

cities=["karachi","lahore","islamabad","multan"]
cities.sort(reverse=True)
print(cities)


# In[10]:

cities=["karachi","lahore","islamabad","multan"]
cities.sort(reverse=False)
print(cities)


# In[11]:

num=[1,2,3,4,5,6]
num.sort(reverse=True)
print(num)


# In[15]:

num=[1,2,3,4,5,6]
num.sort(reverse=False)
print(num)


# In[16]:

cities=["karachi","lahore","islamabad","multan"]
cities.pop()
print(cities)


# In[18]:

cities=["karachi","lahore","islamabad","multan"]
print(cities)


# In[20]:

cities=("karachi","lahore","islamabad","multan",1,2,3,4,5,6)
print(cities)


# In[21]:

cities=["karachi","lahore","islamabad","multan","pindi","hyderabad","peshawar","quetta","sawat","kashmir"]
print(cities)


# In[22]:

cities=("karachi","lahore","islamabad","multan","pindi","hyderabad","peshawar","quetta","sawat","kashmir")
print(cities)


# In[23]:

cities=["karachi","lahore","islamabad","multan","pindi","hyderabad","peshawar","quetta","sawat","kashmir"]
cities.sort(reverse=True)
print(cities)


# In[25]:

cities=["karachi","lahore","islamabad","multan","pindi","hyderabad","peshawar","quetta","sawat","kashmir"]
cities.sort(reverse=False)
print(cities)


# In[35]:

list1=cities[3:8]
print(list1)


# In[37]:

list2=cities[2:4]
list2.sort(reverse=True)
print(list2)


# In[43]:

cities=("karachi","lahore","islamabad","multan","pindi","hyderabad","peshawar","quetta","sawat","kashmir" ) 
x = slice(4)
print(cities[x])


# In[44]:

cities=("karachi","lahore","islamabad","multan","pindi","hyderabad","peshawar","quetta","sawat","kashmir" ) 
x = sorted(cities)
print(x)


# In[ ]:




# In[ ]:



