import math
import os
import random
import re
import sys
from collections import Counter

def get_common_counts(letters,common):
    common_dict = {}
    for item in common:
        common_dict[item] = letters.count(item)
    return common_dict


def makeAnagram(a, b):
    count_add = 0
    common = list(set(a)&set(b))
    dups1 = [x for x in common if list(a).count(x)>1]
    dups2 = [x for x in common if list(b).count(x)>1]
    common_dups = set(dups1)& set(dups2)
    print(len(common_dups))
    for item in common_dups:
        count_add = count_add + min(list(a).count(item)-1,list(b).count(item)-1)*2
    print(len(a),len(b))
    print(count_add)
    return len(a)+len(b)-2*len(common)-count_add

if __name__ == '__main__':
    a = 'imkhnpqnhlvaxlmrsskbyyrhwfvgteubrelgubvdmrdmesfxkpykprunzpustowmvhupkqsyjxmnptkcilmzcinbzjwvxshubeln'
    b = 'wfnfdassvfugqjfuruwrdumdmvxpbjcxorettxmpcivurcolxmeagsdundjronoehtyaskpwumqmpgzmtdmbvsykxhblxspgnpgfzydukvizbhlwmaajuytrhxeepvmcltjmroibjsdkbqjnqjwmhsfopjvehhiuctgthrxqjaclqnyjwxxfpdueorkvaspdnywupvmy'
    result = makeAnagram(a,b)
    print(result)
    if result == 102:
        print("Correct!")
    else:
        print("Test Failed")

