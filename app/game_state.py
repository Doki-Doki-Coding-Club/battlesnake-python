import numpy as np

class Game_State():
	
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
		
	
	def near_end(self, x, y):
		if x < 0 or x > width:
			return 'left'
		if y < 0 or y > height:
			return 'up'

		