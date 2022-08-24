from tkinter import *
import random

def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != " ":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def compMove(board):
        bestScore = -1000
        bestmove = 0
        
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = ' '
                if score > bestScore:
                    bestScore = score
                    bestmove = i

        if (bestmove+1) in [1,2,3]:
            buttons[0][bestmove]['text'] = 'O'
        elif (bestmove+1) in [4,5,6]:
            buttons[1][bestmove-3]['text'] = 'O'
        elif (bestmove+1) in [7,8,9]:
            buttons[2][bestmove-6]['text'] = 'O'
        return

def minimax(board, side):
        
    if check('O', board):
        return 10000
    elif check('X', board):
        return -100
    elif comp_checkDraw(board):
        return 0
        
    if side:
        bestScore = -1000
            
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = ' '
                if score > bestScore:
                    bestScore = score
                        
        return bestScore
    else:
        bestScore = 800
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore

def next_turn(row, column):
    global player
    label.config(text="Tic Tac Toe")
    if not check_winner() and empty_spaces():
        if buttons[row][column]['text'] == ' ':
            buttons[row][column]['text'] = 'X'
            if check_winner():
                label.config(text=('X'+" wins"))
            elif not empty_spaces():
                label.config(text="Tie!")
            
            board = []
            for row in range(3):
                for column in range(3):
                    board.append(buttons[row][column]['text'])
            compMove(board)
            if check_winner():
                label.config(text=('O'+" wins"))
            elif not empty_spaces():
                label.config(text="Tie!")

def comp_checkDraw(board):
    if all([board[i] != ' ' for i in range(9)]):
        if not check('O', board) and not check('X', board):
            return True

def check(letter, board):
    columns = [board[i::3] for i in range(3)]
    for column in columns:
        if all([i == letter for i in column]):
            return True
                
    rows = [board[i:i+3] for i in range(7)[::3]]
    for row in rows:
        if all([i == letter for i in row]):
            return True
        
    if board[0] == letter and board[4] == letter and board[8] == letter:
        return True
        
    if board[2] == letter and board[4] == letter and board[6] == letter:
        return True

def new_game():

    global player

    player = random.choice(players)
    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text=" ",bg="#F0F0F0")
    
    if player == 'O':
        buttons[0][0]["text"] = "O"

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != " ":
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != " ":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != " ":
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != " ":
        return True
    
    else:
        return False


if __name__ == '__main__':
    window = Tk()
    window.title("Tic-Tac-Toe")
    players = ["X","O"]
    player = random.choice(players)
    buttons = [[' ',' ',' '],
               [' ',' ',' '],
               [' ',' ',' ']]
    label = Label(text=player + " turn", font=('consolas',40))

    label.pack(side="top")

    reset_button = Button(text="restart", font=('consolas',20), command=new_game)
    reset_button.pack(side="top")

    frame = Frame(window)
    frame.pack()

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text=buttons[row][column],font=('consolas',40), width=5, height=2,
                                          command= lambda row=row, column=column: next_turn(row,column))
            buttons[row][column].grid(row=row,column=column)

    window.mainloop()