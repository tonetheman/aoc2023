#!/usr/bin/python3

from typing import List

inf = open("sample.txt","r")
data : List[str] = inf.readlines()
inf.close()

class Group:
    def __init__(self):
        self.r = -1
        self.c = -1
        self.val = ""
    def __repr__(self) -> str:
        return str(self.r) + " " +self.val

class Grid:
    def __init__(self,data):
        self.grid = []
        for line in data:
            line = line.rstrip()
            tmp = []
            for c in line:
                tmp.append(c)
            self.grid.append(tmp)
    def __repr__(self):
        ts = ""
        for row in self.grid:
            for c in row:
                ts = ts + str(c)
            ts = ts + "\n"
        return ts
    def get(self,r,c):
        try:
            return self.grid[r][c]
        except IndexError:
            return '.'
        
    def check(self,r,c):
        ii = [
            (-1,-1),
            (-1,0),
            (-1,1),
            (0,-1),
            (0,1),
            (1,-1),
            (1,0),
            (1,1)
        ]
        for (ri,ci) in ii:
            computed_r = r + ri
            computed_c = c + ci
            print(computed_r,computed_c)
            if computed_c<0 or computed_r<0:
                pass # ignore
            elif computed_c>len(self.grid[0]) or computed_r>len(self.grid):
                pass
            else:
                v = self.get(computed_r,computed_c)
                if not v in ['.','0','1','2','3','4','5','6','7','8','9']:
                    return True
        return False

grid = Grid(data)
groups = []

# find groups
r=0
while True:
    ts = ""
    for i in range(10):
        cc = grid.get(r,i)
        if cc in ['0','1','2','3','4','5','6','7','8','9']:
            ts = ts + str(cc)
        elif cc=='.':
            if ts!="":
                print("group create",ts)
                tmp = Group()
                tmp.val = ts
                tmp.r = r
                groups.append(tmp)
                ts = ""
    if ts != "":
        print("group create",ts)
        tmp = Group()
        tmp.val = ts
        tmp.r = r
        groups.append(tmp)
    r += 1
    if r==10:
        break

print(groups)
