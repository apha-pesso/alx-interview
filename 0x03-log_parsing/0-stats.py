#!/usr/bin/python3
"""Log parsing"""

import sys

total_file_size = 0
counter = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


try:
    for line in sys.stdin:
        files = line.split()
        if int(files[-2]) in status_codes.keys() and len(files) == 9:
            code = int(files[-2])
            counter += 1
            status_codes[code] += 1
            total_file_size += int(files[-1])
        if counter % 10 == 0:
            print('File size: {}'.format(total_file_size))
            for key, value in status_codes.items():
                if value:
                    print("{}: {}".format(key, value))
except KeyboardInterrupt as error:
    print('File size: {}'.format(total_file_size))
    for key, value in status_codes.items():
        print("{}: {}".format(key, value))