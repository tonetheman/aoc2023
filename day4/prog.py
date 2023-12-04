

inf = open("input.txt","r")
datalines = inf.readlines()
inf.close()

counter = 0
total_points = 0
for line in datalines:
    sides = line.split("|")

    # parse the front half
    side1 = sides[0].split(":")
    card_name = side1[0]
    winning_data = side1[1].lstrip().rstrip().split()

    # parse the other half
    have_data = sides[1].lstrip().rstrip().split()

    print(winning_data)
    print(have_data)
    points = 0
    for number_i_have in have_data:
        if number_i_have in winning_data:
            if points==0:
                points = 1
            else:
                points = points * 2
    
    print(card_name,points)
    total_points = total_points + points

    counter = counter + 1

print("total points",total_points)

# too high 142813
    