# Currency converter system - STAGE 3 


from datetime import datetime

# SUBROUTINE TO LOG EACH CONVERSION WITH A TIMESTAMP
def log_conversion(GBP, converted_amount, symbol):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")

    with open("conversions.txt", "a") as file:
        file.write(f"{timestamp} - £{GBP:.2f} -> {symbol}{converted_amount:.2f}\n")


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


# SUBROUTINE FOR CURRENCY CONVERSION
def convert(GBP, rate):
    return GBP * rate


# SUBROUTINE TO PRINT RESULT
def output_result(GBP, converted_amount, symbol):
    print(f"£{GBP:.2f} is equal to {symbol}{converted_amount:.2f}\n")



# MAIN CURRENCY CONVERTER
def currency_converter():

    # Task 1: Dictionary for exchange rates
    currency_info = {
        "USD": {"rate": 1.25, "symbol": "$"}, 
        "EUR": {"rate": 1.15, "symbol": "€"}, 
        "JPY": {"rate": 212,  "symbol": "¥"}
    }

    conversions = 0  # counter
    highest_gbp = 0
    lowest_gbp = None
    total_gbp = 0
    
    print("__________________________________________")
    print("Currency Converter Analysis Tool - Stage 3")
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
                       "Either enter your choice or type Q to quit: "
        )
        choice = choice.strip().upper()

        if choice == "Q":
            print() # blank line for spacing
            print(f"You performed {conversions} conversions today.")
            print(f"Highest GBP converted this session: £{highest_gbp:.2f}")
            print(f"Lowest GBP converted this session: £{lowest_gbp:.2f}")
            
            if conversions > 0:
                average_gbp = total_gbp / conversions
                print(f"Average GBP converted this session: £{average_gbp:.2f}")

            print()
            print("Exiting the converter. Thank you for using the tool!")
            
            break

        if choice not in currency_info:
            print("That option isn’t recognised. Please choose one of the suggested inputs.\n")
            continue

        # Usage of the GBP validation subroutine
        GBP = validate_gbp()
        
        if GBP > highest_gbp:
            highest_gbp = GBP

        if lowest_gbp is None or GBP < lowest_gbp:
            lowest_gbp = GBP

        total_gbp += GBP

        
        conversions += 1
        

        rate = currency_info[choice]["rate"]
        symbol = currency_info[choice]["symbol"]

        converted_amount = convert(GBP, rate)
        output_result(GBP, converted_amount, symbol)
        log_conversion(GBP, converted_amount, symbol) 


# Main program
currency_converter()   
