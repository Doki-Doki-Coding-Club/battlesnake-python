import numpy as np

class game_state():
	
	def head_pos(self, data):
		self.head = data["you"]["body"]["data"][0]
		
		return self.head
	
	def move(self, data):
		x = head_pos(data)["x"]
		
		pass
	
	def near_end(self, x, y):
		if x < 0 or x > width:
			return 'left'
		if y < 0 or y > height:
			return 'up'

		