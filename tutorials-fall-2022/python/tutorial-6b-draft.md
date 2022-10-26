## General guidelines for writing summary of your models during submission

* Data request and initial processing: Describe in this step how you extract portions or all of data, engineering features for further analysis.

* Exploratory data analysis: Describe in this step how you visualize, summarize and identify a trend of the data, and how you choose particular algorithms.

* Functions for algorithms: Describe in this step how you define the algorithm, what libraries you used, or how you wrote your own.

* Parameter tuning: Describe in this step how you split data into training and testing, how you tune the parameters to find the best performing model. Please explain why you think the final model will achieve the highest prediction accuracy.

* Model comparison: Describe in this step how you choose models (if applicable).

* Strengths and weaknesses: Describe in this step suggestions and ideas on how the model can be improved.

## A summary example with an ARIMA model. 

After pulling the data, I only kept the columns useful for my analysis. I chose daily data as the level of granularity. I visualized the time series of the target variable and decided to go with the ARIMA model because I could see there is a clear autoregressive trend. ARIMA is implemented in the Statsmodels module, so I don't have to define the model from scratch. In an ARIMA model, I need to find the best parameters for p, d, q. These three parameters account for seasonality, trend, and noise in data. I used a grid-search to look for the best parameters. After finding the best set of parameters that generates the best AIC, I fit the final model using these parameters. I didn't compare with other models because I think the validation is OK. I used the final model to make predictions and made a visualization of the predicted trend.