import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    first_part = s.count('a') #Gives number of 'a' in original string
    print(first_part)
    second_part = n // len(s)
    print(second_part)
    third_part = s[:n % len(s)].count('a')
    print(third_part)
    result = (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
    return result


def main():
    s = 'aba'
    n = 10
    result = repeatedString(s,n)
    print(result)
    if result == 7:
        print("Correcto!")
    else:
        print("Test Failed.. :( ")

main()
