"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure



## implement highest_score



## implement highest_score_for_player



## implement highest_scorer


import datetime

Player = raw_input('Enter the player name: ')

Month = str(datetime.date.today().month)
Day = str(datetime.date.today().day)
Year = str(datetime.date.today().year)
Date = Month +'/'+Day + '/' + Year

Score = raw_input('Enter the player score: ')
score_list = []
player_list = []
player_list.append(Player)
player_list.append(Date)
player_list.append(Score)
score_list.append(Score)

confirm = raw_input("Enter another record? 'y/n' : ")


while confirm == "y":
    
    Player = raw_input('Enter the player name: ')

    Month = str(datetime.date.today().month)
    Day = str(datetime.date.today().day)
    Year = str(datetime.date.today().year)
    Date = Month +'/'+Day + '/' + Year

    Score = raw_input('Enter the player score: ')
    
    player_list.append(Player)
    player_list.append(Date)
    player_list.append(Score)
    score_list.append(Score)
    
    confirm = raw_input("Enter another record? 'y/n' : ")
print'Player'+'\t'+'|'+' Date'+'\t\t|'+'Score'
print'____________________________________'
count = 0
for i in player_list:
    print i,'\t|',
    count+=1
    if count % 3 == 0:
        print


print
print'-----------------------------------------------------'
print
def highest_score(score_list):
    scorer = ()
    highest = 0
    for i in score_list:
        if i >= highest:
            highest = i

    x = player_list.index(highest)
    highest_name = player_list[x-2]
    highest_date = player_list[x-1]

    highest_info = (highest_name,highest_date,highest)

    print 'the highest score is ' ,highest_info
            
highest_score(score_list)

print
print'-----------------------------------------------------'
print



