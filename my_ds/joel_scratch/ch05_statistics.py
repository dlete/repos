#!/usr/bin/env python3
# -*- coding: utf-8 -*

# imports, Python core
from typing import List
import math

# imports, other modules in this same directory
from ch04_linear_algebra import dot
from ch04_linear_algebra import sum_of_squares


Vector = List[float]

v1 = [1, 10, 2, 9, 5]
v2 = [1, 9, 2, 10]
num_friends = [100.0, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15,
               15, 14, 14, 13, 13, 13, 13, 12, 12, 11, 10, 10, 10, 10, 10, 10,
               10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9,
               9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
               8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6,
               6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5,
               5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3,
               3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
               2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1]

daily_minutes = [1, 68.77, 51.25, 52.08, 38.36, 44.54, 57.13, 51.4, 41.42,
                 31.22, 34.76, 54.01, 38.79, 47.59, 49.1, 27.66, 41.03, 36.73,
                 48.65, 28.12, 46.62, 35.57, 32.98, 35, 26.07, 23.77, 39.73,
                 40.57, 31.65, 31.21, 36.32, 20.45, 21.93, 26.02, 27.34, 23.49,
                 46.94, 30.5, 33.8, 24.23, 21.4, 27.94, 32.24, 40.57, 25.07,
                 19.42, 22.39, 18.42, 46.96, 23.72, 26.41, 26.97, 36.76, 40.32,
                 35.02, 29.47, 30.2, 31, 38.11, 38.18, 36.31, 21.03, 30.86,
                 36.07, 28.66, 29.08, 37.28, 15.28, 24.17, 22.31, 30.17, 25.53,
                 19.85, 35.37, 44.6, 17.23, 13.47, 26.33, 35.02, 32.09, 24.81,
                 19.33, 28.77, 24.26, 31.98, 25.73, 24.86, 16.28, 34.51, 15.23,
                 39.72, 40.8, 26.06, 35.76, 34.76, 16.13, 44.04, 18.03, 19.65,
                 32.62, 35.59, 39.43, 14.18, 35.24, 40.13, 41.82, 35.45, 36.07,
                 43.67, 24.61, 20.9, 21.9, 18.79, 27.61, 27.21, 26.61, 29.77,
                 20.59, 27.53, 13.82, 33.2, 25, 33.1, 36.65, 18.63, 14.87,
                 22.2, 36.81, 25.53, 24.62, 26.25, 18.21, 28.08, 19.42, 29.79,
                 32.8, 35.99, 28.32, 27.79, 35.88, 29.06, 36.28, 14.1, 36.63,
                 37.49, 26.9, 18.58, 38.48, 24.48, 18.95, 33.55, 14.24, 29.04,
                 32.51, 25.63, 22.22, 19, 32.73, 15.16, 13.9, 27.2, 32.01,
                 29.27, 33, 13.74, 20.42, 27.32, 18.23, 35.35, 28.48, 9.08,
                 24.62, 20.12, 35.26, 19.92, 31.02, 16.49, 12.16, 30.7, 31.22,
                 34.65, 13.13, 27.51, 33.2, 31.57, 14.1, 33.42, 17.44, 10.12,
                 24.42, 9.82, 23.39, 30.93, 15.03, 21.67, 31.09, 33.29, 22.61,
                 26.89, 23.48, 8.38, 27.81, 32.35, 23.84]

daily_hours = [dm / 60 for dm in daily_minutes]


# The person with 100 friends (who spends only one minute per day on the site)
# is a huge outlier, and correlation can be very sensitive to outliers.
# What happens if we ignore that person?
outlier = num_friends.index(100)    # index of outlier

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]


#
# Central tendency
#

def mean(xs: List[float]) -> float:
    """returns the mean (average) of a collection of numbers
    The mean is the sum of the data divided by its count."""
    mean = sum(xs) / len(xs)
    return round(mean, 2)


assert mean(num_friends) == 7.33, "the calculation of 'mean' is incorrect"


# The underscores indicate that these are "private" functions, as they're
# intended to be called by our median function but not by other people
# using our statistics library.

