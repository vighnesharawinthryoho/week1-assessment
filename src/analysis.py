#!/usr/bin/env python
# coding: utf-8

# # Week 1 Assessment - Data Analysis
# Employee salaries, department budgets, and student marks.

# In[1]:


import numpy as np
import pandas as pd

emp_df = pd.read_csv('../data/employees.csv')
dept_df = pd.read_csv('../data/departments.csv')
summary = emp_df.groupby('department')['salary'].agg(['count', 'mean', 'max'])
print(summary)
merged = pd.merge(summary.reset_index(), dept_df, on='department', how='outer')
print('Departments without employees:', merged[merged['count'].isna()]['department'].tolist())


# ## Benchmark with %timeit

# In[2]:


get_ipython().run_line_magic('timeit', "emp_df['salary'].mean()")

