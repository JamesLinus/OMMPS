#!/usr/bin/env python
#coding=utf-8

import  time

def check(num):
    a = list(str(num))
    b = a[::-1]
    if a == b:
        return True
    return False

def test():
    all = xrange(1,10**7)
    for i in all:
        if check(i):
            if check(i**2):
                i**2
if __name__ == '__main__':
    start=time.time()
    test()
    print time.time()-start