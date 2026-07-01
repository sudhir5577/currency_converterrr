import requests
import json
import sys
from pprint import pprint

# API URL
url = "http://data.fixer.io/api/latest?access_key=33ec7c73f8a4eb6b9b5b5f95118b2275"

# Fetch exchange rates
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if not data["success"]:
        print("API Error:", data["error"]["info"])
        sys.exit()

    fx = data["rates"]

except requests.exceptions.RequestException as e:
    print("Network Error:", e)
    sys.exit()

# Paste your entire currencies list here
currencies = [
    # ... keep your existing currencies list unchanged ...
]

def function1():
    query = input(
        "\nEnter amount, FROM currency, TO currency\n"
        "Example: 100 USD INR\n"
        "Type SHOW to display all currencies\n"
        "Type Q to quit\n> "
    ).strip()

    if query.upper() == "Q":
        print("Goodbye!")
        sys.exit()

    elif query.upper() == "SHOW":
        pprint(currencies)
        return

    try:
        qty, fromC, toC = query.split()

        qty = float(qty)
        fromC = fromC.upper()
        toC = toC.upper()

        if fromC not in fx:
            print(f"Currency '{fromC}' not found.")
            return

        if toC not in fx:
            print(f"Currency '{toC}' not found.")
            return

        # Fixer free plan uses EUR as base currency
        amount = round(qty * fx[toC] / fx[fromC], 2)

        print(f"\n{qty} {fromC} = {amount} {toC}")

    except ValueError:
        print("Invalid input.")
        print("Example: 100 USD INR")

    except KeyError:
        print("Unsupported currency code.")


# Run continuously
while True:
    function1()