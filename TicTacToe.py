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
            return 'player0 wins'
        elif self.board_line1[0] == 'X' and self.board_line2[0] == 'X' and self.board_line3[0] =='X':
            return 'playerX wins'
        elif self.board_line1[1] == '0' and self.board_line2[1] == '0' and self.board_line3[1] =='0':
            return 'player0 wins'
        elif self.board_line1[1] == 'X' and self.board_line2[1] == 'X' and self.board_line3[1] =='X':
            return 'playerX wins'
        elif self.board_line1[2] == '0' and self.board_line2[2] == '0' and self.board_line3[2] =='0':
            return 'player0 wins'
        elif self.board_line1[2] == 'X' and self.board_line2[2] == 'X' and self.board_line3[2] =='X':
            return 'playerX wins'
        elif self.board_line1.count('0') == 3 or self.board_line2.count('0') == 3 or self.board_line3.count('0') == 3:
            return 'player0 wins'
        elif self.board_line1.count('X') == 3 or self.board_line2.count('X') == 3 or self.board_line3.count('X') == 3:
            return 'playerX wins'
        elif self.board_line1[0] == '0' and self.board_line2[1] == '0' and self.board_line3[2] =='0':
            return 'player0 wins'
        elif self.board_line1[0] == 'X' and self.board_line2[1] == 'X' and self.board_line3[2] =='X':
            return 'playerX wins'
        elif self.board_line1[2] == '0' and self.board_line2[1] == '0' and self.board_line3[0] =='0':
            return 'player0 wins'
        elif self.board_line1[2] == 'X' and self.board_line2[1] == 'X' and self.board_line3[0] =='X':
            return 'playerX wins'
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
    
    def __init__(self, name):
        self.name = name
        
        
    # player 1 [0] plays/selects a position    
    def play0(self, a_board): #use parameter a_board to pass the board to the Player class when using this method  
        flag = True
        while flag: #check if position is empty
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
            if pos-1 == i and a_board.board_line1[i] == ' ':
                a_board.board_line1[i] = '0' #put 0 in position chosen by player
            elif pos-4 == i and a_board.board_line2[i] == ' ':
                a_board.board_line2[i] = '0' 
            elif pos-7 == i and a_board.board_line3[i] == ' ':
                a_board.board_line3[i] = '0' 


                
                
    # player 2 [X] plays/selects a position    
    def playX(self, a_board): #use parameter a_board to pass the board to the Player class when using this method
        flag = True
        while flag: #check if position is empty
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
            if pos-1 == i and a_board.board_line1[i] == ' ':
                a_board.board_line1[i] = 'X' #put X in position chosen by player
            elif pos-4 == i and a_board.board_line2[i] == ' ':
                a_board.board_line2[i] = 'X' 
            elif pos-7 == i and a_board.board_line3[i] == ' ':
                a_board.board_line3[i] = 'X' 

# Set up Computer class: computer chooses a position on the board - anticipate against player, update the board

class Computer:
    
    def __init__(self, name):
        self.name = name
        
    
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
                
# Tic-Tac-Toe!! Play against the computer
# Play the game: determine a win or draw. Ask if want to play again.

class PlayComputer:
    
    def __init__(self):
        self._b1 = Board()
        self._p = Player('Player')
        self._c = Computer('Computer')

    def initialise1(self):
    #Initialise the game
        self._b1.clear_board()
        print('Player is [0] and computer is [X]')
        self._b1.display_board()

    def test1(self):
        if self._b1.win() == 'player0 wins':
            print('****Congratulations! You won!****')
            return 're-start'
        elif self._b1.win() == 'playerX wins':
            print('Computer wins. You loose')
            return 're-start'
        elif (self._b1.win() == 'no win') and (self._b1.is_not_full() == False):
            print('Draw')
            return 're-start'

    def another1(self): #ask if want to start another game or not
        flag1 = True
        while flag1:
            cont1 = input('Would you like to play again (y/n): ')
            if cont1 == 'n':
                flag1 = False
                print('Goodbye!')
                return cont1
            elif cont1 == 'y':
                flag1 = False
                print(' ')
                self.initialise1()
                self.play_game()
            else:
                print('Incorrect input.')

    def play_game(self):
        cont1 = 'y'
        while cont1 == 'y':
            self._p.play0(self._b1)
            self._b1.display_board()
            if self.test1() == 're-start':
                cont1 = self.another1()
            if cont1 == 'y':
                self._c.c_play(self._b1)
                self._b1.display_board()
                if self.test1() == 're-start':
                    cont1 = self.another1()

# Tic-Tac-Toe!! Two player game
# Play the game: determine a win or draw. Ask if want to play again.

class TwoPlayer:
    
    def __init__(self):
        self._b2 = Board()

    def initialise2(self):
    #Initialise the game
        self._b2.clear_board()
        print('Tic-Tac-Toe: Player 1 is [0] and Player 2 is [X]')
        self._b2.display_board()

    def test2(self): #test to see if there is a winner or a draw
        if self._b2.win() == 'player0 wins':
            print('****Congratulations! You won!****')
            return 're-start'
        elif self._b2.win() == 'playerX wins':
            print('****Congratulations! You won!****')
            return 're-start'
        elif (self._b2.win() == 'no win') and (self._b2.is_not_full() == False):
            print('Draw')
            return 're-start'

    def another2(self): #ask if want to start another game or not
        flag2 = True
        while flag2:
            cont2 = input('Would you like to play again (y/n): ')
            if cont2 == 'n':
                flag2 = False
                print('Goodbye!')
                return cont2
            elif cont2 == 'y':
                flag2 = False
                print(' ')
                self.initialise2()
                self.two_player()
            else:
                print('Incorrect input')

    # Two player game
    def two_player(self):
        p1name = input('Player 1, enter your name: ')
        p2name = input('Player 2, enter your name: ')
        print(' ')
        p1 = Player(p1name)
        p2 = Player(p2name)
        cont2 = 'y'
        while cont2 == 'y':
            print(p1.name)
            p1.play0(self._b2)
            self._b2.display_board()
            if self.test2() == 're-start':
                cont2 = self.another2()
            if cont2 == 'y':
                print(p2.name)
                p2.playX(self._b2)
                self._b2.display_board()
                if self.test2() == 're-start':
                    cont2 = self.another2()
                    
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
            gamec.initialise1()
            gamec.play_game()
        elif whichgame == 'p':
            gamep = TwoPlayer()
            Q = False
            print(' ')
            gamep.initialise2()
            gamep.two_player()
        else:
            print("Incorrect input.")
