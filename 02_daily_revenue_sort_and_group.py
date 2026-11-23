orders = [
    {"date": "2026-11-03", "amount":10},
    {"date": "2026-11-04", "amount": 20},
    {"date": "2026-11-03", "amount": 15},

]


sorted_orders = sorted(orders, key=lambda order: order["date"])

#print(sorted_orders)

current_date = None
current_total = 0


for i in sorted_orders:
    date = i["date"]
    amount = i["amount"]
    if date != current_date:
        if current_date is not None:
            print(current_date, current_total)
        current_total = 0
        current_date = date
        
    current_total += amount
    
if current_date is not None:
    print(current_date, current_total)
 
    

          