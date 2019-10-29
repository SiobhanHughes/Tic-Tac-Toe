# Set up board and rules of Tic Tac Toe

class Board:
    
    def __init__(self): #board set up - 3 lists
        self.board_line1 = [' ', ' ', ' ']
        self.board_line2 = [' ', ' ', ' ']
        self.board_line3 = [' ', ' ', ' ']


    def display_board(self):
        print(self.board_line1[0], '|', self.board_line1[1], '|', self.board_line1[2])
        print('---------')
        print(self.board_line2[0], '|', self.board_line2[1], '|', self.board_line2[2] )
        print('---------')
        print(self.board_line3[0], '|', self.board_line3[1], '|', self.board_line3[2])
        print('---------')
        print(' ')
        
    def clear_board(self):
        self.board_line1 = [' ' for i in self.board_line1]
        self.board_line2 = [' ' for i in self.board_line2]
        self.board_line3 = [' ' for i in self.board_line3]
        
    def is_not_full(self):
        if self.board_line1.count(' ') == 0 and self.board_line2.count(' ') == 0 and self.board_line3.count(' ') == 0:
            return False
        else:
            return True

            
    def win(self): #rules of tic-tac-toe
        if self.board_line1[0] == '0' and self.board_line2[0] == '0' and self.board_line3[0] =='0':
            return '0'
        elif self.board_line1[0] == 'X' and self.board_line2[0] == 'X' and self.board_line3[0] =='X':
            return 'X'
        elif self.board_line1[1] == '0' and self.board_line2[1] == '0' and self.board_line3[1] =='0':
            return '0'
        elif self.board_line1[1] == 'X' and self.board_line2[1] == 'X' and self.board_line3[1] =='X':
            return 'X'
        elif self.board_line1[2] == '0' and self.board_line2[2] == '0' and self.board_line3[2] =='0':
            return '0'
        elif self.board_line1[2] == 'X' and self.board_line2[2] == 'X' and self.board_line3[2] =='X':
            return 'X'
        elif self.board_line1.count('0') == 3 or self.board_line2.count('0') == 3 or self.board_line3.count('0') == 3:
            return '0'
        elif self.board_line1.count('X') == 3 or self.board_line2.count('X') == 3 or self.board_line3.count('X') == 3:
            return 'X'
        elif self.board_line1[0] == '0' and self.board_line2[1] == '0' and self.board_line3[2] =='0':
            return '0'
        elif self.board_line1[0] == 'X' and self.board_line2[1] == 'X' and self.board_line3[2] =='X':
            return 'X'
        elif self.board_line1[2] == '0' and self.board_line2[1] == '0' and self.board_line3[0] =='0':
            return '0'
        elif self.board_line1[2] == 'X' and self.board_line2[1] == 'X' and self.board_line3[0] =='X':
            return 'X'
        else:
            return 'no win'
        
    def free_space(self): #check which position(s) on the board are empty and return a list of those positions
        free = []
        
        for i in range(len(self.board_line1)):
            if self.board_line1[i] == ' ':
                free.append(i + 1)
            if self.board_line2[i] == ' ':
                free.append(i + 4)
            if self.board_line3[i] == ' ':
                free.append(i + 7)
        return free
            
# Set up Player: player chooses a position on the board, update the board

class Player:
    
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece

    #Place 0 or X on the board
    def play(self, a_board):  # use parameter a_board to pass the board to the Player class when using this method
        flag = True
        while flag:  # check if position is empty
            position = input('Make your move! [1 - 9]: ')
            try:
                pos = int(position)
                if pos < 1 or pos > 9:
                    print('>>> Position not valid! Try again!')
                    a_board.display_board()
                elif pos not in a_board.free_space():
                    print('>>> Position not available! Try again!')
                    a_board.display_board()
                else:
                    flag = False

            except ValueError:
                print('>>> Enter a number between 1 and 9 to select a position')
                a_board.display_board()

        for i in range(len(a_board.board_line1)):
            if pos - 1 == i and a_board.board_line1[i] == ' ':
                a_board.board_line1[i] = self.piece  # put 0 or X in position chosen by player
            elif pos - 4 == i and a_board.board_line2[i] == ' ':
                a_board.board_line2[i] = self.piece
            elif pos - 7 == i and a_board.board_line3[i] == ' ':
                a_board.board_line3[i] = self.piece


