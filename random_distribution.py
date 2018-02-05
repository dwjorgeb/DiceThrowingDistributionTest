# Author: Jorge Batista @ Route Technologies [jorge.batista@route.technology]
# Random distribution tester, using Python 3.6+
# Should work on all systems

import secrets
import string
import time
from concurrent.futures import ThreadPoolExecutor
import traceback

running = True
executor = ThreadPoolExecutor(max_workers=12)
distribution = {}
sequence = string.ascii_uppercase + "9"

runs = 0
MAX = 10000000


def runner():
    global runs, distribution, running

    try:
        while runs < MAX:
            letter = secrets.choice(sequence)
            distribution[letter] += 1
            runs += 1

            time.sleep(0.0001)

        running = False

    except Exception:
        print(traceback.format_exc())


def main():
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
