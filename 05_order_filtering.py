orders = [
    {"order_id": "101", "amount": 10},
    {"order_id": "102", "amount": 20},
    {"order_id": "103", "amount": 15},
    {"order_id": "104", "amount": 8},
    {"order_id": "105", "amount": 5},
]


# Task 1 — Keep orders with amounts of at least 15.
# Expected order IDs: 102, 103

filtered_orders_1 = []

for order in orders:
    amount = order["amount"]
    if amount >= 15:
        filtered_orders_1.append(order)



# Task 2 — Keep orders with amounts from 8 to 15, inclusive.
# Expected order IDs: 101, 103, 104

filtered_orders_2 = []

for i in orders:
    amount = i["amount"]
    if amount >= 8 and amount <= 15:
        filtered_orders_2.append(i)
        
# Task 3 — Keep orders with amounts below 8 or above 15.
# Expected order IDs: 102, 105

filtered_orders_3 = []

for n in orders:
    amount = n["amount"]
    if amount < 8 or amount > 15:
        filtered_orders_3.append(n)
    
print(filtered_orders_1)
print(filtered_orders_2)
print(filtered_orders_3)