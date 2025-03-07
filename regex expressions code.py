#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[9]:


import re
text = "Contact us at support@example.com, john.doe123@company.org, or invalid-email@com. Also, try jane_doe@domain.co.uk."
match = re.findall(r"[A-Za-z0-9._]+@+[A-Za-z0-9.]+",text)
print(match)


# In[7]:


import re
text = "Learning #Python is fun! #coding #100DaysOfCode #Regex_Challenge"
match = re.findall(r"#[A-Za-z0-9.]+",text)
print(match)


# In[11]:


import re
passwords = ["WeakPass", "Str0ng@Pass", "NoSpecial1", "short!1", "Secure#123"]
for password in passwords:
    if (len(password) >= 8 and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and 
        re.search(r"\d", password) and re.search(r"[@$!%*?&]", password)):
        print(f"{password} -> Valid")
    else:
        print(f"{password} -> Invalid")


# In[ ]:




