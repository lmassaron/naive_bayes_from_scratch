# Naive Bayes Classifier

This project contains a C++ implementation of a Gaussian Naive Bayes classifier. The main goal of the classifier is to predict the behavior of vehicles on a highway, such as changing lanes or keeping the current lane, based on sensor data. Additionally, there is a Python implementation of a Naive Bayes classifier from scratch.

The project includes the Eigen library for linear algebra operations.

## Project Structure

- `main.cpp`: The main entry point of the C++ application. It loads data, trains the classifier, and makes predictions.
- `classifier.h`: Header file for the Naive Bayes classifier in C++.
- `classifier.cpp`: Implementation of the Naive Bayes classifier in C++.
- `classifier.py`: A Python implementation of a Gaussian Naive Bayes classifier.
- `prediction.py`: A Python script to make predictions using the Python classifier.
- `predicition_solution.py`: A solution file for the prediction exercise.
- `Eigen-3.3/`: Contains the Eigen library, a C++ template library for linear algebra.
- `docs/`: Contains PDF documents with additional information about Naive Bayes and the project.
- `train_states.txt`, `train_labels.txt`: Training data.
- `test_states.txt`, `test_labels.txt`: Testing data.
- `nd013_pred_data/`: A directory containing additional prediction data.

## Compilation

The C++ application can be compiled on various operating systems. The only dependency is the Eigen library, which is already included in the project. A C++ compiler that supports C++11 is required.

### macOS and Ubuntu (Linux)

On macOS and Linux, you can compile the project using `g++`. If you don't have `g++` installed, you can get it by installing the build-essential package on Ubuntu (`sudo apt-get install build-essential`) or the Xcode Command Line Tools on macOS.

To compile the project, open a terminal in the project's root directory and run the following command:

```bash
g++ -std=c++11 -I./Eigen-3.3/ -o Naive_Bayes main.cpp classifier.cpp
```

This command will create an executable file named `Naive_Bayes` in the project's root directory.

Alternatively, you can use the provided `Makefile`:

```bash
make
```

To run the program, execute the following command:

```bash
./Naive_Bayes
```

### Windows

On Windows, you can use a C++ compiler like MinGW-w64 or the Microsoft Visual C++ compiler.

#### Using MinGW-w64 (g++)

If you have MinGW-w64 installed and configured, you can compile the project by opening a command prompt in the project's root directory and running the following command:

```bash
g++ -std=c++11 -I./Eigen-3.3/ -o Naive_Bayes.exe main.cpp classifier.cpp
```

This will create an executable file named `Naive_Bayes.exe`.

#### Using Microsoft Visual C++ Compiler (MSVC)

If you have Visual Studio installed, you can use the Developer Command Prompt. Navigate to the project's root directory and run the following command:

```bash
cl /EHsc /std:c++14 /I./Eigen-3.3/ main.cpp classifier.cpp /FeNaive_Bayes.exe
```

This will create an executable file named `Naive_Bayes.exe`.

To run the program, execute the following command in the command prompt:

```bash
.\Naive_Bayes.exe
```

## Python Implementation

The project also includes a Python implementation of a Naive Bayes classifier. To run the Python version, you will need to have Python and the `pandas` and `numpy` libraries installed.

You can run the prediction script using the following command:

```bash
python prediction.py
```