class Employee:
    num_employees = 0  # data member to count the number of Employees

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.num_employees += 1  # Incrementing the count

    def average_salary(self, *salaries):
        total_salary = sum(salaries, self.salary)
        return total_salary / (len(salaries) + 1)

class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department, hours_per_week):
        super().__init__(name, family, salary, department)
        self.hours_per_week = hours_per_week

# Creating instances of Employee and FulltimeEmployee classes
employee1 = Employee("John Doe", "Doe Family", 50000, "HR")
employee2 = FulltimeEmployee("Alice Smith", "Smith Family", 60000, "IT", 40)

# Calling member functions
avg_salary_employee1 = employee1.average_salary(55000, 60000)
avg_salary_employee2 = employee2.average_salary(65000, 70000)

# Displaying results
print(f"Average salary for {employee1.name}: ${avg_salary_employee1}")
print(f"Average salary for {employee2.name}: ${avg_salary_employee2}")
print(f"Total number of employees: {Employee.num_employees}")
