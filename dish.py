menu = {
    "Pizza" : 50, 
    "Pasta" : 60, 
    "Coffee" : 80, 
    "Burger" : 78, 
    "Salad" : 50, 
    "Coldcoffe" : 969, 
    "Chilli potato" : 78, 
}

print("WELCOME TO SHIVAMS RESTAURENT")
print("Here is our menu:\n")
print("Pizza : 50\nPasta : 60\nCoffee : 80\nBurger : 78\nSalad : 50\nColdcoffe : 969\nChilli potato : 78\n")

order_total = 0

item_1 = input("Enter the name of item you want to buy = ")
if item_1 in menu :
    order_total += menu[item_1]
    print(f"Your {item_1} has been added to your order")
else:
    print(f"Order item {item_1} is not available yet")

another_order = input("Do you want to add another item ? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the namne of second item = ")
if item_2 in menu :
        order_total += menu[item_2]
        print(f"Your {item_2} has been added to your order")

else:
        
        print(f"Item {item_2} is not available")
print(f"The total ammount of the all items is {order_total}")

