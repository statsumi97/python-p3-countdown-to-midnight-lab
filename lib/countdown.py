# your code goes here!
import time

def countdown(start_number = 10):
    number = start_number

    while number >= 1:
        print(f'{number} SECOND(S)!')
        number -= 1

    print('HAPPY NEW YEAR!')
    return None

def countdown_with_sleep(start_number = 10):
    number = start_number

    while number >= 1:
        print(f'{number} SECOND(S)!')
        number -= 1
        time.sleep(1)

    print('HAPPY NEW YEAR!')
    return None
