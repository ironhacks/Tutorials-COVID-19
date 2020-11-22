## Tutorial III: SOME SQL Basics

In this tutorial, we will introduce you into three some basic SQL Syntax. 

**Why?**

In the IronHacks challenges, you are querying data from BigQuery. BigQuery uses Standard SQL language. With the respective Python library you can query data in the BigQuery tables using Standard SQL.

**What is SQL**?

`SQL` is a standard language for storing, manipulating and retrieving data in databases.

It is used in database systems like MySQL, SQL Server, MS Access, Oracle, Sybase, Informix, Postgres. BigQuery also uses SQL. 

**A notebook to learn SQL by learning from doing? **

We have developed a notebook for you that allows you to try three differeny using SQL statements. You will query the training data sets specifically prepared for this hack. You find them in the projec `ironhacks_covid19_data`. In the dataset `ironhacks_covid_training` you find two tables. One  is `covid19_tests_cases_deaths_IN`. and the other one is `weather_data`. In this tutorial you will apply three simple SQL statements using three important statements. 



1. `SELECT`: The `SELECT` statement is used to select data from a database. Combined with a wildcard you can select all colums in a table, or select on a subset on few ones. 
2. `WHERE`: The `WHERE` clause is used to filter records. It is often used in the `SELECT` statement. Note, that is also used in other statements (e.g. `DELETE`). However, since you are only viewing our tables you will not be able to make such manupliations. 
3. `JOIN`: The `JOIN` statement is a very powerful statement. A `JOIN` clause is used to combine rows from two or more tables, based on a related column between them. As you are hacking you will have access to multiple tables. With SQL `JOINS` you will be able to join data easily. 

View a notebook that gives step by step instruction on basic SQL commands here [here]( https://ironhacks.com/notebook-viewer?path=https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/master/tutorials-fall-2020/python/Part3.ipynb). To work with this notebook we recommend that you.

1. Download it
2. And load it into your workspace. 

Make sure you also have your key ready from your [user profile](www.ironhacks.com/profile)

**Additional links and material**

* Here is a [cheatsheet](../resources/SQL-cheat-sheet.pdf) that is useful for working with SQL. 

* We also recommend you having a look at the official W3 School [tutorial on SQL](https://www.w3schools.com/sql/default.asp)
* Here is the official [BigQuery Syntax for SQL](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)





