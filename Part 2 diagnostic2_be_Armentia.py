pepperoni = input("Do you want Pepperoni? (yes/no): ")
mushrooms = input("Do you want Mushrooms? (yes/no): ")
extra_cheese = input("Do you want Extra Cheese? (yes/no): ")
(input_toppings) = 0
if pepperoni == "yes":
    input_toppings += 1
if mushrooms == "yes": 
    input_toppings += 1
if extra_cheese == "yes": 
    input_toppings += 1  

def calculate_total(input_toppings):
    base_price = 10.00
    topping_price = 1.50
    total_price = base_price + (input_toppings * topping_price)
    return total_price
total_price = calculate_total(input_toppings)
print(f"Total price: ${total_price}")
