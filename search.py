def search_employee(employee_id):
    employees = {
        101: "Sathwik",
        102: "Rahul",
        103: "Arjun"
    }

    return employees.get(employee_id, "Employee not found")


print(search_employee(101))