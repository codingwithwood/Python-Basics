#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = $33.60

print("Welcome to the tip calculator!")
total_bill = float(input("How much was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill_with_tip = tip / 100 * total_bill + total_bill
total_each_person = total_bill_with_tip / people
formatted_total = "{:.2f}".format(total_each_person)

print(f"Each person should pay: ${formatted_total}")
