# Find safe places in Python

### Requirements

For this exercise we will be using python3.

You can [install requirements manually](#manual-installation), or if you are comfortable using [virtual environments](#virtualenv-installation), a `requirements.txt` file has been provided for your convenience.

#### Manual Installation

To get started manually, install the following packages:

pytest

```
pip3 install pytest
```

#### virtualenv Installation

If you do not have virtualenv installed, first install it by running:

```
pip3 install virtualenv
```

Next, create a virtual environment by typing:

```
python3 -m venv env
```

Then, activate the virtual environment as follows:

```
source env/bin/activate
```

Finally, you can install the requirements from `requirements.txt` as follows:

```
pip install -r requirements.txt
```

This will also install numpy and scipy for your convenience. However, you are not required to use these packages to complete the exercise.


### Creating the solution

You should see the file `safe_spaces.py`, which contains a class definition for a class named `SafetyFinder`. This class contains three methods: `convert_coordinates`, `find_safe_spaces`, and `advice_for_alex`.

There are three levels to the challenge. In the first level you are asked to convert alphanumeric map coordinates (e.g. 'A3') to a more easily handled form. In the next level, you are asked to find the "safe spaces" in the map. Finally, in the last level, you are asked to provide feedback to Alex and to handle any edge cases.

For each method, we are expecting `agents` to be a list of coordinates, e.g.

```python
finder = SafetyFinder()
finder.convert_coordinates(['A1', 'B2', 'C3'])
```

The tests expect that you will use this method; however, you may add other methods to the class as necessary for your solution.


### Running tests

To run the test:

```
pytest safe_spaces_test.py
```
