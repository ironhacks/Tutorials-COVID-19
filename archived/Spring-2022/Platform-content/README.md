<h1 align="center">Task Description: IronHacks Data Science Training Challenge Spring 2022</h1>

## 1. Context and Goal

> Using training data to predict unemployment claims in the State of Indiana! 

COVID-19 has impacted citizens significantly. Many employers and industries had a hard time retaining employees and patrons as people stayed away from eating out and were required to work from home given the risk of virus spread inside closed buildings. As additional restrictions were either lifted or reimplemented and citizens got vaccinated, governments and corporations needed to understand how much and where people were most economically impacted.  An increase in the number of unemployment claims can indicate emerging trends in economic activity. Thus, in this training, your task is to predict the unemployment claims in Indiana in order to understand the COVID-19 impact and risk. We preprocessed very large, actual, and granular datasets from our partners. You will use this data to develop a predictive statistical model and communicate the results using data charts and maps. You will make two predictions over the duration of the training. With such predictions, you have the unique opportunity to help the state and leaders to use the outcome of your models and visualizations to monitor and predict economic impact.

We ask you to predict the number of unemployment claims by tract using historical data provided by DWD, as well as COVID-19 vaccine data. The data are **unique**: they are big, and they are granular. 


> This training challenge, including the worktime, is 1 week in length with **TWO** mandatory submissions.

