# Tutorial #3: SQL Basics

## Learn basic commands and syntax using an Jupyter notebook in this tutorial.

In the [#IronHacks](https://twitter.com/search?q=%23IronHacks&src=typed_query) challenges, you will query data from our BigQuery datasets.

BigQuery uses Standard SQL language.

You will write basic SQL queries in combination with some Python helper libraries that will let you connect to our data on BigQuery and use it in your predictions or models.

### What is SQL

`SQL` is a standard language for storing, manipulating and retrieving data in databases.

It is used in database systems like MySQL, SQL Server, MS Access, Oracle, Sybase, Informix, Postgres. BigQuery also uses SQL.

**A notebook to learn SQL by learning from doing?**

We created a notebook for you that allows you to try three different SQL statements.

You will query the training dataset specifically prepared for this hack.

Which you will find in the project `ironhacks_covid19_data`.

In the dataset `ironhacks_covid_training` you find two tables.

- `covid19_cases`
- `weather_data`

In this tutorial you will apply the following simple SQL statements

1. `SELECT` - The `SELECT` statement is used to select data from a database. Combined with a wildcard you can select all column in a table, or select on a subset on few ones.
2. `WHERE` -  The `WHERE` clause is used to filter records. It is used with the `SELECT` statement to reduce the number of results or return only a specific subset of data.
3. `JOIN` -  The `JOIN` statement is used to combine rows from two or more tables, based on a related (key) column between them. As you are hacking you will have access to multiple tables. With SQL `JOINS` you will be able to join data easily.

View a notebook that gives step by step instruction on basic SQL commands here [here](https://ironhacks.com/notebook-viewer?path=https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/master/tutorials-Spring-2022/python/tutorial-3-sql.ipynb). 

To work with this notebook we recommend that you.

1. Download it
2. And load it into your workspace.

Make sure you also have your key ready from your [user profile](https://ironhacks.com/profile)

See the previous tutorial in case you missed this step.

**Additional links and material**

- [SQL Cheatsheet](https://www.sqltutorial.org/sql-cheat-sheet/)
- [W3 School SQL Tutorial](https://www.w3schools.com/sql/default.asp)
- [Google BigQuery Syntax for SQL](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)
