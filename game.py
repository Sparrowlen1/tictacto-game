from player import HumanPlayer,RandomComputerPlayer
class  tictactoe:
    def __init__(self) -> None:
        self.board = ["" for _ in range(9)] #this will represent the 3*3 format
        self.current_winner = None
        pass

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
            print('|' + '|' .join(row) +'|')   

# game = tictactoe()
# game.print_board()   
# print(game)
    @staticmethod
    def print_boardnums():
        numberboard=[[str(i) for i in range(j*3,(j+3)*3)]for j in range(3)]
        for row in numberboard:
            print('|' + '|' .join(row) +'|')
    def available_moves():
        return [i for i,spot in enumerate(self.board) if spot==""] #this is a list comprehension 
    
    
    def empty_squares():
        return " " in self.board
    
    def numberofemptyspaces():
        return self.board.count(' ')
    
    def make_move(self,box,letter):
        if self.board[box] == " ": #if the space in that box is empty we assign that letter to the box as shown below
           self.board[box]=letter 
           if self.winner(box,letter):
               self.current_winner=letter
           return True
        return False
    def winner(self,box,letter):
        row_ind= box//3
        row = self.board[row_ind*3:(row_ind+1)*3]   
        if all([spot==letter for spot in row]): #this is a checker to check spots in the row are letters
            return True 
# now we are going to check the columns
        col_ind = box%3
        column=[self.board[col_ind+i*3] for i in range(3)]
        if all([spot==letter for spot in column]): #this is a checker to check if spots in the column are letters
            return True
# now we are going to check the diagonal
# to do this easily we are going to check if it is divisble by 2 since the indexes of the 3*3 of the diagonals are multiples of 2 i.e 02468
        if box%2==0:
            diagonal1=[self.board[i] for i in [0,4,8]] # diagonal from right to left of the tictacto
            if all([spot==letter for spot in diagonal1]): #this is a checker to check if spots in diagnol1 are letters
                return True            
            diagonal2=[self.board[i] for i in range[2,4,6]]
            if all([spot==letter for spot in diagonal2]): #this is a checker to check if spots in diagnol2 are letters
                return True
            # if all the checks fails we dont have a winner so we return falls
            return False   
def play (game, x_player,o_player, print_game=True):
    #we are going to return the winner if their is one
    if print_game:
        return game.print_boardnums()
    letter='X'

    while game.empty_squares():
        if letter == 'O':
            box= o_player.get_move(game)
        else:
            box=x_player.get_move(game)

        if game.make_move(box,letter):
            if print_game:
                print(letter + f"makes a movie to the box {box}")        
                game.print_board()
                print(' ') #just an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!')    
                    return letter
            letter = 'o' if letter == 'x' else 'x' #we are just switching players    

        if print_game:
            print("it's a tie")        


if __name__=="__main__":
    x_player= HumanPlayer('X')
    o_player= RandomComputerPlayer('O')
    t= tictactoe()
    play(t,x_player,o_player,print_game=True)