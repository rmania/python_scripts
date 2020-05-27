# blueprint for creating instances
class Employee():
    # class variables
    num_of_employees = 0
    raise_amount = 2.4

    def __init__(self, first, last, pay):  # constructor
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_employees += 1

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        # instance variable self.raise_amount allows for indivual value assigning
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    # example how to add employees salaries together
    def __add__(self, other):
        return self.pay + other.pay

    # print how many charcter the fullname of an empployee has.
    def __len__(self):
        return len(self.fullname())

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    # alternative constructor
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split("-")
        return cls(first, last, pay)  # create a new Employee object

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True