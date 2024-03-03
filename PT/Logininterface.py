import customtkinter as ctk
import tkinter as tk
import sqlite3
import Studentinterface

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

window = ctk.CTk()
window.title("Login")
window.geometry("700x800")
window.configure(fg_color="#232E34")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

login_Frame = ctk.CTkFrame(window,fg_color="#1A2127",width=500,height=600)
login_Frame.grid(row=0, column=0,)
login_Frame.grid_propagate(0)


#inner
inner_frame = ctk.CTkFrame(login_Frame,fg_color="#1A2127")
inner_frame.grid(row=0, column=0)

#ID label
login_label_id = ctk.CTkLabel(inner_frame,text="ID",text_color="#a4abba",font=("",16),width=200,anchor="w")
login_label_id.grid(row=0,column=0,pady=(20, 0))

#ID Entry
login_entry_id = ctk.CTkEntry(inner_frame,font=("",20),width=200,corner_radius =15,border_width=2,border_color="#09c7d7",fg_color="#1A2127")
login_entry_id.grid(row=1,column=0,pady=(0, 0))

def on_enter(event):
    login_entry_id.configure(fg_color="#132224")


def on_leave(event):
    login_entry_id.configure(fg_color="#1A2127")

login_entry_id.bind('<Enter>', on_enter)
login_entry_id.bind('<Leave>', on_leave)

#Pass label
login_label_pass = ctk.CTkLabel(inner_frame,text="PASSWORD",text_color="#a4abba",font=("",16),width=200,anchor="w")
login_label_pass.grid(row=2,column=0,pady=(40, 0))

#Pass Entry
login_entry_pass = ctk.CTkEntry(inner_frame,font=("",20),width=200,corner_radius =15,border_width=2,border_color="#09c7d7",fg_color="#1A2127")
login_entry_pass.grid(row=3,column=0,pady=(0, 0))

def on_enter(event):
    login_entry_pass.configure(fg_color="#132224")

def on_leave(event):
    login_entry_pass.configure(fg_color="#1A2127")

login_entry_pass.bind('<Enter>', on_enter)
login_entry_pass.bind('<Leave>', on_leave)

#Login Button
button_frame = ctk.CTkFrame(inner_frame)
button_frame.grid(row=4,column=0,sticky="e",pady=(20, 0))

def Login(id,p):
    Studentinterface.appstart()
    window.destroy()


login_button = ctk.CTkButton(button_frame,
                             fg_color="#1A2127",
                             border_color="#09c7d7",
                             border_width=2,
                             text_color="#09c7d7",
                             text="LOGIN",
                             corner_radius =15,
                             width= 60,
                             command=lambda :Login(login_entry_id.get(),login_entry_pass.get()))

login_button.grid(row=0,column=0)

def on_enter(event):
    login_button.configure(fg_color="#132224")

def on_leave(event):
    login_button.configure(fg_color="#1A2127")

login_button.bind('<Enter>', on_enter)
login_button.bind('<Leave>', on_leave)


login_Frame.grid_rowconfigure(0, weight=1)
login_Frame.grid_columnconfigure(0, weight=1)




try:
    window.mainloop()
except KeyboardInterrupt:
    conn.close()