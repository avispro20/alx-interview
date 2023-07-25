#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line
must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

line list = [<IP Address>, -, [<date>], "GET /projects/260 HTTP/1.1",
<status code>, <file size>]
"""


import sys
import signal

# Define global variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    global total_size, status_counts
    print("Total file size:", total_size)
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")
    print()

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def process_line(line):
    global total_size, status_counts, line_count
    parts = line.split()
    if len(parts) != 10:
        return

    ip_address, date, method, endpoint, http_version, status_code, file_size = parts[0], parts[3][1:], parts[5], parts[6], parts[7], parts[8], int(parts[9])

    if status_code.isdigit():
        status_code = int(status_code)
        if status_code in status_counts:
            status_counts[status_code] += 1

    total_size += file_size
    line_count += 1

try:
    for line in sys.stdin:
        process_line(line)
        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    print_statistics()
