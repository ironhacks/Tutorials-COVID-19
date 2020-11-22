#!/usr/bin/env python
# coding: utf-8

# <h1 style = "text-align: center"> SQL Tutorial </h1>

# #### In this tutorial, we'll learn how to leverage SQL to query the data that we need from Big Query. Below are some examples for your reference. Feel free to explore more from the links that we have provided. In the example below, we are querying the entire data frame to investigate it further. 

# In[4]:


get_ipython().system('python3 -m pip install google.cloud')
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud.bigquery import magics
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='/home/jovyan/ironhacks-covid19-data-680c217a40e7.json'
bigquery_client = bigquery.Client(project='ironhacks-covid19-data')
bigquery_client
bigquery_client = bigquery.Client()



QUERY = """

SELECT *
FROM ironhacks-covid19-data.ironhacks_covid19_training.weather_data




"""

query_job = bigquery_client.query(QUERY)
get_ipython().system('python3 -m pip install pandas')
import pandas
data = query_job.to_dataframe()
data.head()


# #### The command shown below gives us the names of the columns of the dataset called "weather data"

# In[6]:


data.columns.tolist()


# #### Next, we wish to extract the date and relative humidity from the table when the date is 2020-06-16. "WHERE" command comes into play here; it is used when we want to get data with specific constraints, the constraint being the date here.

# In[14]:


from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud.bigquery import magics
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='/home/jovyan/ironhacks-covid19-data-680c217a40e7.json'
bigquery_client = bigquery.Client(project='ironhacks-covid19-data')
bigquery_client
bigquery_client = bigquery.Client()


QUERY = """

SELECT date, max_rel_humidity
FROM ironhacks-covid19-data.ironhacks_covid19_training.weather_data
WHERE date='2020-06-16'




"""

query_job = bigquery_client.query(QUERY)
get_ipython().system('python3 -m pip install pandas')
import pandas
data = query_job.to_dataframe()
data.head()


# #### Now, let's learn how to combine two tables from Google Big Query: "weather_data" and "covid19_tests_cases_deaths_IN". "JOIN" is used here; it combines covid tests from one table with the relative humidity from the other table, in accordance with the dates.

# In[15]:


from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud.bigquery import magics
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='/home/jovyan/ironhacks-covid19-data-680c217a40e7.json'
bigquery_client = bigquery.Client(project='ironhacks-covid19-data')
bigquery_client
bigquery_client = bigquery.Client()


QUERY = """

SELECT
  t1.DATE,
  t1.COVID_TEST,
  t2.max_rel_humidity
FROM ironhacks_covid19_training.covid19_tests_cases_deaths_IN t1
JOIN ironhacks_covid19_training.weather_data t2 ON t1.DATE = t2.date




"""

query_job = bigquery_client.query(QUERY)
get_ipython().system('python3 -m pip install pandas')
import pandas
data = query_job.to_dataframe()
data.head()


# In[ ]:




