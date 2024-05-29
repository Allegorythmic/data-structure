# DataStructure Project

## Overview

This project provides a custom data structure class implementations. The project includes a suite of unit tests to ensure the functionality and correctness of the classes, and uses `pytest` for testing and coverage reporting.

## Features

- Data structure classes
- Unit tests for all class methods
- Test coverage reporting

## Requirements

- Python 3.11
- `pip` for package management
- `make` for automation

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Allegorythmic/data-structure.git
    cd data-structure
    ```

2. Set up a virtual environment:
    ```sh
    python -m venv .venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```sh
        source .venv/bin/activate
        ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running Tests

To run the tests, you can use the following command:
```sh
make test
```

### Generating Coverage Report

To generate a test coverage report, run:
```sh
make coverage
```

### Cleaning Up

To clean up the project directory (remove .pyc files and __pycache__ directories), run:
```shell
make clean
```

### Project Structure

```markdown
project/
├── src/
│   ├── __init__.py
│   └── datastruct/
│       ├── __init__.py
│       └── array.py
├── tests/
│   ├── __init__.py
│   └── test_array.py
├── .github/
│   └── workflows/
│       └── python-package.yml
├── pytest.ini
├── Makefile
├── requirements.txt
└── README.md
```

### Continuous Integration

The project is set up with GitHub Actions for continuous integration. The workflow is defined in .github/workflows/python-package.yml and includes steps to:

- Set up Python
- Install dependencies
- Clean previous test artifacts
- Run tests and generate coverage reports
- Lint the code

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.