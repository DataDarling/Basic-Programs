# Basic Programs

A collection of Python scripts and exercises covering fundamental programming concepts — from string manipulation and iteration to algorithms, data structures, GUI development, and introductory data science.

> **Author:** Darling Ngoh

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Programs](#programs)
  - [Basic String Exercises](#basic-string-exercises)
  - [Exercises on Iteration](#exercises-on-iteration)
  - [Prime Number Evaluator](#prime-number-evaluator)
  - [Tic-Tac-Toe](#tic-tac-toe)
  - [Food Menu](#food-menu)
  - [Roster Manager (Atlanta Braves)](#roster-manager-atlanta-braves)
  - [Vector Operations](#vector-operations)
  - [Bank Management System](#bank-management-system)
  - [Binary Search (File Content)](#binary-search-file-content)
  - [Merge Sort (Recursive)](#merge-sort-recursive)
  - [Quick Sort (Integers)](#quick-sort-integers)
  - [Basic File Analysis](#basic-file-analysis)
  - [Basic SQL Practice — Inventory Database](#basic-sql-practice--inventory-database)
  - [Intro to NumPy](#intro-to-numpy)
  - [Basic OOP with Tkinter](#basic-oop-with-tkinter)
  - [Home Scape (Turtle Graphics)](#home-scape-turtle-graphics)
  - [Event-Driven Programming (Turtle)](#event-driven-programming-turtle)
  - [Turtle Event-Driven Practice](#turtle-event-driven-practice)
  - [Intro to Loss Functions for Regression](#intro-to-loss-functions-for-regression)
- [Running the Programs](#running-the-programs)
- [License](#license)

---

## Overview

This repository serves as a learning portfolio demonstrating core Python programming skills. The programs range from beginner-friendly console scripts to intermediate-level topics such as sorting algorithms, object-oriented programming, GUI applications, database interaction, and machine-learning utility functions.

---

## Prerequisites

- **Python 3.x** (most programs require no additional packages)
- **Standard library dependencies** (included with Python):
  - `math`, `sqlite3`, `tkinter`, `turtle`, `unittest`
- **Third-party dependencies** (install via pip):
  - `numpy` — required for [Intro to NumPy](#intro-to-numpy)

```bash
pip install numpy
```

---

## Programs

### Basic String Exercises

**File:** `Basic String Excercises.py`

A comprehensive set of string manipulation exercises covering common operations such as:
- Reversing strings and words
- Checking for palindromes
- Counting vowels and consonants
- Formatting and parsing text

**Run:**
```bash
python "Basic String Excercises.py"
```

---

### Exercises on Iteration

**File:** `Excercises on Iteration.py`

A set of exercises focused on Python iteration patterns, including `for` loops, `while` loops, list comprehensions, and range-based traversals across various problem types.

**Run:**
```bash
python "Excercises on Iteration.py"
```

---

### Prime Number Evaluator

**File:** `PrimeNumEval.py`

Prompts the user to enter an integer and reports whether the number is:
- Prime
- Not prime
- Negative

Uses an efficient square-root-based algorithm to check for factors.

**Run:**
```bash
python PrimeNumEval.py
```

**Example interaction:**
```
      *** isPrime ***

Please provide an integer: 17
The integer 17 is prime.
```

---

### Tic-Tac-Toe

**File:** `Tictactoe.py`

A console-based Tic-Tac-Toe winner evaluator. The user inputs three rows of a board (using `X`, `O`, or `E` for empty), and the program determines whether X wins, O wins, or the game is a tie.

**Run:**
```bash
python Tictactoe.py
```

**Example interaction:**
```
Please input 3 combine of 'X', 'O', or 'E' as XOE, XXE and so on
ROW0: XXX
ROW1: OEO
ROW2: EOE
X is GOOD in horizontal
```

---

### Food Menu

**File:** `Food Menu.py`

Simulates a restaurant ordering experience at "Dairy King." The program:
- Presents menu items (Grilled Cheese, Nachos, Chicken, Hamburger/Cheeseburger, Hot Dog)
- Accepts `y`/`n` responses from the user
- Calculates the subtotal and total with a 20% tip

**Run:**
```bash
python "Food Menu.py"
```

**Example output:**
```
Welcome to Dairy King! Please enter y or n for your menu selections.
...
The total for your food is $13
The total with 20% tip is $15.6
Thank you for your business!
```

---

### Roster Manager (Atlanta Braves)

**File:** `Roster.py`

An interactive roster management program for the Atlanta Braves. Supports three operations:
1. **Search** — Look up a player's batting statistics
2. **Add** — Add a new player and their stats (handles duplicate names automatically)
3. **Remove** — Delete a player from the roster

Includes a `unittest` test suite covering search, add, and delete operations.

**Run:**
```bash
python Roster.py
```

---

### Vector Operations

**File:** `vector.py`

Implements the following mathematical vector operations on Python lists:
| Function | Description |
|---|---|
| `add_vectors(u, v)` | Element-wise sum of two equal-length lists |
| `scalar_mult(s, v)` | Multiply each element of a list by a scalar |
| `dot_product(u, v)` | Sum of the products of corresponding elements |
| `cross_product(u, v)` | Cross product of two 3-element vectors |
| `replace(s, old, new)` | Replace all occurrences of a substring |
| `swap(x, y)` | Swap two variables using tuple unpacking |

Uncomment the test lines at the bottom of the file to verify each function.

**Run:**
```bash
python vector.py
```

---

### Bank Management System

**File:** `basic bank mgmt system`

An object-oriented `BankAccount` class that models a simple bank account with:
- **Checking** and **savings** account balances
- `deposit_checking(amount)` / `deposit_savings(amount)`
- `withdraw_checking(amount)` / `withdraw_savings(amount)`
- `transfer_to_savings(amount)` — transfers funds from checking to savings

Demo code at the bottom instantiates an account and performs sample transactions.

**Run:**
```bash
python "basic bank mgmt system"
```

---

### Binary Search (File Content)

**File:** `binary search - file content practice`

Reads a list of words from `words.txt` and performs an interactive binary search. The user enters a search term and the program returns:
- The index at which the word was found (or `-1` if not found)
- The number of iterations required

Enter `exit` to quit.

**Requires:** A `words.txt` file in the same directory (sorted word list).

**Run:**
```bash
python "binary search - file content practice"
```

---

### Merge Sort (Recursive)

**File:** `merge sort algorithm - recursive`

Implements the **merge sort** algorithm recursively. Takes an unsorted list of integers and returns them sorted in **descending order**.

**Run:**
```bash
python "merge sort algorithm - recursive"
```

**Example output:**
```
UNSORTED: 10 2 78 4 45 32 7 11
SORTED: 78 45 32 11 10 7 4 2
```

---

### Quick Sort (Integers)

**File:** `quick sort algorithm - integers`

Implements the **quick sort** algorithm using the rightmost element as the pivot. Sorts a list of integers in **ascending order** and prints step-by-step partitioning details.

**Run:**
```bash
python "quick sort algorithm - integers"
```

**Example output:**
```
------ Quick sorting from index: 0  to  7 -----
Array segment before partitioning: 11 12 1 9 6 5 4 7 , Pivot: 7
...
The final sorted array [1, 4, 5, 6, 7, 9, 11, 12]
```

---

### Basic File Analysis

**File:** `basic file analyses practice`

Reads a text file (`example.txt`), analyzes its contents, and writes results to a new output file (`test file.txt`) containing:
- Total number of lines (first 28)
- Total word count (first 28 lines)
- Word count per line for remaining lines

**Requires:** An `example.txt` file in the same directory.

**Run:**
```bash
python "basic file analyses practice"
```

---

### Basic SQL Practice — Inventory Database

**File:** `basic SQL practice - inventory database`

Uses Python's built-in `sqlite3` library to create and query a grocery inventory database. Demonstrates:
- Creating a table (`GROCERY`) with `ProductID`, `ProductName`, `UnitPrice`, and `Quantity`
- Inserting rows (Egg, Milk, Rice)
- Querying all products
- Filtering products by price range (`BETWEEN`)
- Computing the total inventory value using `SUM`

Creates a local `store_inventory.db` SQLite database file.

**Run:**
```bash
python "basic SQL practice - inventory database"
```

---

### Intro to NumPy

**File:** `intro numpy practice`

Demonstrates common NumPy array operations:
- Creating a zero-filled matrix with `np.full`
- Inserting rows and columns with `np.insert`
- Deleting rows and columns with `np.delete`
- Sorting along an axis with `np.sort`
- Flattening an array in row-major order with `np.ravel`

**Requires:** `numpy`

**Run:**
```bash
python "intro numpy practice"
```

---

### Basic OOP with Tkinter

**File:** `basic OOP with tkinter practice`

A GUI application built with Python's `tkinter` library that demonstrates:
- `Entry` widget for user input
- `Text` widget for displaying output
- Key-press event binding (`<KeyPress>`)
- Classifying each keystroke as a number, uppercase letter, lowercase letter, or non-alphanumeric key

**Requires:** `tkinter` (included in most Python distributions)

**Run:**
```bash
python "basic OOP with tkinter practice"
```

---

### Home Scape (Turtle Graphics)

**File:** `Home Scape.py`

A turtle graphics program that draws a detailed scene including:
- Blue sky and green grass background
- Distant mountains
- A house with a dark blue frame, brown roof, windows, and a red door
- White clouds and a yellow sun with rays
- Colorful flowers (yellow, red, purple) and grass tufts

**Requires:** `turtle` (included with Python)

**Run:**
```bash
python "Home Scape.py"
```

---

### Event-Driven Programming (Turtle)

**File:** `Event-Driven-Programming(turtle).py`

Introduces event-driven programming concepts using Python's `turtle` module. Demonstrates binding keyboard or mouse events to trigger drawing actions in real time.

**Run:**
```bash
python "Event-Driven-Programming(turtle).py"
```

---

### Turtle Event-Driven Practice

**File:** `turtle event driven practice.py`

Additional hands-on practice with turtle event-driven programming, exploring user interactions such as key bindings and mouse click handlers to control turtle movement and drawing.

**Run:**
```bash
python "turtle event driven practice.py"
```

---

### Intro to Loss Functions for Regression

**File:** `Intro to Loss Functions For Regression`

Implements three fundamental regression loss (error) functions used in machine learning:

| Function | Description |
|---|---|
| `computeMSE(observed, predicted)` | Mean Squared Error |
| `computeRMSE(observed, predicted)` | Root Mean Squared Error |
| `computeMAE(observed, predicted)` | Mean Absolute Error |

Includes driver code using sample observed/predicted values and prints results rounded to two decimal places.

**Run:**
```bash
python "Intro to Loss Functions For Regression"
```

**Example output:**
```
MSE =  1.40
RMSE =  1.18
MAE =  1.00
```

---

## Running the Programs

Clone the repository and navigate into the directory:

```bash
git clone https://github.com/DataDarling/Basic-Programs.git
cd Basic-Programs
```

Run any script using Python 3:

```bash
python <filename>
```

For scripts with spaces in their name, wrap the filename in quotes:

```bash
python "Food Menu.py"
```

---

## License

This project is open-source and available for educational use.
