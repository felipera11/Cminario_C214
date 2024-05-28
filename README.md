# C214 Seminar - Unit Tests with Python unittest

This repository contains the materials for the C214 seminar on unit tests using Python's `unittest` framework.

## Group Members

- Felipe Silveira
- Thayana Lucero

## Python unittest

`unittest` is Python's built-in unit testing framework. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

The `unittest` module can be used from the command line to run tests from modules, classes, or even individual test methods. It also supports test discovery, which allows you to run all tests in a directory or package.

## Repository Structure

The repository is structured as follows:

- `src`: Contains the source code for the project.
- `tests`: Contains the unit tests for the project.
- `requirements.txt`: Contains the list of dependencies for the project.
- `README.md`: Contains the information about the project.
- `.gitignore`: Contains the list of files and folders to be ignored by Git.
- `.github/workflows`: Contains the GitHub Actions workflow files.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/felipera11/Cminario_C214
   cd Cminario_C214
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv .env     #on Linux: python3 -m venv .env
   .env\Scripts\activate   #on Linux: source .env/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Code

To run the code, use the following command:

    ```

## Running the Tests

To run the tests, use the following command:

    ```bash
    python -m coverage run -m unittest discover -s tests
    ```

To see the coverage report, use the following command:

    ```bash
    python -m coverage html
    ```

Then, open the `htmlcov/index.html` file in your browser to see the coverage report.

## Building the Executable

To build the executable, use the following command:

    ```bash
    pyinstaller --onefile src/main.py
    ```

The executable will be located in the `dist` folder.

## CI/CD

This repository is configured with GitHub Actions to run the tests on every push to the `main` branch. It also runs the tests with coverage and uploads the coverage report as an artifact.

The build process is also triggered on every push to the `main` branch. The executable is built and uploaded as an artifact.
