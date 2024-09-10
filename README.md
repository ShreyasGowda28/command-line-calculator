# Command Line Calculator

## Overview

This project is a simple interactive command line calculator that supports a range of mathematical operations, including basic arithmetic and algebraic expressions. The calculator is built using Python for backend processing and HTML/CSS for the frontend interface.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division, modulus, and exponentiation.
- **Square Root**: Compute square roots using the `sqrt()` function.
- **Trigonometric Functions**: Calculate sine, cosine, and tangent (e.g., `sin(pi/2)`).
- **Logarithms**: Use the `log()` function for natural logarithms.
- **Exponentials**: Evaluate exponentials with the `exp()` function.
- **Factorial**: Calculate factorials using the `!` operator (e.g., `5!`).
- **Mathematical Constants**: Use constants such as `pi` and `e`.
- **Algebraic Expressions**: Handle expressions with variables (e.g., `x^2 - 5x + 6`).

## Installation

### Prerequisites

- Python 3.x
- Flask

### Steps to Install

1. **Clone the Repository**

    ```bash
    git clone https://github.com/ShreyasGowda28/command-line-calculator.git
    cd command-line-calculator
    ```

2. **Install Dependencies**

    Use pip to install Flask and other required packages:

    ```bash
    pip install Flask
    ```

## Usage

1. **Start the Application**

    Run the Flask server:

    ```bash
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000/`.

2. **Access the Interface**

    Open your web browser and navigate to `http://127.0.0.1:5000/` to access the calculator.

3. **Perform Calculations**

    - Enter a mathematical expression in the input field.
    - Click the **Calculate** button to see the result.

## Project Structure

```
command-line-calculator/
│
├── app.py            # Flask application script
├── static/
│   ├── style.css     # CSS file for styling
│
├── templates/
│   ├── index.html    # HTML template for the interface
│
└── README.md         # This README file
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Shreyas Gowda S**