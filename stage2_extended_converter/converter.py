# Stage 2 → Tasks 1 & 2 Completed
# Dictionary for rates + GBP validation subroutine


# SUBROUTINE TO VALIDATE USER INPUT
def validate_gbp():
    """
    Asks the user for a GBP amount.
    Ensures the input is a positive number.
    Returns the valid GBP value.
    """

    while True:
        amount_text = input("Enter the amount in GBP you want converted(positive numbers only): ")

        try:
            GBP = float(amount_text)

            if GBP <= 0:
                print("Please enter a positive number.\n")
                continue

            return GBP   # SUCCESS → return valid number

        except ValueError:
            print("That is not a valid number. Please try again.\n")



# MAIN CURRENCY CONVERTER
def currency_converter():

    # Task 1: Dictionary for exchange rates
    rates = {
        "USD": 1.25,
        "EUR": 1.15,
        "JPY": 212
    }

    conversions = 0  # counter
    print("__________________________________________")
    print("Currency Converter Analysis Tool - Stage 2")
    print("__________________________________________")
    print("Convert GBP into USD, EUR, or JPY.") 
    print("You can perform as many conversions as you like.")
    print("Type 'Q' at any time when choosing a currency to exit program.\n")

    while True:
        choice = input(
                       "Choose a currency to convert your GBP into:\n"
                       " •USD - US Dollars\n"
                       " •EUR - Euros\n"
                       " •JPY - Japanese Yen\n"
                       "Either enter your choice (or type Q to quit): "
        )
        choice = choice.strip().upper()

        if choice == "Q":
            print(f"You performed {conversions} conversions today.")
            print("Exiting the converter. Thank you for using the tool!")
            break

        if choice not in rates:
            print("That option isn’t recognised. Please choose one of the suggested inputs.\n")
            continue

        # Usage of the GBP validation subroutine
        GBP = validate_gbp()

        conversions += 1

        converted_amount = GBP * rates[choice]

        # Output result
        if choice == "USD":
            print(f"£{GBP:.2f} is equal to ${converted_amount:.2f}\n")

        elif choice == "EUR":
            print(f"£{GBP:.2f} is equal to €{converted_amount:.2f}\n")

        elif choice == "JPY":
            print(f"£{GBP:.2f} is equal to ¥{converted_amount:.2f}\n")



# Run the program
currency_converter()
