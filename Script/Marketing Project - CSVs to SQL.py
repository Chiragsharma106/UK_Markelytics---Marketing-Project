# Use this Script to load the data in PostgreSQL

# In[1]:


import pandas as pd
import os
from sqlalchemy import create_engine


# In[2]:


folder = r"C:\Users\chira\Documents\All Files\PortFolio Dashboards💸\#2 MarketingDashboard\Data"


# In[3]:


pg_user = 'postgres'
pg_password = 'xxxxx'
pg_host = 'localhost'
pg_port = '5432'
pg_db = 'MarketingProject'


# In[4]:


PostgresCar = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')


# In[5]:


for files in os.listdir(folder):
    print(files)


# In[6]:


for files in os.listdir(folder):
    names = files.replace('Dim', '').replace('Fact', '').replace('_', '').lower().replace('.csv', '')
    df = pd.read_csv(os.path.join(folder, files))
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)
    df.to_sql(names, con = PostgresCar, if_exists = 'replace', index = False)
    print(f'{names} loading')
    print('Done')
    print("--"*50)
print("All Done")




