#!/usr/bin/python3
""" a python function to find minimun operation number(CopyAll & Paste """


def minOperations(n):
    """
    minOperation - function to find the minumum no of operation to find
    n number of H characters givne a sing H chr in text file
    Arguments:
        n - the number required to reach
    Returns:
        the number of minimum operations
    """
    c = 0
    i = 2
    if type(n) is not int or n < 2:
        return (0)
    while (n != 1):
        if n % i == 0:
            c += i
            n /= i
            i = 1
        i = i + 1

    return (c)
