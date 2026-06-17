# Currency converter system - Stage 4

import requests
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


# SUBROUINE TO SILENCE READ LOG FUNCTION
def read_log_file_silent():
    try:
        with open("conversions.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
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


# SUBROUTINE THAT EXTRACTS EXCHANGE RATES FROM THE LOG FILE
def extract_rates_from_log(lines):
    rates = []

    for line in lines:
        try:
            # Extract GBP amount
            gbp_part = line.split("£")[1]
            gbp_value = float(gbp_part.split()[0])

            # Extract converted amount (after ->)
            right_side = line.split("->")[1].strip()
            converted_str = right_side[1:] # remove currency symbol
            converted_value = float(converted_str)

            # Calculate rate
            rate = converted_value / gbp_value
            rates.append(rate)

        except (IndexError, ValueError):
            continue # skip badly formatted lines

    return rates 


# SUBROUTINE TO CALCULATE STATISTICS FOR EXCHANGE RATES
def calculate_rate_statistics(rates):
    if len(rates) < 2:
        return None # not enouh data to analyse

    highest = max(rates)
    lowest = min(rates)
    average = sum(rates) / len(rates)

    # Percentage change from first to last
    percent_change = ((rates[-1] - rates[0]) / rates[0]) * 100

    # Standard deviation
    mean = average
    variance = sum((r - mean) ** 2 for r in rates) / len(rates)
    std_dev = variance ** 0.5

    return {
        "highest": highest,
        "lowest": lowest,
        "average": average,
        "percent_change": percent_change,
        "std_dev": std_dev
    }


# SUBROUTINE TO DETERMINE TREND OF EXCHANGE RATES
def determine_rate_trend(rates):
    if len(rates) < 2:
        return "Not enough data"

    start = rates[0]
    end = rates[-1]

    change = end - start

    if abs(change) < 0.01:
        return "Relatively Stable"
    elif change > 0:
        return "Increasing"
    else:
        return "Decreasing"


# SUBROUTINE TO DISPLAY ANALYSIS OF EXCHANGE RATES
def show_rate_analysis():
    lines = read_log_file_silent()

    if not lines:
        print("\nNo log data available to analyse, \n")
        return

    rates = extract_rates_from_log(lines)

    if len(rates) < 2:
        print("\nNot enough rate data to analyse trends.\n")
        return

    stats = calculate_rate_statistics(rates)
    trend = determine_rate_trend(rates)

    print("\n--- Exhange Rate Analsis ---")
    print(f"Highest Rate: {stats['highest']:.4f}")
    print(f"Lowest Rate: {stats['lowest']:.4f}")
    print(f"Average Rate: {stats['average']:.4f}")
    print(f"Percentage Change: {stats['percent_change']:.2f}%")
    print(f"Standard Deviation: {stats['std_dev']:.4f}")
    print(f"Trend: {trend}")
    print("--------------------------------\n")
    
          

    


# SUBROUTINE THAT CALCULATES LONG-TERM ANALYSIS FROM THE LOG FILE
def calculate_log_analytics():
    lines = read_log_file()

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
        currency_count[symbol] = currency_count.get(symbol, 0) + 1

    most_popular = max(currency_count, key=currency_count.get)

    # Output results
    print("\n--- Log File Analytics (All Sessions) ---")
    print(f"Highest GBP ever converted : £{highest:.2f}")
    print(f"Lowest GBP ever converted: £{lowest:.2f}")
    print(f"Average GBP across all sessions: £{average:.2f}")
    print(f"Most popular currency overall: {most_popular}")
    print("-----------------------------------------\n")


# SUBROUTINE TO DELETE FILES CONTENT
def clear_log_file():
    confirm = input("Re you sure you want to clear the log file? (Y/N): ").strip().upper()

    if confirm == "Y":
        with open("conversions.txt", "w") as file:
            file.write("") # wipe the file
        print("Log file has been cleared.\n")
    else:
        print("Log file was NOT cleared.\n") 
        
        

# SUBROUTINE TO GET LIVE EXCHANGE RATES
def get_live_rates():
    try:
        response = requests.get("https://api.frankfurter.app/latest?from=GBP")
        data = response.json()
        return data["rates"]
    except:
        print("Could not fetch live exchange rates. Using fallback rates.\n")
        return {
            "USD": 1.25, 
            "EUR": 1.15, 
            "JPY": 212
        }
    


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
    live_rates = get_live_rates() # Fetch live exchange rates

    # Task 1: Dictionary for exchange rates
    currency_info = {
        "USD": {"rate": live_rates["USD"], "symbol": "$"}, 
        "EUR": {"rate": live_rates["EUR"], "symbol": "€"}, 
        "JPY": {"rate": live_rates["JPY"],  "symbol": "¥"}
    }

    conversions = 0  # counter
    highest_gbp = 0
    lowest_gbp = None
    total_gbp = 0
    
    print("__________________________________________")
    print("Currency Converter Analysis Tool - Stage 5")
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
                       " •4 - View log analytics\n"
                       " •5 - Clear log file\n"
                       " •6 - View exchange rate analysis\n"
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

        if choice == "4":
            print("\nLoading analytics...\n")
            calculate_log_analytics()
            continue

        if choice == "5":
            print("\nClearing log file...\n")
            clear_log_file()
            continue

        if choice == "6":
            print("\nLoading exchange rate analysis...\n")
            show_rate_analysis()
            continue

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
