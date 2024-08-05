#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a program to print numbers from 1 to 10, but stop if the number is 5:
for i in range(1, 11):
    if i == 5:
        break
    print(i)


# In[2]:


# Write a program to iterate through a list and stop when encountering a specific element:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stop_element = 7

for element in my_list:
    if element == stop_element:
        break
    print(element)


# In[3]:


# Write a program to skip printing even numbers from 1 to 10:
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


# In[4]:


# Write a program to print numbers from 0 to 9 using range():
for i in range(10):
    print(i)


# In[5]:


# Write a program to print multiplication tables from 1 to 5 but stops after the first table is printed for each number:
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Print a newline after each table
    break  # Stop after the first table


# In[6]:


# Write a program to skip printing even numbers using a while loop:
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1


# In[ ]:




