
import sys


units = 150


rate_per_unit = 5


bill_amount = units * rate_per_unit

# Display the results using sys.stdout.write
sys.stdout.write(f"Electricity Bill Details:\n")
sys.stdout.write(f"Units Consumed : {units}\n")
sys.stdout.write(f"Rate per Unit  : ₹{rate_per_unit}\n")
sys.stdout.write(f"Total Bill     : ₹{bill_amount}\n")
