import sqlite3
from employee import Employee

conn = sqlite3.connect("employees.db") #':memory: for in-mem db

# create cursor
c = conn.cursor()

# create table
# c.execute("""CREATE TABLE employees (
#     first text,
#     last text,
#     pay integer
# )""")


def insert_emp(emp):
    c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
              {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    with conn:
        c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    # context manager
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
        WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def remove_emp(emp):
    # context manager
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


emp_1 = Employee('John', 'Duke', 90000)
emp_2 = Employee('Marian', 'Dolores', 39000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Duke')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Duke')
print(emps)

conn.close()