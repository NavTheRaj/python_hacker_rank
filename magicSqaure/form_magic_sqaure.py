import math
import os
import random
import re
import sys
from statistics import mean

# Complete the formingMagicSquare function below.

def formingMagicSquare(s):
    first_row = int(sum(s[0]))
    second_row = int(sum(s[1]))
    third_row = int(sum(s[2]))
    diag_1 = s[0][0]+s[1][1]+s[2][2]
    diag_2 = s[0][2]+s[1][1]+s[2][0]
    col_1 = s[0][0]+s[1][0]+s[2][0]
    col_2 = s[0][1]+s[1][1]+s[2][1]
    col_3 = s[0][2]+s[1][2]+s[2][2]




if __name__ == '__main__':
    fptr = open('data.txt', 'r')

    data = fptr.readlines()

    s = []

    for i in range(3):
        s.append(list(map(int,data[i].rstrip().split())))

    result = formingMagicSquare(s)


    fptr.close()

