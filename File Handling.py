import json
import os
Employee_file = "employees.json"

def load_employees():
    if os.path.exists(Employee_file):
        with open(Employee_file, "r") as file:
            return json.load(file)
    return {}

def save_employees(employees):
    with open(Employee_file, "w") as file:
        json.dump(employees, file, indent=4)

def generate_employee_id(employees):
    if not employees:
        return "1"  # Start with 1 if no employees exist
    else:
        max_id = max(int(emp_id) for emp_id in employees.keys())
        return str(max_id + 1)

def add_employee(employees):
    emp_id = generate_employee_id(employees)
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = input("Enter employee salary: ")
    employees[emp_id] = {"name": name, "position": position, "salary": salary}
    save_employees(employees)
    print(f"Employee added successfully! ID: {emp_id}")

def update_employee(employees):
    emp_id =input("Enter Employee ID update: ")
    if emp_id not in employees:
        print("Employee ID does not exist")
        return
    print(f"Current details: {employees[emp_id]}")
    name = input("Enter new name: ")
    position = input("Enter new position: ")
    salary = input("Enter new salary: ")
    if name:
        employees[emp_id] ["name"] = name
    if salary:
        employees[emp_id] ["salary"] = salary
    if position:
        employees[emp_id] ["position"] = position
    save_employees(employees)
    print("Employee updated successfully")

def delete_employee(employees):
    emp_id = input("Enter employee ID to delete: ")
    if emp_id not in employees:
        print("Employee not found!")
        return
    delete_employee(emp_id)
    save_employees(employees)
    print("Employee deleted successfully!")

def display_employees(employees):
    if not employees:
        print("No employees found!")
    else:
        for emp_id, details in employees.items():
            print(f"ID: {emp_id}, Name: {details['name']}, Position: {details['position']}, Salary: {details['salary']}")


def main():
    employees = load_employees()
    while True:
        print("\nEmployee Mangement System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Display Employees")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            update_employee(employees)
        elif choice == "3":
            delete_employee(employees)
        elif choice == "4":
            display_employees(employees)
        elif choice == "5":  
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
        



    