# Set up Computer class: computer chooses a position on the board - anticipate against player, update the board

class Computer:
    
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
    
    # Computer plays/selects position - anticipate player (rather than completely random)
    def c_play(self, a_board):
        print("Comupter's choice")
        
        flag = True
        while flag:
            if a_board.board_line1.count('0') == 2 and a_board.board_line1.count(' ') == 1:
                pos = random.randint(1, 3)
                for i in range(len(a_board.board_line1)):
                    if pos-1 == i and a_board.board_line1[i] == ' ':
                        flag = False
            elif a_board.board_line2.count('0') == 2 and a_board.board_line2.count(' ') == 1:
                pos = random.randint(4, 6)
                for i in range(len(a_board.board_line2)):
                    if pos-4 == i and a_board.board_line2[i] == ' ':
                        flag = False
            elif a_board.board_line3.count('0') == 2 and a_board.board_line3.count(' ') == 1:
                pos = random.randint(7, 9)
                for i in range(len(a_board.board_line3)):
                    if pos-7 == i and a_board.board_line3[i] == ' ':
                        flag = False
            elif (a_board.board_line1[0] == '0' and a_board.board_line2[1] == '0' and a_board.board_line3[2] == ' ') or (a_board.board_line1[0] == ' ' and a_board.board_line2[1] == '0' and a_board.board_line3[2] == '0'):
                seq = [1, 9]
                pos = random.choice(seq)
                if pos-1 == 0 and a_board.board_line1[0] == ' ':
                    flag = False
                if pos-7 == 2 and a_board.board_line3[2] == ' ':
                    flag = False
            elif (a_board.board_line1[2] == '0' and a_board.board_line2[1] == '0' and a_board.board_line3[0] == ' ') or (a_board.board_line1[2] == ' ' and a_board.board_line2[1] == '0' and a_board.board_line3[0] == '0'):
                seq = [3, 7]
                pos = random.choice(seq)
                if pos-1 == 2 and a_board.board_line1[2] == ' ':
                    flag = False
                if pos-7 == 0 and a_board.board_line3[0] == ' ':
                    flag = False
            elif (a_board.board_line1[0] == '0' and a_board.board_line2[1] == ' ' and a_board.board_line3[2] == '0') or (a_board.board_line1[2] == '0' and a_board.board_line2[1] == ' ' and a_board.board_line3[0] == '0'):
                pos = 5
                flag = False
            elif (a_board.board_line1[0] == '0' or a_board.board_line2[0] == '0' or a_board.board_line3[0] == '0') and (a_board.board_line1[0] == ' ' or a_board.board_line2[0] == ' ' or a_board.board_line3[0] == ' '):
                seq = [1, 4, 7]
                pos = random.choice(seq)
                if pos-1 == 0 and a_board.board_line1[0] == ' ':
                    flag = False
                if pos-4 == 0 and a_board.board_line2[0] == ' ':
                    flag = False
                if pos-7 == 0 and a_board.board_line3[0] == ' ':
                    flag = False
            elif (a_board.board_line1[1] == '0' or a_board.board_line2[1] == '0' or a_board.board_line3[1] == '0') and (a_board.board_line1[1] == ' ' or a_board.board_line2[1] == ' ' or a_board.board_line3[1] == ' '):
                seq = [2, 5, 8]
                pos = random.choice(seq)
                if pos-1 == 1 and a_board.board_line1[1] == ' ':
                    flag = False
                if pos-4 == 1 and a_board.board_line2[1] == ' ':
                    flag = False
                if pos-7 == 1 and a_board.board_line3[1] == ' ':
                    flag = False
            elif (a_board.board_line1[2] == '0' or a_board.board_line2[2] == '0' or a_board.board_line3[2] == '0') and (a_board.board_line1[2] == ' ' or a_board.board_line2[2] == ' ' or a_board.board_line3[2] == ' '):
                seq = [3, 6, 9]
                pos = random.choice(seq)
                if pos-1 == 2 and a_board.board_line1[2] == ' ':
                    flag = False
                if pos-4 == 2 and a_board.board_line2[2] == ' ':
                    flag = False
                if pos-7 == 2 and a_board.board_line3[2] == ' ':
                    flag = False
            else:
                pos = random.randint(1,9)
                for i in range(len(a_board.board_line1)):
                    if int(pos)-1 == i and a_board.board_line1[i] == ' ':
                        flag = False  
                    elif int(pos)-4 == i and a_board.board_line2[i] == ' ':
                        flag = False
                    if int(pos)-7 == i and a_board.board_line3[i] == ' ':
                        flag = False
                        
        for i in range(len(a_board.board_line1)):
            if pos-1 == i and a_board.board_line1[i] == ' ':
                a_board.board_line1[i] = 'X' #put X in position chosen
            elif pos-4 == i and a_board.board_line2[i] == ' ':
                a_board.board_line2[i] = 'X' 
            elif pos-7 == i and a_board.board_line3[i] == ' ':
                a_board.board_line3[i] = 'X' 
                
