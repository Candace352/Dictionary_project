import json
import tkinter as tk
from ttkthemes import ThemedStyle
from tkinter import Menu

data = json.load(open("data.json")) #opening the json file

def changes():
    word = definition.get("1.0", "end-1c").strip()
    if word in data.keys():
        message.config(text=data.get(word))

    else:
        message_text = data.get(word, "Word Not what what")
        message.config(message_text)

def set_dark_theme():
    style.set_theme("black")
    root.configure(bg=style.lookup('TFrame','background'))
    labels = [blank_label, blank_label1,search_btn,message]
    for i in labels:
        i.configure(bg=style.lookup('TButton','background'), fg=style.lookup('TButton','foreground'))
    root.update_idletasks()

def set_light_theme():
    style.set_theme("breeze")
    root.configure(bg=style.lookup('TFrame','background'))
    labels = [blank_label,blank_label1,search_btn,message]
    for i in labels:
        i.configure(bg=style.lookup('TButton','background'), fg=style.lookup('TButton','foreground'))
    root.update_idletask

root = tk.Tk()
root.geometry("500x450")
root.title("My Dictionary")

menubar = Menu(root)
theme_menu = Menu(menubar, tearoff=0)
theme_menu.add_command(label="Dark", command=set_dark_theme)
theme_menu.add_command(label="Light", command=set_light_theme)
menubar.add_cascade(label="Theme", menu=theme_menu)
root.config(menu=menubar)

style = ThemedStyle(root)
style.set_theme("breeze")

definition = tk.Text(root,height=1.75,width=20,font=('Arial',18))
definition.pack(padx=3,pady=1.5)

blank_label = tk.Label(root, text="")
blank_label.pack()

search_btn = tk.Button(root, text="Search",command=lambda: changes(),width=9,font=('Arial',12))
search_btn.pack(padx=5,pady=7)

blank_label1 = tk.Label(root, text="")
blank_label1.pack()

message = tk.Message(root, width=400, font=('Arial', 11))
message.pack(padx=5, pady=7)

root.mainloop()
