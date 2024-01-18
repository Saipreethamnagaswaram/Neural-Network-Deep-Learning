1#
def inches_to_cm(height_in_inches):
    return height_in_inches * 2.54
num_customers = int(input("Enter the number of customers: "))
heights_inches = []
heights_cm = []

for i in range(num_customers):
    height = float(input(f"Enter height (in inches) for customer {i + 1}: "))
    heights_inches.append(height)
    heights_cm.append(inches_to_cm(height))
print("Heights in centimeters:", heights_cm)

2#   
def inches_to_cm(height_in_inches):
    return height_in_inches * 2.54
num_customers = int(input("Enter the number of customers: "))
heights_inches = [float(input(f"Enter height (in inches) for customer {i + 1}: ")) for i in range(num_customers)]
heights_cm = [inches_to_cm(height) for height in heights_inches]
print("Heights in centimeters:", heights_cm)