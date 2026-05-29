# Currency converter system 


from datetime import datetime

# SUBROUTINE TO LOG EACH CONVERSION WITH A TIMESTAMP
def log_conversion(GBP, converted_amount, symbol):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")

    with open("conversions.txt", "a") as file:
        file.write(f"{timestamp} - £{GBP:.2f} -> {symbol}{converted_amount:.2f}\n")


# SUBROUTINE THAT READS THE CONVERSIONS.TXT LOG FILE AND RETURNS ALL SAVED CONVERSIONS LINES
def read_log_file():
    try:
        with open("conversions.txt", "r") as file:
            lines = file.readlines()

        print("\n--- Log file contents ---")
        for line in lines:
            print(line.strip())

        return lines


    except FileNotFoundError:
        print("No log file found yet. Do some conversions first!")
        return []


# SUBROUTINE THAT EXTRACTS ALL GBP VALUES FROM THE LOG FILE AND RETURNS AS FLOATS
def extract_gbp_from_log(lines):
    gbp_values = []

    for line in lines:
        try:
            parts = line.split("£")[1]  # everything after the £
            gbp_str = parts.split()[0]  # first number after £
            gbp_value = float(gbp_str)  # convert to float 
            gbp_values.append(gbp_value)

        except (IndexError, ValueError):
            continue # skip badly formatted lines

    return gbp_values


# SUBROUTINE THAT EXTRACTS ALL CURRENCY SYMBOLS FROM THE LOG FILE (e.g., $, €, ¥)
def extract_currencies_from_log(lines):
    currencies = []

    for line in lines:
        try:
            # Split at the arrow -> and take the right side
            right_side = line.split("->")[1]

            # Split by space and take the first chunk (e.g., "$140.00")
            currency_chunk = right_side.split()[0]

            # The first character of that chunk is the currency symbol
            currency_symbol = currency_chunk[0]

            currencies.append(currency_symbol)

        except (IndexError, ValueError):
            continue

    return currencies


# SUBROUTINE THATAT CALCULATES LONG-TERM ANALYSIS FROM THE LOG FILE
def calculate_log_analytics():
    lines = read_log_files()

    if not lines:
        print("\nNo log data available to analyse.\n")
        return

    # Extract data
    gbp_values = extract_gbp_from_log(lines)
    currencies = extract_currencies_from_log(lines)

    if not gbp_values:
        print("\nLog file exists but contains no valid GBP data.\n")
        return

    # GBP analytics
    highest = max(gbp_values)
    lowest = min(gbp_values)
    average = sum(gbp_values) / len(gbp_values)

    # Currency popularity
    currency_count = {}
    for symbol in currencies:
        currency_count[symbol} = currency_count.get(symbol, 0) + 1

    most_popular = max(currency_count, key=currency_count.get)

    # Output results
    print("\n--- Log File Analytics (All Sessions) ---")
    print(f"Highest GBP ever converted : £{highest:.2f}")
    print(f"Lowest GBP ever converted: £{lowest:.2f}")
    print(f"Average GBP across all sessions: £{average:.2f}")
    print(f"Most popular currency overall: {most_popular}")
    print("-----------------------------------------\n")
    


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
