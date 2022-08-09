

# Tutorial #2: How to query data from BigQuery in a Notebook

  > Want to jump right into the code? [Click here for the notebook!](https://ironhacks.com/notebook-viewer?path=https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/master/tutorials-Spring-2021/python/tutorial-2-biquery.ipynb)

In part II of our tutorials, we will show you how to access the practice data stored in BigQuery using an access key that can be downloaded from your [user profile](https://ironhacks.com/profile) after you've registered for the event.

  

### Introduction

  

In the COVID-19 Data Science Challenges you will use BigData from our data providers like the **Indiana State Government**, and public datasets like the vaccine data from the [Indiana Data Hub](https://github.com/nytimes/covid-19-data).

  With the amount of data being used with this challenge being more than an average laptop or computer can handle, we figured that using more modern tools for data would be extremely beneficial. Enter Google Cloud's BigQuery!

With BigQuery, we are able to store and send data to all participants without the need to download files manually and automatically run with your code. All you need is a key that is provided for you to download in your profile on the Ironhack's website.

On BigQuery, we have sampled and cleaned the datasets necessary for the challenge. Follow the tutorial to get started and develop modern data science skills!

~~Overall the amount of data being created by these combined efforts is more than what your average analysis project can typically handle on your laptop of home P.C. Also the amount of time it would take for every participant to
download a copy of the data to their local machine in order to start writing code requires us to take a different (cloud-based) approach.~~

  

~~The [#IronHacks](https://twitter.com/search?q=%23IronHacks&src=typed_query)  [#ProtectPurdue](https://twitter.com/search?q=%23ProtectPurdue&src=typed_query) challenge team members have pre-processed all the data and moved it into Google Cloud's BigQuery service so all you will need to get access to the dataset is an access key that is created for you (visit your profile after registration to download) after registration.

  

On BigQuery we have sampled down more than 50 datasets with more than 1 TB and millions of rows into a small set of clean relevant tables.
  
It will also set you up for the future of data science since BigQuery is replacing other BigData services (e.g. Spark).~~

  

### Important Notes

  

- In BigQuery **data are stored in projects**

- Inside a project there are **multiple datasets**

- Each **dataset contains multiple tables**
- Make sure to get your key in your profile on the IronHacks website

  

### Project Setup

  

In this hack we give you access to a project called: `ironhacks-covid19-data`

  

In this project there are two datasets:

  

-  `ironhacks_covid19_training`

-  `ironhacks_covid19_competition`

  

To refer to a dataset use the notation `<PROJECT_ID>:<DATASET>:<TABLE_NAME>`

  

Example:

  

```

ironhacks-covid19-data:ironhacks_covid19_training

```

  

In this tutorial, we will use a data table called `covid19_cases`. This data is streamed and updated on a weekly basis so you should have access to real-time data. We used the public data from the New York Times to build this dataset.

  

You can find a dictionary of columns and meanings for the data [here](https://bit.ly/3pNY26V)

  

### Setting up your notebook for BigQuery

  

ProjectId: `ironhacks-covid19-data`

  

Visit your [user profile](https://ironhacks.com/profile) to download your access key after registering for the hack.

  

The key file is a JSON file with the same name as your IronHacks UserId.

  

There are three steps:

  

1. Download the key

2. Upload it to your hub workspace

3. Follow the instructions in the tutorial below to continue

  

### Short tutorial prepared specifically for you by us

  
  
- View a notebook that gives step by step instruction on how to query BigQuery in a Python notebook check [here](https://ironhacks.com/notebook-viewer?path=https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/master/tutorials-Spring-2021/python/tutorial-2-biquery.ipynb)

- Download it

- Upload it into your workspace

- and follow along with the code

  

### Additional links and information material

  

- Learn more about Google Cloud BigQuery [here](https://cloud.google.com/bigquery)

  

### Final note!

  

You will be accessing data that are updated on a weekly basis so are having access to real-time data that are streamed and updated on weekly basis. So the dataset in this training data also updates on a weekly basis (Thursday 12 pm)