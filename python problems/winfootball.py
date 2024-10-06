def find_winning_team(n,teams):
    team_goals={}
    for team in teams:
        if team in team_goals:
            team_goals[team]+=1
        else:
            team_goals[team]=1
        winning_team=max(team_goals,key=team_goals.get)
        return winning_team  
n=5
teams=["TeamA","TeamB","TeamA","TeamB","TeamB"]
winner=find_winning_team(n,teams)
print(winner)    