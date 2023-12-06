#!/usr/bin/python3

inf = open("input.txt","r")
data = inf.readlines()
inf.close()

class Range:
    def __init__(self,dest,src,range):
        self.dest = int(dest)
        self.src = int(src)
        self.range = int(range)
    def __repr__(self):
        return str(self.dest) + " " + str(self.src) + " " + str(self.range)

def find_num(target, iranges):
    for r in iranges:
        if target >= r.src and target <= r.src+r.range:
            # print("matched this range",r, "target",target)
            adjust = target - r.src
            # print("need to adjust",adjust,r.dest+adjust)
            return r.dest + adjust
    return target

START = 0
SEED_TO_SOIL_MAP = 1
SOIL_TO_FERT = 2
FERT_TO_WATER = 3
WATER_TO_LIGHT = 4
LIGHT_TO_TEMP = 5
TEMP_TO_HUMID = 6
HUMID_TO_LOC = 7
state = START

seed_to_soil = []
seed_to_soil_m = {}

soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_humid = []
humid_to_loc = []

for line in data:
    if line.startswith("seeds:"):
        seed_nums = line.split(":")[1].split()
    elif line.startswith("seed-to-soil map:"):
        state = SEED_TO_SOIL_MAP
    elif line.startswith("soil-to-fertilizer map:"):
        state = SOIL_TO_FERT
    elif line.startswith("fertilizer-to-water map:"):
        state = FERT_TO_WATER
    elif line.startswith("water-to-light map:"):
        state = WATER_TO_LIGHT
    elif line.startswith("light-to-temperature map:"):
        state = LIGHT_TO_TEMP
    elif line.startswith("temperature-to-humidity map:"):
        state = TEMP_TO_HUMID
    elif line.startswith("humidity-to-location map:"):
        state = HUMID_TO_LOC
    else:
        line = line.rstrip()
        if line=="": continue
     
        tmp = line.rstrip().split()
     
        # dest source range
        r = Range(tmp[0],tmp[1],tmp[2])
    
        if state == SEED_TO_SOIL_MAP:
            seed_to_soil.append(r)
        elif state == SOIL_TO_FERT:
            soil_to_fert.append(r)
        elif state == FERT_TO_WATER:
            fert_to_water.append(r)
        elif state == WATER_TO_LIGHT:
            water_to_light.append(r)
        elif state == LIGHT_TO_TEMP:
            light_to_temp.append(r)
        elif state == TEMP_TO_HUMID:
            temp_to_humid.append(r)
        elif state == HUMID_TO_LOC:
            humid_to_loc.append(r)

def test1():
    res = find_num(79, seed_to_soil)
    print(res)
    res = find_num(14, seed_to_soil)
    print(res)
    res = find_num(55, seed_to_soil)
    print(res)
    res = find_num(13, seed_to_soil)
    print(res)

def test2():
    res = find_num(79,seed_to_soil)
    res1 = find_num(res,soil_to_fert)
    res2 = find_num(res1,fert_to_water)
    res3 = find_num(res2,water_to_light)
    res4 = find_num(res3,light_to_temp)
    res5 = find_num(res4,temp_to_humid)
    res6 = find_num(res5,humid_to_loc)

    print(res,res1,res2,res3,res4,res5,res6)

def part1():
    lowest = 999999999
    for n in seed_nums:
        n = int(n)

        res = find_num(n,seed_to_soil)
        res1 = find_num(res,soil_to_fert)
        res2 = find_num(res1,fert_to_water)
        res3 = find_num(res2,water_to_light)
        res4 = find_num(res3,light_to_temp)
        res5 = find_num(res4,temp_to_humid)
        res6 = find_num(res5,humid_to_loc)

        if res6<lowest:
            lowest=res6

    print("low",lowest)

