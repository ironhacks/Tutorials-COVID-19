## General guidelines for writing summary of your models during submission

In the summary section of the [submission template](https://ironhacks.com/hacks/fall-2022/submissions), you are required to explain the inherent logic for the algorithms of your choice. You are welcome to use equations if needed. Your summary would need to be at least 500 characters. 


<img src="https://i.imgur.com/RcNJ01Y.png" alt=" icon" style="float: left; margin-right: 10px;" />


**The guidelines for the summary are detailed below.**

### Description of the algorithm
* Fundamental logic of the algorithm. Please describe how the algorithm actually works, including statistical reasoning, optimization procedure, etc.
* Appropriate conditions for the algorithm. Please describe the conditions (i.e., problem type, data structure) where the algorithm will perform effectively and ineffectively.
* Essential parameters to be tuned. Please describe what the essential parameters for this algorithm mean and how they are tuned to get an optimal model.


### Description of the procedure
* Data request and initial processing: Describe in this step how you extract portions or all of data, engineering features for further analysis.
* Exploratory data analysis: Describe in this step how you visualize, summarize and identify a trend of the data, and how you choose particular algorithms.
* Functions for algorithms: Describe in this step how you define the algorithm, what libraries you used, or how you wrote your own.
* Parameter tuning: Describe in this step how you split data into training and testing, how you tune the parameters to find the best performing model. Please explain why you think the final model will achieve the highest prediction accuracy.
* Model comparison: Describe in this step how you choose models (if applicable).
* Strengths and weaknesses: Describe in this step suggestions and ideas on how the model can be improved.

### Packages used
Please list the packages used in building this model.


<br />
**This is a summary example on the use of ARIMA model for your reference.**
<br />


## A summary example of an ARIMA model. 

### Description of the algorithm
ARIMA is the name for ‘Auto Regressive Integrated Moving Average’ models. ARIMA is one of the most widely used approaches to time series forecasting. There is a component of an autoregressive model, where the dependent variable is forecasted using a linear combination of past values of that variable. This is like a multiple regression but with lagged values of y as predictors. Depending on the number of lags, they are referred to as AR(p) models. There is also a component of a moving average model, where past forecast errors are used in a regression-like model. Depending on the number of lagged differences, they are referred to as MA(q) models. An ARIMA model is characterized by 3 terms: p, d, q, where p is the order of the AR term, q is the order of the MA term, d is the number of differencing required to make the time series stationary.

### Description of the procedure
After pulling the data, I only kept the columns useful for my analysis. I chose daily data as the level of granularity. I visualized the time series of the target variable and decided to go with the ARIMA model because I could see there is a clear autoregressive pattern. ARIMA is implemented in the Statsmodels module, so I don't have to define the model from scratch. In an ARIMA model, I need to find the best parameters for p, d, q. These three parameters account for seasonality, trend, and noise in data. I used a grid-search to look for the best parameters. After finding the best set of parameters that generates the best AIC, I fit the final model using these parameters. I didn't compare with other models because I think the validation is OK. I used the final model to make predictions and made a visualization of the predicted trend.

### Packages used
Statsmodels
sklearn

As usual, if you have any question, feel free to use the "Get in Touch" button on the top right hand corner to message us. 

Happy Hacking! 
