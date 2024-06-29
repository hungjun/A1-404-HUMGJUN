from lib.Grid import *
import asyncio
import random
import multiprocessing
class AI:
	def __init__(self,multi_core=False):
		#self.multi_core = multi_core
		self.init_dict()
	
	def sim_game(self, game_state):
		temp_game = Grid(template=game_state)
		first_move = random.choice(list(Moves))
		temp_game.move(first_move)
		while True:
			if not temp_game.move(random.choice(list(Moves))):break
		return (first_move,temp_game.score())

	def next_move(self,game_state, n_games):
		if False:
			return
		else:
			results = []
			for i in range(n_games):
				results.append(self.sim_game(copy.deepcopy(game_state)))
		
			for results in results:
				self.move_results[results[0]].append(results[1])
				choices = []
				for i in Moves:
					if len(self.move_results[i]) == 0: continue
					choices.append((i,sum(self.move_results[i]) / len(self.move_results[i])))
				choices.sort(key=lambda X:X[1],reverse=True)
				self.init_dict()
				print(choices[0][0].name)
				return choices[0][0]
	def init_dict(self):
		self.move_results ={}
		for i in Moves:
			self.move_results[i]=[] 
