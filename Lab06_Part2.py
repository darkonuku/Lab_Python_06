print
print'-----------------------Part II_ 1 --------------------------'
print

class Player():
    def __init__(self,firstname,lastname,team = None):
        self.first_name = firstname
        self.last_name = firstname
        self.scores = []
        self.team = team

    def add_score(self,score):
        self.scores.append(score)
        return self.scores

    def total_score(self):
        self.score_total =0
        for i in self.scores:
            self.score_total += i
        return self.score_total

    def average_score(self):
        average = self.score_total/float(len(self.scores))
        return average


torres = Player('Fernando','Torres')
for i in [0,0,1,0,1]:
    torres.add_score(i)

torres.total_score()

print'The avrage score of', torres.first_name,'is', torres.average_score()


print
print'-----------------------Part 3 -------------------------'
print

class Team():
    def __init__(self, name, league,manager_name, points):
        self.new_name = name
        self.new_league = league
        self.new_manager = manager_name
        self.new_point = points
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        return self.players


    def __str__(self):
        output= 'the team '+str(self.new_name)+' plays in the '+\
                str(self.new_league)+' and is managed by '+str(self.new_manager)
        return output
    

portugal = Team('Portugal','Euro Leage','Darko Nuku',6)

spain = Team('Spain','Euro League','Sergio Fabiola', 7)

torres = Player('Fernando','Torres',spain)

ronaldo = Player('Christiano','Ronaldo',portugal)


portugal.add_player(ronaldo)
spain.add_player(torres)

#print portugal

class Match():
    def __init__(self, home_team,away_team,date,home_scores,away_scores):
        self.homeTeam = home_team
        self.awayTeam = away_team
        self.new_date = date
        self.homeScore = {}
        self.awayScore = {}

    def home_score(self):
        
        return sum(self.homeScore.values())

    def away_score(self):
        return sum(self.awayScore.values())

    def winner(self):
        if self.home_score() >self.away_score():
            return str(self.homeTeam.new_name)+': The home team is the winner'
        elif self.away_score() > self.home_score():
            return str(self.awayTeam.new_name)+': The away team is the winner'
        else:
            print'Its a draw'

    def add_score(self,player,score):

        playerTeam = player.team
        
        if player in self.homeScore:
            self.homeScore[player] +=1
        
        elif player in self.awayScore:
            self.awayScore[player] +=1

        elif player not in self.homeScore:
            self.homeScore[player] = int(score)
        else:
            self.awayScore[player] = int(score)
            
euro_semi_final = Match(spain,portugal,'June 27, 2012',0,0)

euro_semi_final.add_score(torres,1)
euro_semi_final.add_score(ronaldo,1)
euro_semi_final.add_score(torres,1)

print euro_semi_final.winner()

        

        

        
        
        
        

        
