## Table of contents
* [Introduction](#introduction)
* [Structure](#structure)
* [Installation](#setup)
* [Contribute](#contribute)

## Introduction
The purpose of this project is to solve most of the simplest programmatically challenges in Python language. These challenges are not only simple, but also complex and intensive at the same time.

## Structure
Each challenge is created in a seperate folder which cotains the README question desciption and its solution in another file which is named as "challenge_name_solution.py". Additionaly, test_challenge_name.py is added to test all the possible cases.

## Installation
The best way to not missing current python setup is to created a seperate virtualenv, by following:
 [python-virtualenv](https://docs.python-guide.org/dev/virtualenvs/)
```sh
$ pip install virtualenv
```

Test your installation:
```sh
$ virtualenv --version
```

Create a virtual environment for a project:
```sh
$ cd project_folder
$ virtualenv venv
```


install the test packages using the pip command:
```sh
$ pip install pytest
```

## Testing
To test each challenge, you can go to the challenge_folder and run the py.test:
```sh
$ cd challenge_folder
$ py.test
```

## Contribute
Please fee free to contribute and share pull request any chalenge you might find it interesting. The code is licensed under [MIT](https://mit-license.org).
I would be happy to hear any feeback or comments: hadi.alnehlawi@gmail.com
