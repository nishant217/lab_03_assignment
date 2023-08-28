#
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f"Employee ID: {self.emp_id}, \t Name: {self.name},\t Age: {self.age}, \tSalary: {self.salary}"

class EmployeeDatabase:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def sort_and_print(self, sorting_parameter):
        if sorting_parameter == 1:  
            sorted_employees = sorted(self.employees, key=lambda emp: emp.age)
        elif sorting_parameter == 2:  
            sorted_employees = sorted(self.employees, key=lambda emp: emp.name)
        elif sorting_parameter == 3:  
            sorted_employees = sorted(self.employees, key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter")
            return
        
        for emp in sorted_employees:
            print(emp)

if __name__ == "__main__":
    database = EmployeeDatabase()
    
    
    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))
    
    sorting_option = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))
    
    if sorting_option == 1:
        database.employees.sort(key=lambda emp: emp.age)
    elif sorting_option == 2:
        database.employees.sort(key=lambda emp: emp.name)
    elif sorting_option == 3:
        database.employees.sort(key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter")
        exit(1)
    
    database.sort_and_print(sorting_option)

#