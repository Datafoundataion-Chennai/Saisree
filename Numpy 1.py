#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Numpy Task1
import numpy as np
stock_prices=np.random.randint(100,500,(30,5))
print(stock_prices)
print(np.mean(stock_prices,axis=0))
max_values=stock_prices.max()
day,company=np.where(stock_prices==max_values)
print(f"\nHighest price recorded: {max_values} at Day {day[0] + 1}, Company {company[0] + 1}")
min_price = np.min(stock_prices)
max_price = np.max(stock_prices)
normalized_prices = (stock_prices - min_price) / (max_price - min_price)
print("\nNormalized Prices:\n", np.round(normalized_prices, 2))
risky_days = np.where(stock_prices < 200)  
print("\nRisky Investment Days:")
for day in np.unique(risky_days[0]):
    risky_prices = stock_prices[day][stock_prices[day] < 200]
    print(f"Day {day + 1}: {risky_prices.tolist()}")


# In[2]:


#Numpy Task 2
import numpy as np
resources = np.random.randint(15, 51, (6, 3))
print(resources)
total_resources = np.sum(resources, axis=0)
print(f"Total resources needed (tons): Oxygen: {total_resources[0]}, Water: {total_resources[1]}, Food: {total_resources[2]}")

max_monthly_consumption = np.max(resources, axis=0)
max_month_indices = np.argmax(resources, axis=0)

resource_names = ["Oxygen", "Water", "Food"]
for i in range(3):
    print(f"Highest {resource_names[i]} consumption: {max_monthly_consumption[i]} tons in month {max_month_indices[i] + 1}")

std_deviation = np.std(resources, axis=0)
print(f"Standard deviation of consumption: Oxygen: {std_deviation[0]:.1f}, Water: {std_deviation[1]:.1f}, Food: {std_deviation[2]:.1f}")

transposed_resources = resources.T
print("Transposed matrix:")
print(transposed_resources)


# In[3]:


#Numpy task 3
import numpy as np
resources = np.random.randint(15, 51, (6, 3))
print(resources)
total_resources = np.sum(resources, axis=0)
print(f"Total resources needed (tons): Oxygen: {total_resources[0]}, Water: {total_resources[1]}, Food: {total_resources[2]}")

max_monthly_consumption = np.max(resources, axis=0)
max_month_indices = np.argmax(resources, axis=0)

resource_names = ["Oxygen", "Water", "Food"]
for i in range(3):
    print(f"Highest {resource_names[i]} consumption: {max_monthly_consumption[i]} tons in month {max_month_indices[i] + 1}")

std_deviation = np.std(resources, axis=0)
print(f"Standard deviation of consumption: Oxygen: {std_deviation[0]:.1f}, Water: {std_deviation[1]:.1f}, Food: {std_deviation[2]:.1f}")

transposed_resources = resources.T
print("Transposed matrix:")
print(transposed_resources)


# In[ ]:




