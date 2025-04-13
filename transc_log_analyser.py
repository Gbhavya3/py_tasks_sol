def total_debit_by_user(logs):
    result = {}
    for transaction in logs:
        if transaction['type'].lower() == 'debit':
            user = transaction['user']
            amount = transaction['amount']
            if user in result:
                result[user] += amount
            else:
                result[user] = amount
    return result


logs = [
    {'user': 'Alice', 'amount': 120, 'type': 'debit'},
    {'user': 'Bob', 'amount': 200, 'type': 'credit'},
    {'user': 'Alice', 'amount': 180, 'type': 'debit'},
    {'user': 'Bob', 'amount': 100, 'type': 'debit'}
]
print(total_debit_by_user(logs))
