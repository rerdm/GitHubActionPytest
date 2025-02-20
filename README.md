
- [GitHubActionPytest](#GitHubActionPytest)
    - [Preconditions](#preconditions)
    - [Test (Local)](#test-local)
    - [Starting Githubaction & Workflow](#starting-githubaction--workflow)
    - [Configuration of Path](#configuration-of-path)
    - [Configure email Notifikation in GitHub](#configure-email-notification-in-github)
    - [Example of .github/workflows/ci.yaml file](#example-of-githubworkflowsciyaml-file)
    - [Reporting](#reporting)

<br>
<hr>


# GitHubActionPytest

## Project Description

GitHubActionPytest is a project designed to automate the testing of Python code using GitHub Actions and pytest. It provides a continuous integration and continuous deployment (CI/CD) pipeline that runs tests on every push and pull request to the master branch. The project includes configuration for setting up the Python environment, installing dependencies, running tests, and generating test reports. Additionally, it offers guidance on configuring email notifications for test results and ensuring that test files can locate the source files by modifying the Python path.

## Preconditions

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

## Starting Githubaction & Workflow

- When you make a change now and you commit and push it to master the action 
will be triggered.

## Configure email notofication in GitHub

- When you want to get email notification with the results if the test (after pushing) you have to set it up in GitHub the 
- Email adress in settings/integrations/Email notifications.


## Configuration of Path

To ensure that the test files can locate the source files, you need to configure the Python path. This can be done by adding the following code snippet to the top of your test files:

```python
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
```

This code modifies the `sys.path` list to include the `src` directory, allowing the test files to import modules from the source directory. This is necessary because, by default, Python does not include the parent directory of the test files in the module search path.

### GitHub Actions Workflow
The current GitHub Actions workflow configuration is as follows:


```yaml
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
          pip install pytest pytest-html

      - name: 🛠️ Run Tests with pytest
        env:
          PYTHONPATH: src
        run: pytest --html=report.html

      - name: 📦 Create report directory
        run: |
          mkdir -p report/assets
          mv report.html report/
          cp assets/style.css report/assets/

      - name: 📄 Upload HTML report with assets
        uses: actions/upload-artifact@v4
        with:
          name: test-report-${{ github.sha }}
          path: report
```