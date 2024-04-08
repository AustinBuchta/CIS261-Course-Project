
def get_employee_name():
    return input("Enter employee name: ")

def get_total_hours():
    return float(input("Enter total hours worked: "))

def get_hourly_rate():
    return float(input("Enter hourly rate: "))

def get_income_tax_rate():
    return float(input("Enter income tax rate (in percentage): ")) 

def calculate_pay(total_hours, hourly_rate, tax_rate):
    gross_pay = total_hours * hourly_rate
    income_tax = (gross_pay * tax_rate) / 100
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee_details(name, total_hours, hourly_rate, gross_pay, tax_rate, income_tax, net_pay):
    print("\nEmployee Name:", name)
    print("Total Hours Worked:", total_hours)
    print("Hourly Rate:", hourly_rate)
    print("Gross Pay:", gross_pay)
    print("Income Tax Rate:", tax_rate, "%")
    print("Income Tax:", income_tax)
    print("Net Pay:", net_pay)

def display_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay):
    print("\nTotal Number of Employees:", total_employees)
    print("Total Hours Worked:", total_hours)
    print("Total Gross Pay:", total_gross_pay)
    print("Total Tax:", total_tax)
    print("Total Net Pay:", total_net_pay)

def main():
    total_employees = 0
    total_hours = 0
    total_gross_pay = 0
    total_tax = 0
    total_net_pay = 0

    while True:
        name = get_employee_name()
        if name.lower() == "end":
            break

        total_hours = get_total_hours()
        hourly_rate = get_hourly_rate()
        tax_rate = get_income_tax_rate()

        gross_pay, income_tax, net_pay = calculate_pay(total_hours, hourly_rate, tax_rate)

        display_employee_details(name, total_hours, hourly_rate, gross_pay, tax_rate, income_tax, net_pay)

        total_employees += 1
        total_hours += total_hours
        total_gross_pay += gross_pay
        total_tax += income_tax
        total_net_pay += net_pay

    display_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay)

if __name__ == "__main__":
    main()
