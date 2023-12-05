#!/usr/bin/python3

inf = open("sample.txt","r")
data = inf.readlines()
inf.close()

START = 0
SEED_TO_SOIL_MAP = 1
SOIL_TO_FERT = 2
FERT_TO_WATER = 3
WATER_TO_LIGHT = 4
LIGHT_TO_TEMP = 5
TEMP_TO_HUMID = 6
HUMID_TO_LOC = 7
state = START

for line in data:
    if line.startswith("seeds:"):
        seed_nums = line.split(":")[1].split()
        print("seed nums",seed_nums)
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
        if state == SEED_TO_SOIL_MAP:
            tmp = line.rstrip().split()
            print("seed to soil",tmp)