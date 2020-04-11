#!/home/navraj/anaconda3/bin/python
import os
import sys

def getMoneySpent(keyboards, drives, b):
    result=[(x,y) for x in keyboards for y in drives ]
    high=[x for x in result if (int(x[0])+int(x[1]))<= int(b)]
    if high:
        final=max(list(map(lambda x:int(x[0]) + int(x[1]),high)))
        return final
    return -1



if __name__ == '__main__':
    fptr = open("data.txt", 'r')

    all_data = fptr.readlines()

    prime_data = all_data[0].split()
    keyboard_prices = all_data[1].split()
    usb_prices = all_data[2].split()

    print(prime_data,keyboard_prices,usb_prices)

    b = prime_data[0]

    n = prime_data[1]

    m = prime_data[2]

    print(b,n,m)

    keyboards = keyboard_prices

    drives = usb_prices

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)

    if moneySpent == 622830:
        print("Correct!")
    else:
        print("Mission Failed!")
    
    fptr.close()

