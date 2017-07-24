import csv

csv_file_path = "data/products.csv"

rows = []

# creating a list of all product ids
# product_ids = []
# with open(csv_file_path, "r") as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         products_ids.append(row["id"])

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
    print("Your list of products:")
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row["id"], row["name"], row["aisle"], row["department"], row["price"])

def show_product():
    search_id = input("Enter the product's ID:")
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        product_ids = []
        for row in reader:
            product_ids.append(row["id"])
            if search_id == row["id"]:
                print(row["id"], row["name"], row["aisle"], row["department"], row["price"])
        if search_id not in product_ids:
            print("We're sorry, we couldn't find that product ID.")

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
    print("--------")
    print("See the inventory below including your added product:")
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row["id"], row["name"], row["aisle"], row["department"], row["price"])

def update_product():
    update_id: input("Enter the ID of the product you'd like to update:")
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if update_id == row["id"]:
                print("The current info is:")
                print(row["id"], row["name"], row["aisle"], row["department"], row["price"])


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
