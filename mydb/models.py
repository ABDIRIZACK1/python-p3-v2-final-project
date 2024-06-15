class Team:
    def _init_(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city

class Player:
    def _init_(self, id, name, team_id, position):
        self.id = id
        self.name = name
        self.team_id = team_id
        self.position = position
        
        
        