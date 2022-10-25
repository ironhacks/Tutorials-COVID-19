# Tutorial #2: How to query data from BigQuery in a Notebook

> Want to just right into the notebook? [Click here](https://ironhacks.com/notebook-viewer?path=https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/blob/harshapavuluri/tutorial-2-changes/tutorials-fall-2022/python/tutorial-2-biquery.ipynb)

**Welcome to part II of our tutorials designed for participants in the IronHacks. Here, we will show you how you can access our training data stored in BigQuery using a key stored in your user profile.**

**Before you get started**: This tutorial will not take more than 10 minutes and you should have the basic skill sets to work with the datasets thereafter. 

**Our goal**: Help you get started with the Python BigQuery Library, Python Pandas Library and Python Numpy Library in order to access a first temporal dataset stored in BigQuery! So if you have never used these libraries before this tutorial is critical for you

## # BigQuery - What's that?

BigQuery is Google's flagship data warehousing system: "Serverless, highly scalable, and cost-effective multi-cloud data warehouse designed for business agility". It allows you to analyze large amount of data using ANSI SQL at blazing-fast speeds, with zero operational overhead. You can find out more it at https://cloud.google.com/bigquery

**Why do we use BigQuery?** In the COVID-19 Data Science Challenges you will use BIG DATA from our data providers SafeGraph, the Management Performance Hub (MPH), and other partners (Department of Workforce Development). The first hack Summer 2020, will use preprocessed data so you will not need to use all the functionalities of BIG QUERY as we have sampled down more than 50 datasets with more than 1 TB and millions of raws into a small sets of cleaned tables without missing entries and clear identifiers. However, using BigQuery will still be very helpful as you can see for exploring data without having to use them in memory etc. It will also set you up for the future of data science since BigQuery is replacing other BIG DATA services (e.g. Spark).

**How do we give you access to BigQuery?** In Big Query data are stored in projects. Inside a project there are multiple datasets. Each dataset can contain multiple tables. In this hack we give you access to a project called: `ironhacks-covid19-data`. In this project there are two datasets:`ironhacks-covid19-data:ironhacks_covid19_training` and `ironhacks-covid19-data:ironhacks_competition`. During the training period you will only find data in the first dataset. In this first tutorial we only use one first relatively simply structured table stored in this dataset. It is called `covid19_cases`.

**Keep in mind**: In this tutorial you will learn how to get access to the ironhacks-covid19-data and the datset ironhacks-covid19-data:ironhacks_covid19_training stored inside this project.

**What's BigQuery**: Google Cloud Big Query package allows you to query data stored in BigQuery You can find the official documentation [here](https://googleapis.dev/python/bigquery/latest/index.html)

**What's Pandas** In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series

**What's Numpy** NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays

---


## Authorizing your BigQuery Access

- Open a terminal tab in your Notebook Environment
- Copy each command and follow the instructions provided by Google
- Setting the project(s) names that the you are authorized for to establish the database connection
- Listing the tables in the project

## Accessing BigQuery

To access the BigQuery data avaliable to you, all you need is to input 2 terminal commands and a small code segement and Jupyter Notebook will handle the rest for you! You are now able to access the competition data (when released) with just a few SQL commands.

This terminal command will create a Google Login link for you that will ask for your Google Login. You should login with the same account you registered for the hack for. Otherwise, you will not be able to access the data. 
```
gcloud auth application-default login
```
Now we'll need to set the project in your environment

```
gcloud auth application-default set-quota-project ironhacks-covid19-data
```
Your terminal should look something like this now

<img src="https://i.imgur.com/6ol805q.png" alt=" icon" style="float: left; margin-right: 10px;" />


Now we can go back to our notebook environment and now we can progress as normal!

> Note: You will need to re-run the terminal commands each time you re-open the notebook. But this will only need to be done once per session
```
BIGQUERY_PROJECT = 'ironhacks-covid19-data'
bigquery_client = bigquery.Client(project=BIGQUERY_PROJECT)

```

> Make sure to import the libraries as described in the notebook! 

## Making sure everything works

As some insurance, you can run the following code as a cell in your Jupyter Notebook

```
query = """
SELECT COUNT(*)
FROM `ironhacks-covid19-data.ironhacks_covid19_training.covid19_cases`
"""

query_job = bigquery_client.query(query)
covid19_cases_data = query_job.to_dataframe()
print(covid19_cases_data)
```
If you are able to see a Pandas Dataframe with some data in the output, that means you are all set to go! You can now access Ironhacks data when it is avaliable to you!

## FAQ and Troubleshooting

- I'm getting an ADC error. What do I do?
This would mean that either you didn't use the right login for your account or did not set the project with the second command. Please re-run the terminal commands 

- I just jumped back into my notebook, why am I getting an authorization error? 
You'll need to re-run the terminal commands when you start up your notebook again. 