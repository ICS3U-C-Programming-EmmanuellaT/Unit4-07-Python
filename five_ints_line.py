#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 24th november, 2026
# This program prints out numbers from 1000 to 2000 in 5 numbers in one line


def main():
    # process and output of the numbers in a for loop
    for counter in range(1000, 2001):
        if (counter - 1000) % 5 == 0:
            print(counter)
        else:
            print(counter, end=" ")


if __name__ == "__main__":
    main()
