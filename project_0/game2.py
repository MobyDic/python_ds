import numpy as np

def random_predict(number:int=1) -> int:
    """Функция для случайного угадывания числа

    Args:
        number (int, optional): Заданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return count
    
def score_predict(random_predict) -> int:
    """Среднее кол-во угадываний

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: среднее кол-во
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))   
    print(f'Колличество угадываний из 1000 попыток - {score}')
    return score

#RUN
if __name__ == '__main__':
    score_predict(random_predict)