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

     self.board = np.zeros((self.width, self.height), dtype=int)
     #0 = nothing, 1 = food, 2 = other snake, 3 = this snake
     for i in range(self.food):
         self.board[self.food[0], self.food[1]] = 1
     for s in range(len(self.othersnakes)):
         for b in range(len(self.othersnakes[s].length)):
             self.board[self.othersnakes[s].body[b,0], self.othersnakes[s].body[b,0]] = 2
     for b in range(self.thissnake.length):
        self.board[self.thissnake.body[b,0], self.thissnake.body[b,0]] = 3

    def alltails(self):
        tails = []
        for s in self.othersnakes:
            tails.append(tuple(s.tail))
        return tails

    def allheads(self):
        heads = []
        for s in self.othersnakes:
            heads.append(tuple(s.head))
        return heads

 
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
        
        self.body = np.zeros((len(bd),2), dtype=int)
        for i in range(self.body.shape[0]):
            self.body[i,0] = bd[i]["x"]
            self.body[i,1] = bd[i]["y"]
        self.bodyx = self.body[:,0]
        self.bodyy = self.body[:,1]
        self.head = self.body[0]
        self.tail = self.body[-1]
    def get_head(self):
        return self.body[0]
    def get_tail(self):
        return self.body[-1]
        