#!/usr/bin/python3


def part1():
    inf = open("sample.txt", "r")
    data= inf.readlines()
    inf.close()

    STATE_START = 0
    STATE_ONE = 1

    state = STATE_START


    def parse_line(line):
        nonlocal state
        if state == STATE_START:
            p1 = line.split("{")
            print(p1)
            if p1[0]=="\n":
                state = STATE_ONE
                return False
            rule_name = p1[0]
            rest_of_rule = p1[1].split("}")
            rr = rest_of_rule[0].split(",")
            print("rr",rr)

            # TODO parse out the rest of each rule
            # store somewhere hahaha
            
        elif state == STATE_ONE:
            print("state one", line)

        return True

    for line in data:
        res = parse_line(line)
        if res==False:
            # switch parsing
            pass


part1()