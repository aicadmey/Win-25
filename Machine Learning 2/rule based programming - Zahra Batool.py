# example 01
def diagnose(symptoms):
    if "fever" in symptoms:
        if "cough" in symptoms:
            if "shortness of breath" in symptoms:
                return "Suspected COVID-19"
            else:
                return "Common cold"
        else:
            if "rash" in symptoms:
                return "Measles"
            return "Other fever-related illness"
    else:
        return "No fever detected"

print(diagnose(["fever", "cough", "shortness of breath"]))

# example 02
def calculate_bonus(salary, performance_rating):
    if performance_rating > 4:
        if salary < 50000:
            return salary * 0.2
        else:
            return salary * 0.1
    elif performance_rating >= 3:
        if salary < 50000:
            return salary * 0.1
        else:
            return salary * 0.05
    else:
        return 0
print(calculate_bonus(45000, 5))

# example 03
def grade_student(marks):
    if marks >= 90:
        if marks > 95:
            return "A+"
        return "A"
    elif marks >= 80:
        if marks > 85:
            return "B+"
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "Fail"
print(grade_student(92))

# example 04
def calculate_discount(customer_type, purchase_amount):
    if customer_type == "regular":
        if purchase_amount > 1000:
            return purchase_amount * 0.1
        else:
            return purchase_amount * 0.05
    elif customer_type == "premium":
        if purchase_amount > 1000:
            return purchase_amount * 0.2
        else:
            return purchase_amount * 0.15
    else:
        return 0
print(calculate_discount("premium", 1200))

# example 05
def traffic_light(action, emergency_vehicle=False):
    if action == "red":
        if emergency_vehicle:
            return "Allow emergency vehicle"
        return "Stop"
    elif action == "yellow":
        if emergency_vehicle:
            return "Prepare to stop"
        return "Caution"
    elif action == "green":
        if emergency_vehicle:
            return "Clear the way"
        return "Go"
    else:
        return "Invalid action"
print(traffic_light("red", emergency_vehicle=True))
