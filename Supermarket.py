customers = int(input("Enter the number of customers: "))
for i in range(customers):
    name = input("Enter customer name: ")
    items = int(input("Enter number of items: "))
    total_cost = 0
    for j in range(items):
        item_name = input("Enter item name: ")
        item_cost = float(input("Enter item cost: "))
        total_cost += item_cost
    print("Total cost for customer", name, "is", total_cost)
