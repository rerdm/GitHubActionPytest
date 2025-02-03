# GitHubActionPytest
- In this project a simple pytest will be executed via GitHubActions end send notification via email.


# Preconditions

1. Install python ( and add to environmnt vars)
2. Install pytest ( and add to environmnt vars)
3. Create <code>ci.yaml</code> file in <code>.github/wokflow</code>folder (see example)
4. Create file with functions to be <code>src/calculator.py</code> folder (see example)
5. Create test file with pytest <code>tests/test_calculator.py</code> folder (see example)


## Test (Local)

- Install dependencies  : <code>pip install -r requirements.txt</code> <br>
- Run all tests                 : <code>pytest -m test/</code> <br>
- Run specific testset          : <code>pytest -m tests/test-name-with-extension</code><br>
- Run specific test in testset  : <br><code>pytest -m tests/test-name-with-extension::test_add</code>

## Starting Githubaction Workflow

- When you make a change now and you commit and push it to master the action 
will be triggered.

## Configure email notofication in GitHub

- When you want to get email notification with the results if the test (after pushing) you have to set it up in GitHub the 
- Email adress in settings/integrations/Email notifications.

## Example of .github/workflows/ci.yaml file

```

    name: Python CI/CD

    on:
    push:
        branches:
        - master
    pull_request:
        branches:
        - master

    jobs:
    test:
        runs-on: ubuntu-latest

        steps:
        - name: 🔄 Checkout Repository
            uses: actions/checkout@v3

        - name: 🐍 Set up Python
            uses: actions/setup-python@v4
            with:
            python-version: "3.9"

        - name: 📦 Install dependencies
            run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt

        - name: 🛠️ Run Tests with pytest
          run: python -m pytest tests/test_callculator.py::test_sub

```