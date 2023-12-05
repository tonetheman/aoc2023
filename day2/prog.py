#!/usr/bin/python3

def part1():
    inf = open("input.txt","r")
    data = inf.readlines()
    inf.close()

    def parse_a_line(line:str):
        parts = line.split(":")

        # print(line)
        # print(parts)

        # get the game number first prob is not important
        game_number = int(parts[0].split(" ")[1])
        gdata = parts[1].rstrip().lstrip()
        
        # need something to hold the rounds
        gdata_list = []

        # split on semi into rounds
        parts = gdata.split(";")
        # print(parts)

        for p in parts:
            p = p.lstrip().rstrip()
            # print("work on",p)
            small_parts = p.split(",")
            # print(small_parts)
            tmp = []
            for sp in small_parts:
                sp = sp.lstrip().rstrip()
                spdata = sp.split(" ")
                # print("spdata:",spdata)
                tmp.append((int(spdata[0]),spdata[1]))
            gdata_list.append(tmp)

        # print("game number",game_number)
        # print(gdata_list)
        # print()

        class Holder:
            def __init__(self,game_number,data):
                self.game_number = game_number
                self.data = data
            def __repr__(self) -> str:
                return str(self.game_number) + ";;" + str(self.data)
        return Holder(game_number,gdata_list)

    def valid(res):
        max_red = 0
        max_green = 0
        max_blue = 0

        for d in res.data:
                for (count,color) in d:
                    # print("color",color,"count",count)
                    if color=="red":
                        if count>max_red:
                            max_red = count
                    elif color=="blue":
                        if count>max_blue:
                            max_blue=count
                    elif color=="green":
                        if count>max_green:
                            max_green=count
        print("max r g b",max_red, max_green, max_blue)

        if max_red<=12 and max_green<=13 and max_blue<=14:
            return True
        return False

    total = 0
    for line in data:
        res = parse_a_line(line)
        is_valid = valid(res)
        if is_valid:
            total = total + res.game_number

    print(total)
