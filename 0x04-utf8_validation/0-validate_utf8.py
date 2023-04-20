#!/usr/bin/python3
'''utf-8 validation'''


def validUTF8(data):
    '''Takes a list of integers and check
       if the data conform to utf-8 standards
       returns True if it checks and false of failue.
       Every element is assumed to be one byte.(less than 256)
    '''

    if max(data) > 255:
        return False

    if not data:
        return False

    # convert all element to binary
    bin_data = []
    for num in data:
        bin_data.append(format(num, '08b'))

    for i in range(len(bin_data)):

        # convert to binary
        # num = bin(data[i])
        # element = data[i]
        # bi_num = format(element, '08b')

        # Check if it is four byte
        if bin_data[i][:5] == '11110' and bin_data[i + 1][:2] == '10':
            if bin_data[i + 2][:2] == '10' and bin_data[i + 3][:2] == '10':
                return True
            else:
                False

        # Check if it is 3 bytes
        if bin_data[i][:4] == '1110' and bin_data[i + 1][:2] == '10':
            if bin_data[i + 2][:2] == '10':
                return True
            else:
                return False

        # Check if it is 2 bytes
        if bin_data[i][:3] == '110' and bin_data[i + 1][:2] == '10':
            return True
    return True
