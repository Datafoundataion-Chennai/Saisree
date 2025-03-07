#!/usr/bin/env python
# coding: utf-8

# In[1]:


from  collections import Counter
from collections import OrderedDict
from collections import deque
requests = [
    ("bread", 5),
    ("milk", 2),
    ("bread", 3),
    ("cigarettes", 4),
    ("milk", 1)
]

od=OrderedDict()
for k,q in requests:
    if q in od:
        od[k]+=q
    else:
        od[k]=q
print(od)


# In[2]:


from collections import Counter
from collections import defaultdict

codewords = ["attack", "retreat", "sniper", "danger", "tanks", "enemy"]
intercepted = ["ckatta", "ratreet", "ksnat", "shadow"]

final=defaultdict(lambda:"UNKNOWN")

for word in codewords:
    sorted_word = "".join(sorted(word))
    final[sorted_word] = word
    
decoded_message = []
for word in intercepted:
    sorted_word = "".join(sorted(word))
    decoded_message.append(final[sorted_word])
    
print(final)
print(decoded_message)


# In[ ]:





# In[ ]:




