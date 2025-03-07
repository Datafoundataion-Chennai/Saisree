#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


# pandas Task 1
import pandas as pd

# Given DataFrame
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
    'Age': [25, 32, 29, 41, 37, 45, 26, 38],
    'Salary': [50000, 70000, 65000, 80000, 75000, 90000, 62000, 85000],
    'Experience': [2, 7, 5, 15, 10, 20, 3, 12]
}

df = pd.DataFrame(data)
average_salary = df.groupby('Department')['Salary'].mean()
print("Average salary by department:")
print(average_salary)


highest_paid = df.loc[df.groupby('Department')['Salary'].idxmax()]
print("\nHighest-paid employee in each department:")
print(highest_paid[['Employee', 'Department', 'Salary']])

filtered_employees = df[(df['Experience'] > 5) & (df['Salary'] > 65000)]
count_filtered = filtered_employees.shape[0]
print("\nNumber of employees with more than 5 years of experience and salary above $65,000:", count_filtered)

def assign_seniority(experience):
    if experience < 5:
        return 'Junior'
    elif 5 <= experience <= 10:
        return 'Mid-Level'
    else:
        return 'Senior'

df['Seniority'] = df['Experience'].apply(assign_seniority)
print("\nDataFrame with Seniority column added:")
print(df[['Employee', 'Experience', 'Seniority']])


it_employees_sorted = df[df['Department'] == 'IT'].sort_values(by='Salary', ascending=False)
print("\nIT department employees sorted by salary in descending order:")
print(it_employees_sorted[['Employee', 'Department', 'Salary']])


# In[ ]:





# In[ ]:




