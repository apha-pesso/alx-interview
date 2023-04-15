#!/usr/bin/python3
"""Log parsing"""
from sys import stdin

total_file_size = 0
counter = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in stdin:
        files = line.split()
        # print("line {} -> {}".format(counter, files))
        if (len(files) < 2):
            continue
        # if int(files[-2]) in status_codes.keys() and len(files) == 9:

        try:

            # if int(files[-2]) in status_codes.keys():
            total_file_size += int(files[-1])
            code = int(files[-2])
            counter += 1
            if code in status_codes.keys():
                status_codes[code] += 1
            # print("TOtal size in loop {}".format(total_file_size))

            if counter % 10 == 0:
                print("File size: " + str(total_file_size))
                sorted_codes = dict(sorted(status_codes.items()))
                for key in sorted_codes.keys():
                    if sorted_codes[key]:
                        print(str(key) + ": " + str(sorted_codes[key]))
        except ValueError:
            continue

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
