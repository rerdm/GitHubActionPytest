# GitHubActionPytest
In this project a simple pytest will be executed via GitHubActions.


# Preconditions

1. Install python 
2. Install pytest


## Test (Local)

Install dependencies  : <code>pip install -r requirements.txt</code> <br>
Run all tests                 : <code>pytest -m test/</code> <br>
Run specific testset          : <code>pytest -m tests/test-name-with-extension</code><br>
Run specific test in testset  : <br><code>pytest -m tests/test-name-with-extension::test_add</code>

