import re

def get_employee_name():
    # verification name is entered
    while True:
        try:
            employee_name = input("Enter employee name: ")
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
        except ValueError:
            print("Please enter a valid name.")
            continue
    return employee_name

def get_total_hours():
    # Same code verification as get_hourly_rat
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
    # Same code verification as get_total_hours
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
    # Same code verification as get_total_hours and get_hourly_rat 
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

def calculate_pay(total_hours, hourly_rate, tax_rate):#Automated calculator
    gross_pay = total_hours * hourly_rate
    income_tax = (gross_pay * tax_rate) / 100
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def get_date():#I still wonder if there is a better!
    while True:
        try:
            from_date = input("Enter from date (mm/dd/yyyy): ")
            if from_date.lower() == "all":
                return "all", "all" #To write something twice by mistake i think its entering "all" for to_date
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
            to_date = input("Enter to date (mm/dd/yyyy): ")#copyed from from_date
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

def enter_employee_data():#I spent hours thinking of how to integrate this and the answer was return f!
    print()
    name = get_employee_name()
    if name.lower() == "end":
        return None
    from_date, to_date = get_date()
    if from_date == "all":
        return None
    total_hours = get_total_hours()
    hourly_rate = get_hourly_rate()
    tax_rate = get_income_tax_rate()
    gross_pay, income_tax, net_pay = calculate_pay(total_hours, hourly_rate, tax_rate)
    return f"{from_date}|{to_date}|{name}|{total_hours}|{hourly_rate}|{tax_rate}|{gross_pay}|{income_tax}|{net_pay}\n"

def write_employee_info(): #Fully integrate enter employee data and write employee info
    with open("Hour.txt", "w") as file: 
        while True:
            record = enter_employee_data()
            if record == None:
                return None
            file.write(record)

def display_report(): #Pull directly from the file
    with open("Hour.txt", "r") as file:
        for line in file:
            record = line.strip().split('|')
            print("\nFrom Date:", record[0])
            print("To Date:", record[1])
            print("Employee Name:", record[2])
            print("Total Hours Worked:", record[3])
            print("Hourly Rate: $", record[4])
            print("Gross Pay: $", record[6])
            print("Income Tax Rate:", record[5], "%")
            print("Income Tax: $", record[7])
            print("Net Pay: $", record[8])
            
     
def display_report_total(): #Separated display report into display report total for sanity
    total_employees = 0
    total_hours = 0
    total_gross_pay = 0
    total_tax = 0
    total_net_pay = 0 
    with open("Hour.txt", "r") as file:
        for line in file:
            record = line.strip().split('|')
            total_employees += 1
            total_hours += float(record[3])
            total_gross_pay += float(record[6])
            total_tax += float(record[7])
            total_net_pay += float(record[8])
        print("\nTotal Number of Employees:", total_employees)
        print("Total Hours Worked:", total_hours)
        print("Total Gross Pay: $", total_gross_pay)
        print("Total Tax: $", total_tax)
        print("Total Net Pay: $", total_net_pay)  
            
def main(): 
    while True:
        write_employee_info()
        result = display_report()
        if result == None:
            break
    display_report_total() #always displays total even when 0
    
if __name__ == "__main__":
    main()