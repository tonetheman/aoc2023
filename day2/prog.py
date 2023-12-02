
from dataclasses import dataclass

@dataclass
class Game:
    game_number:int

inf = open("sample1.txt","r")
data = inf.readlines()
inf.close()

def parse_a_line(line:str):
    parts = line.split(":")

    print(line)
    print(parts)

    game_number = int(parts[0].split(" ")[1])
    gdata = parts[1].rstrip().lstrip()

    parts = gdata.split(";")
    print(parts)
    for p in parts:
        p = p.lstrip().rstrip()
        print("work on",p)
        small_parts = p.split(",")
        print(small_parts)

    print("game number",game_number)
    print()

parse_a_line(data[0])