# // is floor Division. The division of operands where the result is the
# quotient in which the digits after the decimal point are removed.
def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
    """If len(xs) is even, it's the average of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2  # e.g. length 4 => hi_midpoint 2
    # because lists start counting elements on 0
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


# % is modulus division. Divides left hand operand by right hand operand
# and returns remainder
def median(v: List[float]) -> float:
    """Finds the 'middle-most' value of v

    The median, is:
    * the middle-most value (if the number of data points is odd)
    * the average of the two middle-most values (if the number of data points is even)."""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


assert median(num_friends) == 6, "the calculation of 'median' is incorrect"


def quantile(xs: List[float], p: float) -> float:
    """Returns the pth-percentile value in xs"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


assert quantile(num_friends, 0.10) == 1, "the calculation of 'the 10th percentile' is incorrect"
assert quantile(num_friends, 0.25) == 3, "the calculation of 'the 25th percentile' is incorrect"
assert quantile(num_friends, 0.75) == 9, "the calculation of 'the 75th percentile' is incorrect"
assert quantile(num_friends, 0.99) == 41, "the calculation of 'the 99th percentile' is incorrect"


def mode(xs: List[float]) -> List[float]:
    """Returns a list, since there might be more than one mode
    mode is the most common value(s)"""
    from collections import Counter
    counts = Counter(xs)
    # counts is (basically) { 0 : 2, 1 : 1, 2 : 1 },
    # where key=number of friends, value=number of people with that number of friends
    max_count = max(counts.values())
    modes = [x for x, count in counts.items() if count == max_count]
    return modes


assert mode(num_friends) == [6, 1], "the calculation of 'mode' is incorrect"


#
# Dispersion
#

def data_range(xs: List[float]) -> float:
    """ returns the range of a data set
    range is the difference between the largest and smallest elements"""
    return max(xs) - min(xs)


assert data_range(num_friends) == 99, "the calculation of 'data_range' is incorrect"


def de_mean(xs: List[float]) -> List[float]:
    """translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def variance(xs: List[float]) -> float:
    # x_bar = mean(xs)
    # variance = (sum([(x - x_bar)**2 for x in xs])) / (len(xs)-1)
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "variance requires at least two elements"

    n = len(xs)                 # data set size
    deviations = de_mean(xs)    # list of elements (x-x_bar) for each x in xs
    variance = sum_of_squares(deviations) / (n - 1)  # (n-1) when n is a sample
    # when we’re dealing with a sample from a larger population, x_bar is only
    # an estimate of the actual mean, which means that on
    # average (x_i- x_bar) ** 2 is an underestimate of x_i ’s squared deviation
    # from the mean, which is why we divide by n-1 instead of n .
    return round(variance, 2)


assert variance(num_friends) == 81.54, "calculation of 'variance' is incorrect"


def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    sigma = math.sqrt(variance(xs))
    return round(sigma, 2)


assert standard_deviation(num_friends) == 9.03, "calculation of 'standard_deviation' is incorrect"


def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and the 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)


assert interquartile_range(num_friends) == 6, "calculation of 'interquartile_range' is incorrect"


#
# Correlation
#

def covariance(xs: List[float], ys: List[float]) -> float:
    """Whereas variance measures how a single variable deviates from its mean,
    covariance measures how two variables vary in tandem from their means:"""
    # both data sets much have the same number of elements
    assert len(xs) == len(ys)

    n = len(xs)     # number of elements
    covariance = dot(de_mean(xs), de_mean(ys)) / (n - 1)

    return round(covariance, 2)


assert covariance(num_friends, daily_minutes) == 22.43, "calculation of 'covariance' is incorrect"
assert covariance(num_friends, daily_hours) == 0.37, "calculation of 'covariance' is incorrect"


def correlation(xs: List[float], ys: List[float]) -> float:
    """Measures how much xs and ys vary in tandem about their means

    correlation is unitless and always lies
    between -1 (perfect anti-correlation)
    and 1 (perfect correlation"""

    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        correlation = covariance(xs, ys) / stdev_x / stdev_y
    else:
        correlation = 0     # if no variation, correlation is zero
    return round(correlation, 2)


assert correlation(num_friends, daily_minutes) == 0.25, "calculation of 'correlation' is incorrect"
assert correlation(num_friends, daily_hours) == 0.24, "calculation of 'correlation' is incorrect"
