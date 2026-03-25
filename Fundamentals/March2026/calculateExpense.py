def calculate_expense(expense):
    if not expense:
        return {"error" : "no expense provided"}
    
    total = sum(expense)

    calculateEx = {
        "total": total,
        "highest": max(expense),
        "lowest": min(expense),
        "average": total / len(expense),
    }

    return calculateEx 


expense = [120, 50, 30, 100, 20]

calculate = calculate_expense(expense)

print(calculate)