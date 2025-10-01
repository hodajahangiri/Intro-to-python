# Movie Ticket Pricing
ticket_type = ""
total_cost = 0
ticket_price = 0

try:
    customer_name = input("Enter your name: ")
    customer_age = int(input("Enter your age: "))
    number_of_ticket = int(input("How many tickets do you want? " ))
    if number_of_ticket == 0:
        print("Number of ticket can not be 0, try again...")
    elif customer_age < 0:
        print("Age can not be under 0, try again...")
    elif customer_age < 13:
        ticket_price = 8
        ticket_type = "Child"
    elif 13 <= customer_age <= 64:
        ticket_price = 12
        ticket_type = "Adult"
    else:
        ticket_price = 9
        ticket_type = "Senior"

    total_cost = number_of_ticket * ticket_price
    if total_cost != 0:
        print("=== MOVIE TICKET RECEIPT ===")
        print(f"Customer: {customer_name}")
        print(f"Ticket Type: {ticket_type} (${ticket_price} each)")
        print(f"Quantity: {number_of_ticket}")
        print(f"Total Cost: ${total_cost}")
        print("Thank you for your purchase!")

except ValueError:
    print("Please Enter valid  age and number of tickets...")
except Exception as e:
    print(f"Something unexpected happens, ERROR: {e}")