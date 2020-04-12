import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(a, b, c):
    if(abs(c-a)==abs(c-b)):
        return ("Mouse C")
    else:
        if(abs(c-a)>abs(c-b)):
            return ("Cat B")
        else:
            return ("Cat A")
    
    
if __name__ == '__main__':
    fptr = open('data.txt', 'r')

    data = fptr.readlines()

    q = int(data[0].split()[0])   
    
    for q_itr in range(q):
        sn=q_itr+1

        x = int(data[sn].split()[0])

        y = int(data[sn].split()[1])

        z = int(data[sn].split()[2])

        result = catAndMouse(x, y, z)

        print(result)

    fptr.close()

