# Analysis currency converter tool - Stage 1
# This program converts an amount in GBP (British Pounds)
# into either USD (US Dollars), EUR (Euros), or JPY (Japanese Yen)

def currency_converter():

    # Fixed exchange rates (example values, not live market rates)
    USD_exchange_rate = 1.25
    EUR_exchange_rate = 1.15
    JPY_exchange_rate = 212
    conversions = 0

    # A friendly welcome message for the user
    print("Welcome to the Currency Converter Analysis Tool!")
    print("We allow conversion from GBP to USD, EUR and JPY.")
    print("Type 'Q' at any time when choosing a currency to quit.\n")

    # Loop to allow the user to perform multiple conversions
    while True:
        # Ask the user which currency they want to convert to
        choice = input("What currency do you want your money converted to? (USD/EUR/JPY or Q to quit): ")

        # Remove extra spaces and make user input uppercase
        choice = choice.strip().upper()

        # If the user types Q, we break out of loop
        if choice == "Q":
            print(f"You performed {conversions} conversions today.")
            print("Exiting the converter. Thank you for using the tool!")
            break

        # If the user doesn't provide required input we tell them it's invalid
        if choice not in ["USD", "EUR", "JPY"]:
            print("Invalid choice. Input allowed includes USD, EUR, JPY or Q only.\n")
            continue

        # Ask the user for amount in GBP
        amount_text = input("Enter the amount in GBP you want converted: ")

        # Try to convert the text input into a number
        try:
            GBP = float(amount_text)
            if GBP <= 0:
                print("Please enter a positive number.\n")
                continue
        except ValueError:
            print("That is not a valid number. Please try again.\n")
            continue

        # Count the conversion
        conversions += 1

        # Perform the conversion based on the chosen currency
        if choice == "USD":
            converted_amount = GBP * USD_exchange_rate
            print(f"£{GBP:.2f} is equal to ${converted_amount:.2f}\n")

        elif choice == "EUR":
            converted_amount = GBP * EUR_exchange_rate
            print(f"£{GBP:.2f} is equal to €{converted_amount:.2f}\n")

        elif choice == "JPY":
            converted_amount = GBP * JPY_exchange_rate
            print(f"£{GBP:.2f} is equal to ¥{converted_amount:.2f}\n")


# Call the function to run the program
currency_converter()
