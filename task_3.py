# Імпорт модуля re для роботи з регулярними виразами
import re

'''
    Функція допомагає нормалізувати телефонні номери до стандартного формату
    '''
def normalize_phone (phone_number):
    # Видалення всіх символів, крім цифр
    cleaned_numbers = re.sub(r'[^0-9]', '', phone_number.strip())
    if cleaned_numbers.startswith('+'):
        cleaned_numbers = cleaned_numbers
    elif cleaned_numbers.startswith('00'):
        cleaned_numbers = '+' + cleaned_numbers[2:]
    elif cleaned_numbers.startswith('380'):
        cleaned_numbers = '+' + cleaned_numbers
    else:
        cleaned_numbers = '+38' + cleaned_numbers
    return cleaned_numbers

raw_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

for number in raw_numbers:
    print(normalize_phone(number))