class Employee:
    """Base class for all employees"""

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def displayNumEmployees(self):
        print 'Total Employees:', Employee.empCount

    def displayEmployeeName(self):
        print 'Name:', self.name

employee1 = Employee("Zara", 2000)
employee2 = Employee("David", 2500)

employee1.displayNumEmployees()
employee1.displayEmployeeName()

employee2.displayEmployeeName()
employee2.displayNumEmployees()
