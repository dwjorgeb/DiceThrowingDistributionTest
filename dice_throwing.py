# Author: Jorge Batista @ Route Technologies [jorge.batista@route.technology]
# Dice throw distribution tester, using Python 3.6+
# Should work on all systems

import secrets
import string
import time
from concurrent.futures import ThreadPoolExecutor
import traceback

running = True
executor = ThreadPoolExecutor(max_workers=12)
dice = [1, 2, 3, 4, 5, 6]
distribution = {}

runs = 0
MAX = 10000000

matrix = {
    1: {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F'},
    2: {1: 'G', 2: 'H', 3: 'I', 4: 'J', 5: 'K', 6: 'L'},
    3: {1: 'M', 2: 'N', 3: 'O', 4: 'P', 5: 'Q', 6: 'R'},
    4: {1: 'S', 2: 'T', 3: 'U', 4: 'V', 5: 'W', 6: 'X'},
    5: {1: 'Y', 2: 'Z', 3: '9'}
}


def roll():
    return secrets.choice(dice)


def runner():
    global runs, distribution, running

    try:
        while runs < MAX:
            dice1 = roll()
            dice2 = 6

            while dice2 == 6:
                dice2 = roll()

            if dice2 == 5 and dice1 > 3:
                continue

            letter = matrix[dice2][dice1]
            distribution[letter] += 1
            runs += 1

            time.sleep(0.0001)

        running = False

    except Exception:
        print(traceback.format_exc())


def main():
    sequence = string.ascii_uppercase + "9"
    for key in sequence:
        distribution[key] = 0

    for i in range(12):
        executor.submit(runner)

    while running:
        d = ' | '.join(['{0}: {1}'.format(key, round(dist / runs, 4)) for key, dist in distribution.items()])
        print("{0} || {1}".format(runs, d))
        time.sleep(1)

    d = ' | '.join(['{0}: {1}'.format(key, round(dist / runs, 4)) for key, dist in distribution.items()])
    print("{0} || {1}".format(runs, d))


if __name__ == '__main__':
    main()