Please review the [rules](https://ironhacks.com/hacks/spring-2022---jupyter-notebooks-python-training-hack/rules) before
you start hacking.


## 2. Data Science Task: Prediction modeling of unemployment claims in Indiana 

Your major task is to build a statistical model using data collected since week 1 of 2021 to predict the unemployment claims for census tracts in Indiana for future weeks.  In other words, you have to predict the `total_claims` for a future week. (Note, you may not need all those historical data in your modeling).

During the training you will learn how to create a data model, but for your submissions you can use a statistical model of your choice to make those predictions using historical data that we will provide you with. In fact, we ask you to **explore** a variety of models - from different kinds of regressions, time-series models, deep-learning models, support vector machines, etc. There is no limit to your effort to experiment. Indeed, we want to see a VARIETY of models being used.

> Note: Even if you are not an expert in modeling temporal data at the start of the training you should not shy away from participation. That's the whole point of the training! A visual inspection of the data and some data exploration analysis (DEA) will indicate that even a simple model may offer a good starting point. To make it up to the highest rank of the participants, we encourage you to explore and try different models! This is a fantastic learning opportunity.

## 3. Data and Libraries

### 3.1. Data

To make those predictions, we are providing pre-processed data from our data providers, including the Department of Workforce Development so that you can focus on the actual work of modeling. The level of analysis, and the most granular resolution of the data is a census tract. In our data, they can be identified with a unique `tract` number. 

There are four major tables that you can work with to train your model. These four tables provide you with the list of `uu_id` for which you should make the prediction. The schema of the pre-processed data that you will be used to "train" your model (e.g. estimating the
coefficient for your regression) is shown in a link to a Google Sheet with the critical parameters. The final table contains the list of `uu_id` for which you should make a prediction for a particular week.  The schema of these tables is discussed in this
[sheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vRXKC3wENGJai4mwOO3URPabezbP2YRNuFckMZ3DAPyf0GKmKfqhxVsa5MnnAO7Y8IYbPQKHWcJ7O-t/pubhtml).

| Nr   | Table name            | Brief Description                                            |
| ---- | :-------------------- | ------------------------------------------------------------ |
| 1    | `unemployment_data`     | This table is the **primary** table for your modeling efforts. This table has 25 columns and includes the historical data from week 1 to the most recent week for the `total_claims` for census tracts in Indiana. It also contains additional metrics such as gender, race, education level, and top industries with respect to claims |
| 2    | `vaccine_data`       | This table provides you with insights about the administration of vaccines in Indiana. This data is also temporal. You have access to data starting from week 1 in 2021 to the most current week in our database |
| 3    | `wage_data`    | This table contains average wage information by census tract. |
| 4    | `prediction_list` | This list provides the list of uu_ids needed to make a prediction for the particular week (see below). This table does not contain any additional data. It just clarifies which list of uu_ids you need to predict for the currently available submissions.

### 3.2. Data access

These tables are stored in BigQuery in a project called: `ironhacks-covid19-data`. In this project, you will find the dataset
`ironhacks_competition`. In there you find the tables with the names listed above.

> How do you get access to this dataset? You have to use your key in your user profile and follow the
> [tutorial #2](https://ironhacks.com/hacks/spring-2022---jupyter-notebooks-python-training-hack/tutorials) that describes
> how you query the data that we have prepared for you. So if you have not looked into these tutorials, it is time to do this immediately!
> If you have questions about it, please email ironhacks.team@gmail.com or get in touch via the "Get in touch"

### 3.3 Libraries

We have pre-installed a set of libraries in [python](https://bit.ly/377ly6m) that you can use throughout the competition to work with the
data in the JupyterLab. As stated in the [rules section](https://ironhacks.com/hacks/spring-2022---jupyter-notebooks-python-training-hack/rules)
you are asked to use those libraries.

## 4. Submission Requirements

You will submit your results via the [submission page](https://ironhacks.com/hacks/spring-2022---jupyter-notebooks-python-training-hack/submissions).
**IMPORTANT**: The detailed submission requirements are spelled out on the submission page so make sure you read carefully.

### 4.3. Submission Deadlines and Mandatory Submissions

In this hack, there are **TWO mandatory submissions**. We will score the **best** submission to qualify for awards. (see [rules](https://ironhacks.com/hacks/spring-2022---jupyter-notebooks-python-training-hack/rules)).
Please **carefully read section 7**  for more details on the submission process.

### 4.1. Required Submission Material for Submissions

For your submissions, you are asked to submit two files, a `.csv` and `.ipynb` file, and complementary information (such as a model description and a selection of tags)

#### 4.1.1. File one: The `.csv` file with your Predictions

Your `.csv` file with the prediction for the census tracts in Indiana with a unique `uu_id` for a specific  `week_number` is the most important part of
your submission. It needs to follow the following structure: A comma-separated CSV file containing all the uu_ids listed in the table
`prediction_list`. Please include the headers in your `.csv` file as follows.

```
uu_id, total_claims
9bee42b55f891413ae7fac2d9d89280a,3
...
```

You need to save this file with the following filename: `submission_prediction_output.csv`.

#### 4.1.2 File two: A Jupyter Notebook (`.ipynb`) to Produce Predictions

In addition to the `.csv` file, you are also required to submit a Jupyter Notebook (`.ipynb`) that you used to produce the results in the
`.csv` file. It should contain the code that you have used to produce the predictions. We recommend that you also comment on your code.
Please save it with the following name `submission_prediction_output.ipynb`.

#### 4.1.3. Complementary Information: Model Summaries, Tags, and References

When you submit you are also asked to provide additional comments such as a description of your model (min 150 words), a list of references
(working website links and doi is required) as well as a list of tags. Please review the submission details carefully about how to write a proper model description.

### 4.2. Submission Preparation

To help you prepare a high-quality submission that meets technical requirements (e.g. formatting of `.csv` and `.ipynb`), we have prepared a
tutorial for you [tutorial #4](https://ironhacks.com/hacks/spring-2022---jupyter-notebooks-python-training-hack/tutorials).
Please check it out so that your submission is successfully considered for evaluation.

In this hack, you are required to use the IronHacks workspace to prepare the submission (see rules) so that all participants work with the
same conditions, packages, and settings. We want this to be a fair competition. So if you are not running your code in our hub, you may lose
points as your effort in the hub will count towards your final performance. Please make sure that you use our template notebook as you are
working in our workspace. You can find the template
[here](https://ironhacks.com/notebook-viewer?path=https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/master/tutorials-fall-2021/python/ironhacks_submission_template.ipynb).

**IMPORTANT**: The detailed submission requirements are spelled out on the submission page. So, make sure you read carefully!

## 5. Evaluation

You will be evaluated on two **EQUALLY** weighted performance dimensions. We will discuss them next.

### 5.1.  Evaluation Category I: Prediction Accuracy

The first evaluation metrics relate to the accuracy of your prediction. Each submission will be evaluated with the
[**Mean Squared Prediction Error (MSPE)**](https://en.wikipedia.org/wiki/Mean_squared_error) as well as the
[**Mean Absolute Prediction Error (MAPE)**](https://en.wikipedia.org/wiki/Mean_absolute_error) of your predicted
values for `total_claims` for each of uu_ids listed in the `prediction_list` for the a. The formula of the **MSPE** and the **MAPE**
are as follows:

```asciimath
MSPE = 1/n sum_(i=1)^n(y_i - hat y_i)^2
```

```asciimath
MAPE = 1/n sum_(i=1)^n abs(y_i - hat y_i)
```

> ~n~ is the number uu_ids in the `prediction_list`  
> ~y~ is the observed `total_claims`  for the prediction week of that particular submission. 
> ~hat y_i~ is the predicted `total_claims` for that prediction week of that particular submission. 

---

We calculate your prediction accuracy right after your submission. 
The results should be visible very quickly - we plan to have your scores up within a day or so! Please be patient - if the scores are not published in the navigation section [`Results`](https://ironhacks.com/hacks/spring-2022---jupyter-notebooks-python-training-hack/results) do not worry! The team might be reviewing your results.  Keep checking on your scores! 

> A note: if you have log-transformed your data before estimating your coefficient, do not forget to revert that
> transformation before you submit your results!

### 5.2. Evaluation Category II: Exploration

There is a secondary and equally important evaluation metric which we call "exploration". Yes, this training is not just about building the best
model. We want you to explore new models that you have not yet tried before. So while we want you to build more predictive models, we also
want to make sure we recognize your effort to explore different models.

- Your effort to improve your statistical model (e.g. the number of value-adding submissions, the amount of value-adding changes to your
  software code without changing your model, number of unique commands)
- Your effort to try different solution approaches (e.g. your attempt to try out different functions and models in the statistical packages
  we have provided you with, or the coding of your own functions and models)
- Your activity in the workspace (e.g. how actively you work on the hub using the JupyterLab and BigQuery)

Such experimentation and exploration will not be evaluated in real-time as it takes some data pre-processing and expert judgment that
cannot be performed in real-time. It will only be examined at the end of the contest. However, we will release a proxy measure for that after each of your submissions.

> So isn't this exciting? You get the opportunity to explore different models?

## 6. Prizes and incentives

We will be evaluating individuals based on the two metrics stated above. Please review the scoring section for more details about how we rank individuals.  At minimum, prizes for individuals will be allocated as follows:

### 6.1. Prizes (monetary)

Top scoring participants who submit in accordance with the Rules will be eligible for a share of $500.

In addition, there are more additional benefits for you: 

* Certificate: Every participant will receive a digital certificate for participation with logos of the sponsors.
* Showcases: We will publish selected models www.ironhacks.com at the end of the competition.
* Fellowship opportunity: Selected participants will have the opportunity to discuss a fellowship at RCODI
* Learning experience: Based on what we have learned from the past, IronHacks will offer a great learning experience and practice for data scientists.

Please note that the top 3 submissions, will also be featured as **showcases**. We will showcase the best models, and discuss them with our partners. 
Thus, candidates that meet the criteria for making it among the top 3 will also have to submit charts in `.html` and `.ipynb`. More details will be stated on the actual submission page. For this training, the additional charts will be solicited from winning participants in cooperation with the RCODI team.

### 6.2 Certificates

Please note that **every** participant who has met all the requirements and rules of the training will receive a digital certificate for
participation. It will certify the successful completion of the IronHacks Data Science Training Challenge and list all partners. You can use this as a digital badge for your data science effort.

### 7. Submission schedule and targeted prediction week

As mentioned under section 3.4., in this challenge, you will work with preprocessed data that is provided to you. 

There are two mandatory submissions required to complete this training. At these milestones, you can get your model scored in terms of its accuracy. Further, you can also get evaluated in terms of your exploration effort.
 
In the table below, we lay out the submission schedule and the related target prediction.

| Submission name            | Date \|  Day       | Target prediction week |
| -------------------------- | :----------------- | ---------------------- |
| submission_week38         | 04/13 \| Wednesday    | Week 38                |
| submission_week39         | 04/15 \| Friday | Week 39                |


> **IMPORTANT**: The detailed submission requirements are spelled out on the [submission page](https://ironhacks.com/hacks/fall-2021-covid-19-data-science-challenge---python/submissions). So, make sure you read carefully!
