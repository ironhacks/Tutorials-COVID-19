## PART II: How to query data from BigQuery in a Notebook

In part II of our tutorials  we will show you how you can access our training data stored in BigQuery using a key stored in your user profile.

**Why?**In the COVID-19 Data Science Challenges you will use BIG DATA from our data providers SafeGraph, the Management Performance Hub (MPH), and other partners (Department of Workforce Development). The first hack Summer 2020, will use preprocessed data so you will not need to use all the functionalities of BigQuery as we have sampled down more than 50 datasets with more than 1 TB and millions of raws into a small sets of cleaned tables without missing entries and clear identifiers. However, using BigQuery will still be very helpful  as you can see for exploring data without having to use them in memory etc. It will also set you up for the future of data science since BigQuery is replacing other BIG DATA services (e.g. Spark).

**What will you exactly access?** In Big Query data are stored in projects. Inside a project there are multiple datasets. Each dataset can contain multiple tables. In this hack we give you access to a project called: `ironhacks-covid19-data`. In this project there are two datasets:`ironhacks-covid19-data:ironhacks_covid19_training` and `ironhacks-covid19-data:ironhacks_covid19_competition`. During the training period you will only find data in the first dataset. In this first tutorial we only use one first relatively simply structured table stored in this dataset. It is called `covid19_tests_cases_deaths_IN`. You can find a data dictionary [here] (https://docs.google.com/spreadsheets/d/1s591Ajha7KJMM0syot0Nc3fRRgEaT8zIU4BCPKeyEzk/edit#gid=557548514)

**How will you access the project?** `ironhacks-covid19-data`: You will access the data using a key. The key is accessible via your user profile. It is a json file. There are three steps: 1) Download the key 2) Add it to your workspace 3) following the instructions in the tutorial below to  use the key to query the database.

### Short tutorial prepared specifically for you by us

* View a notebook that gives you a step by step instruction in how to query BigQuery in an R notebook using your key check [here](https://ironhacks.com/notebook-viewer?path=https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/master/tutorials-fall-2020/R/Part2.ipynb) or download it [here](https://www.dropbox.com/s/le2hue8q98l4kwq/Part-II-BigQuery-and-notebookR_updated.ipynb?dl=0)

### Additional links and information material
For R:
* The `BigRQuery` package allows you to query data stored in BigQuery using R. More  [here}(https://bigrquery.r-dbi.org/)
* The `DBI` package helps you to use R to connect to database management systems (DBMS). You can find the official documentation [here](https://dbi.r-dbi.org/)
* `dplry` is is a grammar of data manipulation and also allows you to query BigQuery in R without using SQL. You can find the official documentation [here](https://dplyr.tidyverse.org/)
