import numpy as np

random_number = np.random.randint(1,100)
cnt = 0

while True:
    input_number = input('Input number-')
    cnt += 1
    if int(input_number) > random_number:
        print('Number too big')
    elif int(input_number) < random_number:
        print('Number too smoll')
    else:
        print(f'Ok!!! random number was {random_number} cnt {cnt}')
        break
