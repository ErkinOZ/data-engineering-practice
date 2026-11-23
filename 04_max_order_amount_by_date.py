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
        
    
        