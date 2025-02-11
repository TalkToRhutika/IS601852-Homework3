# Calculator 
## Project description
This project is done in 2 stages till now using OOP's concepts. It has basic functions as addition, subtraction, multiplication, division, percentage, square root and factorization, also it stores history of calculations.
Project has 3 classes, 1st is Calculator class with static, instance & class methods, 2nd is Calculation class to encapsulate the operations and last is Calculations class to manage hostory.


## My project install instructions
## Install

1. clone
2. pip install -r requirements.txt

## Testing

1. pytest
2. pytest --pylint
3. pytest --pylint --cov

## Notes

1. python version 3.12.3 latest stable is installed already
2. vs code and python microsoft extension is installed already
3. go to the project directory from vscode terminal
4. create virtual environment for python in the vscode pip3 install virtualenv
5. run command in the vs code terminal. cd /projectfolder python3 -m venv venv
6. activate the virtual environment. source venv/bin/activate
7. install testing libraries pip3 install pytest pytest-pylint pytest-cov
8. freeze requirements pip3 freeze > requirements.txt
9. add code for calculator and test in the project
10. run tests to check the code. pytest --pylint --cov

## Calculator 1.1

- Basic functions: add, sub, multi and div

## Calculator 1.2

- Basic functions same as above and add on functions %, square root and factorial with clean code and history management feature.

### Steps: 
1. write the calculator code ie. operations in calculator.py
2. write unit test cases in test2_calculator.py
3. linting and code quality check: create a .pylintrc file by 
   [MESSAGES CONTROL]
   disable=unnecessary-dunder-call, invalid-name
   no**pylint --generate-rcfile > .pylintrc
4. pytest configuration: [pytest]
addopts = --maxfail=2 --disable-warnings --cov=calculator
1. coverage setup: pip install pytest pytest-cov pylint
2. run tests and check coverage: pytest --cov=calculator
3. commit and push to git 
   git add .
git commit -m "Initial complete calculator project with tests"
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main

