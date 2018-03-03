import numpy as np

class game_state():

	#initialize
	def __init__(self, data):
	# 0 = nothing, 1 = food, 2 = other snake, 3 = us
		self.width = data["width"]
		self.height = data["height"]
		self.food = np.zeros((len(data["food"], 2)), dtype=int)
		
		for i in range(len(data["food"])):
			self.food[i,0] = data["food"]["data"][i]["x"]
			self.food[0,i] = data["food"]["data"][i]["y"]
		
		
		self.othersnakes = []
		self.thissnake = snake(data["you"])
		for i in range(len(data["snakes"]["data"])):
			if self.thissnake.id != data["snakes"]["data"][i]["id"]:
				self.othersnakes.append(snake(data["snakes"]["data"][i]))

	
	def head_pos(self, data):
		self.head = data["you"]["body"]["data"][0]
		
		return self.head
	
	def next_move(self, width, height):
		x = head_pos(data)["x"]
		y = head_pos(data)["y"]
		if x > width or x < 0:
			return 'up'
		if y > height or y < 0:
			return 'right'
		
	
		
		
				


class snake():
    def __init__(self, data_snake):
        self.health = data_snake["health"]
        self.id = data_snake["id"]
        self.length = data_snake["length"]
        self.name = data_snake["name"]

        bd = data_snake["body"]
        
        self.body = np.zeros((len(data_snake),2), dtype=int)
        for i in range(self.body.shape[0]):
            self.body[i,0] = data_snake[i]["x"]
            self.body[i,1] = data_snake[i]["y"]

        self.head = self.body[0]
        self.tail = self.tail[-1]
    def get_head(self):
        return self.body[0]
    def get_tail(self):
		return self.body[-1]

    def get_head(self):
        return self.body[0]
    def get_tail(self):
        return self.body[-1]

