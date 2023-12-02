
class GameData:
    color:str
    count:int

class Game:
    id : int
    data : "list[GameData]"


inf = open("sample1.txt","r")
data = inf.readlines()
inf.close()

def parse_a_line(line:str):
    parts = line.split(":")

    print(line)
    print(parts)

    game_number = int(parts[0].split(" ")[1])
    gdata = parts[1].rstrip().lstrip()
    gdata_list = []

    parts = gdata.split(";")
    print(parts)
    for p in parts:
        p = p.lstrip().rstrip()
        print("work on",p)
        small_parts = p.split(",")
        print(small_parts)
        for sp in small_parts:
            sp = sp.lstrip().rstrip()
            spdata = sp.split(" ")
            print("spdata:",spdata)
            gdata_list.append((int(spdata[0]),spdata[1]))

    print("game number",game_number)
    print(gdata_list)
    print()

parse_a_line(data[0])