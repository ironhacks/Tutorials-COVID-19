
# Tutorial #6: Getting your notebook ready for submission

> Need the template? [Find it here!](https://ironhacks.com/notebook-viewer?path=https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/master/tutorials-fall-2022/python/ironhacks_submission_template.ipynb)

This tutorial will tell you how to prepare a submission that is "valid"! 

## 1. Cleaning up your notebook before submission

Before you head to the submission form there's a few steps you take to make sure your notebook is clean and easy to understand for anyone who might be looking at it.

### Remove outputs from cells

Some commands that run in your notebook produce unnecessary output making it harder to read and greatly increase the file size of your submission.

To clear cell output, right click inside the notebook and select `Clear Outputs` or `Clear All Outputs`

![clear cell outputs](https://i.imgur.com/hXNEl15.png)

Some outputs should *always be removed* when you find them.

__1. Notebook setup logging__

![package setup messages](https://i.imgur.com/8bDzUZ8.png)

__2. Error messages__

![cell error message](https://i.imgur.com/tzVcoy5.png)

__3. Notebook Data__

If you have printed out the contents of your working data at various steps this will significantly increase the file size and will also increase loading time in the site's notebook viewer. It is best practice to remove any unnecessary print commands and remove the outputs of any dataframes, query results, or other working data types prior to submitting.

__Hint:__ Use the capture command to disable cell output.

For certain cells you may wish automatically disable output. To do this you can add the [capture](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cellmagic-capture) magic command inside the cell.

```
%%capture
```

The reason for including your notebook file with the submission is for reviewers to understand your methods and through process. This is essentially your submission source code. The notebooks output will not be considered in the review process so it is always safe to clear all outputs before submissions. However, if you have worked to produce a nicely formatted table or some other output you would like to include with your work you can also clear the other cells individually.


### Adding sections/headers

Jupyter Notebooks allow for Markdown formatted cells in addition to code. A good practice to improve your submission's readability is to break many long sections of code up into logical sections using markdown cells with titles and a short description of what the next section is trying to accomplish. See tutorial #1 for more details on markdown language (and cheat sheet)

### Code Comments

You can use code comments while creating your submission, but when submitting your notebook, you will need to remove those in-line comments. Make sure that you check your code cells and make sure to clear any comments that you made.

### Remove empty cells and commented out code 

To keep your notebook readable you should remove any empty cells and any experimental code which is commented out and not used in your submission.

---

## 2. Check for errors in your submission csv file

To evaluate your submissions we make use of several scripts and programs for processing and scoring. We do our best to overcome any inconsistencies in the submission file, but you can take a few steps to ensure there are no issues that will cause your file to be graded incorrectly.

### Submission csv guidelines

- User the correct header values
- Only one record per line
- Values should use quotations unless required (for example a text list containing commas should be wrapped in quotations)
- Spaces between column separators are not required
- No missing values 
- No duplicate entries 
- No skipped or empty lines

__Correct Example:__

Below is an example of a correctly formatted .csv submission.

```
uuid,week,count
00681c7d-46b7-44e9-9b35-98331e53a204,18,34985
013b319a-9146-4623-a13d-a94db23ee41a,18,2273
015ae118-28e7-406d-b981-0bc32eb4859c,18,583
03d1a415-7627-4fa0-a02c-129a079b6e8d,18,154
```

### Avoid these common mistakes

__Mistake: Including Indexes__

Do not include the dataframe index column in your output. This may cause the scoring routine to read the wrong column when computing your score.

```
,uuid,week,count
0,00681c7d-46b7-44e9-9b35-98331e53a204,18,34985
1,013b319a-9146-4623-a13d-a94db23ee41a,18,2273
2,015ae118-28e7-406d-b981-0bc32eb4859c,18,583
3,03d1a415-7627-4fa0-a02c-129a079b6e8d,18,154
```

__Mistake: Incorrect header__

The correct header is given in the task and/or the submission form. Mislabeling your columns can lead to your results being unreadable by the scoring tools.

```
UUID,week_number,Foot_Traffic
00681c7d-46b7-44e9-9b35-98331e53a204,18,34985
013b319a-9146-4623-a13d-a94db23ee41a,18,2273
015ae118-28e7-406d-b981-0bc32eb4859c,18,583
03d1a415-7627-4fa0-a02c-129a079b6e8d,18,154
```

__Mistake: Wrapping output in quotations__

Some libraries may accidentally wrap all outputs in quotations when writing data to a file. This is not necessary and can have unintended side effects when processing your results. Specifically when quotes are wrapped around numbers the processing script may interpret the value as a string and be unable to perform mathematical operations correctly.

```
"uuid","week","count"
"00681c7d-46b7-44e9-9b35-98331e53a204","18","34985"
"013b319a-9146-4623-a13d-a94db23ee41a","18","2273"
"015ae118-28e7-406d-b981-0bc32eb4859c","18","583"
"03d1a415-7627-4fa0-a02c-129a079b6e8d","18","154"
```

__Mistake: Several multiple mistakes at once__

For most of the mentioned errors the submission scoring tools can overcome any single issue present, but if there there are several of these combined in a single submission then scoring will fail.

```
"","UUID","week_number","Foot_Traffic"
"1","00681c7d-46b7-44e9-9b35-98331e53a204","18","34985"
"2","013b319a-9146-4623-a13d-a94db23ee41a","18","2273"
"3","015ae118-28e7-406d-b981-0bc32eb4859c","18","583"
"4","03d1a415-7627-4fa0-a02c-129a079b6e8d","18","154"
```

### General submission tips

There are a few additional things your can check before submitting that aren't technically a mistake but can greatly improve your overall outcome.

- Check for duplicate values. Unless it's required, finding duplicate rows in your output can often point of a logical mistake in your model or code.
- Check to see if your output values make sense. If one of your values is a count of a thing, then you should not expect to find records with negative values in your results file. If this has happened then other non-negative values in your results may also be incorrect.
- Null values and missing rows. If you are finding empty data in your output you may have an error in your code. For example, a misspelled variable or missing key.

---

 ### 3. Running timestamps on a frequent basis

One of the hacks rules is that you are using the IronHacks workspace. To make sure that you are doing this, we ask you to run the notebook activity logging cell included in the submission template notebook during each of your working sessions. 

With this information you can prove that you are using our workspace. Further, it is essential for us to understand your exploration behavior. See the task description of the hack. It also allows us to better understand your usage behavior, and helps our team understand how we can improve the hub experience. 

> Read more about this in the [IronHacks Submission Template Notebook](https://ironhacks.com/notebook-viewer?path=https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/master/tutorials-fall-2022/python/ironhacks_submission_template.ipynb)

