# Tutorial 3: SQL and Practices

This tutorial will go over the SQL language and certain commands that are avaliable for you to use. Since you will be using BigQuery to access the data for the challenge, you can use it to query specific information or perform certain calculations before it comes to your Jupyter notebook! Here, we'll go through a few basic commands for you to try and also some more advanced ones to show the power you have through BigQuery.

## SQL Basics

In this tutorial, we'll learn how to leverage SQL to query the data that we need from Big Query. It will introduce to the following basic sql commands: 

1. SELECT FROM
2. WHERE
3. GROUP BY and JOIN

You will be working with two different tables in the project `ironhacks-covid19-data`: `ironhacks-covid19-data.ironhacks_covid19_training.weather_data` and `ironhacks-covid19-data.ironhacks_covid19_training.covid19_cases`

You can find out more about the schema in those tables [here](https://docs.google.com/spreadsheets/d/1IowaQ8bDQA7xvc92TzpJ252KsHPDL6zbi2mdXNr3irs/edit?usp=drive_web&ouid=111649936971597408311). Indeed, it is important that you make yourself familiar with this schema before you start with this tutorial.

In this tutorial we will use two different libaries. Namely, the `bigquery` library, and the `pandas` library. The later will be used to display the tables as a dataframe. 

### SELECT FROM command

The SELECT FROM command is the most common command you use in SQL. This will help you select data from which ever table you like. You can select certain columns as well to filter out any data you may not need before processing. Some examples are below

```
query = """
SELECT * FROM `ironhacks-covid19-data.ironhacks_covid19_training.weather_data`
"""

query_job = bigquery_client.query(query)
data = query_job.to_dataframe()
data.head()
```

The example above will select all the data from the table because of the * symbol. Below is an example of what it would look like if you select a few columns.
```
query = """
SELECT 
WEEK_NUMBER,
WIND_SPEED
FROM `ironhacks-covid19-data.ironhacks_covid19_training.weather_data`
"""

query_job = bigquery_client.query(query)
data = query_job.to_dataframe()
data.head()
```

### WHERE command

The WHERE command helps us start filtering some of the data. For example, if we only would like the data from certain dates we can accomplish this through the WHERE command. It helps use define parameters for the query and returns a table back to you in which these conditions are true.

```
query = """
SELECT date, max_rel_humidity
FROM ironhacks-covid19-data.ironhacks_covid19_training.weather_data
WHERE date='2020-06-16'
"""

query_job = bigquery_client.query(query)
data = query_job.to_dataframe()
data.head()
"""

This query will now only retrieve entries that have a date as `2020-06-16`. We can also change the `=` to a `<`, `>`, `=>`, or `=<` based on which data you would like.
