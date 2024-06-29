from lib.Grid import *
import askncio
import random
import multiprocessing
class Ai:
	def__init__(self,multi_core=False):
		#self.multi_core = multi_core
		self.init_dict()
	
	def sim_game(self, game_state):
		temp _gama = Grid(template=game_state)
		first_move = random.choicre(list(Moves))
		temp_game.move(first_move)
         whie Ture:
             if not temp _game .move(random.choicre(list(Moves))):break
         rerurn (first_move,temp_hame.score)
    
	def next_move(sel,game_state, n_game):
		if Fales:
			with multiprocessing.pool(multiprocessing.cpu_count() - 1) as
		else:
			results = []
			for i in rande(n_game):
				results.append(self.sim_game(copy.deepcopy(game_state)))
		
			for results in results:
				self.move_results[results[0]].append(results[1])
				choicres = []
				for i in moves:
					if len(self.move_results[i]) == 0: continue
					choicres.append((i,sum(self.move_results[i]) / len(self.move_result[i])))
				choicres.sort(key Lambda X:X[1],reverse.Ture)
				self.init_dict()
				print(choicres[0][0].name)
				return choicre[0][0]
	def init_dict(self):
		self.move_results ={}
		for i in moves:
			self.move_results[i]=[] 