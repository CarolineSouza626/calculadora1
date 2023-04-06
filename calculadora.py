import customtkinter
from tkinter import *

app = customtkinter.CTk()
app.title("calculadora")
app.geometry("250x350")
app.config(bg="#000000")


font1 = ('Arial', 20, 'bold')

i = 0
equacao = ""


def show(value):
    global i
    global equacao
    equacao += value
    result_entry.insert(i, value)
    i = i+1


def clear():
    result_entry.delete(0, END)


def calcular():
    global equacao
    result = ""
    result = eval(equacao)
    clear()
    result_entry.insert(0, result)


result_entry = customtkinter.CTkEntry(
    app, font=font1, width=250, fg_color="#000000", border_color="#000000", text_color="#ffffff")
result_entry.place(x=0, y=10)

Button1 = customtkinter.CTkButton(app, command=clear, text="C", font=font1,
                                  width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
Button1.place(x=10, y=60)

Button2 = customtkinter.CTkButton(app, command=lambda: show(
    "%"), text="%", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
Button2.place(x=70, y=60)

Button3 = customtkinter.CTkButton(app, command=lambda: show(
    "/"), text="/", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
Button3.place(x=130, y=60)

Button4 = customtkinter.CTkButton(app, command=lambda: show(
    "*"), text="*", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
Button4.place(x=190, y=60)

Button5 = customtkinter.CTkButton(app, command=lambda: show(
    "7"), text="7", font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#b5520b")
Button5.place(x=10, y=120)

Button6 = customtkinter.CTkButton(app, command=lambda: show(
    "8"), text="8", font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#b5520b")
Button6.place(x=70, y=120)

Button7 = customtkinter.CTkButton(app, command=lambda: show(
    "9"), text="9", font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#b5520b")
Button7.place(x=130, y=120)

Button8 = customtkinter.CTkButton(app, command=lambda: show(
    "+"), text="+", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
Button8.place(x=190, y=120)

Button9 = customtkinter.CTkButton(app, command=lambda: show(
    "4"), text="4", font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#b5520b")
Button9.place(x=10, y=180)

Button10 = customtkinter.CTkButton(app, command=lambda: show(
    "5"), text="5", font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#b5520b")
Button10.place(x=70, y=180)

Button11 = customtkinter.CTkButton(app, command=lambda: show(
    "6"), text="6", font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#b5520b")
Button11.place(x=130, y=180)

Button12 = customtkinter.CTkButton(app, command=lambda: show(
    "-"), text="-", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
Button12.place(x=190, y=180)

Button13 = customtkinter.CTkButton(app, command=lambda: show(
    "0"), text="0", font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#b5520b")
Button13.place(x=10, y=240)

Button14 = customtkinter.CTkButton(app, command=lambda: show(
    "1"), text="1", font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#b5520b")
Button14.place(x=70, y=240)

Button15 = customtkinter.CTkButton(app, command=lambda: show(
    "2"), text="2", font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#b5520b")
Button15.place(x=130, y=240)

Button16 = customtkinter.CTkButton(app, command=lambda: show(
    "3"), text="3", font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#b5520b")
Button16.place(x=190, y=240)

Button17 = customtkinter.CTkButton(app, command=lambda: show(
    ","), text=".", font=font1, width=50, height=2, fg_color="#2e2a27", hover_color="#b5520b")
Button17.place(x=10, y=300)

Button18 = customtkinter.CTkButton(app, command=calcular, text="=", font=font1,
                                   width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
Button18.place(x=70, y=300)

app.mainloop()
