#!/usr/bin/env python
# coding: utf-8

# In[4]:


items={"biryani":50,"chole":100,"desert":60}
print("welcome to the resturant")
biryani=int(input("Biryani = "))
chole=int(input("chole = "))
desert=int(input("desert = "))
total=biryani*items["biryani"]+chole*items["chole"]+desert*items["desert"]
tax=10
bill=total+tax
print("Your bill is RS" , bill)


# In[ ]:




