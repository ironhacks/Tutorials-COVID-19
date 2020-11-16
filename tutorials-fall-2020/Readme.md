# Tutorials-COVID-19


Welcome to our tutorials and information material for the COVID-19 Data Science Challenges. This document contains an overview of topics we will be covering before and throughout the IronHacks COVID-19 data science challenge. This is "living document" and we will add more tutorials and information as we are working with the participants of the challenge. So please stay tuned for updates and check back in regularly. 

## General information material about the IronHacks platform

Before we dive into specific details, you might want to watch our infosession videos

* **[Infosession Slides](https://docs.google.com/presentation/d/1Eva1xLNyWyXf_zVq4afM2rVYeRnJpaIDPRoKUAog0kA/edit#slide=id.g896a3c3313_8_111)**

* **[Infosession Videos](https://www.youtube.com/watch?v=ta5i7_I5VT8&t=3s)**

We will add more material about the platform and its features as we go! If you have any specific questions, please reach out to the IronHacks team for a walkthrough. 

## Getting to know Juptyer Lab and Jupyter Notbooks

> What is Juptyer Lab? **Juptyer Lab is the generation of Juptyer Notebooks!** 

In this hack, you will be required to use Juptyer Notebooks (`.ipnyb`). If you haven't ever used those, we suggest you check out this first tutorials to get you started on a Notebook in 10 min.

### Short tutorial prepared specifically for you by us

* View a notebook to introduce you to Jupyter notebooks with an R Kernel [here](https://github.com/ironhacks/Tutorials-COVID-19/blob/master/part-1/PartI_IntroNotebookR.ipynb)
* View a notebook to introduce you to Jupyter notebooks with an Python Kernel [here](https://github.com/ironhacks/Tutorials-COVID-19/blob/master/tutorials-fall-2020/pyton/PartI_IntroNotebookPython.ipynb)

### Additional links and information material

* **[Official Juptyer Lab Video](https://www.youtube.com/watch?time_continue=260&v=A5YyoCKxEOU&feature=emb_logo)**
* **[Cheet Sheet Juptyer Notebooks](https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/master/Shortcuts.png?token=AC7DAY2TYDGKRV4CIQBVAG27FRYUG)**

## How to query data from BigQuery in a Notebook

In part II of our tutorials  we will show you how you can access our training data stored in BigQuery using a key stored in your user profile. 

**Why?**In the COVID-19 Data Science Challenges you will use BIG DATA from our data providers SafeGraph, the Management Performance Hub (MPH), and other partners (Department of Workforce Development). The first hack Summer 2020, will use preprocessed data so you will not need to use all the functionalities of BigQuery as we have sampled down more than 50 datasets with more than 1 TB and millions of raws into a small sets of cleaned tables without missing entries and clear identifiers. However, using BigQuery will still be very helpful  as you can see for exploring data without having to use them in memory etc. It will also set you up for the future of data science since BigQuery is replacing other BIG DATA services (e.g. Spark). 

**What will you exactly access?** In Big Query data are stored in projects. Inside a project there are multiple datasets. Each dataset can contain multiple tables. In this hack we give you access to a project called: `ironhacks-covid19-data`. In this project there are two datasets:`ironhacks-covid19-data:ironhacks_covid19_training` and `ironhacks-covid19-data:ironhacks_covid19_competition`. During the training period you will only find data in the first dataset. In this first tutorial we only use one first relatively simply structured table stored in this dataset. It is called `covid19_tests_cases_deaths_IN`. You can find a data dictionary [here] (https://docs.google.com/spreadsheets/d/1s591Ajha7KJMM0syot0Nc3fRRgEaT8zIU4BCPKeyEzk/edit#gid=557548514)

**How will you access the project?** `ironhacks-covid19-data`: You will access the data using a key. The key is accessible via your user profile. It is a json file. There are three steps: 1) Download the key 2) Add it to your workspace 3) following the instructions in the tutorial below to  use the key to query the database. 

### Short tutorial prepared specifically for you by us

* View a notebook that gives you a step by step instruction in how to query BigQuery in an R notebook using your key check [here](https://github.com/ironhacks/Tutorials-COVID-19/blob/master/part-2/Part-II-BigQuery-and-notebookR_updated.ipynb) or download it [here](https://www.dropbox.com/s/le2hue8q98l4kwq/Part-II-BigQuery-and-notebookR_updated.ipynb?dl=0)
* View a notebook that gives step by step instruction in how to query BigQuery in a Python notebook check [here](https://github.com/ironhacks/Tutorials-COVID-19/blob/master/tutorials-fall-2020/pyton/PartI_IntroNotebookPython.ipynb)  or download it [here] (https://www.dropbox.com/s/dh8b133v1yjbujm/Part-II-BigQuery-and-notebook-Python.ipynb?dl=0)

### Additional links and information material
For R: 
* The `BigRQuery` package allows you to query data stored in BigQuery using R. More  [here}(https://bigrquery.r-dbi.org/)
* The `DBI` package helps you to use R to connect to database management systems (DBMS). You can find the official documentation [here](https://dbi.r-dbi.org/) 
* `dplry` is is a grammar of data manipulation and also allows you to query BigQuery in R without using SQL. You can find the official documentation [here](https://dplyr.tidyverse.org/) 

For Python: 
* `Google Cloud Big Query` package allows you to query data stored in BigQuery. More [here](https://googleapis.dev/python/bigquery/latest/index.html)

## PART III: SOME SQL Basics

### Short tutorial prepared specifically for you by us
> This tutorial will be release soon. 

### Additional links and information material
> This tutorial will be release soon. 

## PART IV: To be decided
> This section will be release by August 2 or 3 depending upon requests from participants
