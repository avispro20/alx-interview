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

# Initialize the metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Read lines from stdin
for line in sys.stdin:
    # Split the line into a list
    line_list = line.split()

    # Check if the line is in the correct format
    if len(line_list) != 6:
        continue

    # Get the status code
    status_code = int(line_list[4])

    # Update the metrics
    total_file_size += int(line_list[5])
    status_code_counts[status_code] += 1

    # Print the metrics every 10 lines
    if len(status_code_counts) % 10 == 0:
        print("Total file size:", total_file_size)
        for status_code, count in status_code_counts.items():
            print(status_code, ":", count)
