

0x00. Pascal's Triangle

    By Alexa Orrico, Software Engineer at Holberton School
    Weight: 1
    Ongoing project - started 11-22-2021, must end by 11-26-2021 (in 2 days) - you're done with 0% of tasks.
    Checker was released at 11-24-2021 06:00 AM
    QA review fully automated.

Tasks
0. Pascal's Triangle
mandatory

Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer

guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 

Repo:

    GitHub repository: alx-interview
    Directory: 0x00-pascal_triangle
    File: 0-pascal_triangle.py

Copyright © 2021 Holberton Inc, All rights reserved.

