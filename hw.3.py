##hw.3


# coding: utf-8

# In[3]:


word=input('Please type anything.\n')


# In[6]:


aa=dict()
for s in word:
    if(s in aa):
        aa[s]=(aa[s]+1)
    else:
        aa[s]=1
zz=aa.keys()
number=aa.values()
for item in aa.items():
    zz,number=item
    print("'"+zz+"'",":",number)

