import datetime

# Initialize variables to keep track of totals
total_employees = 0
total_hours = 0
total_gross_pay = 0
total_income_tax = 0
total_net_pay = 0
payroll_data = []

# Open a text file for storing the employee information
file = open("employee_records.txt", "w")

# Continuously prompt for employee information until "End" is entered
while True:
    # Prompt for employee information
    name = input("Enter employee name (Enter 'End' to stop): ")
    if name == "End":
        break
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    tax_rate = float(input("Enter income tax rate (in %): "))
    
    # Get the current date for the record
    current_date = datetime.date.today().strftime("%m/%d/%Y")

    # Calculate gross pay, income taxes, and net pay
    gross_pay = hours_worked * hourly_rate
    income_tax = gross_pay * (tax_rate / 100)
    net_pay = gross_pay - income_tax

    # Display employee information
    print("Employee Name:", name)
    print("Hours Worked:", hours_worked)
    print("Hourly Rate: $", hourly_rate)
    print("Gross Pay: $", gross_pay)
    print("Income Tax Rate:", tax_rate, "%")
    print("Income Taxes: $", income_tax)
    print("Net Pay: $", net_pay)
    print("")

    # Write the record to the text file
    record = f"{current_date}|{name}|{hours_worked}|{hourly_rate}|{tax_rate}"
    file.write(record + "\n")

    # Add to payroll data list
    payroll_data.append([current_date, name, hours_worked, hourly_rate, tax_rate, gross_pay, income_tax, net_pay])

# Close the text file
file.close()

# Define a function to calculate the payroll for a given date
def calculate_payroll(from_date):
    # Initialize totals dictionary
    totals = {"total_employees": 0, "total_hours": 0, "total_income_tax": 0, "total_net_pay": 0}
    
    # Display header
    print("Payroll Report")
    print("From Date:", from_date)
    print("To Date:", datetime.date.today().strftime("%m/%d/%Y"))
    print("")

    # Open the text file for reading
    file = open("employee_records.txt", "r")

    # Loop through the records and calculate payroll
    for line in file:
        record = line.strip().split("|")
        record_date = datetime.datetime.strptime(record[0], "%m/%d/%Y").date()
        if from_date == "All" or from_date == record_date:
            # Unpack the record data
            name, hours_worked, hourly_rate, tax_rate = record[1], float(record[2]), float(record[3]), float(record[4])

            # Calculate gross pay, income taxes, and net pay
            gross_pay = hours_worked * hourly_rate
            income_tax = gross_pay * (tax_rate / 100)
            net_pay = gross_pay - income_tax

            # Display employee information
            print("Employee Name:", name)
            print("Hours Worked:", hours_worked)
            print("Hourly Rate: $", hourly_rate)
            print("Gross Pay: $", gross_pay)
            print("Income Tax Rate:", tax_rate, "%")



