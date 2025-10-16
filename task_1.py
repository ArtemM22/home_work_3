from datetime import datetime
def get_days_from_today(date):
    '''
    Функцію, яка розраховує кількість днів
    між заданою датою і поточною датою
    '''
    try: #У разі неправильного вводу формату обробляє помилку
        one_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        difference = (one_date - current_date).days
        print(f'Різниця між {one_date.date()} і сьогодні: {difference}')
        return difference
    except ValueError:
        print('Помилка неправильного формату дати. Використовуйте формат "YYYY-MM-DD"')
        return None

date = '2024-10-10'
get_days_from_today(date)