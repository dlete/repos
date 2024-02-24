#!/usr/bin/env python3
# -*- coding: utf-8 -*

# imports, Python core
import random
from collections import Counter
from typing import List
from typing import NamedTuple

# imports, same directory
from ch04_linear_algebra import distance, Vector


def raw_majority_vote(labels: List[str]) -> str:
    """returns element that appears most times in a list
    does not know how to deal with ties"""
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner


# No tie
assert raw_majority_vote(['a', 'b', 'c', 'b']) == 'b'
# Tie, it will report the element it finds first
assert raw_majority_vote(['a', 'b', 'a', 'b']) == 'a'
# Tie, it will report the element it finds first
assert raw_majority_vote(['b', 'a', 'b', 'a']) == 'b'


def majority_vote(labels: List[str]) -> str:
    """returns element that appears most times in a list
    deals with ties
    Assumes that labels are ordered from nearest to farthest"""

    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner                       # unique winner, so return it
    else:
        return majority_vote(labels[:-1])   # try again without the farthest


# Tie, so remove one and then look at first 4 (the remaining), then 'b'
assert majority_vote(['a', 'b', 'c', 'b', 'a']) == 'b'
# No tie
assert majority_vote(['a', 'b', 'c', 'c', 'c']) == 'c'


class LabeledPoint(NamedTuple):
    point: Vector
    label: str


def knn_classify(k: int,
                 labeled_points: List[LabeledPoint],
                 new_point: Vector) -> str:
    """each labeled point should be a pair (point, label)"""

    # order the labeled points from nearest to farthest
    by_distance = sorted(labeled_points,
                         key=lambda point_label: distance(point_label[0], new_point))

    # find the labels for the k closest, the first k elements in the ordered list
    k_nearest_labels = [label for _, label in by_distance[:k]]

    # and let them vote
    return majority_vote(k_nearest_labels)

#
# the curse of dimensionality
#


def random_point(dim: int) -> Vector:
    """returns vector of as many dimensions as in input, of random values"""
    return [random.random() for _ in range(dim)]


def random_distances(dim: int, num_pairs: int) -> List[float]:
    """returns list of distances between as many num_pairs as in input,
    where each point is a vector of as many dimensions as in input and random values"""

    return [distance(random_point(dim), random_point(dim))
            for _ in range(num_pairs)]
