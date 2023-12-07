#!/usr/bin/python3

inf = open("sample.txt","r")
data = inf.readlines()
inf.close()

NO_SCORE = "noscore"
FIVE_OF_KIND = "fiveofkind"
FOUR_OF_KIND = "fourofkind"
FULL_HOUSE = "fullhouse"
THREE_OF_KIND ="theeofkind"

def score_hand(line):
    tmp = line.rstrip().split()
    print(tmp)
    s_hand = tmp[0]
    hand = []
    for c in s_hand:
        hand.append(c)
    hand.sort()
    print(hand)
    score = NO_SCORE
    if (hand[0]==hand[1]) and (hand[1]==hand[2]) and (hand[2]==hand[3]) and \
        (hand[3]==hand[4]):
        score = FIVE_OF_KIND
    elif ((hand[0]==hand[1]) and(hand[1]==hand[2]) and (hand[2]==hand[3])) or \
        ((hand[1]==hand[2]) and (hand[2]==hand[3]) and (hand[3]==hand[4])):
        score = FOUR_OF_KIND
    elif ((hand[0]==hand[1]) and (hand[1]==hand[2]) and (hand[3]==hand[4])) or \
        ((hand[0]==hand[1]) and (hand[2]==hand[3]) and (hand[3]==hand[4])):
        score = FULL_HOUSE
    elif ((hand[0]==hand[1]) and (hand[1]==hand[2])) or \
        ((hand[1]==hand[2]) and (hand[2]==hand[3])) or \
        ((hand[2]==hand[3]) and (hand[3]==hand[4])):
        score = THREE_OF_KIND

    print(score)
    return score

assert(score_hand("AAAAA 45")==FIVE_OF_KIND)
assert(score_hand("22223 1")==FOUR_OF_KIND)
assert(score_hand("34444 1")==FOUR_OF_KIND)
assert(score_hand("AA222 1")==FULL_HOUSE)
assert(score_hand("AAA22 1")==FULL_HOUSE)
assert(score_hand("AAA45 1")==THREE_OF_KIND)
assert(score_hand("4AAA5 1")==THREE_OF_KIND)
assert(score_hand("45AAA 1")==THREE_OF_KIND)
