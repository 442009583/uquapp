import time
import customtkinter as ctk
from CTkListbox import *
import sqlite3
import threading

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

window = ctk.CTk()
window.title("aa")
window.geometry("500x600")
window.configure(fg_color="#1A2127")

window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

sid = "4205523"


# Student Info
####################################################################################################################################################################

cursor.execute(f"SELECT name FROM student WHERE id = {sid}")
name = cursor.fetchone()[0]

stuinfo_frame = ctk.CTkFrame(window, fg_color="#1A2127")
stuinfo_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
stuinfo_frame.grid_rowconfigure(0, weight=1)
stuinfo_frame.grid_columnconfigure(0, weight=1)
stuinfo_frame.grid_propagate(0)

in_stuinfo_frame = ctk.CTkFrame(stuinfo_frame, fg_color="#1A2127")
in_stuinfo_frame.grid(row=0, column=0)

stuname = ctk.CTkLabel(in_stuinfo_frame, text=f"الأسم: {name}", font=("", 30))
stuname.grid()

sidlbl = ctk.CTkLabel(in_stuinfo_frame, text=f"الرقم: {sid}", font=("", 30))
sidlbl.grid(sticky="e")

####################################################################################################################################################################


# ATTENDANCE CHOICE
####################################################################################################################################################################
attendance_status = True


def combobox_callback(choice):
    global attendance_status
    if choice == "Yes":
        attendance_status = True
    elif choice == "No":
        attendance_status = False


attenchoice_frame = ctk.CTkFrame(window,corner_radius=0)
attenchoice_frame.grid(row=1, column=0, sticky="nsew")

attenchoice_frame.grid_propagate(0)
attenchoice_frame.grid_rowconfigure(0, weight=1)
attenchoice_frame.grid_columnconfigure(0, weight=1)

in_choice_frame = ctk.CTkFrame(attenchoice_frame)
in_choice_frame.grid(row=0, column=0)

attenlbl = ctk.CTkLabel(in_choice_frame, text="Will You Be Attending?", font=("", 15))
attenlbl.grid()
combobox = ctk.CTkComboBox(in_choice_frame, values=["", "Yes", "No"], command=combobox_callback, font=("", 15))
combobox.grid()

####################################################################################################################################################################


# Classes List
####################################################################################################################################################################

classes_frame = ctk.CTkFrame(window,corner_radius=0 )
classes_frame.grid(row=1, column=1, sticky="nsew")
classes_frame.grid_rowconfigure(0, weight=1)
classes_frame.grid_columnconfigure(0, weight=1)

in_classes_List = ctk.CTkFrame(classes_frame, )
in_classes_List.grid()

cursor.execute(f"SELECT class_id FROM student_classes WHERE student_id = {sid}")
classes = cursor.fetchall()

c = []

for i in classes:
    cursor.execute(f"SELECT name,start,end FROM classes WHERE id = ?", (i[0],))
    c.append(cursor.fetchone())

c.sort(key=lambda x: x[1])

checkbox_vars = []
for item in c:
    boxformat = f"المادة: {item[0]}    {item[1]}-{item[2]}"
    var = ctk.IntVar()
    checkbox_vars.append(var)
    checkbox = ctk.CTkCheckBox(in_classes_List, font=("", 20), text=boxformat, variable=var)
    checkbox.grid(sticky="w", pady=(5, 0))
    checkbox.select()

atcl = []


def checkbox_checked():
    atcl = []
    for i, var in enumerate(checkbox_vars):
        if var.get() == 1:
            atcl.append(list(c[i]))

    print(atcl)


button = ctk.CTkButton(in_classes_List, text='Check', command=checkbox_checked)
button.grid()

####################################################################################################################################################################


# Drivers List
####################################################################################################################################################################


list_bus_frame = ctk.CTkFrame(window,corner_radius=0)
list_bus_frame.grid(row=2, column=0, sticky="nsew", columnspan=2)

list_bus_frame.grid_rowconfigure(0, weight=1)
list_bus_frame.grid_columnconfigure(0, weight=1)

in_bus_List = ctk.CTkFrame(list_bus_frame, )
in_bus_List.grid()

drivers_listbox = CTkListbox(in_bus_List, font=("", 16))
drivers_listbox.grid()


file = open('drivers.txt', 'r', encoding='utf-8')

def showbus():
    while True:
        drivers = []

        d = file.read().splitlines()
        for driver in d:
            a = driver.split(" ")
            drivers.append([a[0]] + [a[1]])

        for driver in drivers:
            drivers_listbox.insert(ctk.END, f"{driver[1]:<8}{driver[0]}")
        time.sleep(2)


selected_driver = None
enrolled_with = None
def handle_selection(event):
    global selected_driver
    ss = drivers_listbox.get(drivers_listbox.curselection())
    sss = str(ss).replace("     "," ")
    selected_driver = sss.split(" ")[0]

drivers_listbox.bind('<<ListboxSelect>>', handle_selection)

####################################################################################################################################################################



sb_frame = ctk.CTkFrame(window,fg_color="#1A2127")
sb_frame.grid(row=4, column=0, columnspan=2)
submit_button = ctk.CTkButton(sb_frame, text="أرسال", command=lambda: enroll())
submit_button.grid(row=0, column=0,pady=10)


def enroll():
    global enrolled_with
    if attendance_status == True and selected_driver != None and selected_driver != enrolled_with:
        if enrolled_with != None:
            busfile = open(f"{enrolled_with}.txt","r+",encoding="utf-8")
            lines = busfile.readlines()
            lines = [line for line in lines if line.strip() != f"{sid},{name}"]
            print(lines)
            print(f"ازيلت الطالبة ({sid}, {name}) من السائق رقم {enrolled_with}")
            busfile.truncate(0)
            busfile.writelines(lines)

        busfile = open(f"{selected_driver}.txt","a",encoding="utf-8")
        busfile.write(f"{sid},{name}")
        busfile.write("\n")
        print(f"تم تسجيل الطالبة ({sid}, {name}) مع السائق رقم {selected_driver}")
        enrolled_with = selected_driver

    else:
        print("try again")



if __name__ == "__main__":
    showthread = threading.Thread(target=showbus)
    showthread.start()
    try:
        window.mainloop()
    except KeyboardInterrupt:
        conn.close()