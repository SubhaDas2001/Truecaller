#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install phonenumbers


# In[11]:


import phonenumbers
number=input("Enter Phone Number with countrycode: ")
from phonenumbers import geocoder
ch_number=phonenumbers.parse(number,"CH")
print ("Country Name: ",(geocoder.description_for_number(ch_number,"en")))
from phonenumbers import carrier
carr=phonenumbers.parse(number,"RO")
print ("Service Provider: ",(carrier.name_for_number(carr,"en")))


# In[ ]:




