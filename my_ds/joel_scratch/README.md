# About this folder

Notes on book: [Data Science from Scratch](https://www.oreilly.com/library/view/data-science-from/9781492041122/), by Joel Grus, O'Reilly.
[Supporting files in Github](https://github.com/joelgrus/data-science-from-scratch)

## Books

### Algebra

* [Linear algebra, from UC Davis](https://www.math.ucdavis.edu/~linear/)
* [Linear Algebra, from Saint Michael’s College](http://joshua.smcvt.edu/linearalgebra/)
* If you are feeling adventurous, [Linear Algebra Done Wrong](http://www.math.brown.edu/~treil/papers/LADW/LADW.html) is a more
advanced introduction

### Calculus

* [Active Calculus 1.0, Grand Valley State University](https://scholarworks.gvsu.edu/books/10/)
* [Active Calculus 2.0, Grand Valley State University](https://scholarworks.gvsu.edu/books/15/)

### Probability

* [Introduction to Probability, Grinstead and Snell](http://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/amsbook.mac.pdf)

#### Sites

[Central Limit Theorem Explained, Jim Forst](https://statisticsbyjim.com/basics/central-limit-theorem/)

[Central Limit Theorem, Boston University](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_probability/BS704_Probability12.html#:~:text=The%20central%20limit%20theorem%20states,will%20be%20approximately%20normally%20distributed.)

### Statistics

* [OpenIntro Statistics](https://www.openintro.org/)
* [OpenStax Introductory Statistics](https://openstax.org/details/introductory-statistics)
* [The Elements of Statistical Learning](https://web.stanford.edu/~hastie/ElemStatLearn/), Stanford, very mathy

## Follow up

### in Linear Regression chapter, understand and verify Using Gradient Descent

You do not understand it.

### Chapter 15 Goodness of Fit

You do not understand it.

### Stocastic Gradient Descent

I do not understand how come in Gradient Descent we have to calculate the gradient in the whole dataset. And do not understand the mechanics of the Stocastic (is it doing x = x - alpha*gradient; or is x random every time?)

### The central limit theorem

<https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_probability/BS704_Probability12.html#:~:text=The%20central%20limit%20theorem%20states,will%20be%20approximately%20normally%20distributed.>
The central limit theorem states that if you have a population with mean μ and standard deviation σ and take sufficiently large random samples from the population with replacementtext (Sampling ''with replacement'' means that when a unit selected at random from the population, it is returned to the population (replaced), and then a second element is selected at random.) annotation indicator, then the distribution of the sample means will be approximately normally distributed. This will hold true regardless of whether the source population is normal or skewed, provided the sample size is sufficiently large (usually n > 30).

<https://en.wikipedia.org/wiki/Central_limit_theorem>
The central limit theorem (CLT) establishes that, in many situations, when independent random variables are added, their properly normalized sum tends toward a normal distribution (informally a bell curve) even if the original variables themselves are not normally distributed. The theorem is a key concept in probability theory because it implies that probabilistic and statistical methods that work for normal distributions can be applicable to many problems involving other types of distributions.

### Hypothesis and inference

Do understand chapter 7, hypothesis and inference. You do not understand it now.
Stochastic Gradient Descent

### `assert all()`

`assert all(len(vector) == vector_dimensions for vector in vectors), "different sizes"`

### `assert round()`

`assert round(distance(v1, v2)) == 5, "the 'squared_distance' calculation is incorrect"`

### In a Python list

Can have indexes that are not integers?

See in Chapter 2:

### bars are by default width 0.8, so we'll add 0.1 to the left coordinates so that each bar is centered

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
xs = [i + 0.1 for i, _ in enumerate(movies)]
print(xs)   # [0.1, 1.1, 2.1, 3.1, 4.1] !!!!!!!!!!!!!!!

### `dot` product

understand the visual and how to calculate, and what represents

### DataSciencester

What is DataSciencester?

### ch02, first-class functions

* Python functions are first-class, which means that we can assign them to variables and pass them into functions just like any other arguments
* anonymous functions, or lambdas

## Glossary

* binary search
* Binary or binomial classification: exactly two classes to choose between (usually 0 and 1, true and false, or positive and negative)
* binomial random variables; independent Bernoulli(p) random variables, each of which equals 1 with probability p
* Central Limit Theorem
* cdf, cumulative distribution function
* classification problems have discrete and finite outputs called classes or categories
* deep neural network, neural network with more than one hidden layer
* feed-forward neural network, neural network that consists of discrete layers of neurons, each connected to the next. Each neuron takes the outputs of the previous layer, performs some calculation, and passes the result to the next layer
* k-Nearest Neighbors
* Multiclass or multinomial classification: three or more classes of the outputs to choose from
* *nearest neighbors classification*
* pdf
* perceptron, approximates a single neuron with *n* binary inputs
* predictors, input, independent variables
* random variable
* Regression problems have continuous and usually unbounded outputs
* response, output, dependent variablesLogistic regression is a linear classifier, so you’ll use a linear function 𝑓(𝐱) = 𝑏₀ + 𝑏₁𝑥₁ + ⋯ + 𝑏ᵣ𝑥ᵣ, also called the logit. The variables 𝑏₀, 𝑏₁, …, 𝑏ᵣ are the estimators of the regression coefficients, which are also called the predicted weights or just coefficients.
and 0 with probability 1 − p :

## Know this

### Imports

[Stackoverflow, What's the correct way to sort python `import x` and `from x import y` statement?](https://stackoverflow.com/questions/20762662/whats-the-correct-way-to-sort-python-import-x-and-from-x-import-y-statement)

[Realpython, Python import: Advanced Techniques and Tips](https://realpython.com/python-import/)

[Realpython, Absolute vs Relative Imports in Python](https://realpython.com/absolute-vs-relative-python-imports/)

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/#imports)

### PEP 263, coding

[PEP 263 -- Defining Python Source Code Encodings](https://www.python.org/dev/peps/pep-0263/)

[Realpython, Unicode & Character Encodings in Python: A Painless Guide](https://realpython.com/python-encodings-guide/)

<https://towardsdatascience.com/a-guide-to-unicode-utf-8-and-strings-in-python-757a232db95c#:~:text=By%20default%20in%20Python%203,encodings%20can%20also%20be%20used.>

<https://docs.python.org/3/howto/unicode.html>

<https://www.python.org/dev/peps/pep-0597/>

<http://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html>

### Formulas in Jupyter notebooks

<https://medium.com/analytics-vidhya/writing-math-equations-in-jupyter-notebook-a-naive-introduction-a5ce87b9a214>

```Jupyter
$\hat{Y} = \hat{\beta}_{0} + \sum \limits _{j=1} ^{p} X_{j}\hat{\beta}_{j}$
```

<https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Typesetting%20Equations.html>
