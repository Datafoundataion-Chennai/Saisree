#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries 
import numpy as np 
import matplotlib.pyplot as plt 

# Creating dataset 
days= np.arange(1,11) 
stock_price = [150, 152, 149, 155, 160, 162, 158, 165, 170, 175]
trading_volume = [1.2, 1.4, 1.1, 1.8, 2.0, 2.5, 2.2, 2.7, 3.0, 3.5] 
#creating a figure and ax1 subplots to 
fig,ax1=plt.subplots()
# Plot stock price on left Y-axis
ax1.set_xlabel('Days')
ax1.set_ylabel('Stock Price (USD)', color='blue')
ax1.plot(days, stock_price, 'o-', color='blue', label='Stock Price')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax1.grid(True, linestyle='--', alpha=0.6)

# Create a second Y-axis
ax2 = ax1.twinx()
ax2.set_ylabel('Trading Volume (Million Shares)', color='tab:red')
ax2.plot(days, trading_volume, 's--', color='tab:red', label='Trading Volume')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Title and legend
plt.title("Stock Price & Trading Volume Over 10 Days")
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

plt.show()


# In[3]:


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
rent = [1200, 1200, 1200, 1200, 1250, 1250]
food = [400, 420, 450, 480, 500, 520]
entertainment = [150, 200, 220, 180, 250, 300]
transport = [100, 120, 130, 110, 140, 160]
plt.stackplot(months,rent,food,entertainment,transport,labels=['rent', 'food', 'entertainment', 'transport'],colors = ['red', 'yellow', 'green', 'blue'])
plt.xlabel("Months")
plt.ylabel("Prices")
plt.grid(True)
plt.legend(loc ="upper left")
plt.title("Monthly Expenses Comparision")
plt.show()


# In[4]:


import numpy as np
import matplotlib.pyplot as plt



weeks = np.arange(1, 9)  
covid_cases = [500, 700, 1200, 2000, 3000, 4500, 6000, 8000]  
vaccination_rate = [5, 10, 20, 35, 50, 65, 75, 85]  # In percentage

fig,ax=plt.subplots(2,1,figsize=(10,8))


ax[0].plot(weeks,covid_cases,marker='x',linestyle='-',color='red',label="week_cases")
ax[0].set_xlabel("Weeks")
ax[0].set_ylabel("covid_cases")
ax[0].set_title("weekly COVID-19 cases")
ax[0].legend()
ax[0].grid(True)



ax[1].bar(weeks,vaccination_rate,color='blue',label="vaccination_rate")
ax[1].set_xlabel("Weeks")
ax[1].set_ylabel("vaccination_rate")
ax[1].set_title("vaccination progress (%)")
ax[1].legend()
#ax[1].grid(True)
ax[1].grid(axis="y",linestyle="--",alpha=0.7)
           
plt.tight_layout()
plt.show()


# In[ ]:




