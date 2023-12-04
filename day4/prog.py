


def part1():
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



def part2():
    inf = open("input.txt","r")
    datalines = inf.readlines()
    inf.close()


    card_counts = [0]*250 # card 0 does not exist!
    total_points = 0


    for i in range(1,len(datalines)+1):
        card_counts[i]=1
    print(card_counts)

    for line in datalines:
        print(line.rstrip())
        sides = line.split("|")

        # parse the front half
        side1 = sides[0].split(":")
        card_name = side1[0]
        card_number = int(card_name.split()[1])

        winning_data = side1[1].lstrip().rstrip().split()

        # parse the other half
        have_data = sides[1].lstrip().rstrip().split()

        # how many copies do we have?
        number_of_copies_of_me = card_counts[card_number]

        winning_count = 0
        for number_i_have in have_data:
            if number_i_have in winning_data:
                winning_count = winning_count + 1

        for j in range(number_of_copies_of_me):  
            start=card_number+1
            for i in range(winning_count):
                card_counts[start+i]=card_counts[start+i]+1

    print(card_counts)
    total = 0
    for c in card_counts:
        total = total + c
    print(total)

