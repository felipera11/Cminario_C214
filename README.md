# C214 Seminar - Unit Tests with Python unittest

This repository contains the materials for the C214 seminar on unit tests using Python's `unittest` framework.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/felipera11/Cminario_C214
    ```

2. Create a virtual environment and activate it:

    ```
    python -m venv .env
    .env\Scripts\activate
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Running the Code

To run the code, use the following command:
    
    ```
    python src/main.py
    ```

## Running the Tests

To run the tests, use the following command:

    ```
    python -m coverage run -m unittest discover -s tests
    ```

To see the coverage report, use the following command:

    ```
    python -m coverage html
    ```

Then, open the `htmlcov/index.html` file in your browser to see the coverage report.

## Building the Executable

To build the executable, use the following command:

    ```
    pyinstaller --onefile src/main.py
    ```

The executable will be located in the `dist` folder.