#!/usr/bin/env python3


# Here is the code to generate a report to 'report.txt'

from news import *


def report():
    '''to print the top 3 articles'''
    with open('report.txt', 'w') as write_file:
        write_file.write('\n\n\t\tmost popular articles\n\n'.title())
        for table in popular_articles():
            write_file.write('{} - {} views\n'.format(table[0], table[1]))
        write_file.write('-' * len(str(table)))

    with open('report.txt', 'a') as write_file:
        write_file.write('\n\n\n\t\tmost popular authors\n\n'.title())
        for table in popular_authors():
            write_file.write('{} - {} views\n'.format(table[0], table[1]))
        write_file.write('-' * len(str(table)))

    with open('report.txt', 'a') as write_file:
        write_file.write('\n\n\n\t\terrors\n\n'.title())
        for table in get_errors():
            write_file.write('{} - {}%\n'.format(table[0], table[1]))
        write_file.write('-' * len(str(table)))


if __name__ == '__main__':
    report()
