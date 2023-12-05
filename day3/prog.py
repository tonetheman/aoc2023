#!/usr/bin/python3

from typing import List


inf = open("sample.txt","r")
data = inf.readlines()
inf.close()

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
            else:
                v = self.get(computed_r,computed_c)
                if not v in ['.','0','1','2','3','4','5','6','7','8','9']:
                    return True
        return False

grid = Grid(data)
groups = []

rindex = 0
for line in grid.grid:
    cindex = 0
    in_group = False
    current_group = ""
    current_group_status = False
    for c in line:
        if c in ['0','1','2','3','4','5','6','7','8','9']:
            if in_group:
                current_group = current_group + str(c)
            else:
                in_group = True
                current_group = current_group + str(c)
            if grid.check(rindex,cindex):
                if current_group_status==False:
                    current_group_status = True
        elif c=='.':
            if in_group:

                print("not in group anymore",current_group_status,current_group)
                # no longer in a group
                in_group = False
                current_group = ""
                current_group_status = False
        print(current_group)
    
    if in_group:
        print("in group at end of line")

        cindex += 1
    rindex += 1