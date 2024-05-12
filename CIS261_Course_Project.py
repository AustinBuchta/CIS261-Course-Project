import re

def get_employee_name():
    while True:
        try:
            employee_name = input("Enter employee name: ")
        except ValueError:
            print("Please enter a valid name.")
            continue
        if not employee_name:
            print("Name cannot be blank!")
            continue
        elif employee_name.isdigit():
            print("Name cannot contain numbers.")
            continue
        elif re.search(r'[-+=!@#$%^&*(),.?":{}|<>]', employee_name):
            print("Name cannot contain special characters.")
            continue
        else:
            break
    return employee_name

def get_total_hours():
    while True:
        try:
            hours = float(input("Enter total hours worked: "))
            if hours < 0:
                print("Hours cannot be negative.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid number of hours.")
            continue
    return hours

def get_hourly_rate():
    while True:
        try:
            rate = float(input("Enter hourly rate: "))
            if rate < 0:
                print("Rate cannot be negative.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid hourly rate.")
            continue
    return rate

def get_income_tax_rate():
    while True:
        try:
            tax_rate = float(input("Enter income tax rate: "))
            if tax_rate < 0:
                print("Tax rate cannot be negative.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid tax rate.")
            continue
    return tax_rate

def calculate_pay(total_hours, hourly_rate, tax_rate):
    gross_pay = total_hours * hourly_rate
    income_tax = (gross_pay * tax_rate) / 100
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay):
    print("\nTotal Number of Employees:", total_employees)
    print("Total Hours Worked:", total_hours)
    print("Total Gross Pay: $", total_gross_pay)
    print("Total Tax: $", total_tax)
    print("Total Net Pay: $", total_net_pay)

def get_date():
    while True:
        try:
            from_date = input("Enter from date (mm/dd/yyyy): ")
            if from_date.lower() == "all":
                return "all", "all"
            if from_date:
                from_date = re.sub(r'\D', '', from_date)    
                if len(from_date) == 8:
                    from_date = from_date[:2] + '/' + from_date[2:4] + '/' + from_date[4:]
                elif len(from_date) == 6:
                    from_date = from_date[:2] + '/' + from_date[2:4] + '/20' + from_date[4:]
                elif len(from_date) == 7 or len(from_date) <= 5 or len(from_date) >= 9:
                    print("Invalid date format. Please enter the date in mm/dd/yyyy format.")
                    continue
                else: 
                    raise ValueError
                break
        except ValueError:
            print("Unexpected error. Please enter the date in mm/dd/yyyy format.")
            continue

    while True:
        try:
            to_date = input("Enter to date (mm/dd/yyyy): ")
            if to_date:
                to_date = re.sub(r'\D', '', to_date)    
                if len(to_date) == 8:
                    to_date = to_date[:2] + '/' + to_date[2:4] + '/' + to_date[4:]
                elif len(to_date) == 6:
                    to_date = to_date[:2] + '/' + to_date[2:4] + '/20' + to_date[4:]
                elif len(to_date) == 7 or len(to_date) <= 5 or len(to_date) >= 9:
                    print("Invalid date format. Please enter the date in mm/dd/yyyy format.")
                    continue
                else: 
                    raise ValueError
                break
        except ValueError:
            print("Unexpected error. Please enter the date in mm/dd/yyyy format.")
            continue
    return from_date, to_date

def enter_employee_data():
    name = get_employee_name()
    if name.lower() == "end":
        return None
    from_date, to_date = get_date()
    if from_date == "all":
        return
    total_hours = get_total_hours()
    hourly_rate = get_hourly_rate()
    tax_rate = get_income_tax_rate()
    gross_pay, income_tax, net_pay = calculate_pay(total_hours, hourly_rate, tax_rate)
    return [from_date, to_date, name, total_hours, hourly_rate, tax_rate] 

def write_employee_info(employee_data):
    employee_data_list = []  # Initialize list to store employee data

    gross_pay_total = 0
    income_tax_total = 0
    net_pay_total = 0
    
    with open("Hour.txt", "w") as file: 
        for data in employee_data:
            
            from_date, to_date, name, total_hours, hourly_rate, tax_rate = data
            if from_date == "all" or name == "end":
                continue  # Skip this record
            gross_pay, income_tax, net_pay = calculate_pay(total_hours, hourly_rate, tax_rate)
            employee_data_list.append((name, from_date, to_date, total_hours, hourly_rate, gross_pay, tax_rate, income_tax, net_pay))
            record = f"{from_date}{to_date}{name}{total_hours}{hourly_rate}{tax_rate}{gross_pay}{income_tax}{net_pay}\n"
            file.write(record)
            
            # Add employee details to the list
            gross_pay_total += gross_pay
            income_tax_total += income_tax
            net_pay_total += net_pay
            
            # Display employee details
            print("\nEmployee Name: ", name)
            print("From Date: ", from_date)
            print("To Date: ", to_date)
            print("Total Hours Worked:", total_hours)
            print("Hourly Rate: $", hourly_rate)
            print("Gross Pay: $", gross_pay)
            print("Income Tax Rate:", tax_rate, "%")
            print("Income Tax: $", income_tax)
            print("Net Pay: $", net_pay)
    
    return employee_data_list, gross_pay_total, income_tax_total, net_pay_total

def main(): 
    employee_data = []

    while True:
        print()
        record = enter_employee_data()
        if record is None:
            break
        employee_data.append(record)

    # Write employee information to the file and calculate totals
    employee_list, gross_pay_total, income_tax_total, net_pay_total = write_employee_info(employee_data)
    
    display_totals(
        len(employee_list),
        sum(record[3] for record in employee_list),  # Total hours worked
        gross_pay_total,
        income_tax_total,
        net_pay_total
    )

if __name__ == "__main__":
    main() 