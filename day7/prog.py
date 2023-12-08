#!/usr/bin/python3

NO_SCORE = "noscore"
FIVE_OF_KIND = "fiveofkind"
FOUR_OF_KIND = "fourofkind"
FULL_HOUSE = "fullhouse"
THREE_OF_KIND ="theeofkind"
TWO_PAIR = "twopair"
ONE_PAIR = "onepair"
HI_CARD = "hicard"

def score_hand(line):
    tmp = line.rstrip().split()
    s_hand = tmp[0]
    hand = []
    for c in s_hand:
        hand.append(c)
    hand.sort()
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
    elif (hand[0]==hand[1]) and (hand[2]==hand[3]) or \
        (hand[0]==hand[1]) and (hand[3]==hand[4]) or \
        (hand[1]==hand[2]) and (hand[3]==hand[4]):
        score = TWO_PAIR
    elif (hand[0]==hand[1]) or \
        (hand[1]==hand[2]) or \
        (hand[2]==hand[3]) or \
        (hand[3]==hand[4]):
        score = ONE_PAIR
    else:
        score = HI_CARD

    return score

def test1():
    assert(score_hand("AAAAA 45")==FIVE_OF_KIND)
    assert(score_hand("22223 1")==FOUR_OF_KIND)
    assert(score_hand("34444 1")==FOUR_OF_KIND)
    assert(score_hand("AA222 1")==FULL_HOUSE)
    assert(score_hand("AAA22 1")==FULL_HOUSE)
    assert(score_hand("AAA45 1")==THREE_OF_KIND)
    assert(score_hand("4AAA5 1")==THREE_OF_KIND)
    assert(score_hand("45AAA 1")==THREE_OF_KIND)
    assert(score_hand("22334 1")==TWO_PAIR)
    assert(score_hand("22433 1")==TWO_PAIR)
    assert(score_hand("42233 1")==TWO_PAIR)
    assert(score_hand("KK456 1")==ONE_PAIR)
    assert(score_hand("4KK56 1")==ONE_PAIR)
    assert(score_hand("45KK6 1")==ONE_PAIR)
    assert(score_hand("456KK 1")==ONE_PAIR)
    assert(score_hand("A2345 1")==HI_CARD)

inf = open("sample.txt","r")
data = inf.readlines()
inf.close()

class RData:
    def __init__(self,line):
        self.line = line
        self.score = score_hand(self.line)
        self.dead = False
        self.rank = -1
    def __repr__(self):
        return str(self.dead) + " " + self.score + " " + self.line

all_items = set()
rd = []
for line in data:
    tmp = RData(line)
    rd.append(tmp)
    all_items.add(tmp)

card_power = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

rank = 1
# five of kind first
# four of kind next
# full house
# three of kind
tmp = set()
for i in range(len(rd)):
    r = rd[i]
    if r.dead: continue
    if r.score==THREE_OF_KIND:
        tmp.add(r)
        r.dead = True
        r.rank = 10
print(rd)
print(tmp)
