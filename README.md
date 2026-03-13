[![Greeting Tests](https://github.com/fathimaafi/greeting/actions/workflows/python-tests.yml/badge.svg)](https://github.com/fathimaafi/greeting/actions/workflows/python-tests.yml)

# Greeter Project

A simple Python project that greets users and includes automated tests. It features a basic command-line interface and a modular `greet` function.

## Project Structure

- `greeter.py`: Core logic with a `greet` function and an interactive command-line interface.
- `test_greet.py`: Unit tests using the `unittest` framework to verify the greeting logic.
- `.github/workflows/python-tests.yml`: GitHub Actions workflow configuration for automated testing and linting.

## How to Run Locally

### 1. Run the Greeter Script
To run the interactive script, execute the following command from the project root:

```bash
python greeter.py
```

### 2. Run Tests
To run the unit tests and verify the project, use the following command:

```bash
python -m unittest discover -v .
```

### 3. Linting
This project uses **Pylint** for static code analysis.

#### What is Linting?
Linting is the process of running a tool (a "linter") that analyzes your source code for potential errors, bugs, stylistic issues, and suspicious constructs. It helps maintain code quality, ensures consistency across the codebase, and can catch common mistakes before they become run-time issues.

#### How to Run Linting Locally
To run Pylint on the project files, follow these steps:

1.  **Install Pylint:**
    ```bash
    pip install pylint
    ```

2.  **Run Pylint:**
    ```bash
    python -m pylint greeter.py test_greet.py
    ```

## GitHub Actions
The project includes a GitHub Action workflow located in `.github/workflows/python-tests.yml`. This workflow automatically runs the tests and performs linting on every push to the `main` branch or when a pull request is created. This ensures that the codebase remains stable and follows quality standards.

## Pull Requests and CI
To maintain the quality of the project, all changes should be submitted through Pull Requests (PRs).

### 1. Creating a Pull Request
- Create a new branch for your changes: `git checkout -b feature-name`.
- Commit and push your changes to your fork or the repository.
- Open a Pull Request against the `main` branch on GitHub.

### 2. Continuous Integration (CI)
- Once a PR is opened, the GitHub Actions CI workflow will automatically trigger.
- It will install dependencies, run **Pylint** for code quality, and execute the **unittest** suite.
- You can monitor the progress in the "Checks" tab of your PR.

### 3. Reviewing a Pull Request
- **Check CI Status:** Ensure all checks have passed (indicated by a green checkmark). If any checks fail, review the logs in the GitHub Actions tab to identify and fix the issues.
- **Code Review:** Review the code for logic, readability, and adherence to project standards.
- **Merge:** Once the CI passes and the code is approved, the PR can be safely merged into the `main` branch.
