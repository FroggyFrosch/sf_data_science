"""Игра "Угадай число"
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number) -> int:
    """Угадываем число

    Args:
        number (int): Загаданное число.

    Returns:
        int: Число попыток
    """
    our_number = np.random.randint(1, 101) # компьютер произвольно пробует угадать число
    attempt = 0 # счетчик попыток
    smallest = 1 # самое мелкое возможное число
    biggest = 100 # самое большое возможное число
    while True:
        attempt += 1
        if our_number > number:
            biggest = our_number - 1
            our_number = round ((biggest + smallest)// 2)
        elif our_number < number:
            smallest = our_number + 1
            our_number = round ((biggest + smallest) // 2)
        else:
            print(f'Компьютер угадал загаданное число за {attempt} попыток. Это число {number}')
            break # конец игры и выход из цикла
    return(attempt)


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_list = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список произвольных чисел

    for number in random_array:
        count_list.append(random_predict(number))

    score = int(np.mean(count_list))
    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    #запускаем
    score_game(random_predict)