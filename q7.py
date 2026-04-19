#Q7. Simple Interest Using Function
#Create a function to calculate Simple Interest.

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Main program
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (per annum): "))
time = float(input("Enter time period (in years): "))

# Calculate simple interest
si = calculate_simple_interest(principal, rate, time)
amount = principal + si

# Display results
print("\n--- Simple Interest Calculator ---")
print(f"Principal: ₹{principal:.2f}")
print(f"Rate: {rate}% per annum")
print(f"Time: {time} years")
print(f"Simple Interest: ₹{si:.2f}")
print(f"Total Amount: ₹{amount:.2f}")