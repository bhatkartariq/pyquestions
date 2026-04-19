#Q2. Electricity Bill Calculator (Slab Based)
#Calculate electricity bill using slabs:
#First 100 units → ₹5/unit
#Next 100 units → ₹7/unit
#Above 200 units → ₹10/unit

# Input units consumed
units = float(input("Enter the number of units consumed: "))

# Calculate bill based on slabs
bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Display results
print("\n--- Electricity Bill ---")
print(f"Units Consumed: {units}")
print(f"Total Bill: ₹{bill:.2f}")