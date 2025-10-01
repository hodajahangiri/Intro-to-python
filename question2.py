# Restaurant Order System 
print("=== Restaurant Menu ===")
print("1. Pizza - $15.99")
print("2. Burger - $12.50")
print("3. Salad - $9.99")
print("4. Pasta - $13.75")

try:
    choice = int(input("Enter your choice (1-4): "))
    drink_choice = input("Would you like a drink? (+$2.50) (yes/no): ")
    drink_price = 0
    food_name = ""
    food_price = 0
    subtotal = 0
    tax = 0
    total_price = 0

    if choice < 1 or choice > 4:
        print("wrong choice, Choose (1-4)...")
        exit()
    else:
        if drink_choice.lower() != "yes" and drink_choice.lower() != "no":
            print("for drink say yes or no...")
            exit()
        elif drink_choice.lower() == "yes":
            drink_price = 2.50
    if choice == 1:
        food_price = 15.99
        food_name = "Pizza"
    elif choice == 2:
        food_price = 12.50
        food_name = "Burger"
    elif choice == 3:
        food_price = 9.99
        food_name = "Salad"
    else:
        food_price = 13.75
        food_name = "Pasta"
    
    subtotal = food_price + drink_price
    tax = subtotal * 0.08
    total_price = subtotal + tax
    print("=== YOUR ORDER ===")
    print(f"Food: {food_name} - ${food_price}")
    print(f"Drink: {drink_choice.upper()} - ${drink_price}")
    print(f"Subtotal: ${round(subtotal, 2)}")
    print(f"Tax (8%): ${round(tax, 2)}")
    print(f"Total: ${round(total_price, 2)}")

except ValueError:
    print("Please Enter valid number for choice...")
except Exception as e:
    print(f"Something unexpected happens, ERROR: {e}")