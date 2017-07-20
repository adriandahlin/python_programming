import csv

csv_file_path = "data/products.csv"

rows = []

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    for row in reader:
        rows.append(row)

menu = '''
HELLO. YOU'RE THE BEST.

There are {0} products.

Please pick one of these five operations that you may conduct on these products:
(case sensitive)
- List
- Show
- Create
- Update
- Destroy
'''.format(len(rows))

operations = ["List", "list", "Show", "show", "Create", "create", "Update", "update", "Destroy", "destroy"]

inp = input(menu)

def list_products():
    print("You are listing a product or products.")

def show_product():
    print("You are showing a product.")

def create_product():
    print("creating a product")
#    product_id = input("Enter the product's id:")
    product_name = input("Enter the product's name:")
    product_aisle = input("Enter the aisle where the product sits:")
    product_department = input("Enter the department the product is in:")
    product_price = input("Enter the product's price:")
    new_product = {
        "id": len(rows) + 1,
        "name": product_name.title(),
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
        writer.writerow(new_product)

def update_product():
    print("You are updating a product.")

def destroy_product():
    print("You are destroying a product.")

def handler():
    if inp == "List":
        print(list_products())
    if inp == "Show":
        print(show_product())
    if inp == "Create":
        create_product()
    if inp == "Update":
        print(update_product())
    if inp == "Destroy":
        print(destroy_product())
    if inp not in operations:
        print("Unrecognized Operation. Please choose one of: 'List', 'Show', 'Create', 'Update', or 'Destroy'.")

handler()

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
   for row in reader:
        print(row["id"], row["name"], row["aisle"], row["department"], row["price"])
