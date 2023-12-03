#!/usr/bin/python3

inf = open("input.txt","r")
data = inf.readlines()
inf.close()

groups = []


def is_part(v):
    return v in ['0','1','2','3','4','5','6','7','8','9']

def pg(g):
    for line in g:
        print(line)

def make_grid(data):
    grid = []
    for line in data:
        line=line.rstrip()
        tmp = []
        for c in line:
            if c=='.':
                tmp.append('.')
            elif is_part(c):
                tmp.append(c)
            else:
                tmp.append(c)
        grid.append(tmp)
    return grid


def look_for_symbol(grid,r,c):
    
    def get_val(_r,_c):
        try:
            tmp = grid[_r][_c]
        except IndexError:
            return '.'
        return tmp
    
    def check(_v):
        if _v=='.' or is_part(_v):
            return False
        return True

    # diag
    tmp = get_val(r+1,c+1) # diag front right
    if check(tmp):
        return True
    tmp = get_val(r-1,c-1) # diag back left
    if check(tmp):
        return True
    tmp = get_val(r-1,c+1)
    if check(tmp):
        return True
    tmp = get_val(r+1,c-1)
    if check(tmp):
        return True
    
    # ahead
    tmp = get_val(r,c+1)
    if check(tmp):
        return True
    # behind
    tmp = get_val(r,c-1)
    if check(tmp):
        return True
    # up
    tmp = get_val(r-1,c)
    if check(tmp):
        return True
    # down
    tmp = get_val(r+1,c)
    if check(tmp):
        return True
    
    return False

groups = {}
current_group = ""
in_group = False
has_sym = False
grid = make_grid(data)
pg(grid)

for i in range(len(grid)): # rows
    for j in range(len(grid[0])): # cols
        if is_part(grid[i][j]):
            if in_group:
                current_group = current_group + str(grid[i][j])
                if look_for_symbol(grid,i,j):
                    has_sym = True
            else:
                # make a new group
                in_group = True
                current_group = str(grid[i][j])
                if look_for_symbol(grid,i,j):
                    has_sym = True
        else:
            if current_group=="":
                pass
            else:
                if not current_group in groups:
                    groups[current_group] = 1

            if has_sym:
                print("this group had a sym",current_group)
                groups[current_group] = 0

            # not a part reset group
            current_group = ""
            in_group = False
            has_sym = False
        
        # print("current group",current_group)

total = 0
for k in groups.keys():
    if groups[k]==0:
        print(k)
        total = total + int(k)
print(total)