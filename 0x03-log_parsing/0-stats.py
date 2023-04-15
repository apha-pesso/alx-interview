#!/usr/bin/python3
"""Log parsing"""
from sys import stdin

total_file_size = 0
counter = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in stdin:
        files = line.split()
        if (len(files) < 2):
            pass

        if int(files[-2]) in status_codes.keys() and len(files) == 9:
            code = int(files[-2])
            counter += 1
            status_codes[code] += 1
            total_file_size += int(files[-1])
        # else:
            # pass

        if counter % 10 == 0:
            print("File size: " + str(total_file_size))
            # print('File size: {}'.format(total_file_size))
            sorted_codes = dict(sorted(status_codes.items()))
            for key in sorted_codes.keys():
                if sorted_codes[key]:
                    print(str(key) + ": " + str(sorted_codes[key]))
    print("File size: " + str(total_file_size))
    for key in status_codes.keys():
        if status_codes[key]:
            print(str(key) + ": " + str(status_codes[key]))

except (KeyboardInterrupt):
    print("File size: " + str(total_file_size))
    # print('File size: {}'.format(total_file_size))
    sorted_codes = dict(sorted(status_codes.items()))
    # for key, value in sorted_codes.items():
    # print("{}: {}".format(key, value))
    for key in sorted_codes.keys():
        if sorted_codes[key]:
            print(str(key) + ": " + str(sorted_codes[key]))
    raise
