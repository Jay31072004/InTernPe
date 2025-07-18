import tkinter as tk
from tkinter import messagebox
import random

# Globals
current_player = "X"  # Player always starts
board = [""] * 9
buttons = []

# Handle button click by player
def button_click(index):
    global current_player
    if board[index] == "" and current_player == "X":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")

        if check_winner("X"):
            messagebox.showinfo("Game Over", "You win!")
            disable_all_buttons()
            return
        elif "" not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            disable_all_buttons()
            return

        current_player = "O"
        label_turn.config(text="Computer's turn...")
        root.after(500, computer_move)  # Delay for realism

# Computer's move (AI = O)
def computer_move():
    global current_player
    empty_indexes = [i for i in range(9) if board[i] == ""]
    if not empty_indexes:
        return

    index = random.choice(empty_indexes)  # Random move
    board[index] = "O"
    buttons[index].config(text="O", state="disabled")

    if check_winner("O"):
        messagebox.showinfo("Game Over", "Computer wins!")
        disable_all_buttons()
        return
    elif "" not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        disable_all_buttons()
        return

    current_player = "X"
    label_turn.config(text="Your turn")

# Check for win
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Disable all buttons
def disable_all_buttons():
    for btn in buttons:
        btn.config(state="disabled")

# Reset game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    label_turn.config(text="Your turn")
    for btn in buttons:
        btn.config(text="", state="normal")

# GUI Setup
root = tk.Tk()
root.title("Tic Tac Toe - Vs Computer")
root.geometry("350x500")
root.resizable(False, False)

label_turn = tk.Label(root, text="Your turn", font=("Arial", 18))
label_turn.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

# Create 9 buttons
for i in range(9):
    btn = tk.Button(frame, text="", width=6, height=3,
                    font=("Arial", 24),
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 14), command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()