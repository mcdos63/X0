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
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        reset_game()

    elif all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_game()

    else:
        current_player = "O" if current_player == "X" else "X"


# Сброс игры
def reset_game():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""


# Создание кнопок
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(
            window,
            text="",
            font=("Arial", 20),
            width=3,  # Увеличиваем ширину кнопок для лучшего вида
            height=1,  # Увеличиваем высоту кнопок для лучшего вида
            command=lambda r=i, c=j: on_click(r, c)
        )
        btn.grid(row=i, column=j, padx=1, pady=1)  # Добавляем отступы между кнопками
        row.append(btn)
    buttons.append(row)

# Вычисление минимального размера окна
window.update_idletasks()  # Обновляем окно для корректного вычисления размеров
window.geometry(f"{window.winfo_reqwidth()}x{window.winfo_reqheight()}")

# Запуск основного цикла
window.mainloop()