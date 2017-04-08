interest_rate_pa = 279.83

def calculate_interest_per_month():
    loan_amount = int(input("Kolik si chces pujcit penez?"))
    interest_per_month = loan_amount / 100 * interest_rate_pa / 12
    return interest_per_month

def calculate_month_payment(interest_per_month):
    month_payment = (loan_amount/12) + interest_per_month
    return month_payment

def calculate_total_costs(interest_per_month):
    number_of_months = int(input("Kolik mesicu chces splacet?"))
    total_costs = interest_per_month * number_of_months
    return total_costs






