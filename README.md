
Class example re-structred for pytest and command line script calling.

This example is a bit different from the example in class where we were in "interactive" mode
where we were running the code one line at a time.

When we put files into sub directories, we need to use the `__file__` to find the file for the path.
Since we are now in terminal calling mode, we can use `__file__`.
There is no `__file__` when you are writing python code directly in the interpreter,
since you are not running code in a script file.

## Pytest

run `pytest` at the root of the directory to run the tests found in `tests/`.

It's important you have this line in the top of the test file to find the module to load

```python
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.count_class import count_classes
```

## Running the scripts

The scripts are run from the terminal with

```bash
python scripts/my_script.py
```
