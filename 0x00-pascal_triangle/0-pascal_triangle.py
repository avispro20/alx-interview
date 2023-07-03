#!/usr/bin/python3
'''
Pascal Triangle Interview Challenge conducted by me
'''


def pascal_triangle(n):
    '''
    Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n
    - You can assume n will be always an integer.
    '''

    pascal_list = []
    if n <= 0:
        return pascal_list
    for i in range(n):
        row = [1]
        if pascal_list:
            last_row = pascal_list[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        pascal_list.append(row)
    return (pascal_list)
