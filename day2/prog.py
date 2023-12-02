inf = open("sample1.txt","r")
data = inf.readlines()
inf.close()


def parse_a_line(line:str):
    parts = line.split(" ")

    print(line)
    print(parts)

    game_number = int(parts[1].split(":")[0])

    print("game number",game_number)

    print()

parse_a_line(data[0])