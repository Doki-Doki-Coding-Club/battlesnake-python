import numpy as np

class game_state():

    #initialize
    def __init__(self, data):
     self.height = data["height"]
     self.width = data["width"]
     self.food = np.zeros((len(data["food"], 2)), dtype=int)
     for i in range(len(data["food"])):
         self.food[i,0] = data["food"]["data"][i]["x"]
         self.food[i,0] = data["food"]["data"][i]["y"]
     self.othersnakes = []
     self.thissnake = snake(data["you"])
     for i in range(len(data["snakes"]["data"])):
        if self.thissnake.id != data["snakes"]["data"][i]["id"]:
            self.othersnakes.append(snake(data["snakes"]["data"][i]))

     self.board = np.zeros((self.width, self.height))

 
 
    def move():
     pass
    #find best move
    def find_food():
     pass
    #find safest food
    def read_board():
     pass
    #read board state

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
    def get_head(self):
        return self.body[0]
    def get_tail(self):
        return self.body[-1]
        