
import requests

API_URL = "https://open.er-api.com/v6/latest/{}"

CURRENCIES = {
    "1": ("USD", "United States Dollar", "$"),
    "2": ("GBP", "British Pound", "£"),
    "3": ("EUR", "Euro", "€"),
    "4": ("JPY", "Japanese Yen", "¥"),
    "5": ("AED", "UAE Dirham", "د.إ"),
}


def get_inr_rate(currency):
    """Fetch the latest available rate for 1 unit of currency in INR."""
    response = requests.get(
        API_URL.format(currency),
        timeout=15
    )
    response.raise_for_status()

    data = response.json()

    if data.get("result") != "success":
        raise ValueError("The exchange-rate service returned an error.")

    rates = data.get("rates", {})
    inr_rate = rates.get("INR")

    if inr_rate is None:
        raise ValueError("INR rate was not available.")

    return inr_rate, data.get("time_last_update_utc", "Not provided")


def main():
    print("=" * 48)
    print("       CURRENCY CONVERTER TO INDIAN RUPEES")
    print("=" * 48)

    while True:
        print("\nChoose a currency to convert into INR:")

        for key, (code, name, symbol) in CURRENCIES.items():
            print(f"{key}. {name} ({code}, {symbol})")

        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("Thank you for using Currency Converter!")
            break

        if choice not in CURRENCIES:
            print("Invalid choice. Please select 0 to 5.")
            continue

        currency, name, symbol = CURRENCIES[choice]

        try:
            amount = float(
                input(f"Enter amount in {currency}: ").strip()
            )

            if not 0 < amount < float("inf"):
                print("Please enter a positive, finite amount.")
                continue

            rate, updated_at = get_inr_rate(currency)
            result = amount * rate

            print("\n" + "-" * 48)
            print(f"Currency       : {name} ({currency})")
            print(f"Exchange rate  : 1 {currency} = ₹{rate:,.4f}")
            print(f"Amount entered : {symbol}{amount:,.2f}")
            print(f"Converted value: ₹{result:,.2f}")
            print(f"Rate updated   : {updated_at}")
            print("-" * 48)

        except ValueError as error:
            print(f"Input or data error: {error}")
        except requests.exceptions.RequestException:
            print(
                "Could not retrieve exchange rates. "
                "Check your internet connection and try again."
            )


if __name__ == "__main__":
    main()