#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#
# imports
#
import math

from typing import Callable
from typing import List
from typing import Tuple

#
# Type hints
#
Matrix = List[List[float]]
Vector = List[float]
Vectors = List[List[float]]

#
# Factories
#
v1 = [1, 2, 3]  # vector
v2 = [4, 5, 6]  # vector
v3 = [7, 8, 9]  # vector
s1 = 3          # scalar

A = [[1, 2, 3],  # Matrix A has 2 rows and 3 columns
     [4, 5, 6]]

B = [[1, 2],     # Matrix B has 3 rows and 2 columns
     [3, 4],
     [5, 6]]


def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vectors_add_two(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert vectors_add_two(v1, v2) == [5, 7, 9], "the 'vector_add' calculation is incorrect"


def vectors_subtract_two(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert vectors_subtract_two(v1, v2) == [-3, -3, -3], "'vector_subtract' calculation is incorrect"


def vector_sum(vectors: Vectors) -> Vector:
    """Sums all corresponding elements"""
    # check that vectors is not empty
    assert vectors, "no vectors provided!"

    # check vectors are of the same dimension (lenght)
    vector_dimensions = len(vectors[0])
    assert all(len(vector) == vector_dimensions for vector in vectors), "different sizes"

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(vector_dimensions)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def scalar_multiply(scalar: float, vector: Vector) -> Vector:
    """ multiplies a vector by a scalar"""
    return [scalar * v_i for v_i in vector]


assert scalar_multiply(s1, v1) == [3, 6, 9], "the 'scalar_multiply' calculation is incorrect"


def vector_mean(vectors: List[Vector]) -> Vector:
    """compute the vector whose i-th element is the mean of the
    i-th elements of the input vectors"""
    # check that vectors is not empty
    assert vectors, "no vectors provided!"

    # check vectors are of the same dimension (lenght)
    vector_dimensions = len(vectors[0])
    assert all(len(vector) == vector_dimensions for vector in vectors), "different sizes"

    # sum all vectors given, and divide by the number of vectors we have been given
    number_of_vectors = len(vectors)
    return scalar_multiply(1/number_of_vectors, vector_sum(vectors))


assert vector_mean([v1, v2, v3]) == [4, 5, 6], "the 'vector_mean' calculation is incorrect"


def dot(v: Vector, w: Vector) -> float:
    """sum of the component wise product of two vectors
    v_1 * w_1 + ... + v_n * w_n

    The dot product measures how far the vector v extends in the w direction.
    For example, if w = [1, 0] then dot(v, w) is just the first component of v.
    Another way of saying this is that it’s the length of the vector you’d get
    if you projected v onto w.
    """
    # check that vectors are not empty
    assert v, "no vectors provided!"
    assert w, "no vectors provided!"

    # check vectors are of the same dimension (lenght)
    assert len(v) == len(w), "vectors are not of the same dimension"

    # sum dimension/element wise
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot(v1, v2) == 32, "the dot product is incorrect"


def sum_of_squares(v: Vector) -> float:
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


assert sum_of_squares(v1) == 14, "the 'sum_of_squares' calculation is incorrect"


def magnitude(v: Vector) -> float:
    """ magnitude/lenght of a vector"""
    return math.sqrt(sum_of_squares(v))


assert round(magnitude(v1), 2) == 3.74, "the 'magnitude' calculation is incorrect"


def squared_distance(v: Vector, w: Vector) -> float:
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    # check vectors are of the same dimension (lenght)
    assert len(v) == len(w), "vectors must be of the same lenght"

    return sum_of_squares(vectors_subtract_two(v, w))


assert round(squared_distance(v1, v2)) == 27, "the 'squared_distance' calculation is incorrect"


def distance(v: Vector, w: Vector) -> float:
    """distance between two vectors"""
    # check vectors are of the same dimension (lenght)
    assert len(v) == len(w), "vectors must be of the same lenght"

    return math.sqrt(squared_distance(v, w))


assert round(distance(v1, v2)) == 5, "the 'squared_distance' calculation is incorrect"


#
# functions for working with matrices
#

def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A)"""
    # check that the matrix is not empty
    assert A, "no matrix provided!"

    # check rows are of the same dimension (lenght)
    assert all((len(row) == len(A[0])) for row in A), "rows of different sizes"

    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


assert shape(A) == (2, 3), "the shape of matrix calculation is incorrect "  # 2 rows, 3 columns


def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    # check that the matrix is not empty
    assert A, "no matrix provided!"

    # check rows are of the same dimension (lenght)
    assert all((len(row) == len(A[0])) for row in A), "rows are of different sizes"

    return A[i]


assert get_row(A, 0) == [1, 2, 3], "the calculation of 'get_row' is incorrect"


def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    # check that the matrix is not empty
    assert A, "no matrix provided!"

    # check rows are of the same dimension (lenght)
    assert all((len(row) == len(A[0])) for row in A), "rows are of different sizes"

    return [A_i[j] for A_i in A]


assert get_column(A, 1) == [2, 5], "the calculation of 'get_column' is incorrect"


def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable) -> Matrix:
    """returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i, j)"""
    # check that columns and rows dimension/length are bigger than zero
    assert all((dimension > 0) for dimension in (num_rows, num_cols))

    return [[entry_fn(i, j) for j in range(num_cols)]
            for i in range(num_rows)]


def my_func(i: int, j: int) -> int:
    """returns the sum of two numbers"""
    return i+j


my_matrix = [[0, 1, 2, 3], [1, 2, 3, 4]]
assert make_matrix(2, 4, my_func) == my_matrix, "the calculation of 'make matrix' is incorrect"


def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0


assert make_matrix(5, 5, is_diagonal) == ([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                                          [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])


def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix
    the dentity matrix is n x n and has 1s
    on the diagonal and 0s elsewhere"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]


# Use #1:
# We can use a matrix to represent a data set consisting of multiple vectors,
# simply by considering each vector as a row of the matrix. For example, if
# you had the heights, weights, and ages of 1,000 people you could put them
# in a 1,000 × 3 matrix:
data = [[70, 170, 40],
        [65, 120, 26],
        [77, 250, 19],
        # ...
        ]

#
# use #2:
# we can use an n × k matrix to represent a linear function that maps
# k-dimensional vectors to n-dimensional vectors.
#

# Use #3:
# matrices can be used to represent binary relationships
#
# Before we had:
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# We could also represent this as:
#            user 0  1  2  3  4  5  6  7  8  9
#
friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # user 0
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # user 1
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # user 2
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # user 3
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # user 4
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # user 5
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 6
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 7
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # user 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # user 9

assert friend_matrix[0][2] == 1, "0 and 2 are friends"
assert friend_matrix[0][8] == 0, "0 and 8 are not friends"

# only need to look at one row
friends_of_five = [i
                   for i, is_friend in enumerate(friend_matrix[5])
                   if is_friend]
