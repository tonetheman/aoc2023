#!/usr/bin/python3

"""
eval could be interesting for this
>>> eval("a",None,{"a":10})
10
>>> eval("a<200",None,{"a":10})
True
>>> eval("a>200",None,{"a":10})
False
"""

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
            for r in rr:
                print("\t",r)
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

def junk():
    class MatchRule:
        def __init__(self,match,target):
            self.match = match
            self.target = target

    class Rule:
        def __init__(self,name):
            self.name = name
            self.rules = []
        def add(self,ropts):
            self.rules.append(ropts)

    r1 = Rule("in")
    r1.add(MatchRule("s<1351","px"))
    r1.add(MatchRule("DEFAULT","qqz"))

    r2 = Rule("qqz")
    r2.add(MatchRule("s>2770","qs"))
    r2.add(MatchRule("m<1801","hdj"))
    r2.add(MatchRule("TERM","R"))

    r3 = Rule("qs")
    r2.add(MatchRule("s>3448","A"))
    r2.add(MatchRule("DEFAULT","lnx"))
                     
    def test_rule(r,x,m,a,s):
        # do not dig this from all the dumb dict
        # syntax
        current_rule = 0
        while True:
            print(r)
            res = eval(r.rules[current_rule].match,None,
                    {"a":a,
                     "x":x,
                     "m":m,
                     "s":s})
            if res==False:
                # move to next rule in this case
                current_rule = current_rule + 1
                if r.rules[current_rule].match == "DEFAULT":
                    return r.rules[current_rule].target
            else:
                # found a match bug out quick
                return r.rules[current_rule].target

        
        

    print( test_rule(r1,787,2655,1222,2876) )
    print( test_rule(r2,787,2655,1222,2876) )
    print( test_rule(r3,787,2655,1222,2876) )



junk()



