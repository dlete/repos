#!/usr/bin/env python3
# -*- coding: utf-8 -*

from typing import Tuple

from ch04_linear_algebra import Vector
from ch05_statistics import correlation
from ch05_statistics import de_mean
from ch05_statistics import mean
from ch05_statistics import standard_deviation
from ch05_statistics import num_friends_good, daily_minutes_good

#
# y = beta * x + alpha
# y_i = βx_i + α + ε_i


def predict(alpha: float, beta: float, x_i: float) -> float:
    """returns dependant varialble when relationship with independent variable is linear"""
    return beta * x_i + alpha


assert predict(2, 3, 4) == 14, "linear prediction is incorrect"


def error(alpha: float, beta: float, x_i: float, y_i: float) -> float:
    """
    The error from predicting beta * x_i + alpha
    when the actual value is y_i
    """
    return predict(alpha, beta, x_i) - y_i


assert error(2, 3, 4, 17.5) == -3.5, "'error calculation' is incorrect"


def sum_of_sqerrors(alpha: float, beta: float, xs: Vector, ys: Vector) -> float:
    """returns sum of squared errors
    when the actual values are ys"""
    errors = [error(alpha, beta, x_i, y_i) for x_i, y_i in zip(xs, ys)]
    errors_squared = [error ** 2 for error in errors]
    return sum(errors_squared)


xs_actual = [1, 2, 3]
ys_actual = [4.5, 8.5, 12.5]
assert sum_of_sqerrors(2, 3, xs_actual, ys_actual) == 2.75, "'sum_of_squares' is incorrect"


def least_squares_fit(x: Vector, y: Vector) -> Tuple[float, float]:
    """
    Given two vectors x and y,
    find the least-squares values of alpha and beta
    """
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return round(alpha, 3), round(beta, 3)


xs_sample = [i for i in range(-100, 110, 10)]
ys_sample = [3 * i - 5 for i in xs_sample]
# Should find that y = 3x - 5
assert least_squares_fit(xs_sample, ys_sample) == (-5, 3), "'least_squares_fit' is incorrect"

xs_actual = [2, 3, 5, 7, 9]     # daily hours of sunshine
ys_actual = [4, 5, 7, 10, 15]   # ice creams sold
alpha, beta = least_squares_fit(xs_actual, ys_actual)
assert 0.28 < alpha < 0.29      # alpha is 0.289
assert 1.5 < beta < 1.6         # beta is 1.521

alpha, beta = least_squares_fit(num_friends_good, daily_minutes_good)
assert 22.9 < alpha < 23.0      # alpha is 22.98
assert 0.8 < beta < 0.905      # beta is 0.9


def total_sum_of_squares(ys: Vector) -> float:
    """the total squared variation of y_i's from their mean"""
    return sum(v ** 2 for v in de_mean(ys))


def r_squared(alpha: float, beta: float, x: Vector, y: Vector) -> float:
    """
    the fraction of variation in y captured by the model, which equals
    1 - (the fraction of variation in y not captured by the model)
    """
    # coefficient of determination (or R-squared),
    # which measures the fraction of the total variation in the dependent variable
    # that is captured by the model.
    return 1.0 - (sum_of_sqerrors(alpha, beta, x, y) /
                  total_sum_of_squares(y))


rsq = r_squared(alpha, beta, num_friends_good, daily_minutes_good)
assert 0.328 < rsq < 0.330      # 0.329

