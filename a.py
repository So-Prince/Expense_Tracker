spending = {}
for spend in expenses:
    if spend in spending:
        spending[spend["category"]] += spend['amount']
    else:
        spending[spend["category"]] = spend['amount']

for item in spending.items():
    return spending


lis = list(map(lambda x: x.strip().lower(), normalize))
return lis


for task in tasks:
    if task.get("id") == task_id:
        return task
return None


lis = rate * balance
return balance + lis



def count_by_author(books):
    faith = {}
    for book in books:
        if book['author'] in faith:
            faith[book['author']] += 1
        else:
            faith[book['author']] = 1
    return faith



low_products =[(product["id"], target - product["quantity"]) for product in products if product["quantity"] < threshold]
return sorted(low_products, key = lambda x: x[0])
