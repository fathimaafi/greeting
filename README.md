# Greeter Project

A simple Python project that greets users and includes automated tests.

## Project Structure

- `greeter/`
  - `greeter.py`: Core logic with a `greet` function.
  - `test_greet.py`: Unit tests using the `unittest` framework.
  - `__init__.py`: Package initialization.

## How to Run Locally

### 1. Run the Greeter Script
To run the interactive script, execute the following command from the root directory:

```bash
python greeter/greeter.py
```

### 2. Run Tests
To run the unit tests and verify the project, use the following command:

```bash
python -m unittest discover -v greeter
```

## GitHub Actions
The project includes a GitHub Action workflow located (currently) in `greeter/.github/workflows/python-tests.yml`. Note: For GitHub to automatically detect and run this workflow on push, the `.github` folder must be located at the root of the repository.
