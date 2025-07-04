# Currency Converter

## Overview

The Currency Converter is a Python application that allows users to convert amounts from one currency to another using real-time exchange rates fetched from an API. The application utilizes the Fixer.io API to retrieve the latest currency exchange rates.

## Features

- **Real-time Currency Conversion**: Converts amounts between different currencies based on the latest exchange rates.
- **Error Handling**: Provides informative error messages for unsupported currencies and API errors.

## Technologies Used

- Python
- Requests library for making HTTP requests

## Installation

To run this application locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/currency-converter.git
   cd currency-converter
   ```

2. Ensure you have Python installed on your machine. This script is compatible with Python 3.x.

3. Install the required library:

   ```
   pip install requests
   ```

4. Run the application:

   ```
   python currency_converter.py
   ```

## Usage

1. **Enter Initial Currency**: When prompted, enter the currency code you want to convert from (e.g., USD, EUR, INR ).
2. **Enter Target Currency**: Enter the currency code you want to convert to.
3. **Enter Amount**: Input the amount you wish to convert.
4. **View Result**: The application will display the converted amount in the target currency.

## Example

```
Enter the initial Currency: USD
Enter the target Currency: EUR
Enter the amount: 100
100 USD = 85.50 EUR
```

## Code Structure

- **ConvertCurrency Class**: 
  - `__init__`: Initializes the class and fetches the latest exchange rates.
  - `get_exchange_rates`: Fetches exchange rates from the Fixer.io API.
  - `convert`: Converts the specified amount from the initial currency to the target currency.

- **Main Function**: 
  - Handles user input and displays the converted amount or error messages.

## API Key

The application uses a hardcoded API key for the Fixer.io service. For production use, consider storing the API key securely and not hardcoding it in the source code. You can sign up for a free account at [Fixer.io](https://fixer.io/) to obtain your own API key.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## Acknowledgments

- Thanks to the Fixer.io API for providing reliable currency exchange rates.
- Thanks to the Python community for their support and resources.

---
