from typing import List
from typing import Tuple
from typing import TypeVar
import random
X = TypeVar('X')    # generic type to represent a data point
Y = TypeVar('Y')    # generic type to represent output variables


def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    """Split data into fractions [prob, 1 - prob]"""
    data = data[:]                  # Make a shallow copy
    random.shuffle(data)            # because shuffle modifies the list
    cut = int(len(data) * prob)     # Use prob to find a cutoff
    return data[:cut], data[cut:]   # and split the shuffled list there


data = [n for n in range(1000)]
train, test = split_data(data, 0.75)

# The proportions should be correct
assert len(train) == 750, "the 'train' data is longer or shorter than expected"
assert len(test) == 250, "the 'test' data is longer or shorter than expected"

# And the original data should be preserved (in some order)
assert sorted(train + test) == data, "the train + test data is different from the original data"


def train_test_split(xs: X, ys: Y, train_pct: float) -> Tuple[List[X], List[X], List[Y], List[Y]]:
    """Split xs and ys data into fractions [xsprob, 1 - prob] for xs and ys"""
    assert len(xs) == len(ys), "the size of xs and ys is not the same"
    zipped_data = list(zip(xs, ys))                   # zip both xs and ys
    train, test = split_data(zipped_data, train_pct)  # split into train and test
    xs_train, ys_train = zip(*train)                  # unzip train xs and ys
    xs_test, ys_test = zip(*test)                     # unzip test xs and ys
    return xs_train, xs_test, ys_train, ys_test


# generate sample xs and ys data
xs = [x for x in range(1000)]
ys = [2*x for x in xs]

# split xs and ys into train and test
xs_train, xs_test, ys_train, ys_test = train_test_split(xs, ys, 0.75)

# Check that data has not been lost
assert len(xs_train) + len(xs_test) == len(xs), "have lost data splitting xs into train + test"
assert len(ys_train) + len(ys_test) == len(ys), "have lost data splitting ys into train + test"

# Check that the proportions are correct
assert len(xs_train) == len(ys_train), "the amount of xs_train and ys_train is not the same"
assert len(xs_test) == len(ys_test), "the amount of xs_train and ys_train is not the same"

# Check that the corresponding data points are paired correctly.
assert all(y == 2 * x for x, y in zip(xs_train, ys_train))
assert all(y == 2 * x for x, y in zip(xs_test, ys_test))


def accuracy(tp: int, fp: int, fn: int, tn: int) -> float:
    """accuracy is defined as the fraction of correct predictions
    correct predictions = true positives + true negatives"""
    predictions_correct = tp + tn
    predictions_total = tp + fp + tn + fn
    return predictions_correct / predictions_total


assert accuracy(70, 4930, 13930, 981070) == 0.98114, "accuracy calculation function has an error"


def precision(tp: int, fp: int, fn: int, tn: int) -> float:
    """Precision measures how accurate our positive predictions were"""
    return tp / (tp + fp)


assert precision(70, 4930, 13930, 981070) == 0.014, "precision calculation function has an error"


def recall(tp: int, fp: int, fn: int, tn: int) -> float:
    """recall measures what fraction of the positives our model identified"""
    return tp / (tp + fn)   # fn, false negative, is in fact a positive


assert recall(70, 4930, 13930, 981070) == 0.005, "recall calculation function has an error"


def f1_score(tp: int, fp: int, fn: int, tn: int) -> float:
    """returns the harmonic mean of recall and precision and necessarily lies between them"""
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)
    return 2 * p * r / (p + r)


assert f1_score(70, 4930, 13930, 981070) == 0.00736842105263158, "f1_score calculation function has an error"
assert precision(70, 4930, 13930, 981070) > f1_score(70, 4930, 13930, 981070), "f1_score is not lower than precision"
assert recall(70, 4930, 13930, 981070) < f1_score(70, 4930, 13930, 981070), "f1_score is not higher than precision"
