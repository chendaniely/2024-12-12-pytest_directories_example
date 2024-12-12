import pytest
import pandas as pd

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.count_class import count_classes

df = pd.DataFrame({
    "class_labels": ["c1", "c2", "c1", "c2"],
    "values" : [1, 2, 1, 1]
})

# `count_classes` should return a data frame, or tibble,
# with the number of rows corresponding to the number of unique classes
# in the `class_col` from the original dataframe. The new dataframe
# will have a `class column` whose values are the unique classes,
# and a `count` column, whose values will be the number of observations
# for each  class
def test_count_classes():
    calculated = count_classes(df, 'class_labels')
    expected = pd.DataFrame({
        "class": ["c1", "c2"],
        "count": [2, 2]
    })
    print(expected)
    assert isinstance(count_classes(df, 'class_labels'), pd.DataFrame)
    assert calculated.equals(expected)

# `count_classes` should return an empty data frame, or tibble,
# if the input to the function is an empty data frame
def test_count_classes_empty():
  pass


# `count_classes` should throw an error when incorrect types
# are passed to the `data_frame` argument
def test_count_classes_errors():
  pass
