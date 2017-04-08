
def calculate_gross_salary(net_salary):
    net_salary = int(input("Zadej cistou mzdu, kterou bys chtel mit kazdy mesic:"))
    gross_salary = (net_salary - 2070)/ 0.689
    print("Pro cistou mzdu ve vysi %d si musis u pohovoru rici o %d Kc v hrube mzde." % (net_salary, gross_salary ))
    return gross_salary
calculate_gross_salary(net_salary)
