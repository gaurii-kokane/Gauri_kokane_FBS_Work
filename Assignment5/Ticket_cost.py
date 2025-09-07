passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter ticket cost: "))
total = 0

for i in range(passengers):
    age = int(input(f"Enter age of passenger {i+1}: "))
    if age < 12:
        total += ticket_cost * 0.7
    elif age > 59:
        total += ticket_cost * 0.5
    else:
        total += ticket_cost

print("Total Ticket Cost =", total)
