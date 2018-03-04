import numpy as np

class game_state():

    #initialize
    def __init__(self, data):
     self.height = data["height"]
     self.width = data["width"]
     self.food = np.zeros((len(data["food"]), 2), dtype=int)
     for i in range(len(data["food"]["data"])):
         self.food[i,0] = data["food"]["data"][i]["x"]
         self.food[i,0] = data["food"]["data"][i]["y"]
     self.othersnakes = []
     self.thissnake = snake(data["you"])
     for i in range(len(data["snakes"]["data"])):
        if self.thissnake.id != data["snakes"]["data"][i]["id"]:
            self.othersnakes.append(snake(data["snakes"]["data"][i]))

     self.board = np.zeros((self.width, self.height), dtype=int)
     #0 = nothing, 1 = food, 2 = other snake, 3 = this snake
     for i in range(self.food.shape[0]):
         self.board[self.food[0], self.food[1]] = 1
     for s in range(len(self.othersnakes)):
         for b in range(self.othersnakes[s].length):
             self.board[self.othersnakes[s].body[b,0], self.othersnakes[s].body[b,1]] = 2
     for b in range(self.thissnake.length):
        self.board[self.thissnake.body[b,0], self.thissnake.body[b,1]] = 3

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
        return game_state(raw)

    def move():
     pass
    #find best move
    def find_food():
     pass
    #find safest food
    def read_board():
     pass
    #read board state

def get_example_raw():
    return {
      "food": {
        "data": [
          {
            "object": "point",
            "x": 0,
            "y": 9
          }
        ],
        "object": "list"
      },
      "height": 20,
      "id": 1,
      "object": "world",
      "snakes": {
        "data": [
          {
            "body": {
              "data": [
                {
                  "object": "point",
                  "x": 13,
                  "y": 19
                },
                {
                  "object": "point",
                  "x": 13,
                  "y": 19
                },
                {
                  "object": "point",
                  "x": 13,
                  "y": 19
                }
              ],
              "object": "list"
            },
            "health": 100,
            "id": "58a0142f-4cd7-4d35-9b17-815ec8ff8e70",
            "length": 3,
            "name": "Sonic Snake",
            "object": "snake",
            "taunt": "Gotta go fast"
          },
          {
            "body": {
              "data": [
                {
                  "object": "point",
                  "x": 8,
                  "y": 15
                },
                {
                  "object": "point",
                  "x": 8,
                  "y": 15
                },
                {
                  "object": "point",
                  "x": 8,
                  "y": 15
                }
              ],
              "object": "list"
            },
            "health": 100,
            "id": "48ca23a2-dde8-4d0f-b03a-61cc9780427e",
            "length": 3,
            "name": "Typescript Snake",
            "object": "snake",
            "taunt": ""
          }
        ],
        "object": "list"
      },
      "turn": 0,
      "width": 20,
      "you": {
        "body": {
          "data": [
            {
              "object": "point",
              "x": 8,
              "y": 15
            },
            {
              "object": "point",
              "x": 8,
              "y": 15
            },
            {
              "object": "point",
              "x": 8,
              "y": 15
            }
          ],
          "object": "list"
        },
        "health": 100,
        "id": "48ca23a2-dde8-4d0f-b03a-61cc9780427e",
        "length": 3,
        "name": "Typescript Snake",
        "object": "snake",
        "taunt": ""
      }
    }



class snake():
    def __init__(self, data_snake):
        self.health = data_snake["health"]
        self.id = data_snake["id"]
        self.length = data_snake["length"]
        self.name = data_snake["name"]
        bd = data_snake["body"]["data"]
        
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



def __main__():
    gs = game_state(get_example_raw())
    print "unit test"
    print gs.board
    print ""

if __name__ == "__main__":
    __main__()