
# Currency Converter to Indian Rupees

A Python project that converts currencies from five countries into
Indian Rupees (INR) using the latest available exchange rates.

## Supported Currencies

- USD - United States Dollar
- GBP - British Pound
- EUR - Euro
- JPY - Japanese Yen
- AED - UAE Dirham

## Features

- Live exchange-rate retrieval through an online API
- Menu-driven currency selection
- Conversion into Indian Rupees
- Displays the rate update timestamp
- Input validation and network error handling

## Requirements

- Python 3
- Internet connection
- Requests library

## Installation

1. Clone this repository or download the project.
2. Open a terminal in the project directory.
3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python main.py
   ```

On Windows, you can use `py` instead of `python` if necessary.

## Exchange Rate Source

Rates are retrieved from:

https://open.er-api.com/

Exchange rates fluctuate, and the latest available data may not be
real-time. Verify rates independently before making financial decisions.

## Author

Created as a Python learning project.