# Tutorial #2: How to query data from BigQuery in a Notebook

In part II of our tutorials we will show you how to access the practice data stored in BigQuery using an access key that can be downloaded from your [user profile](https://ironhacks.com/profile) after you've registered for the event.

### Introduction

In the COVID-19 Data Science Challenges you will use BigData from our data providers **SafeGraph**, the **Indiana Management Performance Hub (MPH)**, and other partners like the **Indiana Department of Workforce Development**.

Overall the amount of data being created by these combined efforts is more than what your average analysis project can typically handle on your laptop of home P.C. Also the amount of time it would take for every participant to
download a copy of the data to their local machine in order to start writing code requires us to take a different (cloud based) approach.

The [#IronHacks](https://twitter.com/search?q=%23IronHacks&src=typed_query) [#ProtectPurdue](https://twitter.com/search?q=%23ProtectPurdue&src=typed_query) challenge team members have pre-processed all the data and moved it into Google Cloud's BigQuery service so all you will need to get access to the dataset is a an access key that is created for you (visit your profile after registration to download) after registration.

On BigQuery we have sampled down more than 50 datasets with more than 1 TB and millions of rows into a small sets of clean relevant tables.

It will also set you up for the future of data science since BigQuery is replacing other BigData services (e.g. Spark).

### Important Notes

- In BigQuery **data are stored in projects**
- Inside a project there are **multiple datasets**
- Each **dataset contains multiple tables**

### Project Setup

In this hack we give you access to a project called: `ironhacks-covid19-data`

In this project there are two datasets:

- `ironhacks_covid19_training`
- `ironhacks_covid19_competition`

To refer to a dataset use the notation `<PROJECT_ID>:<DATASET>`

Example:

```
ironhacks-covid19-data:ironhacks_covid19_training
```

During the training period you will only find data in the first training dataset.

In this first tutorial we only use a relatively simple table stored from the training dataset called `covid19_tests_cases_deaths_IN`.

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

- View a notebook that gives step by step instruction on how to query BigQuery in a Python notebook check [here](https://bit.ly/3ltrpYJ)
- Download it
- Upload it into your workspace
- and follow along with the code

### Additional links and information material

- Learn more about Google Cloud BigQuery [here](https://cloud.google.com/bigquery)
