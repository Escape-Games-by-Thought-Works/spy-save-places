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

### Running tests

To run the test:

```
pytest safe_spaces_test.py
```