def part2():

    lowest = 999999999

    seeds = []
    pos = 0
    print("len",len(seed_nums))
    while True:
        starting = int(seed_nums[pos])
        pos += 1
        r = int(seed_nums[pos])
        pos += 1
        for i in range(r):
            n = starting+i
            res = find_num(n,seed_to_soil)
            res1 = find_num(res,soil_to_fert)
            res2 = find_num(res1,fert_to_water)
            res3 = find_num(res2,water_to_light)
            res4 = find_num(res3,light_to_temp)
            res5 = find_num(res4,temp_to_humid)
            res6 = find_num(res5,humid_to_loc)
            if res6<lowest:
                lowest=res6


        if pos == len(seed_nums):
            break




    print("low",lowest)

c1 = {}
def find_num1(target, iranges):
    if target in c1: return c1[target]
    for r in iranges:
        if target >= r.src and target <= r.src+r.range:
            # print("matched this range",r, "target",target)
            adjust = target - r.src
            # print("need to adjust",adjust,r.dest+adjust)
            c1[target] = r.dest + adjust
            return r.dest + adjust
    c1[target] = target
    return target
c2 = {}
def find_num2(target, iranges):
    if target in c2: return c2[target]
    for r in iranges:
        if target >= r.src and target <= r.src+r.range:
            # print("matched this range",r, "target",target)
            adjust = target - r.src
            # print("need to adjust",adjust,r.dest+adjust)
            c2[target] = r.dest + adjust
            return r.dest + adjust
    c2[target] = target
    return target
c3 = {}
def find_num3(target, iranges):
    if target in c3: return c3[target]
    for r in iranges:
        if target >= r.src and target <= r.src+r.range:
            # print("matched this range",r, "target",target)
            adjust = target - r.src
            # print("need to adjust",adjust,r.dest+adjust)
            c3[target] = r.dest + adjust
            return r.dest + adjust
    c3[target] = target
    return target
c4={}
def find_num4(target, iranges):
    if target in c4: return c4[target]
    for r in iranges:
        if target >= r.src and target <= r.src+r.range:
            # print("matched this range",r, "target",target)
            adjust = target - r.src
            # print("need to adjust",adjust,r.dest+adjust)
            c4[target] = r.dest  + adjust
            return r.dest + adjust
    c4[target] = target
    return target
c5={}
def find_num5(target, iranges):
    if target in c5: return c5[target]
    for r in iranges:
        if target >= r.src and target <= r.src+r.range:
            # print("matched this range",r, "target",target)
            adjust = target - r.src
            # print("need to adjust",adjust,r.dest+adjust)
            c5[target] = r.dest + adjust
            return r.dest + adjust
    c5[target] = target
    return target
c6={}
def find_num6(target, iranges):
    if target in c6: return c6[target]
    for r in iranges:
        if target >= r.src and target <= r.src+r.range:
            # print("matched this range",r, "target",target)
            adjust = target - r.src
            # print("need to adjust",adjust,r.dest+adjust)
            c6[target] = r.dest + adjust
            return r.dest + adjust
    c6[target] = target
    return target
c7={}
def find_num7(target, iranges):
    if target in c7: return c7[target]
    for r in iranges:
        if target >= r.src and target <= r.src+r.range:
            # print("matched this range",r, "target",target)
            adjust = target - r.src
            # print("need to adjust",adjust,r.dest+adjust)
            c7[target] = r.dest + adjust
            return r.dest + adjust
    c7[target] = target
    return target

# big cache
cc={}

def part2a():
    lowest = 999999999

    seeds = []
    pos = 0
    print("len",len(seed_nums))
    while True:
        starting = int(seed_nums[pos])
        pos += 1
        r = int(seed_nums[pos])
        pos += 1
        print("checking r",pos,r)
        for i in range(r):
            n = starting+i
            if n in cc:
                res6 = cc[n]
                print("cc hit")
            else:
                res = find_num(n,seed_to_soil)
                res1 = find_num(res,soil_to_fert)
                res2 = find_num(res1,fert_to_water)
                res3 = find_num(res2,water_to_light)
                res4 = find_num(res3,light_to_temp)
                res5 = find_num(res4,temp_to_humid)
                res6 = find_num(res5,humid_to_loc)
                cc[n] = res6
            if res6<lowest:
                lowest=res6


        if pos == len(seed_nums):
            break




    print("low",lowest)





part2a()