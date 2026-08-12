input_weight = float(input("Enter your weight on Earth: "))
(earth_weight) = input_weight
input_destination = input("Enter your destination (moon, mars, jupiter): ")

def calculate_space_weight(earth_weight, destination):
    if destination == "moon":
        return earth_weight * 0.16
    elif destination == "mars": 
        return earth_weight * 0.38
    elif destination == "jupiter":
        return earth_weight * 2.34 
    else:
        print("Invalid destination. Please enter 'moon', 'mars', or 'jupiter'.")
        return None

print("Your weight on", input_destination, "is:", calculate_space_weight(earth_weight, input_destination))