# Exercise 03 — Count orders by date.
# Practice dictionary membership checks and separate counters per date.
#
# Run:
# python3 03_order_count_by_date.py
#
# Expected output:
# {'2026-11-03': 2, '2026-11-04': 2, '2026-11-05': 1}


orders = [
    {"date": "2026-11-03", "amount": 10},
    {"date": "2026-11-04", "amount": 20},
    {"date": "2026-11-03", "amount": 15},
    {"date": "2026-11-05", "amount": 8},
    {"date": "2026-11-04", "amount": 5},
]


#count_date = 0
#current_date = None
result = {}


for i in orders:
    date = i["date"]
    if date in result:
        result[date] += 1
    else:
        result[date] = 1

print(result)



