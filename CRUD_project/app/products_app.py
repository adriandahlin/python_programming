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
    update_id = input("Enter the ID of the product you'd like to update:")
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        product_ids = []
        for row in reader:
            product_ids.append(row["id"])
            if update_id == row["id"]:
                print("The current info for that product is:")
                print(row["id"], row["name"], row["aisle"], row["department"], row["price"])
                product_name = input("Enter the product's updated name:")
                product_aisle = input("Enter the updated aisle where the product sits:")
                product_department = input("Enter the updated department the product is in:")
                product_price = input("Enter the product's updated price:")
        with open(csv_file_path, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
            writer.writeheader()
            for row in rows:
                if update_id != row["id"]:
                    writer.writerow(row)
                if update_id == row["id"]:
                    row["name"] = product_name
                    row["aisle"] = product_aisle
                    row["department"] = product_department
                    row["price"] = product_price
                    writer.writerow(row)
                    for row in rows:
                        print("--------")
                        print("Here is your current inventory")
                        print(row["id"], row["name"], row["aisle"], row["department"], row["price"])
        if update_id not in product_ids:
            print("We're sorry, we couldn't find that product ID.")

def destroy_product():
    destroy_id = input("Enter the ID of the product you'd like to destroy:")
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        product_ids = []
        for row in reader:
            product_ids.append(row["id"])
            if destroy_id == row["id"]:
                print("You are about to remove the following product from your list:")
                print(row["id"], row["name"], row["aisle"], row["department"], row["price"])
                continuation = input("Are you sure you want to remove this product? Y/N: ")
                if continuation == "Y":
                    with open(csv_file_path, "w") as csv_file:
                        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
                        writer.writeheader()
                        for row in rows:
                            if destroy_id != row["id"]:
                                writer.writerow(row)
                    with open(csv_file_path, "r") as csv_file:
                        reader = csv.DictReader(csv_file)
                        print("--------")
                        print("Here is your current inventory:")
                        for row in reader:
                            print(row["id"], row["name"], row["aisle"], row["department"], row["price"])
                if continuation != "Y":
                    print("You have chosen not to delete a product at this time.")
        if destroy_id not in product_ids:
            print("We're sorry, we couldn't find that product ID.")

def handler():
    if inp == "List":
        list_products()
    if inp == "Show":
        show_product()
    if inp == "Create":
        create_product()
    if inp == "Update":
        update_product()
    if inp == "Destroy":
        destroy_product()
    if inp not in operations:
        print("Unrecognized Operation. Please choose one of: 'List', 'Show', 'Create', 'Update', or 'Destroy'.")

handler()
