
# Program 10: In-Memory Inventory Tracker

# Inventory of different store locations
store1 = {
    "Apple": 50,
    "Banana": 30,
    "Mango": 20
}

store2 = {
    "Apple": 25,
    "Orange": 40,
    "Mango": 15
}

store3 = {
    "Banana": 10,
    "Orange": 20,
    "Grapes": 35
}

# Display individual inventories
print("Store 1 Inventory:", store1)
print("Store 2 Inventory:", store2)
print("Store 3 Inventory:", store3)

# Check whether a product exists
product = "Apple"

if product in store1:
    print(product, "exists in Store 1")
else:
    print(product, "does not exist in Store 1")

# Safely access inventory using get()
print("Grapes in Store 1:", store1.get("Grapes", 0))

# Merge inventories by adding quantities
total_inventory = {}

for store in (store1, store2, store3):
    for item, quantity in store.items():
        total_inventory[item] = total_inventory.get(item, 0) + quantity

print("\nTotal Inventory:", total_inventory)

# Create a new dictionary using dictionary comprehension
low_stock = {
    item: quantity
    for item, quantity in total_inventory.items()
    if quantity < 50
}

print("Products with stock below 50:", low_stock)

# Merge dictionaries using update()
merged_inventory = store1.copy()
merged_inventory.update(store2)
merged_inventory.update(store3)

print("Inventory after update():", merged_inventory)
