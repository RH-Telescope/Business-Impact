#Create filename and validate input
while True:
    filename = input("Business Criticality Assessment: ")
    if filename:
        break
    else:
        print("Please enter a valid filename.")

# Inquire about BCA status and assign score
while True:
    bca_answer = input("Is this a business critical application? (yes or no) ")
    if bca_answer.lower() in ['yes', 'no']:
        bca_score = 10 if bca_answer.lower() == 'yes' else 1
        break
    else:
        print("Please enter a valid response (yes or no).")

# Ask about financial unit of measurement
while True:
    unit_answer = input("What is the financial unit of measurement? ")
    try:
        unit_factor = float(input(f"Enter the conversion factor for {unit_answer} to dollars (e.g., 1000): "))
        break
    except ValueError:
        print("Please enter a valid number.")

# Prompt the user to enter relevant data for each field
while True:
    critical_risk = input("Enter the amount of financial damage which is greater than a 'critical' risk: ")
    if critical_risk.startswith(">"):
        try:
            critical_risk_val = float(critical_risk[1:])
            if unit_answer.upper() == 'K':
                critical_risk_val *= 1000
            elif unit_answer.upper() == 'M':
                critical_risk_val *= 1000000
            break
        except ValueError:
            print("Please enter a valid number (e.g., 10.0).")
    else:
        print("Please enter a valid value (e.g., >10.0).")

while True:
    low_risk = input("Enter the amount of financial damage which is less than a 'low' risk: ")
    if low_risk.startswith("<"):
        try:
            low_risk_val = float(low_risk[1:])
            if unit_answer.upper() == 'K':
                low_risk_val *= 1000
            elif unit_answer.upper() == 'M':
                low_risk_val *= 1000000
            break
        except ValueError:
            print("Please enter a valid number (e.g., 10.0).")
    else:
        print("Please enter a valid value (e.g., <10.0).")

while True:
    important_risk = input("Enter the range of financial damage you consider equivalent to an 'important' risk: ")
    if "-" in important_risk and important_risk.count("-") == 1:
        try:
            important_risk_low, important_risk_high = map(float, important_risk.split("-"))
            if unit_answer.upper() == 'K':
                important_risk_low *= 1000
                important_risk_high *= 1000
            elif unit_answer.upper() == 'M':
                important_risk_low *= 1000000
                important_risk_high *= 1000000
            if important_risk_low < important_risk_high and important_risk_high <= critical_risk_val:
                break
            else:
                print("Please enter a valid range (e.g., 10.0-20.0 with low < high and high <= critical_risk_val).")
        except ValueError:
            print("Please enter a valid range (e.g., 10.0-20.0).")
    else:
        print("Please enter a valid range (e.g., 10.0-20.0).")

while True:
    moderate_risk = input("Enter the range of financial damage you consider equivalent to a 'moderate' risk: ")
    if "-" in moderate_risk and moderate_risk.count("-") == 1:
        try:
            low, high = map(float, moderate_risk.split("-"))
            if unit_answer.upper() == 'K':
                low *= 1000
                high *= 1000
            elif unit_answer.upper() == 'M':
                low *= 1000000
                high *= 1000000
            if low < high and high <= important_risk_high:
                break
            else:
              print("Please enter a valid range (e.g., 10.0-20.0 with low < high and high <= important_risk_high).")
        except ValueError:
            print("Please enter a valid range (e.g., 10.0-20.0).")
    else:
        print("Please enter a valid range (e.g., 10.0-20.0).")

# Define a dictionary to map string values to numerical scores
score_mapping = {
    'yes': 10,
    'no': 1,
    'critical': 10,
    'important': 7,
    'moderate': 4,
    'low': 1
}

# Write the data to a text file with numerical scores
with open(f"{filename}.txt", "w") as f:
    f.write(f"bca: {bca_answer} ({score_mapping[bca_answer.lower()]})\n")
    f.write(f"unit: {unit_answer}\n")
    f.write(f"critical: {critical_risk_val} ({score_mapping['critical']})\n")
    f.write(f"important: {low}-{high} ({score_mapping['important']})\n")
    f.write(f"moderate: {low}-{high} ({score_mapping['moderate']})\n")
    f.write(f"low: {low_risk_val} ({score_mapping['low']})\n")

print(f"Data saved to {filename}.txt successfully!")
