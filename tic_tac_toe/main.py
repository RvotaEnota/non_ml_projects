import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Крестики-нолики")
root.iconbitmap("icon1.ico") 

current_player = "X"
game_over = False
buttons = []
game_mode = None 

def start_game(mode):
    global game_mode
    game_mode = mode
    menu_frame.pack_forget()
    reset_game()
    game_frame.pack()

menu_frame = tk.Frame(root)
menu_label = tk.Label(menu_frame, text="Режим игры", font=("Arial", 20))
menu_label.pack(pady=10)

human_button = tk.Button(menu_frame, text="Человек", font=("Arial", 16), command=lambda: start_game("human"))
ai_button = tk.Button(menu_frame, text="Компьютер", font=("Arial", 16), command=lambda: start_game("ai"))

human_button.pack(pady=5)
ai_button.pack(pady=5)
menu_frame.pack()

game_frame = tk.Frame(root)

def reset_game():
    global current_player, game_over
    current_player = "X"
    game_over = False
    for button in buttons:
        button.config(text="", bg="SystemButtonFace", state="normal")

def check_winner():
    global game_over
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]              
    for combo in winning_combinations:
        a, b, c = combo
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            game_over = True
            return True
    return False

def ai_move():
    global current_player
    empty_indices = [i for i, b in enumerate(buttons) if b["text"] == ""]
    if empty_indices:
        index = random.choice(empty_indices)
        buttons[index]["text"] = "O"
        if check_winner():
            messagebox.showinfo("Победа!", "Победил O!")
            return
        elif all(button["text"] != "" for button in buttons):
            messagebox.showinfo("Ничья!", "Игра окончена. Ничья!")
            return
        current_player = "X"

def on_click(index):
    global current_player
    if buttons[index]["text"] == "" and not game_over:
        buttons[index]["text"] = current_player

        if check_winner():
            messagebox.showinfo("Победа!", f"Победил {current_player}!")
            return
        elif all(button["text"] != "" for button in buttons):
            messagebox.showinfo("Ничья!", "Игра окончена. Ничья!")
            return

        if game_mode == "human":
            current_player = "O" if current_player == "X" else "X"
        elif game_mode == "ai":
            current_player = "O"
            root.after(200, ai_move)


for i in range(9):
    button = tk.Button(
        game_frame,
        text="",
        font=("Arial", 30),
        width=5,
        height=2,
        command=lambda idx=i: on_click(idx)
    )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

reset_button = tk.Button(game_frame, text="Новая игра", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

root.mainloop()