#!/usr/bin/python3


def part1():
    inf = open("input.txt","r")
    lines = inf.readlines()
    inf.close()
    res = 0
    for data in lines:
        data = data[:-1]
        first = True
        ts = ""
        for c in data:
            digit = ord(c)-ord('0')
            if digit>=0 and digit<=9:
                if first:
                    ts = str(digit)
                    first = False
        first = True
        for c in data[::-1]:
            digit = ord(c)-ord('0')
            if digit>=0 and digit<=9:
                if first:
                    ts = ts + str(digit)
                    first = False
        print(ts,data)
        res = res + int(ts)
    print("part1",res)    
    
    
part1()