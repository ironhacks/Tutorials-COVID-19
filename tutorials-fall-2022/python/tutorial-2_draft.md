# Tutorial #2: How to query data from BigQuery in a Notebook

> Want to just right into the notebook? [Click here](https://ironhacks.com/notebook-viewer?path=https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/master/tutorials-fall-2022/python/tutorial-2-biquery.ipynb)

**Welcome to part II of our tutorials designed for participants in the IronHacks. Here, we will show you how you can access our training data stored in BigQuery using a key stored in your user profile.**

**Before you get started**: This tutorial will not take more than 10 minutes and you should have the basic skill sets to work with the datasets thereafter. 

**Our goal**: Help you get started with the Python BigQuery Library, Python Pandas Library and Python Numpy Library in order to access a first temporal dataset stored in BigQuery! So if you have never used these libraries before this tutorial is critical for you

## # BigQuery - What's that?

BigQuery is Google's flagship data warehousing system: "Serverless, highly scalable, and cost-effective multi-cloud data warehouse designed for business agility". It allows you to analyze large amount of data using ANSI SQL at blazing-fast speeds, with zero operational overhead. You can find out more it at https://cloud.google.com/bigquery

**Why do we use BigQuery?** In the Unemployment Data Science Challenges you will use BIG DATA from our data provider, the Department of Workforce Development (DWD). Using Big Query will be very helpful as you can explore data without having to use them in memory etc. It will also set you up for the future of data science since BigQuery is replacing other BIG DATA services (e.g. Spark).

**How do we give you access to BigQuery?** In Big Query data are stored in projects. Inside a project there are multiple datasets. Each dataset can contain multiple tables. In this hack we give you access to a project called: `ironhacks-data`. In this project there are two datasets:`ironhacks-data:ironhacks_training` and `ironhacks-data:ironhacks_competition`. During the training period you will only find data in the first dataset. In this first tutorial we only use one first relatively simply structured table stored in this dataset. It is called `covid19_cases`.

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
gcloud auth login
```
Now we'll need to set the project in your environment

```
gcloud auth application-default login
```
Now we've set the credentials for your profile. Now lets set the project.
```
gcloud auth application-default set-quota-project ironhacks-data
```
Your terminal should look something like this now

<img src="https://i.imgur.com/6ol805q.png" alt=" icon" style="float: left; margin-right: 10px;" />


Now we can go back to our notebook environment and now we can progress as normal!

> Note: You will need to install "db-dtypes" for now to run the entire notebook. Run `pip install db-dtypes`. Once you run this, restart the kernal and you should be good to go!
```
BIGQUERY_PROJECT = 'ironhacks-data'
bigquery_client = bigquery.Client(project=BIGQUERY_PROJECT)

```

> Make sure to import the libraries as described in the notebook! 

## Making sure everything works

As some insurance, you can run the following code as a cell in your Jupyter Notebook

```
query = """
SELECT COUNT(*)
FROM `ironhacks-data.ironhacks_training.covid19_cases`
"""

query_job = bigquery_client.query(query)
covid19_cases_data = query_job.to_dataframe()
print(covid19_cases_data)
```
If you are able to see a Pandas Dataframe with some data in the output, that means you are all set to go! You can now access Ironhacks data when it is avaliable to you!

## FAQ and Troubleshooting

- **I'm getting an ADC error. What do I do?**

This would mean that either you didn't use the right login for your account or did not set the project with the second command. Please re-run the terminal commands 

- **I just jumped back into my notebook, why am I getting an authorization error?** 

You'll need to re-run the terminal commands when you start up your notebook again. 

- **I ran into a strange issue, Please help!**

No worries! This is a fairly new authentication method we are using, so feel free to email us [here](c562462b.groups.purdue.edu@amer.teams.ms)

## Authentication FAQ

- **I got a `USER_ACCOUNT_DENIED` Error. What do I do?**

This would usually indicate that you are a new register and have not been give permissions yet. Since this is a manual process, please give the team a bit of time to update. The last update happened on 11/2 at 9 AM. 

> If you still have this issue, then your Google account is not on the platform yet. We encourage you to use the same account you signed into Ironhacks with when logging into the workspace. Since we use Google to authenticate, we'll need a Google Account to make sure you get access to the project. If this is the case for you, please reach out to the team using the "Get in Touch" button in the top right of the Ironhacks website.  


- **I'm getting an ADC error in the terminal. Help me!**

Please run the commands `gcloud auth application-default login` and  `gcloud auth application-default set-quota-project ironhacks-data`. The first will be a authentication link similar to `gcloud auth login` and the other will run to save your credentials.  This should resolve the issue. Tutorial 2 has been updated for this as well, so you can use that as reference to make sure you input the commands in the correct order.

- **I'm getting a "ModuleNotFound" or "db-dtypes needs to be installed". What do I do?**

This package is unfortunately not installed. Please install it in a code cell using `!pip install db-dtypes` and then restart the kernel. You won't have to run this command again for the rest of the hack.
