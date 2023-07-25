#!/usr/bin/python3
import random
import sys
import datetime

def generate_log_line():
    return "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    )

try:
    for i in range(10000):
        sys.stdout.write(generate_log_line())
        sys.stdout.flush()
        random_sleep = random.random()
        if random_sleep < 0.2:  # Sleep longer if random value is less than 0.2 to simulate keyboard interruption
            sys.stderr.write("Sleeping for a longer duration...\n")
            sys.stderr.flush()
            sleep_time = random.randint(1, 5)
            sleep(sleep_time)

except KeyboardInterrupt:
    sys.stderr.write("Keyboard interruption received. Exiting...\n")
    sys.stderr.flush()
    sys.exit(0)
