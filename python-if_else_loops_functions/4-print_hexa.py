#!/usr/bin/python3
# 4-print_hexa.py
# Christian Alexander Vazquez Gonzalez <dev.chrisvaz@gmail.com>

"""Print numbers 0 to 98 in decimal and hexadecimal."""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
