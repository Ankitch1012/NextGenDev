import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg='white')
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        self.moves_made = 0

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=('Arial', 40), width=5, height=2,
                                               bg='lightblue', fg='black',
                                               command=lambda i=i, j=j: self.button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def button_click(self, i, j):
        if self.buttons[i][j]["text"] == "" and self.current_player:
            self.buttons[i][j]["text"] = self.current_player
            self.buttons[i][j]["fg"] = 'red' if self.current_player == "X" else 'blue'
            self.moves_made += 1
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.moves_made == 9:
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["bg"] = 'lightblue'
        self.current_player = "X"
        self.moves_made = 0

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
