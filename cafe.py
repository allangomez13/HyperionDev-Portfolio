#Menu that stores list of food for cafe
menu = ['Coffee Cake', 'Carrot Cake', 'Cupcakes', 'Brownies']

#Dictionary called stock that contains stock value for each item on the menu
stock = {'Coffee Cake': 25,
         'Carrot Cake': 20,
         'Cupcakes': 18,
         'Brownies': 10
         }

#Contains the prices for each item on the menu
price = {'Coffee Cake': 3.00,
         'Carrot Cake': 3.00,
         'Cupcakes': 2.00,
         'Brownies': 2.50
         }

#calculates the total_stock worth in the cafe as well as lojops through the dictionary list
total = 0
for food in menu:                        
    total += stock[food] * price[food]

#Prints out the total worth of stock
print("The total worth of stock is : " + (str(total)))