from application.salary import calculate_salary
from application.db.people import get_emloyees
from datetime import datetime
from tqdm import tqdm
from time import sleep


def get_date():
    cur_date = datetime.today().date()
    return cur_date

def progressbar():
    for _ in tqdm([1, 2, 3, 4]):
        sleep(0.25)
    return 'research complete'

if __name__ == '__main__':
    print(progressbar())
    print(get_date())
    print(calculate_salary())
    print(get_emloyees())

