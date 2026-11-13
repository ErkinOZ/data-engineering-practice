orders = [
    {"order_id": "101", "date": "2026-11-01", "amount": "29.90"},
    {"order_id": "102", "date": "2026-11-01", "amount": "15.00"},
    {"order_id": "103", "date": "2026-11-02", "amount": ""},
    {"order_id": "104", "date": "2026-11-02", "amount": "invalid"},
    {"order_id": "101", "date": "2026-11-01", "amount": "29.90"},
    {"order_id": None, "date": "2026-11-03", "amount": "10.00"},
]


#first_order = orders[0]
#print(type(orders))
#print(len(orders))
#print(type(first_order))
#print(first_order["order_id"])
#print(type(first_order["amount"]))
#count_of_id = 0
#missing_id_count = 0
#for i in orders:
#    orders_id = i["order_id"]
#
#    if orders_id is None or orders_id == "":
#        missing_id_count += 1
#    else:
#        count_of_id += 1
#
#print(count_of_id)
#print(missing_id_count)

#from decimal import Decimal, InvalidOperation


valid_amount_count = 0

invalid_amount_count = 0

#for i in orders:
#    amount = i["amount"]    
#    try:
#        convert_amount = Decimal(amount)
#        valid_amount_count += 1
#        print(convert_amount)
#    except InvalidOperation:
#        invalid_amount_count += 1
#        print("invalid amount:", repr(amount))

#print(valid_amount_count)
#print(invalid_amount_count)

orders = [
    {"order_id": "101", "date": "2026-11-01", "amount": "29.90"},
    {"order_id": "102", "date": "2026-11-01", "amount": "15.00"},
    {"order_id": "103", "date": "2026-11-02", "amount": ""},
    {"order_id": "104", "date": "2026-11-02", "amount": "invalid"},
    {"order_id": "101", "date": "2026-11-01", "amount": "29.90"},
    {"order_id": None, "date": "2026-11-03", "amount": "10.00"},
]



from decimal import Decimal, InvalidOperation

rejected_count = 0
accepted_count = 0
seen_order_ids = set()
duplicated_count = 0

for order in orders:

    order_id = order["order_id"]

    if order_id is None or order_id == "":
        rejected_count += 1
        continue
    try:
        amount = Decimal(order["amount"])
    except InvalidOperation:
        rejected_count += 1
        continue

    if order_id in seen_order_ids:
        duplicated_count += 1
    else:
        seen_order_ids.add(order_id)
        accepted_count += 1


print(rejected_count)
print(accepted_count)
print(duplicated_count)