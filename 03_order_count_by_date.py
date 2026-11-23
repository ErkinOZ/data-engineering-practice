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



