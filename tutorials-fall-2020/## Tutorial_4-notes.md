# Tutorial #4: Getting your notebook ready for submission

This tutorial will tell you how to prepare a submission that is "valid"! 

## 1. Cleaning up your notebook before submission

Before you head to the submission form there's a few steps you take to make sure your notebook is clean and easy to understand for anyone who might be looking at it.

### Remove outputs from cells

Some commands that run in your notebook produce unneccessary output making it harder to read and greatly increase the file size of your submission.

To clear cell output, right click inside the notebook and select `Clear Outputs` or `Clear All Outputs`

![clear cell outputs](https://i.imgur.com/hXNEl15.png)

Some outputs should *always be removed* when you find them.

__1. Notebook setup logging__

![package setup messages](https://i.imgur.com/8bDzUZ8.png)

__2. Error messages__

![cell error message](https://i.imgur.com/tzVcoy5.png)

__3. Notebook Data__

If you have printed out the contents of your working data at various steps this will siginificanltly increase the file size and will also increase loading time in the site's notebook viewer. It is best practice to remove any unecessary print commands and remove the outputs of any dataframes, query results, or other working data types prior to submitting.

__Hint:__ Use the capture command to disable cell output.

For certain cells you may wish automatically disable output. To do this you can add the [capture](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cellmagic-capture) magic command inside the cell.

```
%%capture
```

The reason for including your notebook file with the submission is for reviewers to understand your methods and through process. This is essentially your submission source code. The notebooks output will not be considered in the review process so it is always safe to clear all outputs before submissions. However, if you have worked to produce a nicely formatted table or some other output you would like to include with your work you can also clear the other cells individually.


### Adding sections/headers

Jupyter Notebooks allow for Markdown formatted cells in addition to code. A good practice to improve your submission's readability is to break many long sections of code up into logical sections using markdown cells with titles and a short description of what the next section is trying to accomplish.

### Code Comments

You may also make use of code comments throughout your notebook, but take care not to overuse them. Avoid using inline comments to the right of a line of code. Keep comments short and purposeful when they are used. If you find yourself writing a long explanation inside a code cell comment, it is probably better to move it into a more readable Markdown cell above.

--- 

## 2. Submitting properly formated notebooks

* .csv
* 	Removing index (pandas)
* 	Remove quotations around strings

 ### 3. Running timestamps on a frequent basis
One of the hacks rules is that you are using the IronHacks workspace. To make sure that you are doing this, we ask you to run a few cells everytime you execute your notebook

> [Insert cells here ] 

With this information you can prove that you are using our workspace. It also allows us to better understand your usage behavior, and develop features in the feature. 
