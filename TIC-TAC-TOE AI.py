import tkinter as tk
from tkinter import messagebox
import math

# Initialize the board as a list of 9 empty spaces
board = [' ' for _ in range(9)]

# Function to check for a winner
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),  (0, 4, 8), (2, 4, 6)]  # Diagonals
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

# Function to check if the board is full (draw condition)
def is_draw(board):
    return ' ' not in board

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):  # AI wins
        return 1
    elif check_winner(board, 'X'):  # Human wins
        return -1
    elif is_draw(board):  # Draw
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'  # AI's move
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '  # Undo move
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'  # Human's move
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '  # Undo move
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# AI move: Find the best move using the Minimax algorithm
def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'  # AI's move
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '  # Undo move
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'
    buttons[best_move].config(text='O', state=tk.DISABLED)
    if check_winner(board, 'O'):
        messagebox.showinfo("Tic-Tac-Toe", "AI wins! Better luck next time.")
        reset_game()
    elif is_draw(board):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        reset_game()

# Human move: When the player clicks a button
def human_move(index):
    if board[index] == ' ':
        board[index] = 'X'
        buttons[index].config(text='X', state=tk.DISABLED)
        if check_winner(board, 'X'):
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations! You win!")
            reset_game()
        elif is_draw(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_game()
        else:
            ai_move()

# Reset the game
def reset_game():
    global board
    board = [' ' for _ in range(9)]
    for button in buttons:
        button.config(text=' ', state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create buttons for the Tic-Tac-Toe grid
buttons = []
for i in range(9):
    button = tk.Button(window, text=' ', font=('Arial', 24), width=5, height=2,
                       command=lambda i=i: human_move(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Start the main loop
window.mainloop()
