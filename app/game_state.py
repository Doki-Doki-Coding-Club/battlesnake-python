import numpy as np

class game_state():

    def __init__(self, height, width, game_id):
        self.width = width
        self.height = height
        self.id = game_id
        
        self.board = np.zeros((height,width), dtype=int)
        self.board_e = np.zeros((height,width), dtype=int)
        self.snakes = []
		self.food = []
		
	def parse_data(self, data):
		#process the data, from Patrick Ryan (bailed on us last minute but here in spirit)
		self.snakes = []
        self.board = np.zeros((self.height,self.width), dtype=int)
        for snake in data["snakes"]:
            if snake["id"] == data["you"]:
                self.snakes.insert(0,snake)
            else:
                self.snakes.append(snake)
        
        self.board = self.parse_board(True)
        self.board_e = self.parse_board(False)
		self.food = data["food"]["data"]
		
	def move():
	#find best move
	
	
	def find_food():
	#find safest food
	def read_board():
	#read board state
		