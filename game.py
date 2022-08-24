class Game():
    def __init__(self):
        self._board = [' ', ' ', ' ', 
                       ' ', ' ', ' ', 
                       ' ', ' ', ' ', ]
        self._run = True
    
    def display(self) -> None:
        print('------------------')
        for i in range(9)[::3]:
            print('#     #     #     #')
            print(f'#  {self._board[i]}  #  {self._board[i+1]}  #  {self._board[i+2]}  #')
            print('#     #     #     #')
            print('------------------')
    
    def help_display(self) -> None:
        print('------------------')
        for i in range(9)[::3]:
            frist = (i + 1) if self._board[i] == ' ' else self._board[i]
            second = (i + 2) if self._board[i+1] == ' ' else self._board[i+1]
            third = (i + 3) if self._board[i+2] == ' ' else self._board[i+2]
            print('#     #     #     #')
            print(f'#  {frist}  #  {second}  #  {third}  #')
            print('#     #     #     #')
            print('-------------------')
    
    def check(self, letter):
        columns = [self._board[i::3] for i in range(3)]
        for column in columns:
            if all([i == letter for i in column]):
                return True
                
        rows = [self._board[i:i+3] for i in range(7)[::3]]
        for row in rows:
            if all([i == letter for i in row]):
                return True
        
        if self._board[0] == letter and self._board[4] == letter and self._board[8] == letter:
            return True
        
        if self._board[2] == letter and self._board[4] == letter and self._board[6] == letter:
            return True
    
    def pre_check_move(self, move):
        if self._board[move-1] != ' ':
            return False
        return True
    
    def comp_checkDraw(self):
        if all([self._board[i] != ' ' for i in range(9)]):
            if not self.check('O') and not self.check('X'):
                return True

    def checkDraw(self):
        if all([self._board[i] != ' ' for i in range(9)]):
            if not self.check('O') and not self.check('X'):
                self._run = False
                return True
    
    def ask_move(self):
        move = input('Enter next move [1-9]: ')
        
        test = True 
        
        while test:
            if move in ['1','2','3','4','5','6','7','8','9']:
                if self.pre_check_move(int(move)):
                    test = False
                    break
            print()
            print('try again')
            move = input('Enter next move [1-9]: ')
        
        
        self.update(int(move), 'X')
    
    def update(self, move, letter):
        self._board[move-1] = letter
        if self.check(letter) or self.checkDraw():
            self._run = False
    
    def compMove(self):
        bestScore = -1000
        bestmove = 0
        
        for i in range(9):
            if self._board[i] == ' ':
                self._board[i] = 'O'
                score = self.minimax(self._board, False)
                self._board[i] = ' '
                if score > bestScore:
                    bestScore = score
                    bestmove = i
        
        self.update(bestmove + 1, 'O')
        return

    def minimax(self, board, side):
        
        if self.check('O'):
            return 10000
        elif self.check('X'):
            return -100
        elif self.comp_checkDraw():
            return 0
        
        if side:
            bestScore = -1000
            
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    score = self.minimax(board, False)
                    board[i] = ' '
                    if score > bestScore:
                        bestScore = score
                        
            return bestScore
        else:
            bestScore = 800
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    score = self.minimax(board, True)
                    board[i] = ' '
                    if score < bestScore:
                        bestScore = score
            return bestScore

if __name__ == '__main__':
    game = Game()
    game.help_display()
    while game._run:
        game.compMove()
        print()
        print('COMP MOVE')
        game.display()
        if game._run:
            game.ask_move()
            game.display()