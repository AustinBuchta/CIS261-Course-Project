import re

def get_employee_name():
    # verification name is entered
    while True:
        try:
            employee_name = input("Enter employee name: ")
        except ValueError:
            print("I don't understand")
            continue
        if not employee_name:
            print("Answer cannot be blank!")
            continue
        elif employee_name.isdigit():
            print("That is a number. Please enter a name without numbers.")
            continue
        elif re.search(r'[-+=!@#$%^&*(),.?":{}|<>]', employee_name):
            print("Special characters are not allowed. Please enter text only.")
            continue
        else: 
            break
    return employee_name
    
def get_total_hours():
    # Same code verification as get_hourly_rat
    while True:
        try:
            hours = int(input("Enter total hours worked: "))
            if isinstance(hours, int):
                break
            else:
                print("Please enter number of total hours worked: ")
                continue
        except ValueError:
            print("Please enter number of total hours worked: ")
            continue
    return hours

def get_hourly_rate():
    # Same code verification as get_total_hours
    while True:
        try:
            rate = int(input("Enter hourly rate: "))
            if isinstance(rate, int):
                break
            else:
                print("Please enter number of hourly rate: ")
                continue
        except ValueError:
            print("Please enter number of hourly rate: ")
            continue
    return rate

def get_income_tax_rate():
    # Same code verification as get_total_hours and get_hourly_rat 
    while True:
        try:
            create_tax_rate = int(input("Enter income tax rate: "))
            if isinstance(create_tax_rate, int):
                break
            else:
                print("Please enter number of income tax rate: ")
                continue
        except ValueError:
            print("Unexpected error! Please enter number of income tax rate: ")
            continue
    return create_tax_rate

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

def get_date():
    # Is there a better way?!?
    while True:
        try:
            get_from_date = input("Enter from date (mm/dd/yyyy): ")
            if '/' not in get_from_date:
            # Check if the length of the input is exactly 8 digits (no '/'), then add '/' accordingly
                get_from = re.sub(r'\D', '', get_from_date)    
                if len(get_from) == 8:
                    from_date = get_from[:2] + '/' + get_from[2:4] + '/' + get_from[4:]
                    break
                if len(get_from) <= 7:
                    print("Invalid date format. Please enter the date in mm/dd/yyyy format.")
                    continue
                else: 
                    print("Unexpected Error, Please enter the date in mm/dd/yyyy format.")
                    continue
            # Check if the input contains only digits and '/' then rebuild '/'
            elif '/' in get_from_date:
                get_from = re.sub(r'\D', '', get_from_date)
                if len(get_from) == 8:
                    from_date = get_from[:2] + '/' + get_from[2:4] + '/' + get_from[4:]
                    break
                else:
                    print("Invalid date format. Please enter the date in mm/dd/yyyy format.")
                    continue
            else:
                print("Invalid characters. Please enter digits and '/' only.")
                continue
        except ValueError:
            print("Unexpected error. Please enter the date in mm/dd/yyyy format.")
            continue
    while True:
        try:
            get_to_date = input("Enter to date (mm/dd/yyyy): ")
            if '/' not in get_to_date:
            # Check if the length of the input is exactly 8 digits (no '/'), then add '/' accordingly
                get_to = re.sub(r'\D', '', get_to_date)    
                if len(get_to) == 8:
                    to_date = get_to[:2] + '/' + get_to[2:4] + '/' + get_to[4:]
                    break
                else:
                    print("Invalid date format. Please enter the date in mm/dd/yyyy format.")
                    continue
            # Check if the input contains only digits and '/' then rebuild '/'
            elif '/' in get_to_date:
                get_to = re.sub(r'\D', '', get_to_date)
                if len(get_to) == 8:
                    to_date = get_to[:2] + '/' + get_to[2:4] + '/' + get_to[4:]
                    break
                else:
                    print("Invalid date format. Please enter the date in mm/dd/yyyy format.")
                    continue
            else:
                print("Invalid characters. Please enter digits and '/' only.")
                continue
        except ValueError:
            print("Invalid date format. Please enter the date in mm/dd/yyyy format.")
            continue
    return from_date, to_date

def enter_employee_data():
    name = get_employee_name()
    if name.lower() == "end":
        return None
    from_date, to_date = get_date()
    employee_hours = get_total_hours()
    hourly_rate = get_hourly_rate()
    tax_rate = get_income_tax_rate()
    return [from_date, to_date, name, employee_hours, hourly_rate, tax_rate]

def calculate_pay_total_pay(employee_data):
    total_gross_pay = sum(data[0] for data in employee_data)
    total_tax = sum(data[1] for data in employee_data)
    total_net_pay = sum(data[2] for data in employee_data)
    return total_gross_pay, total_tax, total_net_pay

def process_employee_data(data):
#Index:0     ,   1    ,  2  ,     3       ,     4      ,     5
    from_date, to_date, name,  total_hours, hourly_rate, tax_rate = data
    gross_pay, income_tax, net_pay = calculate_pay(total_hours, hourly_rate, tax_rate)
    print("\nEmployee Name:", name)
    print("From Date:", from_date)
    print("To Date:", to_date)
    print("Total Hours Worked:", total_hours)
    print("Hourly Rate:", hourly_rate)
    print("Gross Pay:", gross_pay)
    print("Income Tax Rate:", tax_rate, "%")
    print("Income Tax:", income_tax)
    print("Net Pay:", net_pay)
    return gross_pay, income_tax, net_pay

def display_totals_from_dict(employee_data):
    total_employees = len(employee_data)
    total_all_hours = sum(data[3] for data in employee_data)
    total_gross_pay = sum(data[0] for data in employee_data)
    total_tax = sum(data[1] for data in employee_data)
    total_net_pay = sum(data[2] for data in employee_data)
    print("\nTotal Number of Employees:", total_employees)
    print("Total Hours Worked:", total_all_hours)
    print("Total Gross Pay:", total_gross_pay)
    print("Total Tax:", total_tax)
    print("Total Net Pay:", total_net_pay)

def main():
    employee_data = []
    
    while True:
        print()
        data = enter_employee_data()
        if data is None:
            break
        employee_data.append(data)

    processed_data = [process_employee_data(data) for data in employee_data]
    total_gross_pay, total_tax, total_net_pay = calculate_pay_total_pay(processed_data)
    display_totals(len(employee_data), sum(data[3] for data in employee_data), total_gross_pay, total_tax, total_net_pay)

if __name__ == "__main__":
    main()
    