from tkinter import Tk, Canvas, PhotoImage, Button

import requests


# ______________________________ get Chuck Norris endpoint data & Send Jokes to btn ______________________________

def send_joke():
    response = requests.get(url="https://api.chucknorris.io/jokes/random")
    response.raise_for_status()
    data = response.json()
    random_joke = data['value']
    canvas.itemconfig(joke, text=random_joke)


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
canvas = Canvas(width=320, height=480, highlightthickness=0, background=BG)

bg_img = PhotoImage(file="./images/background.png")
canvas.create_image(160, 240, image=bg_img)
canvas.grid_configure(row=0, column=0)

joke = canvas.create_text(160, 208, text="Chuck Norris Jokes", width=250, font=("Arial", 20, "bold"), fill="white")

chuck_norris_image = PhotoImage(file="./images/chuck-norris.png")
chuck_btn = Button(
    image=chuck_norris_image,
    bg=BG,
    activebackground="#8B668B",
    bd=0,
    highlightthickness=0,
    command=send_joke
)
chuck_btn.grid_configure(row=1, column=0)

window.mainloop()
