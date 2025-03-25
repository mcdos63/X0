import tkinter as tk
from tkinter import messagebox

# Создание основного окна
window = tk.Tk()
window.title("Крестики-нолики")

# Фиксация размеров окна
window.resizable(False, False)  # Запрещаем изменение размеров окна

# Переменные для игры
current_player = "X"
buttons = []
player_x_wins = 0
player_o_wins = 0

# Проверка победителя
def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

# Обработчик нажатия на кнопку
def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        update_score(current_player)
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        reset_game()

    elif all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_game()

    else:
        current_player = "O" if current_player == "X" else "X"

# Сброс игры
def reset_game():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

# Обновление счета
def update_score(winner):
    global player_x_wins, player_o_wins
    if winner == "X":
        player_x_wins += 1
    else:
        player_o_wins += 1
    update_score_label()

# Обновление метки со счетом
def update_score_label():
    score_label.config(text=f"Игрок X: {player_x_wins} | Игрок O: {player_o_wins}")

# Сброс счета и игры
def reset_all():
    global player_x_wins, player_o_wins, current_player
    player_x_wins = 0
    player_o_wins = 0
    current_player = "X"
    reset_game()
    update_score_label()

# Выбор игрока
def choose_player(player):
    global current_player
    current_player = player
    reset_game()

# Создание кнопок
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(
            window,
            text="",
            font=("Arial", 25),
            width=3,  # Увеличиваем ширину кнопок для лучшего вида
            height=1,  # Увеличиваем высоту кнопок для лучшего вида
            command=lambda r=i, c=j: on_click(r, c)
        )
        btn.grid(row=i, column=j, padx=1, pady=1)  # Добавляем отступы между кнопками
        row.append(btn)
    buttons.append(row)

# Метка для отображения счета
score_label = tk.Label(window, text="Игрок X: 0 | Игрок O: 0", font=("Arial", 12))
score_label.grid(row=3, column=0, columnspan=3, pady=5)

# Кнопка сброса игры
reset_button = tk.Button(window, text="Сбросить игру", command=reset_game, font=("Arial", 12))
reset_button.grid(row=4, column=0, columnspan=3, pady=5)

# Кнопка сброса всего (счета и игры)
reset_all_button = tk.Button(window, text="Сбросить все", command=reset_all, font=("Arial", 12))
reset_all_button.grid(row=5, column=0, columnspan=3, pady=5)

# Выбор игрока
choose_player_frame = tk.Frame(window)
choose_player_frame.grid(row=6, column=0, columnspan=3, pady=5)

choose_x_button = tk.Button(choose_player_frame, text="Выбрать X", command=lambda: choose_player("X"), font=("Arial", 12))
choose_x_button.pack(side=tk.LEFT, padx=5)

choose_o_button = tk.Button(choose_player_frame, text="Выбрать O", command=lambda: choose_player("O"), font=("Arial", 12))
choose_o_button.pack(side=tk.RIGHT, padx=5)

# Вычисление минимального размера окна
window.update_idletasks()  # Обновляем окно для корректного вычисления размеров
window.geometry(f"{window.winfo_reqwidth()}x{window.winfo_reqheight()}")

# Запуск основного цикла
window.mainloop()