# Tic-Tac-Toe!!
#General methods required to play
# Set up functions to initialise the board, test for a win and ask if want to play again

class PlayGame:

    def __init__(self):
        self._b = Board()

    def initialise(self):
        self._b.clear_board()
        self._b.display_board()

    def test(self):
        if self._b.win() == '0' or self._b.win() == 'X':
            return 'Win'
        elif (self._b.win() == 'no win') and (self._b.is_not_full() == False):
            return 'Draw'

    def another(self):  # ask if want to start another game or not
        while True:
            cont = input('Would you like to play again (y/n): ')
            if cont == 'n':
                print('Goodbye!')
                return cont
            elif cont == 'y':
                print(' ')
                self.initialise()
                return cont
            else:
                print('Incorrect input.')


# Tic-Tac-Toe!! Play against the computer
# Play the game: determine a win or draw. Ask if want to play again.

class PlayComputer(PlayGame):

    def __init__(self):
        super().__init__()


    def play_game(self):
        print('Player is [0] and Computer is [X]')
        p = Player('Player', '0')
        c = Computer('Computer', 'X')
        cont = 'y'
        while cont == 'y':
            p.play(self._b)
            self._b.display_board()
            if super().test() == 'Win':
                print('****Congratulations! You won!****')
                cont = super().another()
                if cont == 'y':
                    self.play_game()
            elif super().test() == 'Draw':
                print('Draw')
                cont = super().another()
                if cont == 'y':
                    self.play_game()
            elif cont == 'y':
                c.c_play(self._b)
                self._b.display_board()
                if super().test() == 'Win':
                    print('Computer wins. You loose')
                    cont = super().another()
                    if cont == 'y':
                        self.play_game()
                elif super().test() == 'Draw':
                    print('Draw')
                    cont = super().another()
                    if cont == 'y':
                        self.play_game()


# Tic-Tac-Toe!! Two player game
# Play the game: determine a win or draw. Ask if want to play again.

class TwoPlayer(PlayGame):

    def __init__(self):
        super().__init__()


    # Two player game
    def two_player(self):
        print('Tic-Tac-Toe: Player 1 is [0] and Player 2 is [X]')
        p1name = input('Player 1, enter your name: ')
        p2name = input('Player 2, enter your name: ')
        print(' ')
        p1 = Player(p1name, '0')
        p2 = Player(p2name, 'X')
        cont = 'y'
        while cont == 'y':
            print(p1.name)
            p1.play(self._b)
            self._b.display_board()
            if super().test() == 'Win':
                print('****Congratulations! You won!****')
                cont = super().another()
                if cont == 'y':
                    self.two_player()
            elif super().test() == 'Draw':
                print('Draw')
                cont = super().another()
                if cont == 'y':
                    self.two_player()
            elif cont == 'y':
                print(p2.name)
                p2.play(self._b)
                self._b.display_board()
                if super().test() == 'Win':
                    print('****Congratulations! You won!****')
                    cont = super().another()
                    if cont == 'y':
                        self.two_player()
                elif super().test() == 'Draw':
                    print('Draw')
                    cont = super().another()
                    if cont == 'y':
                        self.two_player()


# Choose a game of Tic-Tac-Toe

import random

if __name__ == '__main__':

    Q = True
    while Q:
        whichgame = input('Press c to play against the computer, p to play against another player (c/p): ')
        if whichgame == 'c':
            gamec = PlayComputer()
            Q = False
            print(' ')
            gamec.initialise()
            gamec.play_game()
        elif whichgame == 'p':
            gamep = TwoPlayer()
            Q = False
            print(' ')
            gamep.initialise()
            gamep.two_player()
        else:
            print("Incorrect input.")
