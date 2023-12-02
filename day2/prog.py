#!/usr/bin/python3

inf = open("sample1.txt","r")
data = inf.readlines()
inf.close()

def parse_a_line(line:str):
    parts = line.split(":")

    print(line)
    print(parts)

    # get the game number first prob is not important
    game_number = int(parts[0].split(" ")[1])
    gdata = parts[1].rstrip().lstrip()
    
    # need something to hold the rounds
    gdata_list = []

    # split on semi into rounds
    parts = gdata.split(";")
    print(parts)

    for p in parts:
        p = p.lstrip().rstrip()
        print("work on",p)
        small_parts = p.split(",")
        print(small_parts)
        tmp = []
        for sp in small_parts:
            sp = sp.lstrip().rstrip()
            spdata = sp.split(" ")
            print("spdata:",spdata)
            tmp.append((int(spdata[0]),spdata[1]))
        gdata_list.append(tmp)

    print("game number",game_number)
    print(gdata_list)
    print()

    class Holder:
        def __init__(self,game_number,data):
            self.game_number = game_number
            self.data = data
        def __repr__(self) -> str:
            return str(self.game_number) + ";;" + str(self.data)
    return Holder(game_number,gdata_list)

res = parse_a_line(data[0])
print(res)