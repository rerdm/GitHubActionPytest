# GitHubActionPytest
In this project a simple pytest will be executed via GitHubActions.


# Preconditions

1. Install python 
2. Install pytest
3. Create <code>ci.yaml</code> file in <code>.github/wokflow</code>folder (see example)
4. Create file with functions to be <code>src/calculator.py</code> folder (see example)
5. Create test file with pytest <code>tests/test_calculator.py</code> folder (see example)


## Test (Local)

Install dependencies  : <code>pip install -r requirements.txt</code> <br>
Run all tests                 : <code>pytest -m test/</code> <br>
Run specific testset          : <code>pytest -m tests/test-name-with-extension</code><br>
Run specific test in testset  : <br><code>pytest -m tests/test-name-with-extension::test_add</code>

## Starting Githubaction Workflow

When you make a change now and you commit and push it to master the action 
will be triggered.

## Configure email notofication in GitHub

When you want to get Email notification with the results if the test (after pushing) you have to set it up in GitHub the 
Email adress in : <code>settings/integrations/Email notifications.

