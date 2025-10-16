from random import randint

def get_numbers_ticket(min, max, quantity):
    '''
    Функція допомагає отримати набір унікальних випадкових чисел лотереї
    '''
    if not (1 <= min <= max <= 1000):
        return []
    if not (0 < quantity <= (max - min + 1)):
        return []

    result_array = set() # здійснюється формування множини
    while len(result_array) < quantity:
        result_array.add(randint(min, max))
    return sorted(list(result_array))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)