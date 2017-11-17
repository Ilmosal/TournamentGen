class Player:
	"""
	A class for a single player. Contains the information of the single player
	
	Attributes:
		name (str): name of the player	

	"""
	def __init__(self, name):
		self.name = name

	def toString(self):
		return "Name: " + self.name

class Team:
	"""
	A class for a team. Contains players of the team.

	Attributes:
		name (str): name of the team
		players(Player): a list of player objects
		team_color(float[3]): the color of the players
	Args:
		
	"""
	def __init__(self, name, players, team_color):
		self.name = name
		self.players = players
		self.team_color = team_color

	def toString(self):
		team_string = "Team name: {0}\n".format(self.name)							
		for i in range(0, len(self.players)):
			team_string += "Player {0}\n{1}\n".format(i+1, self.players[i].toString())

		return team_string
