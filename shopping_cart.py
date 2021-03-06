import time
import code
# code.interact(local=locals())

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]


var = 0
item_ids = []
product_ids = []
for product in products:
    product_ids.append(str(product["id"]))
while var == 0:
    num = input("Please input a product identifier or 'DONE' if there are no more items: ")
    if num in product_ids:
        item_ids.append(num)
    if num == 'DONE':
        break
    if num not in product_ids:
        print("Please check your product ID and try again.")

## Print Receipt
print('''------------
FOODS-R-US
Phone: (123) 456-7890
Purchase Time:''')
print(time.strftime("%H:%M:%S"), time.strftime("%d/%m/%Y"))
print("------------")

print("Items purchased today:")

#prints item names and prices,
# including an unwanted line with "None" after each item.
def id_to_name(id):
    for product in products:
        if product["id"] == int(id): # data type is important here
            print("+ " + product["name"] + " (${0:.2f})".format(product["price"]))
for item in item_ids:
    print(id_to_name(item))

# don't know why the following doesn't work:
#for product in products:
#    if product["id"] in item_ids:
#        print("+ " + product["name"] + " (${0:.2f}".format(product["price"]) + ")")

print("------------")

#prints sum of product prices
prices = []
def grab_price(id):
    for product in products:
        if product["id"] == int(id):
            prices.append(product["price"])
for item in item_ids:
    grab_price(item)
print("Subtotal:                     $" + str(sum(prices)))

#adds tax
tax = sum(prices) * 0.08875
total = sum(prices) * 1.08875
print("Tax at 8.875%:               " + " ${0:.2f}".format(tax))
print("Your total for today comes to" + " ${0:.2f}".format(total))

print('''------------
Thank you for shopping at Foods-R-Us!''')
