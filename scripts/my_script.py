import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.count_class import count_classes

#import src.count_class

#?count_classes

#src.count_class.count_classes()

import pandas as pd

df = pd.DataFrame({
    "class_labels": ["c1", "c2", "c1", "c2"],
    "values" : [1, 2, 1, 1]
})

calculated = count_classes(df, 'class_labels')

print(calculated.equals(calculated))
