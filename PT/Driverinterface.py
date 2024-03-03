import time
import tkinter

import customtkinter as ctk
from CTkListbox import *
import sqlite3
import threading

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

window = ctk.CTk()
window.title("aa")
window.geometry("500x400")
window.configure(fg_color="#232E34")

window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=1)

window.grid_columnconfigure(0, weight=1)




register_frame = ctk.CTkFrame(window,corner_radius=0)
register_frame.grid(row=0, column=0, sticky="nsew")

register_frame.grid_propagate(0)
register_frame.grid_rowconfigure(0, weight=1)
register_frame.grid_columnconfigure(0, weight=1)

in_reg_frame = ctk.CTkFrame(register_frame)
in_reg_frame.grid(row=0, column=0)

in_reg_frame.grid_propagate(0)
in_reg_frame.grid_rowconfigure(0,weight=1)
in_reg_frame.grid_rowconfigure(2,weight=1)

in_reg_frame.grid_columnconfigure(0,weight=1)


id_label = ctk.CTkLabel(in_reg_frame,text="ID")
id_label.grid(row=0,column=0,sticky="sw")

id_entry = ctk.CTkEntry(in_reg_frame)
id_entry.grid(row=1,column=0,sticky="nsew")


name_label = ctk.CTkLabel(in_reg_frame,text="Name")
name_label.grid(row=2,column=0,sticky="sw")

name_entry = ctk.CTkEntry(in_reg_frame)
name_entry.grid(row=3,column=0,sticky="nsew")

button_enter = ctk.CTkButton(in_reg_frame,text="سجل",command=lambda :addDriver())
button_enter.grid(row=4,column=0)


sid = [0,0]
def addDriver():
    global sid
    sid = [name_entry.get(),id_entry.get()]

    file = open('drivers.txt', 'a+', encoding='utf-8')
    file.write(f"{sid[0]} {sid[1]}\n")

    file.close()








def showstu():
    while True:
        try:
            file = open(f'{sid[1]}.txt', 'r+', encoding='utf-8')
        except FileNotFoundError:
            open(f'{sid[1]}.txt', 'w+', encoding='utf-8')
            continue

        students = []
        d = file.read().splitlines()
        for student in d:
            a = student.split(",")
            students.append([a[0]] + [a[1]])

        drivers_listbox.delete("all")
        for student in students:
            drivers_listbox.insert(ctk.END, f"{student[1]} {student[0]}")


        time.sleep(5)


list_bus_frame = ctk.CTkFrame(window,corner_radius=0)
list_bus_frame.grid(row=1, column=0, sticky="nsew", columnspan=2)

list_bus_frame.grid_rowconfigure(0, weight=1)
list_bus_frame.grid_columnconfigure(0, weight=1)

in_bus_List = ctk.CTkFrame(list_bus_frame, )
in_bus_List.grid()

drivers_listbox = CTkListbox(in_bus_List, font=("", 16))
drivers_listbox.grid()


if __name__ == "__main__":
    showthread = threading.Thread(target=showstu)
    showthread.start()
    try:
        window.mainloop()
    except KeyboardInterrupt:
        conn.close()

