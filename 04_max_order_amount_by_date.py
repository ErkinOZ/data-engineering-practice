# Exercise 04 — Find the largest order amount for each date.
# Practice dictionary membership checks and value comparisons.
#
# Run:
# python3 04_max_order_amount_by_date.py
#
# Expected output:
# {'2026-11-03': 15, '2026-11-04': 20, '2026-11-05': 8}

orders = [
    {"date": "2026-11-03", "amount": 10},
    {"date": "2026-11-04", "amount": 20},
    {"date": "2026-11-03", "amount": 15},
    {"date": "2026-11-05", "amount": 8},
    {"date": "2026-11-04", "amount": 5},
]



result = {}
#first_date = None
#largest_amount = 0

for i in orders:
    date = i["date"]
    amount = i["amount"]

    if date not in result:
        result[date] = amount
    elif amount > result[date]:
        result[date] = amount
    
print(result)
        
    
        