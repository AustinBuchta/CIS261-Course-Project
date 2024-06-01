import re

def CreateUsers():
    print("Create users, passwords, and role")
    with open("Users.txt", "a+") as UsersFile:
        while True:
            username = GetUserName().lower()
            if username == "end":
                break
            password = GetUserPassword()
            getrole = GetUserRole()
            UserDetail = username + "|" + password + "|" + getrole + "\n"
            UsersFile.write(UserDetail)
    UserInfo()

def GetUserName():# get_employee_name reused
    while True:
        try:
            username = input("Enter user name: ")
            if not username:
                print("Name cannot be blank!")
                continue
            elif username.isdigit():
                print("Name cannot contain numbers.")
                continue
            elif re.search(r'[-+=!@#$%^&*(),.?":{}|<>]', username):
                print("Name cannot contain special characters.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid name.")
            continue
    return username       

def GetUserPassword():
    while True:
        try:
            upass = input("Enter password: ")
            if not upass:
                print("Password cannot be blank!")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid password.")
            continue
    return upass

def GetUserRole():
    getrole = input("Enter role (Admin or User): ").lower()
    while True:
        if getrole in ["admin", "user"]:
            return getrole
        else:
            getrole = input("Invalid must enter (Admin or User): ")

def UserInfo():
    with open("Users.txt", "r") as UsersFile:
        while True:
            UserDetail = UsersFile.readline()
            if not UserDetail:
                break
            UserDetail = UserDetail.replace("\n", "")
            UserData = UserDetail.split("|")
            print("User Name:", UserData[0], "Password:", UserData[1], "Role:", UserData[2])

def Login():
    while True:
        UserName = input("Enter User Name: ").lower()
        Userupass = input("Enter Password: ")
        with open("Users.txt", "r") as UsersFile:
            for UserDetail in UsersFile:
                UserDetail = UserDetail.strip()
                UserData = UserDetail.split("|")
                if UserName == UserData[0] and Userupass == UserData[1]:
                    return UserData[2]
        print(f"\n{UserName}, Invalid credentials!\n")
        return"none"

def get_employee_name(): # verification name is entered
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

def get_total_hours(): # Same code verification as get_hourly_rat
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

def get_hourly_rate(): # Same code verification as get_total_hours
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

def get_income_tax_rate(): # Same code verification as get_total_hours and get_hourly_rat 
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

def get_date():#I know there is a better way but i have commited to this now! from datetime import date
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
    return f"{from_date}|{to_date}|{name}|{total_hours:.2f}|{hourly_rate:.2f}|{tax_rate:.0f}|{gross_pay:.2f}|{income_tax:.2f}|{net_pay:.2f}\n"

def write_employee_info(): #Fully integrate enter employee data and write employee info
    with open("Hour.txt", "w") as file: 
        print("\nData Entry")
        while True:
            record = enter_employee_data()
            if record == None:
                break
            file.write(record)
        
def display_report(): #Pull directly from the file
    with open("Hour.txt", "r") as file:
        for line in file:
            record = line.strip().split('|')
            print("\nFrom Date:",record[0])
            print("To Date:",record[1])
            print("Employee Name:",record[2])
            print("Total Hours Worked:",record[3])
            print("Hourly Rate: $",record[4])
            print("Gross Pay: $",record[6])
            print("Income Tax Rate:",record[5],"%")
            print("Income Tax: $",record[7])
            print("Net Pay: $",record[8])
                
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
        print(f"\nTotal Number of Employees:{total_employees:,.0f}")# print must stay in this spot!
        print(f"Total Hours Worked:{total_hours:,.2f}")
        print(f"Total Gross Pay: ${total_gross_pay:,.2f}")
        print(f"Total Tax: ${total_tax:,.2f}")
        print(f"Total Net Pay: ${total_net_pay:,.2f}")    
          
def main():
    CreateUsers()
    Authorization = Login()
    while True:
        if Authorization == "none":
            break
        if Authorization == "user":
            display_report()
            break
        if Authorization == "admin":
            write_employee_info()
            result = display_report()
            if result == None:
                display_report_total()
                break
            
if __name__ == "__main__":
    main()      