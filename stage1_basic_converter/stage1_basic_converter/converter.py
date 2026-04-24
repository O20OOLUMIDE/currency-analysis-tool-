# Analysis currency converter tool - Stage 1
# This program converts an amount in GBP (British Pounds)
# into either USD (US Dollars) or EUR (Euros)


def currency_converter():
    """
    This subroutine asks the user:
    1) Which currency they want to convert into GBP into(USD or EUR)
    2) How much GBP they want to convert
    Then it calculates and displays the result.
    The user can then repeat conversions or exit the program
    """

    # Fixed exchange rates(these are example values, not live market rates)
    USD_exchange_rate = 1.25
    EUR_exchange_rate = 1.15

    # A friendly welcome message for the user
    print("Welcome to the Currency Converter Analysis Tool!")
    print("We allow conversion from GBP to USD or EUR.")
    print("Type `Q` at any time when choosing a currency to quit.\n")

    # loop to allow the user to perform multiple conversions
    while True:
        # Ask the user which currency they want to convert to
        choice = input("What currency do you want your money converted to?")

        # Remove extra spaces and make user input uppercase
        choice = choice.strip().upper()

        # If the user types Q, we break out of loop
        if choice == "Q":
            print("Exiting the converter. Thank you for using the tool!")
            break

        # If the user doesnt provide required input we tell them its invalid
        if choice != "USD" and choice != "EUR":
            print("Invalid choice. Input allowed includes USD/Q/EUR only")
            continue

        # Ask the user for amount in GBP
        amount_text = input("Enter the amount in GBP you want converted: ")

        # Try to convert the text input into a number
        try:
            GBP = float(amount_text)
        except ValueError:
            # If user types something that is not a number
            print("That is not a valid number. Please try again. \n")
            continue # goes back to the top of the loop



        if choice == "USD":
            converted_amount = GBP * EUR_exchange_rate
            print(f"£{GBP:.2f} is equal to €{converted_amount:.2f}\n")

        elif choice == "USD":
            converted_amount = GBP * EUR_exchange_rate
            print(f"£{GBP:.2f} is equal to €{converted_amount:.2f}\n")

            # When the loop ends after user choose Q, the function finishes


# Main program
currency_converter()
