# About

[ML Concepts](#02-ml-concepts)

* [Framing](#01-framing)
* [Descencing into ML](#02-descending-into-ml)
* [Reducing loss](#03-reducing-loss)
* [First steps with TF](#04-first-steps-with-tf)
* [Generalization](#05-generalization)
* [Training and Test Sets](#06-training-and-test-sets)
* [Validation Set](#07-validation-set)
* [Representation](#08-representation)
* [Feature Crosses](#09-feature-crosses)
* [Regularization: Simplicity](#10-regularization-simplicity)
* [Logistic Regression](#11-logistic-regression)
* [Classification](#12-classification)
* [Regularization: Sparsity](#13-regularization-sparsity)
* [Neural Networks](#14-neural-networks)
* [Training Neural Nets](#15-training-neural-networks)
* [Multi-Class Neural Networks](#16-multi-class-neural-networks)
* [Embeddings](#17-embeddings)

## **00 NumPy ([NumPy Ultraquick Tutorial](https://colab.research.google.com/github/google/eng-edu/blob/master/ml/cc/exercises/numpy_ultraquick_tutorial.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=mlcc-prework&hl=en))**

NumPy is a Python library for creating and manipulating **vectors** and **matrices**.

## **01 Overview Introduction to Machine Learning Problem Framing**

Objectives:

* Define common ML terms
* Describe examples of products that use ML and general methods of ML problem-solving used in each
* Identify whether to solve a problem with ML
* Compare and contrast ML to other programming methods
* Apply hypothesis testing and the scientific method to ML problems
* Have conversations about ML problem-solving methods

### This course

* Articulate problem
* See if any labelled data exists
* Design your data for the model
* Determine where data comes from
* Determine easily obtained inputs
* Determine quantifiable outputs

### Common ML problems

ML makes *predictions*.
There is *supervised* and *unsupervised*.
Supervised ~ regression?
Unsupervised ~ cluster?
Reinforcement Learning (RL). In RL you don't collect examples with labels. Imagine you want to teach a machine to play a very basic video game and never lose. You set up the model (often called an agent in RL) with the game, and you tell the model not to get a "game over" screen. During training, the agent receives a reward when it performs this task, which is called a reward function. With reinforcement learning, the agent can learn very quickly how to outperform humans.

#### Common problems

* Classification
* Regression
* Clustering
* Association rule learning
* Structured output
* Ranking

### ML mindset

#### Get Comfortable with Some Uncertainty

Beyond simply thinking about problems differently, implementing ML is different than traditional programming. In traditional programming, you have set parameters and you understand how everything should behave. With ML, the non-coding work can be very complicated, but you'll usually write far less code.

Will you end-up with a usable model? You don't really know at the start.

#### Scientific Method

To address the challenges of transitioning to ML, it is helpful to think of the ML process as an experiment where we run test after test after test to converge on a workable model. Like an experiment, the process can be exciting, challenging, and ultimately worthwhile.

Step, Example

1. Set the research goal. I want to predict how heavy traffic will be on a given day.
2. Make a hypothesis. I think the weather forecast is an informative signal.
3. Collect the data. Collect historical traffic data and weather on each day.
4. Test your hypothesis. Train a model using this data.
5. Analyze your results. Is this model better than existing systems?
6. Reach a conclusion. I should (not) use this model to make predictions, because of X, Y, and Z.
7. Refine hypothesis and repeat. Time of year could be a helpful signal.

### Identifying Good Problems for ML

* Clear Use Case. Start with the problem, not the solution. Make sure you aren't treating ML as a hammer for your problems.
* Know the Problem Before Focusing on the Data. Be prepared to have your assumptions challenged.
* Lean on Your Team's Logs. ML requires a lot of relevant data. Data collected specifically for your task is going to be the most useful. In practice, you may not be able to do this, and you'll rely on whatever data you can get that's close enough.
* Predictive Power. Your features contain predictive power.
* Predictions vs. Decisions. Aim to make decisions, not just predictions.

### Hard ML Problems

* Clustering. What does each cluster mean in an unsupervised learning problem? For example, if your model indicates that the user is in the blue cluster, you'll have to determine what the blue cluster represents.
* Anomaly detection.
* Causation. ML can identify correlations—mutual relationships or connections between two or more things. Determining causation (one event or factor causing another) is much harder. In other words, it is easy to see that something happened, but much harder to understand why it happened.
* No Existing Data. As previously mentioned, if you have no data to train a model, then machine learning cannot help you.

### Deciding on ML

* Start Clearly and Simply. In plain terms, what would you like your ML model to do?
* What is Your Ideal Outcome?
* Success and Failure Metrics
  * Quantify It. How will you know if your system has succeeded or failed? Your success and failure metrics should be phrased independently of your evaluation metrics such as precision, recall, or AUC.
  * Are the Metrics Measurable? A measurable metric provides enough information for successful real-world evaluation.
* What Output Would You Like the ML Model to Produce?
  * Classification
  * Regression
  * Clustering
  * Association rule learning
  * Ranking
* Properties of Good Output.
  * The Output Must Be Quantifiable with a Clear Definition that the Machine can Produce.
  * The Output Should Be Connected To Your Ideal Outcome.
* Bad Objectives
* Heuristics

## **02 ML Concepts**

* Reduce time programming. Either you do, or take off the shelf ML tool.
* Customize and scale your products.
* Solve problems that you do not know how to code.

Shift from mathematics to natural. Think like a scientist.

### 01 Framing

In this course: Supervised Machine Learning.

What is (Supervised) ML?. ML systems learn to create models:

* how to combine input
* to produce useful predictions
* on never-before-seen data

#### Terminology

* ML systems learn how to combine input to produce useful predictions on never-before-seen data
* Label, the variable, the target, we are predicting. The **y**
* Features, input variables describing the data. The **{x<sub>1</sub>, x<sub>2</sub>}, ..., x<sub>n</sub>}**
* Example, is a particular instance of data, **x**
  * Labeled example has **{features, label}: (x, y)**. Used to train the model
  * Unlabeled example contains features but not the label **{features, ?}: (x, ?)**. Used for making predictions on new data
  * **y'** predicted label
* Model, relationship between labels and features. Model maps examples to predicted labels. Model is something we learn from data.
  * Training means creating or learning the model. That is, you show the model labeled examples and enable the model to gradually learn the relationships between features and label.
  * Inference means applying the trained model to unlabeled examples. That is, you use the trained model to make useful predictions (y').
* Regression vs. Classification
  * A regression model predicts continuous values.
  * A classification model predicts discrete values.

#### Pearls

* The labels applied to some examples might be unreliable.
* Good features are concrete and quantifiable.
Adoration is not an observable, quantifiable metric. The best we can do is search for observable proxy metrics for adoration.

### 02 Descending into ML

#### Linear regression

* **Linear regression** is a method for finding the straight line or hyperplane that best fits a set of points.

* In Linear regression the model looks like: ***y' = b + w<sub>i</sub>x<sub>i</sub>***. Where:
  * **y'** is the predicted label (a desired output).
  * **b** is the bias (the y-intercept). In ML they call the "b" **bias**. In Algebra **y-intercept**
  * **w<sub>1</sub>** is the weight of feature *1*. Weight is the same concept as the "slope" in the traditional equation of a line. In ML they call the slope of the line **weight**. In Algebra: **m**
  * **x<sub>1</sub>** is a feature (a known input)
* To infer (predict) the temperature for a new chirps-per-minute value, just substitute the value into this model.

#### Training and Loss

* **Training** a model simply means learning (determining) good values for all the weights and the bias from labeled examples.
* **empirical risk minimization**, in supervised learning, a machine learning algorithm builds a model by examining many examples and attempting to find a model that minimizes loss; this process is called empirical risk minimization
* **Loss** is the penalty for a bad prediction. That is, loss is a number indicating how bad the model's prediction was on a single example. If the model's prediction is perfect, the loss is zero; otherwise, the loss is greater. The goal of training a model is to find a set of weights and biases that have low loss, on average, across all examples. Loss, in linear regression: difference between predicted value and real value; between prediction and label, *(y' - y)*, maybe better: *(y'(x) - y(x))*
* **loss function**, mathematical function that aggregates the individual losses in a meaningful fashion
  * **L<sub>2</sub> Loss**, also known as **squared error** , sum of ***(y - y')^2***, **(observation - prediction(x))^2**, over entire dataset (*D*)
  * **Mean square error (MSE)** is the average squared loss per example over the whole dataset. To calculate MSE, sum up all the squared losses for individual examples and then divide by the number of examples. ***MSE = (L<sub>2</sub> Loss) / N***.
    * *N* is the number of examples in *D*
    * Although MSE is commonly-used in machine learning, it is neither the only practical loss function nor the best loss function for all circumstances.

NOTE: loss is *(y - y')*, so it is ON THE VERTCAL!!!! ONLY!!!!, ONLY ON THE LABEL!!!

#### Pearls

* In Linear Regression the model looks like: ***y' = b + w<sub>i</sub>x<sub>i</sub>***
* Loss
* Loss function
  * **L<sub>2</sub> Loss**
  * **Mean square error (MSE)**
* NOTE: loss is *(y - y')*, so it is ON THE VERTCAL!!!! ONLY!!!!, ONLY ON THE LABEL!!!

### 03 Reducing loss

In this module, you'll learn how a machine learning model **iteratively** reduces loss.

How to reduce loss?

* Hyperparameters, tune them. Trial and error?
* Derivative of *(y - y')^2* with respect to the weights and biases tells us how loss changes for a given example. Simple to compute and convex.
* So we repeatedly take small steps in the direction that minimizes loss. Take Gradient Steps using the Gradient Descent strategy.

#### An iterative approach

* "Hot and Cold" approach
* Loss reduction **converges** to the set of hyperparameters that minimizes the loss function.
* Iterative strategies are prevalent in machine learning, primarily because they scale so well to large data sets.
* Pick values for *b* and *w<sub>i</sub>*; calculate loss function; iterate over *b* and *w<sub>i</sub>*; iterate until overall loss stops changing or at least changes extremely slowly.
* For linear regression problems, it turns out that the starting values of *b* and *w<sub>i</sub>* aren't important.

#### Gradient descent

* match indicates that we should compute the gradient ***over all examples in our data set***. This is the only way to guarantee that our gradient steps are exactly in the right direction.
* Calculating the loss function for every conceivable value of  over the entire data set would be an inefficient way of finding the convergence point.
* The gradient of the loss is equal to the derivative (slope) of the curve
* Computing gradient of the loss function on small data samples, up to on one single sample, that mostly works too. You have to take more steps though.
* Stochastic Gradient Descent: one example at a time
* Mini-Batch Gradient Descent: batches of 10-1000. Loss & gradients are averaged over the batch.
* Regression problems yield convex loss vs. weight plots.
* Convex problems have only one minimum; that is, only one place where the slope is exactly 0. That minimum is where the loss function converges.
* When there are multiple weights, the gradient is a vector of partial derivatives with respect to the weights.
* convex, the resulting plot of loss vs. w<sub>i</sub> will always be convex
  * bowl shape
  * just one minimum
  * initial values do not matter that much
* Foreshadowing:
  * non-convex: think of an egg crate
  * more than one minimum
  * strong dependency on initial values

#### Learning Rate

* Gradient descent algorithms multiply the gradient by a scalar known as the **learning rate** (also sometimes called **step size**) to determine the next point.
* Hyperparameters are the knobs that programmers tweak in machine learning algorithms.
* Most machine learning programmers spend a fair amount of time tuning the learning rate. If you pick a learning rate that is too small, learning will take too long. Conversely, if you specify a learning rate that is too large, the next point will perpetually bounce haphazardly across the bottom of the well like a quantum mechanics experiment gone horribly wrong.
* There's a Goldilocks learning rate for every regression problem. The Goldilocks value is related to how flat the loss function is. The goldilocks learning rate is the learning rate that takes the fewest possible steps to achieve minimal loss.
* The ideal learning rate in one-dimension is ***1/y(x)''*** (the inverse of the second derivative of f(x) at x).
* The ideal learning rate for 2 or more dimensions is the inverse of the [Hessian](https://en.wikipedia.org/wiki/Hessian_matrix) (matrix of second partial derivatives).
* In practice, finding a "perfect" (or near-perfect) learning rate is not essential for successful model training. The goal is to find a learning rate large enough that gradient descent converges efficiently, but not so large that it never converges.

#### Stochastic Gradient Descent

* In gradient descent, a batch is the total number of examples you use to calculate the gradient in a single iteration.
* What if we could get the right gradient on average for much less computation? By choosing examples at random from our data set, we could estimate (albeit, noisily) a big average from a much smaller one. Stochastic gradient descent (SGD) takes this idea to the extreme--it uses only a single example (a batch size of 1) per iteration. Given enough iterations, SGD works but is very noisy. The term "stochastic" indicates that the one example comprising each batch is chosen at random.
* Mini-batch stochastic gradient descent (mini-batch SGD) is a compromise between full-batch iteration and SGD. A mini-batch is typically between 10 and 1,000 examples, chosen at **random**. Mini-batch SGD reduces the amount of noise in SGD but is still more efficient than full-batch
* epoch. Each iteration is the span in which the system processes one batch. One epoch spans sufficient iterations to process every example in the dataset. For example (in a data set with 12 examples), if the batch size is 12, then each epoch lasts one iteration. However, if the batch size is 6, then each epoch consumes two iterations.

* iterative approach
* gradient descent
* learning rate
* optimizing learning rate
* stocastic gradient descent

#### Pearls

* **iterative**
* Trial and error?
* Hyperparameters are the configuration settings used to tune how the model is trained.
  * Learning Rate (scalar). Gradient Step = (Learning Rate) * (Gradient)
* Learning Rate ~ Scalar * Gradient Step
* If Learning Step is too big, the model diverges (the error increases instead of decreasing). In this case, we should reduce the Learning Step by an order of magnitude.
* A Machine Learning model is trained by starting with an initial guess for the weights and bias and iteratively adjusting those guesses until learning the weights and bias with the lowest possible loss.
* Hyperparameters
  * Learning Rate
  * epochs
  * Batch size

### 04 First Steps with TF

[TensorFlow](https://www.tensorflow.org/)
[TensorFlow extended TFX](https://www.tensorflow.org/tfx)

### 05 Generalization

#### Objectives

* Develop intuition about overfitting.
* Determine whether a model is good or not.
* Divide a data set into a training set and a test set.

* How Do We Know If Our Model Is Good?
  * Theoretically:
    * Interesting field: generalization theory
    * Based on ideas of measuring model simplicity / complexity
  * Intuition: formalization of Ockham's Razor principle
    *The less complex a model is, the more likely that a good empirical result is not just due to the peculiarities of our sample
  * Empirically
    * Asking: will our model do well on a new sample of data?
    * Evaluate: get a new sample of data-call it the test set
    * Good performance on the test set is a useful indicator of good performance on the new data in general: if the test set is large enough; if we don't cheat by using the test set over and over

#### Peril of overfitting

* overfitting, model fits very well on training data, but poorly in test data. Overfitting occurs when a model tries to fit the training data so closely that it does not generalize well to new data.
* overfit. overfitting is caused by making a model more complex than necessary. The less complex an ML model, the more likely that a good empirical result is not just due to the peculiarities of the sample.
* overfitting does not generalize?
* generalization, ML is not as much as fitting, as it is about generalization. Performing well in the test data. Do a correct inference
* generalization bounds--a statistical description of a model's ability to generalize to new data based on factors such as:
  * the complexity of the model
  * the model's performance on training data

Training vs. Test Sets

* training set, a subset to train a model
* test set, a subset to test the model

Three basic assumptions in all of the above

    * We draw examples independently and identically (i.i.d.) at random from the distribution. In other words, examples don't influence each other.
    * The distribution is stationary: It doesn't change over time
    * We always pull from the same distribution: Including training, validation, and test sets

In practice, we sometimes violate these assumptions.

* If the key assumptions of supervised ML are not met, then we lose important theoretical guarantees on our ability to predict on new data.
* When we know that any of the preceding three basic assumptions are violated, we must pay careful attention to metrics.

Test loss 0.345
Training loss 0.280

#### Pearls

* Overfitting occurs when a model tries to fit the training data so closely that it does not generalize well to new data.
* If the key assumptions of supervised ML are not met, then we lose important theoretical guarantees on our ability to predict on new data.

### 06 Training and Test Sets

#### Splitting Data

Slice the single data set as follows:

* training set, a subset to train a model
* test set, a subset to test the model. Ensure that:
  * Is large enough to yield statistically meaningful results.
  * Is representative of the data set as a whole. In other words, don't pick a test set with different characteristics than the training set.

* Do randomization before splitting data (e.g. avoid all "winter" data ends in one set only)
* Split sizes. The larger the Train, the better the model. The larger the Test the more **confidence** will have in the model.
* small data set may force to do cross-valiation.
* Split about 80% train, 20% test
* Test set serves as a proxy for new data

#### Pearls

* Never train on test data
* Do randomization before splitting data (e.g. avoid all "winter" data ends in one set only)
* Split about 80% train, 20% test

### 07 Validation Sets

Partitioning a data set into a training set and test set lets you judge whether a given model will generalize well to new data. However, using only two partitions may be insufficient when doing many rounds of hyperparameter tuning.

You can greatly reduce your chances of overfitting by partitioning the data set into the three subset:

* Training set
* Validation set. Use it to evaluate results from the training set.
* Test set. Uset it to double-check your evaluation after the model has "passed" the validation set.

### 08 Representation

#### **Objectives**

* Map fields from logs and protocol buffers into useful ML features.
* Determine which qualities comprise great features.
* Handle outlier features.
* Investigate the statistical properties of a data set.
* Train and evaluate a model with tf.estimator.

#### **Feature Engineering**

* Data does not come clean.
* **Feature engineering**, the process of extracting features from raw data. You spend about 75% of the time there.
* Mapping categorical values
  * Feature vector, vector of features?
  * String values
  * vocabulary of possible values in categorical features, to integers
  * OOV (out-of-vocabulary) bucket, catch all for the rest
  * sparse representation in which only nonzero values are stored

A machine learning model can't directly see, hear, or sense input examples. Instead, you must create a **representation** of the data to provide the model with a useful vantage point into the data's key qualities. That is, in order to train a model, you must choose the set of features that best represent the data.

The left side of Figure 1 illustrates raw data from an input data source; the right side illustrates a **feature vector**, which is the set of floating-point values comprising the examples in your data set. **Feature engineering** means transforming raw data into a feature vector.

Categorical data. Create a **binary vector** (that is that is only made of "0"s and "1"s)for each categorical feature in our model that represents values as follows:

* For values that apply to the example, set corresponding vector elements to 1.
* Set all other elements to 0.

The length of this vector is equal to the number of elements in the vocabulary. This representation is called a **one-hot encoding** when a single value is 1, and a **multi-hot encoding** when multiple values are 1.

* One-hot encoding extends to numeric data that you do not want to directly multiply by a weight, such as a postal code.
* sparse representation in which only nonzero values are stored.

#### **Qualities of Good Features**

* Avoid rarely used discrete feature values; non-zero several times
* clear meaning (e.g. years in 2010, instead of seconds since UNIX epoc)
* Good floating-point features don't contain peculiar out-of-range discontinuities or "magic" values.
* **indicator feature** says if another feature has values or not (in the market yes/no). Usually a boolean
* not change over time
* not crazy outliers
* Account for upstream instability

#### **Cleaning data**

Scaling feature values

* Scaling means converting floating-point feature values from their natural range (for example, 100 to 900) into a standard range (for example, 0 to 1 or -1 to +1). If a feature set consists of only a single feature, then scaling provides little to no practical benefit. If, however, a feature set consists of multiple features, then feature scaling provides the following benefits

* Helps gradient descent converge more quickly.
* Helps avoid the "NaN trap," in which one number in the model becomes a NaN (e.g., when a value exceeds the floating-point precision limit during training),
* Helps the model learn appropriate weights for each feature. Without feature scaling, the model will pay too much attention to the features having a wider range.

Handling extreme outliers

* log
* log scaling
* "cap" or "clip" the maximum value

Binning

* binning trick. Allows to map non-linearities into a model. Binning (e.g. divide latitudes into "bins")

Scrubbing

Until now, we've assumed that all the data used for training and testing was trustworthy. In real-life, many examples in data sets are unreliable due to one or more of the following:

* Omitted values. For instance, a person forgot to enter a value for a house's age.
* Duplicate examples. For example, a server mistakenly uploaded the same logs twice.
* Bad labels. For instance, a person mislabeled a picture of an oak tree as a maple.
* Bad feature values.
* Once detected, you typically "fix" bad examples by removing them from the data set.

Know your data. Do:

* Visualize
* Debug: Duplicate examples? Missing values? Outliers? Data agrees with dashboards? Training and Validation data similar?
* Monitor: Feature quantiles, number of examples over time?

Know your data. Follow these rules:

* Keep in mind what you think your data should look like.
* Verify that the data meets these expectations (or that you can explain why it doesn’t).
* Double-check that the training data agrees with other sources (for example, dashboards).
* Treat your data with all the care that you would treat any mission-critical code. Good ML relies on good data.

#### **Pearls**

* One-hot encoding extends to numeric data that you do not want to directly multiply by a weight, such as a postal code.
* Scaling feature values. Scaling means converting floating-point feature values from their natural range (for example, 100 to 900) into a standard range (for example, 0 to 1 or -1 to +1). If a feature set consists of only a single feature, then scaling provides little to no practical benefit. If, however, a feature set consists of multiple features, then feature scaling provides the following benefits
  * Helps gradient descent converge more quickly.
  * Helps avoid the "NaN trap," in which one number in the model becomes a NaN (e.g., when a value exceeds the floating-point precision limit during training),
  * Helps the model learn appropriate weights for each feature. Without feature scaling, the model will pay too much attention to the features having a wider range.

### 09 Feature Crosses

#### **Objectives**

* Build an understanding of feature crosses.
* Implement feature crosses in TensorFlow.

#### **Encoding Nonlinearity**

To solve the nonlinear problem, create a **feature cross**. A feature cross is a *synthetic feature* that *encodes nonlinearity* in the feature space by multiplying two or more input features together. (The term cross comes from [cross product](https://wikipedia.org/wiki/Cross_product).)

How to build a feature cross:

* Start with: *y = b + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub>*
* Create: *x<sub>3</sub> = x<sub>1</sub>x<sub>2</sub>*
* Adjust to: *y = b + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + w<sub>3</sub>x<sub>3</sub>*

Kinds of feature crosses. We can create many different kinds of feature crosses. For example:

* [A X B]: a feature cross formed by multiplying the values of two features.
* [A x B x C x D x E]: a feature cross formed by multiplying the values of five features.
* [A x A]: a feature cross formed by squaring a single feature.

Why

* Linear learners use linear models
* Such learners scale well to massive data e.g., Vowpal Wabbit, sofia-ml
* But without feature crosses, the expressivity of these models would be limited
* Using feature crosses + massive data is one efficient strategy for learning highly complex models

Thanks to stochastic gradient descent, linear models can be trained efficiently. Consequently, supplementing scaled linear models with feature crosses has traditionally been an efficient way to train on massive-scale data sets.

**feature columns**, it is a TensorFlow structure, which provide a sophisticated way to represent features

#### **Crossing One-Hot Vectors**

Think of feature crosses of one-hot feature vectors as logical conjunctions (`country:usa AND language:spanish`). For example, suppose we have two features: country and language. A one-hot encoding of each generates vectors with binary features that can be interpreted as country=USA, country=France or language=English, language=Spanish. Then, if you do a feature cross of these one-hot encodings, you get binary features that can be interpreted as logical conjunctions, such as:

#### **Pearls**

* feature cross is a *synthetic feature* that *encodes nonlinearity* in the feature space by multiplying two or more input features together
* Linear learners scale well to massive data. Using feature crosses on massive data sets is one efficient strategy for learning highly complex models. Neural networks provide another strategy.
* Best result: One feature cross + bins: [binned latitude X binned longitude X binned roomsPerPerson]

### 10 Regularization Simplicity

* **regularization**, penalize complex models
* Regularization is, to sum it up, is not trusting your examples too much.
* Regularization is what we do to prevent overfitting.
* Regularization strategies
  * early stopping, stop the training before you really converge on the training data
  * penalize the model **complexity**
    * prefer smaller weights
    * total number of features with nonzero weights

Regularization changes:

* Before: empirical risk minimization;
  * *`minimize: Loss(Data | Model)`*
* Now: add a second term penalize complexity (structural risk minimization);
  * *`minimize: Loss(Data | Model) + complexity(Model`*
  * *structural risk minimization = empirical risk minimization + `complexity(Model`*
  * loss function = loss term + regularization term
  * loss function = structural risk minimization = empirical risk minimization + `complexity(Model`*
  * loss function = `minimize: Loss(Data | Model) + complexity(Model`*
  * loss function ***Loss(Data|Model) + λ(w<sub>1</sub><sup>2</sup> + ... + w<sub>n</sub><sup>2</sup>)***

Where:

* loss term, which measures how well the model fits the data
* and the regularization term, which measures model complexity.

#### **Objectives**

* Learn about trade-offs between complexity and generalizability.
* Experiment with *L<sub>2</sub>* regularization.

#### ***L<sub>2</sub>* Regularization**

**Overcrossing**, overuse of feature crosses. Why removing (cross-product) features improve performance?

* The data in this exercise is basically linear data plus noise. If we use a model that is too complicated, such as one with too many crosses, we give it the opportunity to fit to the noise in the training data (overfitting?), often at the cost of making the model perform badly on test data.
* Removing all the feature crosses gives a saner model (there is no longer a curved boundary suggestive of overfitting) and makes the test loss converge.

Benefits of L<sub>2</sub> regularization has the following effect on a model

* Encourages weight values toward 0 (but not exactly 0)
* Encourages the mean of the weights toward 0, with a normal (bell-shaped or Gaussian) distribution.

We can quantify complexity using the L<sub>2</sub> regularization term:

**L<sub>2</sub> regularization term = w<sub>1</sub><sup>2</sup> + w<sub>2</sub><sup>2</sup> + ... + w<sub>n</sub><sup>2</sup>**,

Model developers tune the overall impact of the regularization term by multiplying its value by a scalar known as lambda (also called the regularization rate). That is, model developers aim to do the following:

A Loss function with L<sub>2</sub> regularization.

***Loss(Data|Model) + λ(w<sub>1</sub><sup>2</sup> + ... + w<sub>n</sub><sup>2</sup>)***

Where:

* Loss: aims for low training error
* λ, scalar value that controls how weights are balanced to penalize complexity
* **w<sub>1</sub><sup>2</sup> + ... + w<sub>n</sub><sup>2</sup>**, square of L<sub>2</sub> norm. Note that this term does NOT depend on the data, it just indicates that you want a simpler model.

#### **Lambda**

* ***λ***, **regularization rate**, scalar to tune the overall impact of the regularization term
* *`minimize: Loss(Data | Model) + λ complexity(Model`*
* *loss function = loss term + λ regularization term*
* *loss function = loss term + regularization rate x regularization term*

Choice of lambda

* if too high, model will be simple, but run the risk of underfitting your data. Your model won't learn enough about the training data to make useful predictions.
* if too low, model will be more complex, but run the risk of overfitting your data. Your model will learn too much about the particularities of the training data, and won't be able to generalize to new data.

#### **Pearls**

* Regularization is, to sum it up, is not trusting your examples too much.
* Regularization is what we do to prevent overfitting.
* Why removing features improve performance?. When the data is basically linear data plus noise. If we use a model that is too complicated, such as one with too many crosses, we give it the opportunity to fit to the noise in the training data (overfitting?), often at the cost of making the model perform badly on test data.
* a curved boundary is suggestive of overfitting
* structural risk minimization); *`minimize: Loss(Data | Model) + complexity(Model`*. In other words: *structural risk minimization = empirical risk minimization + `complexity(Model`*
* λ, scalar value that controls how weights are balanced to penalize complexity
* λ too high, underfit, model does not learn enough, will not generalize neither
* λ too low, overfit, model will not generalize.

### 11 Logistic Regression

#### **Objectives**

* Understand logistic regression.
* Explore loss and regularization functions for logistic regression.

#### **Summary**

* **Logistic regresion**, output is a probability
* probability estimates are **calibrated**: *p(house will sell) x price = expected outcome*
* useful for when we need a binary classification: *spam or not spam? → p(Spam)*
* How it works?
  * take the Linear Model
  * stick the Linear Model into a *sigmoid function*
* Training loss function uses **LogLoss function**, not squared loss function
* Regularization is super important for logistic regression (asymptotes)
* Benefits of Logistic Regression
  * Very fast training and prediction times.
  * Short / wide models use a lot of RAM

#### **Calculating a Probability**

Instead of predicting exactly 0 or 1, logistic regression generates a probability, a value between 0 and 1.

* How it works? how to calculate probability?
  * take the Linear Model
  * stick the Linear Model into a *sigmoid function*

*y' = 1 / (1 + e<sup>-z</sup>)*

Where:

* y' is the output of the logistic regression model for a particular example.
* *z = b + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + ... + w<sub>N</sub>x<sub>N</sub>*

And note that it can be reversed. Note that z is also referred to as the **log-odds** because the inverse of the sigmoid states that z can be defined as the log of the probability of the "1" label (e.g., "dog barks") divided by the probability of the "0" label.

log-odds, inverse of sigmoid: *z = log(y/(1-y))*

#### **Loss and Regularization**

Loss function for Logistic Regression
The loss function for linear regression is squared loss. The loss function for logistic regression is Log Loss, which is defined as follows:

*Log Loss = sum<sub>(x,y) in D</sub>(-y log(y') - (1-y)log(1-y'))*

Regularization in Logistic Regression
Regularization is extremely important in logistic regression modeling. Without regularization, the asymptotic nature of logistic regression would keep driving loss towards 0 in high dimensions. Consequently, most logistic regression models use one of the following strategies to dampen model complexity:

* L<sub>2</sub> regularization.
* Early stopping, that is, limiting the number of training steps or the learning rate.
* L<sub>1</sub> regularization.

### 12 Classification

#### **Objectives**

* Evaluating the accuracy and precision of a logistic regression model.
* Understanding ROC Curves and AUCs.

#### **Summary**

If our model does not have a zero bias, that is definitely a cause for concern, there is something wrong with the model.

#### **Thresholding**

In order to map a logistic regression value to a binary category, you must define a classification threshold (also called the decision threshold). hresholds are problem-dependent, and are therefore values that you must tune.

Model **confusion matrix**
True positive
False positive
False negative
True negative

Accuracy. Has problems with **class imbalance**, when positives or negatives are extremely rare

Evaluation Metrics: Precision and Recall. To fully evaluate the effectiveness of a model, you must examine both precision and recall. Unfortunately, precision and recall are often in tension.

#### **ROC Curve and AUC**

An **ROC curve** (receiver operating characteristic curve) is a graph showing the performance of a classification model at all classification thresholds. This curve plots two parameters:

* True Positive Rate (TPR) is a synonym for recall
* False Positive Rate

**AUC** stands for "Area under the ROC Curve." That is, AUC measures the entire two-dimensional area underneath the entire ROC curve (think integral calculus) from (0,0) to (1,1).

#### **Prediction Bias**

**Prediction bias** is a quantity that measures how far apart are the predictions from the reality?

***prediction bias = average of predictions - average of labels in data set***

In Logistic regression predictions should be unbiased. That is:

"average of predictions" should ≈ "average of observations"

A significant nonzero prediction bias tells you there is a bug somewhere in your model, as it indicates that the model is wrong about how frequently positive labels occur.

Bucketing and Prediction Bias

### 13 Regularization Sparsity

#### **Objectives**

* Learn how to drive uninformative coefficient values to exactly 0, in order to save RAM.
* Learn about other kinds of regularization besides L<sub>2</sub>.

#### **Summary**

* Sparse vectors often contain many dimensions. Consume a lot of RAM
* L<sub>1</sub> regularization, encourage weights to drop to exactly 0
* L<sub>2</sub> regularization encourages weights to be small, but doesn't force them to exactly 0.0

L<sub>1</sub> vs. L<sub>2</sub> regularization

Penalize weight differently

* L<sub>2</sub> penalizes *weight<sup>2</sup>*
* L<sub>1</sub> penalizes *|weight|*

Hence, L<sub>2</sub> and L<sub>1</sub> have different derivatives

* The derivative of L<sub>2</sub> is *2 x weight*. You can think of the derivative of L2 as a force that removes x% of the weight every time. At any rate, L<sub>2</sub> does not normally drive weights to zero.
* The derivative of L<sub>1</sub> is *k* (a constant, whose value is independent of weight). You can think of the derivative of L<sub>1</sub> as a force that subtracts some constant from the weight every time. However, thanks to absolute values, L<sub>1</sub> has a discontinuity at 0, which causes subtraction results that cross 0 to become zeroed out. For example, if subtraction would have forced a weight from +0.1 to -0.2, L<sub>1</sub> will set the weight to exactly 0. Eureka, L<sub>1</sub> zeroed out the weight.

#### **Pearls**

* L<sub>1</sub> regularization—penalizing the absolute value of all the weights—turns out to be quite efficient for wide models.
* Switching from L2 to L1 regularization dramatically reduces the delta between test loss and training loss.
* Switching from L2 to L1 regularization dampens all of the learned weights.
* Increasing the L1 regularization rate generally dampens the learned weights; however, if the regularization rate goes too high, the model can't converge and losses are very high.

### 14 Neural Networks

#### **Objectives**

* Develop some intuition about neural networks, particularly about:
  * hidden layers
  * activation functions

#### **Summary**

The standard components of what people usually mean when they say "neural network":

* A set of nodes, analogous to neurons, organized in layers.
* A set of weights representing the connections between each neural network layer and the layer beneath it. The layer beneath may be another neural network layer, or some other kind of layer.
* A set of biases, one for each node.
* An activation function that transforms the output of each node in a layer. Different layers may have different activation functions.

"Nonlinear" means that you can't accurately predict a label with a model of the form  In other words, the "decision surface" is not a line. Previously, we looked at feature crosses as one possible approach to modeling nonlinear problems. Neural networks might help with nonlinear problems,

Structure

* Input
* hidden layer" of intermediary values.
* Output

Each yellow node in the hidden layer is a weighted sum of the blue input node values.

**Activation Functions**. This nonlinear function is called the activation function. To model a nonlinear problem, we can directly introduce a nonlinearity.

Common Activation Functions

* Sigmoid
* Relu, Rectified Linear Unit activation function (or ReLU, for short) often works a little better than a smooth function like the sigmoid, while also being significantly easier to compute. ***F(x) = max(0, x)***
* Tanh
* In fact, any mathematical function can serve as an activation function.

#### **Pearls**

* combination of linear functions is still linear
* non-convex optimization -> initialization data matters very much
* Training with backpropagation (variation of gradient descent)
* 3 neurons are enough because the XOR function can be expressed as a combination of 3 half-planes (ReLU activation).

### 15 Training Neural Networks

#### **Summary**

In this chapter:

* explains backpropagation's failure cases
  * Vanishing Gradients. When the gradients vanish toward 0 for the lower layers (closer to the input), these layers train very slowly, or not at all.
  * Exploding Gradients. If the weights in a network are very large, then the gradients for the lower layers involve products of many large terms. In this case you can have exploding gradients: gradients that get too large to converge
  * Dead ReLU Units
* and the most common way to regularize a neural network
  * Dropout is a form of neural regularization for neural networks. It works by randomly "dropping out" unit activations in a network for a single gradient step. The more you drop out, the stronger the regularization:

Backpropagation is the most common training algorithm for neural networks. It makes gradient descent feasible for multi-layer neural networks.

Failure cases
Dropout Regularization

### 16 Multi-Class Neural Networks

#### **Summary**

* Multi-class classification, which can pick from multiple possibilities. For example:
  * is this dog a beagle, a basset hound, or a bloodhound?
  * is this flower a Siberian Iris, Dutch Iris, Blue Flag Iris, or Dwarf Bearded Iris?
  * Is that plane a Boeing 747, Airbus 320, Boeing 777, or Embraer 190?
  * Is this an image of an apple, bear, candy, dog, or egg?
* Multi-class classification problems, particularly Softmax

One vs. All
Given a classification problem with N possible solutions, a one-vs.-all solution consists of N separate binary classifiers—one binary classifier for each possible outcome.
This approach is fairly reasonable when the total number of classes is small, but becomes increasingly inefficient as the number of classes rises.

Softmax extends this idea into a multi-class world. That is, Softmax assigns decimal probabilities to each class in a multi-class problem. Those decimal probabilities must add up to 1.0. This additional constraint helps training converge more quickly than it otherwise would.

Softmax options:

* Full Softmax. Softmax calculates a probability for every possible class.
* Candidate sampling. Softmax calculates a probability for all the positive labels but only for a random sample of negative labels. For example, if we are interested in determining whether an input image is a beagle or a bloodhound, we don't have to provide probabilities for every non-doggy example.

One Label vs. Many Labels
Softmax assumes that each example is a member of exactly one class. Some examples, however, can simultaneously be a member of multiple classes. For such examples:
You may not use Softmax.
You must rely on multiple logistic regressions.

### 17 Embeddings

**Embedding** is a relatively low-dimensional space into which you can translate high-dimensional vectors. Embeddings: Translating to a Lower-Dimensional Space

#### **Summary**

* embedding layer is a hidden layer
* rule-of-thumb: embedding dimensions *(possible values)<sup>1/4</sup>*

* No separate training process needed -- the embedding layer is just a hidden layer with one unit per dimension
* Supervised information (e.g. users watched the same two movies) tailors the learned embeddings for the desired task
* Intuitively the hidden units discover how to organize the items in the d-dimensional space in a way to best optimize the final objective

#### **Objectives**

* Learn what an embedding is and what it's for.
* Learn how embeddings encode semantic relations.
* Learn how to use embeddings.
* Learn how to train meaningful embeddings (using word2vec, for example).

#### **Motivation from Collaborative Filtering**

Collaborative filtering is the task of making predictions about the interests of a user based on interests of many other users.

Too many data to store (e.g. suppose we have 1,000,000 users, and a list of the movies each user has watched (from a catalog of 500,000 movies).)

#### **Categorical Input Data**

Categorical data refers to input features that represent one or more discrete items from a finite set of choices. For example, it can be the set of movies a user has watched, the set of words in a document, or the occupation of a person

sparse tensors, which are tensors with very few non-zero elements.

Ways to represent data:

* one-hot encoding, if you assign "horse" to index 1247, then to feed "horse" into your network you might copy a 1 into the 1247th input node and 0s into all the rest. This sort of representation is called a one-hot encoding,
* embeddings
  * create vocabulary (dictionary)
  * an embedding is a matrix in which each column is the vector that corresponds to an item in your vocabulary.

#### **Translating to a Lower-Dimensional Space**

#### **Obtaining Embeddings**

Standard Dimensionality Reduction Techniques

* PCA, principal component analysis, given a set of instances like bag of words vectors, PCA tries to find highly correlated dimensions that can be collapsed into a single dimension
* Word2vec, algorithm for training word embeddings. Word2vec relies on the distributional hypothesis to map semantically similar words to geometrically close embedding vectors.
* Training an Embedding as Part of a Larger Model

## **03 ML Engineering**

Components in a production ML system

* data collection
* feature extraction
* process management tools
* data verification
* configuration
* machine resource management
* analysis tools
* monitoring
* serving infrastructure

Static vs. Dynamic Training

* Static model
  * Trained offline
  * Trained once
  * Incorporated into the model once, at the beginning
  * easy to build and test; use batch train & test, iterate until good
  * still requires monitoring of inputs
  * easy to let this grow stale
* Dynamic model
  * Trained online
  * Trained continuously
  * Incorporated into the model constantly in form of small updates
  * progressive validation rather than batch training & test
  * Needs monitoring, model rollback & data quarantine capabilities
  * adapt to changes, staleness issues avoided

Static vs. Dynamic Inference

* offline inference
  * Make all possible predictions in a batch, using a MapReduce or something similar
  * Write to a table, then feed these to a cache/lookup table (e.g. an SSTable or Bigtable, and then feed these to a cache/lookup table)
  * Upside: don't need to worry much about cost of inference
  * Upside: can likely use batch quota
  * Upside: can do post-verification of predictions on data before pushing
  * Downside: can only predict things we know about -- bad for long tail.
  * Downside: update latency likely measured in hours or days.
* online inference. Predict on demand, using a server.
  * Upside: can predict any new item as it comes in -- great for long tail
  * Downside: compute intensive, latency sensitive -- may limit model complexity.
  * Downside: monitoring needs are more intensive.

Data Dependencies

* features take the place of code in ML (so, not possible to do unit test)
* reliable, is input data always available?
* versioning, need to have versions in the input data?
* necessity?
* correlations
* feedback loops. Do not want non-stationary in our system. Simplest way is to have input data depend on output of our model

Fairness

Types of Bias

* cognitive blindspot
* reporting bias
* selection bias
* overgeneralization
* out-group homogeneity bias
* unconscious bias
* confirmation bias
* automation bias

### **Pearls**

* Train the model to account for bias

## **09 Pearls**

* The labels applied to some examples might be unreliable.
* Good features are concrete and quantifiable.
* Rules of Machine Learning, Rule #1: Don't be afraid to launch a product without machine learning
* Hyperparameters
  * Learning Rate
  * epoch
  * batch size
  * training split
  * validation_split
  * test split
  * ***λ***, **regularization rate**, scalar to tune the overall impact of the regularization term
  * in classification, classification threshold (also called the decision threshold). Thresholds are problem-dependent, and are therefore values that you must tune.
  * L<sub>1</sub> regularization
  * L<sub>2</sub> regularization
  * in neural networks
    * activation function for non-linearity
    * number of hidden layers
    * number of neurons in each layer
  * Dropout is a form of neural regularization for neural networks.
  * Embeddings Dimemsions, number of

* Iterative strategies are prevalent in machine learning, primarily because they scale so well to large data sets.
* A Machine Learning model is trained by starting with an initial guess for the weights and bias and iteratively adjusting those guesses until learning the weights and bias with the lowest possible loss.
* Regression problems yield convex loss vs. weight plots.
* When performing gradient descent, we generalize the above process to tune all the model parameters simultaneously. For example, to find the optimal values of both *w<sub>i</sub>* and the bias *b*, we calculate the gradients with respect to both *w<sub>i</sub>* and *b*. Next, we modify the values of *w<sub>i</sub>* and *b* based on their respective gradients. Then we repeat these steps until we reach minimum loss.
* Most machine learning programmers spend a fair amount of time tuning the learning rate. If you pick a learning rate that is too small, learning will take too long. Conversely, if you specify a learning rate that is too large, the next point will perpetually bounce haphazardly across the bottom of the well like a quantum mechanics experiment gone horribly wrong.
* In practice, finding a "perfect" (or near-perfect) learning rate is not essential for successful model training. The goal is to find a learning rate large enough that gradient descent converges efficiently, but not so large that it never converges.
* An oscillating loss curve strongly suggests that the learning rate is too high
* Most machine learning problems require a lot of hyperparameter tuning. Unfortunately, we can't provide concrete tuning rules for every model. Lowering the learning rate can help one model converge efficiently but make another model converge much too slowly. You must experiment to find the best set of hyperparameters for your dataset. That said, here are a few rules of thumb:
  * Training loss should steadily decrease, steeply at first, and then more slowly until the slope of the curve reaches or approaches zero.
  * If the training loss does not converge, train for more epochs.
  * If the training loss decreases too slowly, increase the learning rate. Note that setting the learning rate too high may also prevent training loss from converging.
  * If the training loss varies wildly (that is, the training loss jumps around), decrease the learning rate.
  * Lowering the learning rate while increasing the number of epochs or the batch size is often a good combination.
  * Setting the batch size to a very small batch number can also cause instability. First, try large batch size values. Then, decrease the batch size until you see degradation.
  * For real-world datasets consisting of a very large number of examples, the entire dataset might not fit into memory. In such cases, you'll need to reduce the batch size to enable a batch to fit into memory.
* Remember: the ideal combination of hyperparameters is data dependent, so you must always experiment and verify.
* Overfitting occurs when a model tries to fit the training data so closely that it does not generalize well to new data.
* If the key assumptions of supervised ML are not met, then we lose important theoretical guarantees on our ability to predict on new data.
* Never train on test data
* Do randomization before splitting data (e.g. avoid all "winter" data ends in one set only)
* Split about 80% train, 20% test
* scaling means converting floating-point feature values from their natural range (for example, 100 to 900) into a standard range (for example, 0 to 1 or -1 to +1)
* One-hot encoding extends to numeric data that you do not want to directly multiply by a weight, such as a postal code.
* Scaling feature values. Scaling means converting floating-point feature values from their natural range (for example, 100 to 900) into a standard range (for example, 0 to 1 or -1 to +1). If a feature set consists of only a single feature, then scaling provides little to no practical benefit. If, however, a feature set consists of multiple features, then feature scaling provides the following benefits
  * Helps gradient descent converge more quickly.
  * Helps avoid the "NaN trap," in which one number in the model becomes a NaN (e.g., when a value exceeds the floating-point precision limit during training),
  * Helps the model learn appropriate weights for each feature. Without feature scaling, the model will pay too much attention to the features having a wider range.
* feature cross is a *synthetic feature* that *encodes nonlinearity* in the feature space by multiplying two or more input features together
* Linear learners scale well to massive data. Using feature crosses on massive data sets is one efficient strategy for learning highly complex models. Neural networks provide another strategy.
* Best result: One feature cross + bins: [binned latitude X binned longitude X binned roomsPerPerson]
* Regularization is, to sum it up, is not trusting your examples too much.
* Regularization is what we do to prevent overfitting.
* Why removing features improve performance?. When the data is basically linear data plus noise. If we use a model that is too complicated, such as one with too many crosses, we give it the opportunity to fit to the noise in the training data (overfitting?), often at the cost of making the model perform badly on test data.
* a curved boundary is suggestive of overfitting
* structural risk minimization); *`minimize: Loss(Data | Model) + complexity(Model`*. In other words: *structural risk minimization = empirical risk minimization + `complexity(Model`*
* λ, scalar value that controls how weights are balanced to penalize complexity
* λ too high, underfit, model does not learn enough, will not generalize neither
* λ too low, overfit, model will not generalize.
* Logistic regression models generate probabilities.
* Log Loss is the loss function for logistic regression.
* Logistic regression is widely used by many practitioners.
* When creating a model with multiple features, the values of each feature should cover roughly the same range. For example, if one feature's range spans 500 to 100,000 and another feature's range spans 2 to 12, then the model will be difficult or impossible to train. Therefore, you should normalize features in a multi-feature model.
* normalizes datasets by converting each raw value (including the label) to its Z-score. A Z-score is the number of standard deviations from the mean for a particular raw value. For example, consider a feature having the following characteristics:
* L<sub>1</sub> regularization—penalizing the absolute value of all the weights—turns out to be quite efficient for wide models.
* L<sub>1</sub> regularization—penalizing the absolute value of all the weights—turns out to be quite efficient for wide models.
* Switching from L2 to L1 regularization dramatically reduces the delta between test loss and training loss.
* Switching from L2 to L1 regularization dampens all of the learned weights.
* Increasing the L1 regularization rate generally dampens the learned weights; however, if the regularization rate goes too high, the model can't converge and losses are very high.
* Train the model to account for bias

## **10 follow up**

* why convex?
* The ideal learning rate in one-dimension is  (the inverse of the second derivative of f(x) at x).
* The ideal learning rate for 2 or more dimensions is the inverse of the Hessian (matrix of second partial derivatives).
* batch
* batch size
* Stochastic gradient descent (SGD)
* The less complex an ML model, the more likely that a good empirical result is not just due to the peculiarities of the sample.
* Regularization rate
* Regularization
* Learning rate
* Noise?
* Batch size
* <http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/>
