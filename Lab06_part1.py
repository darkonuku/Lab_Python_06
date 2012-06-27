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
player_stats = []
player_stats.append(Player)
player_stats.append(Date)
player_stats.append(Score)
score_list.append(Score)

confirm = raw_input("Enter another record? 'y/n' : ")


while confirm == "y":
    
    Player = raw_input('Enter the player name: ')

    Month = str(datetime.date.today().month)
    Day = str(datetime.date.today().day)
    Year = str(datetime.date.today().year)
    Date = Month +'/'+Day + '/' + Year

    Score = raw_input('Enter the player score: ')
    
    player_stats.append(Player)
    player_stats.append(Date)
    player_stats.append(Score)
    score_list.append(Score)
    
    confirm = raw_input("Enter another record? 'y/n' : ")

print'Player'+'\t'+'|'+' Date'+'\t\t|'+'Score'
print'____________________________________'
count = 0
for i in player_stats:
    print i,'\t|',
    count+=1
    if count % 3 == 0:
        print


print
print'-------------------------Part I_ 1a----------------------------'
print
def highest_score(score_list):
    scorer = ()
    highest = 0
    for i in score_list:
        if i >= highest:
            highest = i

    x = player_stats.index(highest)
    highest_name = player_stats[x-2]
    highest_date = player_stats[x-1]

    highest_info = (highest_name,highest_date,highest)

    print 'the highest score is ' ,highest_info
            
highest_score(score_list)

print
print'------------------------Part I_ 1b-----------------------------'
print



def highest_score_for_player(player_stats, Player_name):
    player_score = []
    highest = 0
    if Player_name in player_stats:
        for i in range(len(player_stats)):
            if player_stats[i] == Player_name:
                player_score.append(player_stats[i+2])
    else:
        print 'None'
        print
    for j in player_score:
        if j>= 0:
            highest = j
    x = player_stats.index(highest)
    highest_name = player_stats[x-2]
    highest_date = player_stats[x-1]

    highest_info = (highest_name,highest_date,highest)
    
    print 'the highest score of',Player_name ,highest_info
                

highest_score_for_player(player_stats, 'nuku')
highest_score_for_player(player_stats, 'mensah')
        
        
        
    

