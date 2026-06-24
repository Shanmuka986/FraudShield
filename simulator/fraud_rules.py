def calculate_risk(amount):

    if amount > 75000:
        return "Critical"

    elif amount > 50000:
        return "High"

    elif amount > 20000:
        return "Medium"

    return "Low"