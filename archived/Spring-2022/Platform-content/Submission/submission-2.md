<h3 align="center">Submission_week38a </h3>
<p align="center"> Your opportunity to submit a prediction for week 38 on Wednesday</p>



This is one of the multiple submission opportunities for the *COVID-19 Data Science Challenge Fall 2021* that has the goal to predict unemployment claims in Indiana.



> **This submission is not required to qualify for individual prizes and rewards laid out in the [task description](https://ironhacks.com/hacks/fall-2021-covid-19-data-science-challenge---python/task). However, we strongly suggest you submit often and early as the two best submissions will be considered for the final rewards. 

We hoped you enjoyed working with the unemployment data, vaccine data, as well as wage data in Indiana. 

This submission has the name **submission_week38a** because you are predicting the unemployment claims for week 38. 

Your task was to predict the `total_claims` for **week 38**. For each week there is a distinct list of **uu_ids** with unique `uu_id` in the table `prediction_list`. You should predict a value for each of those `uu_ids`. It is important that you review this list every time you work on a new week, as the list is changing over time (given the streaming nature of the data)

Please review the [task description](https://ironhacks.com/hacks/fall-2021-covid-19-data-science-challenge---python/task) or contact the IronHacks team if you have any questions about that.

> Note: It does not have your best submission.  In the end, your two best predictions will count when we select the top individuals. This submission is your first opportunity to check how good your model is. 

Empty submissions will not be considered, but you have plenty of room to improve afterward.

### Preparation of your submission

As articulated in the [task description](https://ironhacks.com/hacks/fall-2021-covid-19-data-science-challenge---python/task), you are required to prepare your submission using the workspace. Otherwise, we cannot evaluate your effort to explore.

Please include the following code snippet in your notebook so that you meet the requirements and [rules](https://ironhacks.com/hacks/fall-2021-covid-19-data-science-challenge---python/rules) of this challenge.

```
%%capture
%logstop
%logstart -t -r -q ipython_command_log.py global

#- IRONHACKS RESEARCH TRACKING CODE
#----------------------------------
# The following code is used to help our research team understand how you 
# our notebook environment. We do not collect any personal information with
# the following code, it is used to measure when and how often you work on
# your submission files.

import os
from datetime import datetime
import IPython.core.history as history

ha = history.HistoryAccessor()
ha_tail = ha.get_tail(1)
ha_cmd = next(ha_tail)
session_id = str(ha_cmd[0])
command_id = str(ha_cmd[1])
timestamp = datetime.utcnow().isoformat()
history_line = ','.join([session_id, command_id, timestamp]) + '\n'
logfile = open(os.environ['HOME']+'/ipython_session_log.csv', 'a')
logfile.write(history_line)
logfile.close()
```

We strongly recommend that you use the [IronHacks Submission Template Notebook](https://ironhacks.com/notebook-viewer?path=https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/master/tutorials-Spring-2021/python/ironhacks_submission_template.ipynb) to prepare your submission

---

### Required submission components

For this submission, there will be two **mandatory files**. In addition, you are also required to provide non-code-related submission material. 

**1. Prediction Output**

This is a `.csv` file containing your prediction output. 

- It should have 1 header row + # (one for each uu_id) rows
- 2 columns with the following structure and naming convention

```
uu_id, total_claims
c003ae43-1e0b-4ce2-bdc7-0734dc269393,3
...
```

This file should be named: `submission_prediction_output.csv`.

*Refer to [tutorial #4](https://ironhacks.com/hacks/fall-2021-covid-19-data-science-challenge---python/tutorials/cTe0J2XZYhjb0YDaCpPIL) for common mistakes that may prevent your submission from being scored.*

**2. Source Code Notebook**

This is the Jupyter Notebook (`.ipynb`) you used to create the prediction output file (1). 

It should contain all the code used to produce the prediction file and should be able to run again by another person to create the same '.csv' output file you submit along with it.

We recommend that you also comment on your code.

This file should be named: `submission_prediction_output.ipynb`.

---

**3. Additional submission components**

In addition, we also ask you to complete four additional non-programming or code-related questions about your submission. They should be written in natural language. 

1. **Model Summary**

We asked you to write a concise summary of your model, including: 

*  The model type (e.g. ARIMA)
*  The tables ([sheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vTCAQpHIcHaj8Tus9rkxqAbUQzBEc1zDCWgaDYReLjb7s9HTmzSwHQIrie9pYEEb1kVr2eI9qkLfzok/pubhtml)) and variables you used (also referred to as features)
*  Feature extraction/variable transformations performed
*  Key functions used (from existing libraries) or written (your own)
*  Approach for training and validating the model
*  Strengths and weaknesses of the model 
*  Modeling comparisons performed (if any)
*  Suggestions/ideas on how the model can be improved

Please be concise and use **natural language** to describe your model. You may include the original variable names but it is important that you do not go into all the model implementation details but highlight the components of your model. 

This section should be between 200 to 500 words (*min 500 characters).

> Please note that this information may be shared with your group members, so it is important that you take the time to write a proper model description. 

2. **Tags**

Please select 5 tags from a list of tags. We kindly ask you to use the existing tag list. If you feel that there is a tag missing, you can create your own tag as well (in case you want to create your own tags, we kindly ask you to use at least 3 tags from the existing tag list.

3. **Rationale**

In addition, we kindly ask you to share some more details on why you created and submitted this particular model. 

> Please not that this information will only be shared with the IronHacks team. It helps us to understand how you tackled the task. 

4. **References**

In order to comply with the IronHacks Honor's Code (see [rules](https://ironhacks.com/hacks/fall-2021-covid-19-data-science-challenge---python/rules), you are asked to submit all references that influenced your work. Please list URLs of GitHub repositories, online publications (DOIs), as well as other "grey references" (e.g. StackOverflow pages) that influenced your work. Please list each reference on a new line. 

See the example below for two references, one being a link to a paper and another one being a link to a website

```
https://doi-org.ezproxy.lib.purdue.edu/10.1038/s41586-020-2923-3
https://drsimonj.svbtle.com/ridge-regression-with-glmnet
```

Please do **NOT** list general website links (`https://www.stackoverflow.com`) as such links are NOT a source. A source needs to be clearly identifiable. In other words, we or other participants need to be able to check on it. 

**Optional: Visualizations/charts (`.html`)**: 

If you want you can also submit visualizations of your time-series data as an `html` file. This allows you to get ready for the final submissions where we ask you to also submit a visualization of your results. 

Please provide these visualizations in an `html` file with the name: `submission_visualization.html`

> *Note: This step is not required for this submission*
