filename = input("Business Criticality Assessment: ")

# Inquire about BCA status
bca_answer = input("Is this a business critical application? (yes or no) ")


# Prompt the user to enter relevant data for each field
critical_risk = input("Enter the amount of financial damage which is equal or greater to a 'critical' risk: ")
important_risk = input("Enter the range of financial damage you consider equivalent to an 'important' risk: ")
moderate_risk = input("Enter the range of financial damage you consider equivalent to a 'moderate' risk: ")
low_risk = input("Enter the amount of financial damage which is equal or less than a 'low' risk: ")

# Write the data to a text file
with open(f"{filename}.txt", "w") as f:
    f.write(f"bca: {bca_answer}\n")
    f.write(f"critical: {critical_risk}\n")
    f.write(f"important: {important_risk}\n")
    f.write(f"moderate: {moderate_risk}\n")
    f.write(f"low: {low_risk}\n")

print(f"Data saved to {filename}.txt successfully!")