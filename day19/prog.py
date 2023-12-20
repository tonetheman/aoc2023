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

from typing import Any


class MatchRule:
    def __init__(self,match,target):
        self.match = match
        self.target = target
    def __repr__(self) -> str:
        return str(self.match) + " " + str(self.target)

class Rule:
    def __init__(self,name):
        self.name = name
        self.rules = []
    def add(self,ropts):
        self.rules.append(ropts)
    def __str__(self) -> str:
        return str(self.name)

class Values:
    def __init__(self,_s):
        self._s = _s

        self._s = self._s[1:]
        
        self._s = self._s[0:len(_s)-3]
        tmp = self._s.split(",")
        # interesting that each element in tmp
        # looks like x = 10 or s = 20
        # these can be evaluated too
        # though not sure how to get the assignment
        # to escape the eval
        for t in tmp:
            crud = t.split("=")
            if crud[0]=='x':
                self.x = int(crud[1])
            elif crud[0]=='m':
                self.m = int(crud[1])
            elif crud[0]=='a':
                self.a = int(crud[1])
            elif crud[0]=='s':
                self.s = int(crud[1])
    def __repr__(self) -> str:
        ts = "x=" + str(self.x)
        ts += "m=" + str(self.m)
        ts += "a=" + str(self.a)
        ts += "s=" + str(self.s)
        return ts
    
def part1():
    inf = open("sample.txt", "r")
    data= inf.readlines()
    inf.close()

    STATE_START = 0
    STATE_ONE = 1

    state = STATE_START
    indexed_rules = {}
    all_values = []

    def parse_line(line):
        nonlocal state
        if state == STATE_START:
            p1 = line.split("{")
            if p1[0]=="\n":
                state = STATE_ONE
                return False
            rule_name = p1[0]
            cr = Rule(rule_name)
            indexed_rules[rule_name] = cr # save a reference
            rest_of_rule = p1[1].split("}")
            rr = rest_of_rule[0].split(",")
            for r in rr:
                colon_index = r.find(":")
                if colon_index!=-1:
                    rs= r.split(":")
                    if len(rs)==2:
                        cr.add(MatchRule(rs[0],rs[1]))
                else:
                    cr.add(MatchRule("DEFAULT",r))

            # TODO parse out the rest of each rule
            # store somewhere hahaha
            
        elif state == STATE_ONE:
            v = Values(line)
            all_values.append(v)

        return True

    for line in data:
        res = parse_line(line)
    
    # all_values has stuff in it
    v = values[0]




def junk():

    r1 = Rule("in")
    r1.add(MatchRule("s<1351","px"))
    r1.add(MatchRule("DEFAULT","qqz"))

    r2 = Rule("qqz")
    r2.add(MatchRule("s>2770","qs"))
    r2.add(MatchRule("m<1801","hdj"))
    r2.add(MatchRule("DEFAULT","R")) # not sure about match name

    r3 = Rule("qs")
    r3.add(MatchRule("s>3448","A"))
    r3.add(MatchRule("DEFAULT","lnx"))

    r4= Rule("lnx")
    r4.add(MatchRule("m>1548","A"))
    r4.add(MatchRule("DEFAULT","A"))


    def test_rule(r,x,m,a,s):
        # do not dig this from all the dumb dict
        # syntax
        current_rule = 0
        while True:
            # print(r.name)
            cr = r.rules[current_rule]
            # print("\t",cr.match,cr.target)
            if cr.match=="DEFAULT":
                return cr.target # this could be A R or a legit target!
            
            res = eval(cr.match,None,
                    {"a":a,
                     "x":x,
                     "m":m,
                     "s":s})
            if res==False:
                # move to next rule in this case
                current_rule = current_rule + 1
            else:
                # found a match bug out quick
                return r.rules[current_rule].target

        
        

    print( test_rule(r1,787,2655,1222,2876) )
    print( test_rule(r2,787,2655,1222,2876) )
    print( test_rule(r3,787,2655,1222,2876) )
    print( test_rule(r4,787,2655,1222,2876) )



part1()


