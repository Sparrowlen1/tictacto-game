import math
import random

class player:
    def __init__(self,letter) -> None:
        # where the letter can be x or o
        self.letter=letter

        # now we want our players ot get the next move
        pass
    def get_move():
        pass

# now we are going to define our machine or computer player through inheritance

class RandomComputerPlayer(player):
    def __init__(self, letter) -> None:
        super().__init__(letter) #this super function inherits all the properties of the subclass
        pass
    def get_move(self,game):
        box=random.choice(game.available_moves())
        return box

# now we define our human player

class HumanPlayer(player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
        pass
    def get_move(self,game):
        valid_square=False
        val=None
        while not valid_square:
            box=input(self.letter + 'input the move in terms of ranges (0-9)')
        try:
            val=int(box)
            if val not in game.available_moves():
                raise valid_square
            valid_square=True
        except ValueError:
            print('invalid bos try again')        

        return val    