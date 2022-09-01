# Long Short Term Models

  

## What is a LSTM?

  

Before we understand what a Long Short Term Model is, we have to begin to understand what a Recurrent Neural Network is. A Recurrent Neural Network, RNN for short, is a type of model that works on sequential data or time-series data. A simple way to explain this is the way you may read the book. Based on the previous chapter of a book, you can make predictions about the next chapter. But an RNN has some short-comings. It fails to retain information over a long time. In comes the LSTM to solve this issue.

  

A Long Short Term Model, LSTM for short, is a type of recurrent neural network that learns long term dependencies in a dataset. LSTM fixes the issue an RNN as it discards information that doe not help the model and keeps information that adds value to the model. This way, it can keep predicting the next input and keep learning from each new piece of data that is fed to it. Below we have a formula for how LSTM works.

  ```asciimath

i_t = sigma(w_i[h_(t-1),x_t]+b_i)

```

```asciimath

f_t = sigma(w_f[h_(t-1),x_t]+b_f)

```
```asciimath

o_t = sigma(w_o[h_(t-1),x_t]+b_o)

```

The 3 formulas here represent the input gate, forget gate,  and output gate respectively. Using a Sigmoid function, the W in each formula represents the neural weights for each respective gate. Inside each of the weights, you'll notice that it refers to the LSTM block from the previous input and X, which is the current timestamp. Then the B in each Sigmoid represents the biases for each gate.

## Packages used

  

When developing a a LSTM model, you will generally use the following packages:

- TensorFlow or Pytorch: Since you need to create a RNN, you'll need a machine learning package

- Pandas: This will help you handle the data retrieval and handling of any transformations

- Matplotlib: To plot and visualize the data

- Numpy: To do anymore data transformations that Pandas may not be able to achieve for data preparation

## How to build your model
Here's a step by step process to give you an idea for how to get the LSTM model working

 1. Request the Data from BigQuery
 2. Make sure you convert the Time-Stamp data to a numeric number
 3. Sequence the data into batches
 4. Run the data through a Min-Max Scaler to process the data easier
 5. Split the dataset into a train and test dataset
 6. Move the data into the GPU to process faster
 7. Define the LSTM Model
 8. Move the Model into the GPU
 9. Train the model and keep track of the training accuracy and loss
 10. Test the model using the test dataset to confirm its accuracy
 11. Feed sample dates to the model to get predictions

## References

-  [LSTM and its Equations](https://medium.com/@divyanshu132/lstm-and-its-equations-5ee9246d04af)
- Rumelhart, David E., Geoffrey E. Hinton, and Ronald J. Williams. "Learning representations by back-propagating errors." _nature_ 323.6088 (1986): 533-536.

