class Employee:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def display_details(self):
        print("Employee:", self.name)
        print("ID:", self.employee_id)
        print("Department:", self.department)


employee = Employee("Sathwik", 101, "Engineering")
employee.display_details()