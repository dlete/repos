# Lecture 5.2: Introduction to the Quantum Approximate Optimization Algorithm and Applications with Johannes Weidenfeller

## Variational Quantum Eigensolvers

### Summary

Variational Quantum Eigensolvers (VQE) are: variational quantum algorithms that try to approximate the ground state of quantum systems.
QAOA are special case of VQE.

### Definitions

***Hamiltonian*** is an operator, expressed as an Hermitian matrix, corresponding to the total energy of a quantum system.

***Hermitian matrix*** <=> `H = H†`
Energy of system in state |ψ⟩ given by expectation value `E(|ψ⟩) = ⟨ψ|H|ψ⟩`

***Ground State***: the lowest energy state `|ψ*⟩` of a quantum system. `|ψ*⟩ = argmin E(|ψ⟩)`, where `|ψ⟩ ∈ H`.

### The variational method

Method for approximating ground state `|ψ*⟩` and lowest energy E<sub>min</sub> of a quantum system.

1. Choose **ansatz** or **trial state** parametrized by θ, `|ψ(θ)⟩`
1. Vary parameters θ to minimize the energy value, `E(θ) = ⟨ψ(θ)|H|ψ(θ)⟩`

## QUBO and MaxCut

### Summary

Problems that QAOA can solve:

* Quadratic Unconstrained Binary Optimization (QUBO) problems.
* MaxCut

## The QAOA Circuit

### Summary

How the QAOA circuit looks in detail.

## Adiabatic Quantum Computing

### Summary

Connection between VQE and Adiabatic Quantum Computing.

## Recent Results and Caveats

# Lecture 4.1: Introduction to Classical Machine Learning with Amira Abbas

## Ingredients

* Data
* Model
* Cost

### Data

each image is a data point in a dataset  
image has pixels  
each pixel represented as a vector => each data point is represented as a vector  
each vector has as many entries as pixels -> entry = ***feature***  (***dimension of the data*** = number of features; number of features = dimension of the data = size of the data)
all the data points of the dataset represented as a matrix  
the dimension of the data is represented by D  

### Model

function attempting to reproduce the real function for the data  
`g(x_bar, theta)`,  theta are parameters, sets of parameters
produces output which is a prediction (***label***) (also output or distibution)  

DATA    MODEL            OUTPUT
x_bar   f(x_var, theta)  y_hat

### Cost

Function that scores how well a model predicts the output  
Compares how well each model predictions to the correct outputs  
C(f(x_bar, theta), correct) = C(y_hat, y)  
y_hat = f(x_bar, theta)  
y = correct  
score <- C(f(x_hat, theta), y)  
low error -> high score  
high error -> low score  
MSE, mean square error = (y_hat - y)^2

## Examples

### Classification

* cats
* spam
* image recognition, MNIST dataset

### Regression

learn from historical and relevant to make predictions, numerical, to make predictions about future events  

### Clustering

take lots of data and group together with similar behaviour/patters

### Generate data, Machine Learning task to generate new data

feed a lot of data/historical data, then the ML model learns and understands structures under the data, and generates new data
