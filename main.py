filename = input("Business Criticality Assessment: ")

# Inquire about BCA status
while True:
    bca_answer = input("Is this a business critical application? (yes or no) ")
    if bca_answer.lower() in ['yes', 'no']:
        break
    else:
        print("Please enter a valid response (yes or no).")

# Ask about financial unit of measurement
while True:
    unit_answer = input("Is the financial damage measured in thousands or millions of dollars? (K or M) ")
    if unit_answer.upper() in ['K', 'M']:
        break
    else:
        print("Please enter a valid response (K or M).")

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
            low, high = map(float, important_risk.split("-"))
            if unit_answer.upper() == 'K':
                low *= 1000
                high *= 1000
            elif unit_answer.upper() == 'M':
                low *= 1000000
                high *= 1000000
            if low < high:
                break
            else:
                print("Please enter a valid range (e.g., 10.0-20.0 with low < high).")
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
            if low < high:
                break
            else:
              print("Please enter a valid range (e.g., 10.0-20.0 with low < high).")
        except ValueError:
            print("Please enter a valid range (e.g., 10.0-20.0).")
    else:
        print("Please enter a valid range (e.g., 10.0-20.0).")
# Write the data to a text file
with open(f"{filename}.txt", "w") as f:
    f.write(f"BCA: {bca_answer}\n")
    f.write(f"financial unit: {unit_answer}\n")
    f.write(f"critical: {critical_risk_val}\n")
    f.write(f"important: {low}-{high}\n")
    f.write(f"moderate: {low}-{high}\n")
    f.write(f"low: {low_risk_val}\n")

print(f"Data saved to {filename}.txt successfully!")
