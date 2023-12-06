
import std/strutils

proc makefilebuffer*(inputfile:string) : seq[string] =
    var buffer : seq[string]
    for line in lines(inputfile):
        buffer.add(line)
    return buffer

proc find_num(target : int64, iranges : seq[ tuple[dest:int,src:int,range:int]]) : int64 =
    for r in iranges:
        if target >= r.src and target <= r.src+r.range:
            # print("matched this range",r, "target",target)
            let adjust = target - r.src
            # print("need to adjust",adjust,r.dest+adjust)
            return r.dest + adjust
    return target


type States = enum
    START = 0, SEED_TO_SOIL_MAP = 1, SOIL_TO_FERT = 2, 
    FERT_TO_WATER = 3, WATER_TO_LIGHT = 4, LIGHT_TO_TEMP = 5,
    TEMP_TO_HUMID = 6,HUMID_TO_LOC = 7

var state = START

var seed_to_soil : seq[ tuple[dest:int,src:int,range:int]]
var soil_to_fert : seq[ tuple[dest:int,src:int,range:int]]
var fert_to_water : seq[ tuple[dest:int,src:int,range:int]]
var water_to_light : seq[ tuple[dest:int,src:int,range:int]]
var light_to_temp : seq[ tuple[dest:int,src:int,range:int]]
var temp_to_humid : seq[ tuple[dest:int,src:int,range:int]]
var humid_to_loc : seq[ tuple[dest:int,src:int,range:int]]

let data = makefilebuffer("sample.txt")
var seed_nums : seq[string]
for line in data:
    if line.startsWith("seeds:"):
        seed_nums = line.strip().split(":")[1].strip().split()
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
        if line.strip()=="": continue

        let tmp = line.strip().split()
        echo(tmp)
        let r = (dest:parseInt(tmp[0]),src:parseInt(tmp[1]),range:parseInt(tmp[2]))
        if state==SEED_TO_SOIL_MAP:
            seed_to_soil.add(r)
        elif state == SOIL_TO_FERT:
            soil_to_fert.add(r)
        elif state == FERT_TO_WATER:
            fert_to_water.add(r)
        elif state == WATER_TO_LIGHT:
            water_to_light.add(r)
        elif state == LIGHT_TO_TEMP:
            light_to_temp.add(r)
        elif state == TEMP_TO_HUMID:
            temp_to_humid.add(r)
        elif state == HUMID_TO_LOC:
            humid_to_loc.add(r)


var lowest : int64 = 999999999
var pos = 0
while true:
    let starting = parseInt(seed_nums[pos])
    pos=pos+1
    let r = parseInt(seed_nums[pos])
    pos=pos+1
    for i in 0 ..< r:
        let n = starting+i
        let res = find_num(n,seed_to_soil)
        let res1 = find_num(res,soil_to_fert)
        let res2 = find_num(res1,fert_to_water)
        let res3 = find_num(res2,water_to_light)
        let res4 = find_num(res3,light_to_temp)
        let res5 = find_num(res4,temp_to_humid)
        let res6 = find_num(res5,humid_to_loc)

        if res6<lowest:
            lowest=res6
    if pos==len(seed_nums):
        break

echo(lowest)