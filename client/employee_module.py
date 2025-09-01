class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.bonus = 0.0

    def apply_bonus(self, percentage):
        self.bonus = self.salary * (percentage / 100)
        self.salary += self.bonus
        return self.salary
