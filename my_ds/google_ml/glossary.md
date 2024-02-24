# Glossary

[A](#a), [B](#b), [C](#c), [D](#d), [E](#e), [F](#f), [G](#g), [H](#h), [I](#i), [J](#j), [L](#l), [M](#m), [N](#n), [O](#o), [P](#p), [Q](#q), [R](#r), [S](#s), [T](#t), [U](#u), [V](#v), [W](#w)

## A

* Accuracy
* Activation Functions, introduces non-linearity in neuronal networks
* AUC stands for "Area under the ROC Curve."

## B

* backpropagation, training method for neural networks, a variant of gradient descent
* batch. In gradient descent, a batch is the total number of examples you use to calculate the gradient in a single iteration.
* bias, in ML they call the bias to the "b" of y = w<sub>i</sub>x<sub>i</sub> + b, in linear regression. In Algebra: **intercept**
* binary vector (that is that is only made of "0"s and "1"s. Use to represent categorical data.
* Bucketing and Prediction Bias

## C

* class imbalance, when positives or negatives are extremely rare
* classification model predicts discrete values
* In order to map a logistic regression value to a binary category, you must define a classification threshold (also called the decision threshold).
* categorical data, see categorical features
* categorical features have a discrete set of possible values
* collaborative filtering is the task of making predictions about the interests of a user based on interests of many other users.
* confusion matrix, an NxN table that summarizes how successful a classification model's predictions were.
* converged model, you iterate until overall loss stops changing or at least changes extremely slowly. When that happens, we say that the model has converged.
* convex, he resulting plot of loss vs. w<sub>i</sub> will always be convex.

## D

* data set, collection of examples?
* *D*, entire dataset
* diverge, model diverges (the error increases instead of decreasing). Happens when the Learning Rate is too big.
* Dropout Regularization, form of neural regularization for neural networks

## E

* edge, in neural networks, weight
* embeddings, which translate large sparse vectors into a lower-dimensional space that preserves semantic relationships.
* empirical risk minimization, in supervised learning, a machine learning algorithm builds a model by examining many examples and attempting to find a model that minimizes loss; this process is called empirical risk minimization; *`minimize: Loss(Data | Model)`*
* epoch, a full training pass over the entire dataset such that each example has been seen once. Thus, an epoch represents N/batch size training iterations, where N is the total number of examples. Each iteration is the span in which the system processes one batch. One epoch spans sufficient iterations to process every example in the dataset. One epoch spans sufficient iterations to process every example in the dataset. For example (in a data set with 12 examples), if the batch size is 12, then each epoch lasts one iteration. However, if the batch size is 6, then each epoch consumes two iterations.
* Example, is a particular instance of data, **x**
* encoding, **one-hot encoding** when a single value is 1, and a **multi-hot encoding** when multiple values are 1

## F

* feature, the descriptive attributes. The *x<sub>i</sub>* of a function.
* feature columns, it is a TensorFlow structure, which provide a sophisticated way to represent features
* feature cross is a *synthetic feature* that *encodes nonlinearity* in the feature space by multiplying two or more input features together.
* foreshadowing, loss function that is non-convex (egg crate shape). Has more than one minimum.
* feature engineering, the process of extracting features from raw data. You spend about 75% of the time there.
* feature vector, vector where strings are represented as floats (picture street names). Feature vector, which is the set of floating-point values comprising the examples in your data set.
* feedback-loop?

## G

* generalization, ML is not as much as fitting, as it is about generalization
* backpropagation's failure cases
* goldilocks learning rate is the learning rate that takes the fewest possible steps to achieve minimal loss
* Gradient Descent, strategy to find minimum point of loss function. Repeatedly take small steps in the direction that minimizes loss
* Gradient Steps, steps in the direction that minimizes loss. Learning Rate (scalar). Gradient Step = (Learning Rate/scalar) * (Gradient)

## H

* hidden layer" of intermediary values.
* Hyperparameters are the knobs that programmers tweak in machine learning algorithms. Hyperparameters are the configuration settings used to tune how the model is trained.

## I

* **indicator feature** says if another feature has values or not (in the market yes/no). Usually a boolean
* infer, predict y'
* inference means applying the trained model to unlabeled examples

## L

* L<sub>1</sub> regularization, encourage weights to drop to exactly 0
* L<sub>2</sub> regularization encourages weights to be small, but doesn't force them to exactly 0.0
* L<sub>2</sub> Loss, also known as **squared error**, sum of ***(y - y')^2*** over entire dataset (*D*)
* L<sub>2</sub> Regularization, penalizing complex models. ***Loss(Data|Model) + λ(w<sub>1</sub><sup>2</sup> + ... + w<sub>n</sub><sup>2</sup>)***
* label, what you're attempting to predict or forecast. The *y* of a function.
* Labeled example has {features, label}: (x, y)
* learning rate, Gradient descent algorithms multiply the gradient by a scalar known as the learning rate (also sometimes called step size). Learning Rate (scalar). Gradient Step = (Learning Rate) * (Gradient)
* Linear regression is a method for finding the straight line or hyperplane that best fits a set of points.
* LogLoss function, loss function used when training Logistic Regression models.
* logical conjunctions, `country:usa AND language:spanish`
* Logistic regresion, output is a probability. Instead of predicting exactly 0 or 1, logistic regression generates a probability, a value between 0 and 1.
* **loss function**, mathematical function that aggregates the individual losses in a meaningful fashion. There are many: L<sub>2</sub> Loss/sum of squared loss, MSE, gradient, ...

## M

* Mean Square Error (MSE) is the average squared loss, the L<sub>2</sub> Loss, per example over the whole dataset.
* ML is the process of training a piece of software, called a model, to make useful predictions using a data set.
* ML systems learn how to combine input to produce useful predictions on never-before-seen data
* memorizing the data (in neural networks), when a large model learns an island around an individual point of noise
* model, relationship between features and their corresponding labels.
* **multi-hot encoding** when multiple values are 1, and **one-hot encoding** when a single value is 1

## N

* Natural Language Understanding (NLU)
* neural networks might help with nonlinear problems,
* noise that will make it impossible to successfully classify every example
* normalization, The process of converting an actual range of values into a standard range of values, typically -1 to +1 or 0 to 1. For example, suppose the natural range of a certain feature is 800 to 6,000. Through subtraction and division, you can normalize those values into the range -1 to +1.

## O

* One vs. Al
* overfit
* **one-hot encoding** when a single value is 1, and a **multi-hot encoding** when multiple values are 1
* OOV (out-of-vocabulary) bucket, catch all for the rest
* overcrossing, overuse of feature crosses

## P

* precission,
* Prediction Bias
* predicted label, **y'**

## R

* recall,
* regression model predicts continuous values
* regularization, prevent overfitting by penalizing complex models
* L₁ Regularization
* risk minimization; empirical risk minimization, in supervised learning, a machine learning algorithm builds a model by examining many examples and attempting to find a model that minimizes loss; this process is called empirical risk minimization; *`minimize: Loss(Data | Model)`*
* risk minimization; structural risk minimization, add a second term penalize complexity; *`minimize: Loss(Data | Model) + complexity(Model`*
* ROC curve (receiver operating characteristic curve)

## S

* scaling means converting floating-point feature values from their natural range (for example, 100 to 900) into a standard range (for example, 0 to 1 or -1 to +1)
* sigmoid function
* Softmax extends this idea into a multi-class world. That is, Softmax assigns decimal probabilities to each class in a multi-class problem
* sparse representation in which only nonzero values are stored
* sparse tensors
* squared errorm, L<sub>2</sub> Loss, also known as "squared error", sum of **(y - y')^2** over entire dataset (*D*)
* step size, see Learning Rate
* structural risk minimization, add a second term to the *empirical risk minimization*, penalize complexity; *`minimize: Loss(Data | Model) + complexity(Model`*. In other words: *structural risk minimization = empirical risk minimization + `complexity(Model`*
* supervised learning is a type of ML where the model is provided with labeled training data
* synthetic feature, created artificially by us (e.g. rooms/person)

## T

* tail, long-tail
* tail, short-tail
* Training a model simply means learning (determining) good values for all the weights and the bias from labeled examples. Feed the features and their corresponding labels into an algorithm. Training means creating or learning the model.
* training set—a subset to train a model.
* test set—a subset to test the model.
* True Positives and False Positives

## U

* unlabeled example contains features but not the label **{features, ?}: (x, ?)**. Used for making predictions on new data
* unsupervised learning, the machine must learn from an unlabeled data set

## V

* vocabulary of possible values in categorical features, to integers.

## W

* weight, in ML they call the slope of the line **weight**, as in *y = w<sub>i</sub>x<sub>i</sub> + b*. In Algebra: ***m***

## Y

* y = w<sub>i</sub>x<sub>i</sub> + b. weight, in ML they call the slope of the line "weight". in ML they call the "b" -> bias
* **y'**, predicted label

* low-recall heuristic????
