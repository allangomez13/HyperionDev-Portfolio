
# Calculates the total cost for each night
def hotel_cost(num_nights):
    return num_nights * 100  

# Calculates the total cost of plane tickets
def plane_cost(city_flight):
    if city_flight == "New York":
        return 500
    elif city_flight == "London":
        return 700
    elif city_flight == "Paris":
        return 600
    else:
        return 0

# Calculates the total cost of length of renting a car
def car_rental(rental_days):
    return rental_days * 50

# Calculates all 3 inputs above and returns a overall cost for the holiday
def holiday_cost(city_flight, num_nights, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost


# Asks the user to input destination, number of nights and length of car rental days.
city_flight = input("Which city are you flying to? ")
num_nights = int(input("How many nights are you staying at the hotel? "))
rental_days = int(input("How many days are you renting a car? "))

print("Holiday Details")
print("City Flight: " + city_flight)
print("Number of Nights: " + str(num_nights))
print("Number of Rental Days: " + str(rental_days))
print("Total Cost: " + str(holiday_cost(city_flight, num_nights, rental_days)))