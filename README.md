# Advanced Calculator 
## Basic commands for macOS(zsh)
1. Create virtual environment: go the directory where want to create virtual environment
   python3 -m venv venv

2. Activate virtual environment
   source venv/bin/activate

3. Deactivate virtual environment 
   deactivate

4. Install packages using pip
   python3 -m pip install Faker 

5. Save installed packages with their versions to a file
   python3 pip freeze > requirements.txt

6. Install Faker
   python3 -m pip install Faker


## Project description
This project has been completed in two phases applying the concepts of OOP. In addition to storing calculation history, it performs fundamental operations such addition, subtraction, multiplication, division, percentage, square root, and factorization. Three classes define the project: the Calculator class, which has static, instance, and class methods; the Calculation class, which encapsulates the operations; and the Calculations class, which manages the history.

## Calculator 1.2
- Basic functions same as previous homework2 and few add-on functions %, square root and factorial with clean code and history management feature.

### Steps: 
1. write the calculator code ie. operations in calculator.py and calculations.py
2. write unit test cases in test_calculator.py
3. you can run program using main.py to check functionality.
4. linting and code quality check
5. run pytest
6. check coverage 
pytest --cov=calculator
7. git commit to repository
   i. create new repository on the git using terminal
   ii. go the project folder in the terminal
   iii. create repository in the git using token : curl -u "username:github_pat_1" \
  https://api.github.com/user/repos \
  -d '{"name":"IS601852-Homework3"}'
   iv. git init
   v. git add .
   vi. git commit -m "Initial complete calculator project with tests"
   vii. git remote add origin <your-repo-url>
   viii. git branch -M main
   ix.git push -u origin main
8. Create a new brach for feature/add-faker in existing repository
9. Run the changes, commit and merge it in the existing branch.
   python3 -m pytest /Users/tc/Documents/Semester4/WebSystems/IS601852-Homework3/tests/test_faker.py


## Challenges faced
1. Frquent error for faker as "ModuleNotFoundError"
   Reason: Faker was not installed in venv correctly.
   Solution: Recreate the virtual environment using python3 -m venv venv, activate it, and reinstall dependencies.





