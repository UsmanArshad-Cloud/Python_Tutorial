# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def generate_payroll_report(employees):
    emp_string = []
    for employee in employees:
        name = employee['name']
        salary = employee['salary']
        emp_string.append(f'Name: {name} and Salary is: {salary}')
    return emp_string

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello")
    print_hi('PyCharm')
    print('*'*10)
    #name = input("Hello! Enter Your Name:")
    #print("Good"+"Your Name is"+name)
    #birth_year = int(input("Enter Your Birth Year:"))
    #age = 2023-birth_year
    #print(age)
    check = bool(2)
    print(check)
    str_val = "hello"
    list_val = list(str_val)
    tuple_val = tuple(str_val)
    set_val = set(str_val)
    print(list_val)  # Output: ['h', 'e', 'l', 'l', 'o']
    print(tuple_val)  # Output: ('h', 'e', 'l', 'l', 'o')
    print(set_val)  # Output: {'h', 'e', 'l', 'o'}
    course = '''
    Hello!
    How are You I am fine What are you doing in my property
    Nothing just hanging around
    '''
    course1 = "Usman's Laptop"
    course2 = 'This is "Usman Laptop"'
    print(course)
    print(course1)
    print(course2)
    text = "Python Programming"

    # Slicing a portion of the string
    print(text[0:6])  # Output: "Python"
    print(text[6])
    print(text[7:18])  # Output: "Programming"

    # If the starting index is omitted, it defaults to 0
    print(text[:6])  # Output: "Python"

    # If the ending index is omitted, it goes to the end of the string
    print(text[7:])  # Output: "Programming"

    # Negative indices can also be used for slicing
    print(text[-11:-1])  # Output: "Programmin"

    employees = [
        {"name": "John Doe", "id": 101, "department": "Engineering", "salary": 5000.0},
        {"name": "Jane Smith", "id": 102, "department": "Sales", "salary": 4000.0},
        {"name": "Mike Johnson", "id": 103, "department": "Finance", "salary": 4500.0}
    ]

    report = generate_payroll_report(employees)
    print(report)
    print(2+10*4**2)


    ###Car Game


# See PyCharm help at https://www.jetbrains.com/help/pycharm/