import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Global variables
currentPlayer = "X"
board = [""] * 9

# Function to handle button clicks
def onClick(index):
    global currentPlayer
    if buttons[index]["text"] == "" and currentPlayer == "X":
        buttons[index]["text"] = "X"
        board[index] = "X"
        currentPlayer = "O"
        checkWin()
    elif buttons[index]["text"] == "" and currentPlayer == "O":
        buttons[index]["text"] = "O"
        board[index] = "O"
        currentPlayer = "X"
        checkWin()

# Function to check for a win or tie
def checkWin():
    global currentPlayer
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != "":
            showWin(board[condition[0]])
            return
    
    if all(cell != "" for cell in board):
        showTie()

# Function to display the winner
def showWin(player):
    messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
    root.quit()

# Function to display a tie
def showTie():
    messagebox.showinfo("Tic Tac Toe", "It's a tie!")
    root.quit()

# Create buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Helvetica", 20), height=3, width=6, 
                       command=lambda i=i: onClick(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the main event loop

root.mainloop()