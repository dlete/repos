#!/usr/bin/env python3
# -*- coding: utf-8 -*

# imports, Python core
import enum
import math
import random
from typing import List


# An Enum is a typed set of enumerated values. We can use them
# to make our code more descriptive and readable.
class Kid(enum.Enum):
    BOY = 0
    GIRL = 1


def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])


both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    older = random_kid()
    younger = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

# print("P(both | older):", round(both_girls / older_girl, 3))       # 0.514 ~ 1/2
# print("P(both | either): ", round(both_girls / either_girl, 3))    # 0.342 ~ 1/3


def uniform_pdf(x: float) -> int:
    """the uniform distribution puts equal weight on all
    the numbers between 0 and 1"""
    return 1 if x >= 0 and x < 1 else 0


def uniform_cdf(x: float) -> float:
    """returns the probability that a uniform random variable is <= x"""
    if x < 0:
        return 0    # uniform random is never less than 0
    elif x < 1:
        return x    # e.g. P(X <= 0.4) = 0.4
    else:
        return 1    # uniform random is always less than 1


def normal_pdf(x: List[float], mu: float = 0, sigma: float = 1) -> float:
    """returns the Normal Distribution, probability distribution function"""
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))


def normal_cdf(x: List[float], mu: float = 0, sigma: float = 1) -> float:
    """returns the Normal Distribution, cummulative distribution function
    the probability that a normal variable is <= x"""
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p: float,
                       mu: float = 0,
                       sigma: float = 1,
                       tolerance: float = 0.00001) -> float:
    """find approximate inverse using binary search

    Find the value (x axis value) corresponding to a specified probability (y axis value)
    Input probability -> return/output value with that probability
    """

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z = -10.0                       # normal_cdf(-10) is (very close to) 0
    hi_z = 10.0                         # normal_cdf(10)  is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2      # consider the midpoint
        mid_p = normal_cdf(mid_z)       # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z = mid_z
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z = mid_z
        else:
            break

    return mid_z


def bernoulli_trial(p: float) -> int:
    """returns 0 or 1 depending if random generated number is
    bigger or smaller than input p

    p, 0 <= probability <= 1
    """

    return (1 if random.random() < p else 0)


def binomial(n: int, p: float) -> float:
    """returns Binomial(n,p) random variable: the sum of n independent Bernoulli(p) random
    variables, each of which equals 1 with probability p and 0 with probability 1 − p

    n, independent Bernoulli(p) random variables
    p, probability
    """
    return sum(bernoulli_trial(p) for _ in range(n))
