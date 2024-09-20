from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("643x394")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 394,
    width = 643,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    330.5, 197.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    439.5, 137.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#fffbfb",
    highlightthickness = 0)

entry0.place(
    x = 332.0, y = 117,
    width = 215.0,
    height = 39)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    400.5, 277.0,
    image = entry1_img)

entry1 = Text(
    bd = 0,
    bg = "#fffbfb",
    highlightthickness = 0)

entry1.place(
    x = 254.0, y = 237,
    width = 293.0,
    height = 78)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 337, y = 340,
    width = 127,
    height = 41)

window.resizable(False, False)
window.mainloop()
