import numpy as np

class game_state():

	#initialize
	def __init__(self, data):
     self.food = np.zeros((len(data["food"], 2)), dtype=int)
     for i in range(len(data["food"])):
         self.food[i,0] = data["food"]["data"][i]["x"]
         self.food[i,0] = data["food"]["data"][i]["y"]
    self.othersnakes = []
    for i in range(len(data["snakes"]["data"])):
        self.othersnakes.append(snake(data["snakes"]["data"]["body"]["data"]))
    self.thissnake = snake(data["you"]["body"]["data"])
    self.health = data["health"]
    self.length = data["length"]



 
	def move():
	#find best move
	def find_food():
	#find safest food
	def read_board():
	#read board state

class snake():
    def __init__(self, data_snake):
        self.body = np.zeros((len(data_snake),2), dtype=int)
        for i in range(self.body.shape[0]):
            self.body[i,0] = data_snake[i]["x"]
            self.body[i,1] = data_snake[i]["y"]
    def get_head(self):
        return self.body[0]
    def get_tail(self):
        return self.body[-1]
        