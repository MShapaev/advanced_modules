import random
from application.db.data import salary, currency
from application.db.people import get_emloyees



def calculate_salary():
    return f'зарплата сотрудника с фамилией {get_emloyees()} составляет {random.choice(salary)} ' \
           f'{random.choice(currency)}'