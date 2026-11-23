orders = [

    {"date": "2026-11-03", "amount": 10},
    {"date": "2026-11-04", "amount": 20},
    {"date": "2026-11-03", "amount": 15},


]


revenue = {}


for i in orders:
    date = i["date"]
    amount = i["amount"]
    if date in revenue:
        revenue[date] += amount
    else:
        revenue[date] = amount

print(revenue)
        
