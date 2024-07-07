"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    first_number = 0 # Используем для сокращения поля выборки (первое число поля)
    end_number = 101 # Используем для сокращения поля выборки (последнее число поля)
    predict_number = 51 #Назначаем число для сокращения поля поиска в 2 раза 

    while True:
        count += 1        
        if number > predict_number: 
            first_number = predict_number
        else:
            end_number = predict_number
        predict_number = np.random.randint(first_number, end_number) #Получаем случайное число в сокращенном поле выборки
        if number == predict_number + 1:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
