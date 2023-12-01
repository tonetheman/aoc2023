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
    
    
# part1()

def part2():
    inf = open("sample2.txt","r")
    lines = inf.readlines()
    inf.close()

    res = 0
    for data in lines:
        first = True
        ts = ""
        for i in range(len(data)):
            c = data[i]
            if c in ['o','t','f','s','e','n']:
                # check for case where digit is spelled
                if data[i:].startswith("two"):
                    if first:
                        ts = "2"
                        first = False
                elif data[i:].startswith("one"):
                    if first:
                        ts = "1"
                        first = False
                elif data[i:].startswith("three"):
                    if first:
                        ts = "3"
                        first = False
                elif data[i:].startswith("four"):
                    if first:
                        ts = "4"
                        first = False
                elif data[i:].startswith("five"):
                    if first:
                        ts = "5"
                        first = False
                elif data[i:].startswith("six"):
                    if first:
                        ts = "6"
                        first = False
                elif data[i:].startswith("seven"):
                    if first:
                        ts = "7"
                        first = False
                elif data[i:].startswith("eight"):
                    if first:
                        ts = "8"
                        first = False
                elif data[i:].startswith("nine"):
                    if first:
                        ts = "9"
                        first = False
            elif c in ['0','1','2','3','4','5','6','7','8','9']:
                if first:
                    ts = str(c)
                    first = False       
        first = True
        rdata = data[::-1]
        for i in range(len(rdata)):
            c = rdata[i]
            if c in ['o','t','f','s','e','n']:
                # check for case where digit is spelled
                if data[i:].startswith("two"):
                    if first:
                        ts = ts + "2"
                        first = False
                elif data[i:].startswith("one"):
                    if first:
                        ts = ts + "1"
                        first = False
                elif data[i:].startswith("three"):
                    if first:
                        ts = ts + "3"
                        first = False
                elif data[i:].startswith("four"):
                    if first:
                        ts = ts + "4"
                        first = False
                elif data[i:].startswith("five"):
                    if first:
                        ts = ts + "5"
                        first = False
                elif data[i:].startswith("six"):
                    if first:
                        ts = ts + "6"
                        first = False
                elif data[i:].startswith("seven"):
                    if first:
                        ts = ts + "7"
                        first = False
                elif data[i:].startswith("eight"):
                    if first:
                        ts = ts + "8"
                        first = False
                elif data[i:].startswith("nine"):
                    if first:
                        ts = ts + "9"
                        first = False
            elif c in ['0','1','2','3','4','5','6','7','8','9']:
                if first:
                    ts = ts + str(c)
                    first = False

        print(ts)
        res = res + int(ts)
    print("res",res)

part2()