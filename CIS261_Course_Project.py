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
    while True:
        try:
            get_from_date = input("Enter from date (mm/dd/yyyy): ")
            if get_from_date.lower() == "all":
                from_date = get_from_date
                to_date = get_from_date  # Assign the same value to 'to_date'
                return from_date, to_date  # Return both from_date and to_date
            if get_from_date:
                get_from = re.sub(r'\D', '', get_from_date)    
                if len(get_from) == 8:
                    from_date = get_from[:2] + '/' + get_from[2:4] + '/' + get_from[4:]
                    break
                if len(get_from) == 6:
                    from_date = get_from[:2] + '/' + get_from[2:4] + '/20' + get_from[4:]
                    break
                if len(get_from) == 7 or len(get_from) <= 5:
                    print("Invalid date format. Please enter the date in mm/dd/yyyy format.")
                    continue
                else: 
                    raise ValueError
        except ValueError:
            print("Unexpected error. Please enter the date in mm/dd/yyyy format.")
            continue
    while True:
        try:
            get_to_date = input("Enter to date (mm/dd/yyyy): ")
            if get_to_date:
                get_to = re.sub(r'\D', '', get_to_date)    
                if len(get_to) == 8:
                    to_date = get_to[:2] + '/' + get_to[2:4] + '/' + get_to[4:]
                    break
                if len(get_to) == 6:
                    to_date = get_to[:2] + '/' + get_to[2:4] + '/20' + get_to[4:]
                    break
                if len(get_to) == 7 or len(get_to) <= 5:
                    print("Invalid date format. Please enter the date in mm/dd/yyyy format.")
                    continue
                else: 
                    raise ValueError
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

def open_file():
    try:
        file = open("Hour.txt", "a")  # Open the file in "append" mode
        return file
    except FileNotFoundError:
        print("File not found.")
        return None

# Function to write employee information to the text file
def write_employee_info(employee_data):
    with open("Hour.txt", "w") as file:
        for data in employee_data:
            from_date, to_date, name, total_hours, hourly_rate, tax_rate = data
            gross_pay, income_tax, net_pay = calculate_pay(total_hours, hourly_rate, tax_rate)
            record = f"{from_date}|{to_date}|{name}|{total_hours}|{hourly_rate}|{tax_rate}|{gross_pay}|{income_tax}|{net_pay}\n"
            file.write(record)
            if from_date == "all":
                file.pop(record)
                return None
    
def main(): 
    employee_data = []
    
    while True:
        print()
        data = enter_employee_data()
        if data is None:
            break
        employee_data.append(data)
        

    write_employee_info(employee_data)
    
    processed_data = [process_employee_data(data) for data in employee_data]
    total_gross_pay, total_tax, total_net_pay = calculate_pay_total_pay(processed_data)
    display_totals(len(employee_data), sum(data[3] for data in employee_data), total_gross_pay, total_tax, total_net_pay)

if __name__ == "__main__":
    main()
    