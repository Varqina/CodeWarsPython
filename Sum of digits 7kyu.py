"""
Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
Note: a and b are not ordered!
"""
from urllib3.connectionpool import xrange


def get_sum(a,b):
    valueMax, valueMin, result=b,a,0
    if valueMin>valueMax:valueMin=b;valueMax=a
    for x in range(valueMin,valueMax+1):
        result=result + x
    return result

def get_sum_best_practice(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))


print(get_sum(1,5))

print(get_sum_best_practice(1,5))
#EnvTest