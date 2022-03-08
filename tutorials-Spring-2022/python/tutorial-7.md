# Tutorial 7 - Building a Basic Regression Model

> Want to jump right into the code? [Click here for the notebook!](https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/harshpavuluri/tutorial-7-dev/tutorials-Spring-2022/python/tutorial-7-regression.ipynb)

One of the most basic forms of modeling you can do is a regression. It can come in many forms (Linear, Ridge, etc). Understanding how regression works and how to implement it is one of the foundational things to understand when begenning your journey as a data scientist. In this tutorial, we will be going through the fundementals over Logistic Regression, as well as looking over some code examples that you can run on your JupyterHub on the Ironhacks Platform.

## Outline

End of this tutorial, you should know the following:
 - Understand a lag regression model (Theory, properties, etc)
 - Be able to implement lag regression in python
 - Include preprocessing??
 - Be able to implement a simple solution for the hack (Using other related/similar data)

## Sections
 - Theory
  - Formulas
  - When is it useful?
  - Implementation on Time-Series
  - Underlying estimator and optimization 
 - Python Implementation
  - Packages
  - Data Retrival
  - Data Cleaning
  - Feature Engineering
  - Implementation (Jupyter Notebook)
  - Validation/ Evaulation
  - Visualization
 - Summary (How to use in the hack?)


## Theory

In this section, we will go through the implmentation on lag regression models, so that you can understand and be able to implement a simple model immediatly. 

A Distributed Lag Model is a model that lags a variable to get a better fitted data.

### Formulas

<!-- $$y = \alpha + \beta(L)x_t + u_t = \alpha + \sum_{s=0}^\inf \beta_s x_{t-s} + u_t$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=y = \alpha + \beta(L)x_t + u_t = \alpha + \sum_{s=0}^\inf \beta_s x_{t-s} + u_t"></div>

```u``` here is a stationary error term to make adjustments to the model. $\alpha$ represents the initial values. $\beta$ represents the lag weights for the independent variable, ```x```. This is the essential part of the the lag regression. Both $\beta$ and ```x``` create the lag distrubution when combined together. 

### When is it useful?



### Implementation on Time-Series

### Underlying estimator and optimization

## Implementation

> Check out the Jupyter Notebook here! [Logistic Regression](https://raw.githubusercontent.com/ironhacks/Tutorials-COVID-19/harshpavuluri/tutorial-7-dev/tutorials-Spring-2022/python/tutorial-7-regression.ipynb)




