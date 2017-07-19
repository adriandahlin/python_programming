import csv

# print('''
# HELLO. YOU'RE THE BEST.
#
# There are 1,000,000 products.
#
# Please pick one of these five operations that you may conduct on these products:
# (case sensitive)
# - List
# - Show
# - Create
# - Update
# - Destroy
# ''')

operations = ["List", "list", "Show", "show", "Create", "create", "Update", "update", "Destroy", "destroy"]

#inp = input("Type operation here:")

def list_products():
    print("You have selected the", inp, "operation.")

def show_product():
    print("You have selected the", inp, "operation.")

def create_product():
    print("You have selected the", inp, "operation.")
    #name = input("Enter the product's name:")
    #department = input("Enter the department the product is in:")
    #aisle = input("Enter the aisle where the product sits:")
    #price = input("Enter the product's price:")
    #ident

def update_product():
    print("You have selected the", inp, "operation.")

def destroy_product():
    print("You have selected the", inp, "operation.")

def handler(inp):
    if inp == "List":
        print(list_product(inp))
    if inp == "Show":
        print(show_product(inp))
    if inp == "Create":
        create_product(inp)
    if inp == "Update":
        print(update_product(inp))
    if inp == "Destroy":
        print(destroy_product(inp))
    if inp not in operations:
        print("Unrecognized Operation. Please choose one of: 'List', 'Show', 'Create', 'Update', or 'Destroy'.")

#print(handler(inp))

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    for row in reader:
         print(row["name"])

#with open(csv_file_path, "r") as csv_file:
    #reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    #for row in reader:
        #print(row["id"], row["name"], row["aisle"], row["department"], row["price"])
