# Daily order statistics.
# Task 1 — Maximum order amount by date.
# Task 2 — Minimum order amount by date.
# Task 3 — Average order amount by date (to be completed).
#
# Run:
# python3 04_daily_order_statistics.py

orders = [
    {"date": "2026-11-03", "amount": 10},
    {"date": "2026-11-04", "amount": 20},
    {"date": "2026-11-03", "amount": 15},
    {"date": "2026-11-05", "amount": 8},
    {"date": "2026-11-04", "amount": 5},
]

# Task 1 — Maximum order amount by date.
# Expected: {'2026-11-03': 15, '2026-11-04': 20, '2026-11-05': 8}

max_by_date = {}

for order in orders:
    date = order["date"]
    amount = order["amount"]

    if date not in max_by_date:
        max_by_date[date] = amount
    elif amount > max_by_date[date]:
        max_by_date[date] = amount

print("Maximum:", max_by_date)

# Task 2 — Minimum order amount by date.
# Expected: {'2026-11-03': 10, '2026-11-04': 5, '2026-11-05': 8}

min_by_date = {}

for order in orders:
    date = order["date"]
    amount = order["amount"]

    if date not in min_by_date:
        min_by_date[date] = amount
    elif amount < min_by_date[date]:
        min_by_date[date] = amount

print("Minimum:", min_by_date)

# Task 3 — Average order amount by date.
# Calculate the total and count for each date, then divide total by count.
# Expected: {'2026-11-03': 12.5, '2026-11-04': 12.5, '2026-11-05': 8.0}

totals_by_date = {}
counts_by_date = {}

for i in orders:
    date = i["date"]
    amount = i["amount"]
    if date in totals_by_date:
        totals_by_date[date] += amount
        counts_by_date[date] += 1
    else:
        totals_by_date[date] = amount
        counts_by_date[date] = 1

average_by_date = {}

for date in totals_by_date:
     average_by_date[date] = totals_by_date[date] / counts_by_date[date]



print(totals_by_date)
print(counts_by_date)
print("Average:", average_by_date)