from tkinter import Tk, Canvas, PhotoImage
import requests

# ______________________________ window confs ______________________________

BG = "#800080"
window = Tk()
window.title("Chuck Norris Jokes")
window.config(bg=BG, pady=50, padx=50)

# ______________ Grid system ______________

ROWS = 2
COLUMNS = 1
for row in range(ROWS):
    window.grid_rowconfigure(index=row, weight=1)

for col in range(COLUMNS):
    window.grid_columnconfigure(index=col, weight=1)

# ______________ Canvas ______________
canvas = Canvas(width=320, height=434, highlightthickness=0, background=BG)
bg_img = PhotoImage(file="./images/background.png")
canvas.create_image(150, 207, image=bg_img)
canvas.grid_configure(row=0, column=0)

window.mainloop()
