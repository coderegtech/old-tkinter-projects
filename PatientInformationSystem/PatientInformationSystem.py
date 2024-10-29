from tkinter import *
from tkinter import messagebox
from PatientRecord_db import PatientData

main_window = Tk()

main_window_width = main_window.winfo_screenwidth()
main_window_height = main_window.winfo_screenheight()
main_window.geometry("%dx%d+0+0" % (main_window_width, main_window_height))
main_window.configure(background = "#ccc")
main_window.title("PATIENT INFORMATION SYSTEM")
main_window.resizable(False, False)
#main window title
main_window_title = Label(main_window, width = "70", text = "PATIENT INFORMATION SYSTEM", font = ("helverica 25 bold"),
                          bg = "#111", fg = "white", anchor = CENTER)
main_window_title.grid(row = 0, column = 0, columnspan = 2, ipady = 15, sticky =W+E)

#database
db = PatientData("PatientRecord.db")

def select_item(event):
    try:
        global selected_item
        index = record_list.curselection()
        selected_item = record_list.get(index)
    except IndexError:
        pass

def add_to_query():
    record_list.delete(0, END)
    for row in db.show_query():
        record_list.insert(END, row)


def submit():
    if name_entry.get() == '' or address_entry.get() == '' or telephone_no_entry.get() == '' or age_entry.get() == ''\
        or occupation_entry.get() == '' or status_entry.get() == '' or medical_his_entry.get() == '' or general_health_entry.get() == ''\
        or headaches_entry.get() == '' or allergies_entry.get() == '' or bleeding_gums_entry.get() == '' or heart_bp_entry.get() == ''\
        or family_his_entry.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(
        name_entry.get(), address_entry.get(), telephone_no_entry.get(),
        age_entry.get(), occupation_entry.get(),status_entry.get(),
        medical_his_entry.get(), general_health_entry.get(), headaches_entry.get(),
        allergies_entry.get(),bleeding_gums_entry.get(), heart_bp_entry.get(),
        family_his_entry.get()
    )
    add_to_query()
    clear_input()

def delete_rec():
    db.remove(selected_item[0])
    add_to_query()

def clear_input():
    name_entry.delete(0, END)
    address_entry.delete(0, END)
    telephone_no_entry.delete(0, END)
    age_entry.delete(0, END)
    occupation_entry.delete(0, END)
    status_entry.delete(0, END)
    medical_his_entry.delete(0, END)
    general_health_entry.delete(0, END)
    headaches_entry.delete(0, END)
    allergies_entry.delete(0, END)
    bleeding_gums_entry.delete(0, END)
    heart_bp_entry.delete(0, END)
    family_his_entry.delete(0, END)


#frame2
frame2 = LabelFrame(main_window, text = "PATIENT SHOW ALL RECORD", border = 15)
frame2.grid(row = 1, column = 1, rowspan = 4, ipadx = 10, ipady = 15, padx = 50, pady = 10)

# listbox
record_list = Listbox(frame2, height=11, width = "70", font = ("calibri 13"), bg="#fefefe")
record_list.grid(row=1, column=0, columnspan=2)
# scrollbar
scrollbar = Scrollbar(frame2)
scrollbar.grid(row=1, column=2, ipady=10)
# set scrollbar to listbox
record_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=record_list.yview)
# Bind select
record_list.bind('<<ListboxSelect>>', select_item)

#put to query
add_to_query()

# add to record button
show_info_record = Button(frame2, text="Show Info", font = ("monospace 10 bold"), bd = 5)
show_info_record.grid(row=2, column=0, pady = 10)
# go back to menu
delete_record = Button(frame2, text="Delete", font = ("monospace 10 bold"), bd = 5, command = delete_rec)
delete_record.grid(row=2, column=1, pady = 10)

#frame
frame = LabelFrame(main_window, text = "PATIENT INPUT RECORD", border = 15)
frame.grid(row = 1, column = 0, ipadx = 10, ipady = 30, padx = 10, pady = 10, sticky = W+E)

#labels
name_label = Label(frame, text = "Name", font = ("calibri 12"))
name_label.grid(row = 0, column = 0, padx = 8, pady = 3, sticky = W)
address_label = Label(frame, text = "Address", font = ("calibri 12"))
address_label.grid(row = 0, column = 3, padx = 8, pady = 3, sticky = W)
telephone_no_label = Label(frame, text = "Telephone No.", font = ("calibri 12"))
telephone_no_label.grid(row = 1, column = 0, padx = 8, pady = 3, sticky = W)
age_label = Label(frame, text = "Age", font = ("calibri 12"))
age_label.grid(row = 1, column = 3, padx = 8, pady = 3, sticky = W)
occupation_label = Label(frame, text = "Occupation", font = ("calibri 12"))
occupation_label.grid(row = 2, column = 0, padx = 8, pady = 3, sticky = W)
status_label = Label(frame, text = "Status", font = ("calibri 12"))
status_label.grid(row = 2, column = 3, padx = 8, pady = 3, sticky = W)
medical_his_label = Label(frame, text = "Medical History", font = ("calibri 12"))
medical_his_label.grid(row = 3, column = 0, padx = 8, pady = 3, sticky = W)
general_health_label = Label(frame, text="General Health", font=("calibri 12"))
general_health_label.grid(row=3, column=3, padx=8, pady=3, sticky=W)
headaches_label = Label(frame, text="Headaches", font=("calibri 12"))
headaches_label.grid(row=4, column=0, padx=8, pady=3, sticky=W)
allergies_label = Label(frame, text="Allergies", font=("calibri 12"))
allergies_label.grid(row=4, column=3, padx=8, pady=3, sticky=W)
bleeding_gums_label = Label(frame, text="Bleeding of Gums", font=("calibri 12"))
bleeding_gums_label.grid(row=5, column=0, padx=8, pady=3, sticky=W)
heart_bp_label = Label(frame, text="Heart - B.P.", font=("calibri 12"))
heart_bp_label.grid(row=5, column=3, padx=8, pady=3, sticky=W)
family_his_label = Label(frame, text="Family History", font=("calibri 12"))
family_his_label.grid(row=6, column=0, padx=8, pady=3, sticky=W)

#entry
name_entry = Entry(frame, border = 3)
name_entry.grid(row = 0, column = 1, pady = 3)
address_entry = Entry(frame, border = 3)
address_entry.grid(row=0, column=4, pady = 3)
telephone_no_entry = Entry(frame, border = 3)
telephone_no_entry.grid(row=1, column=1, pady = 3)
age_entry = Entry(frame, border = 3)
age_entry.grid(row=1, column=4, pady = 3)
occupation_entry = Entry(frame, border = 3)
occupation_entry.grid(row=2, column=1, pady = 3)
status_entry = Entry(frame, border = 3)
status_entry.grid(row=2, column=4, pady = 3)
medical_his_entry = Entry(frame, border = 3)
medical_his_entry.grid(row=3, column=1, pady = 3)
general_health_entry = Entry(frame, border = 3)
general_health_entry.grid(row=3, column=4, pady=3)
headaches_entry = Entry(frame, border = 3)
headaches_entry.grid(row=4, column=1, pady=3)
allergies_entry = Entry(frame, border = 3)
allergies_entry.grid(row=4, column=4, pady=3)
bleeding_gums_entry = Entry(frame, border = 3)
bleeding_gums_entry.grid(row=5, column=1, pady=3)
heart_bp_entry = Entry(frame, border = 3)
heart_bp_entry.grid(row=5, column=4, pady=3)
family_his_entry = Entry(frame, border = 3)
family_his_entry.grid(row=6, column=1, pady=3)

#add to record button
add_to_record = Button(frame, text = "Add To Record", font = ("monospace 10 bold"), bd = 5, command = submit)
add_to_record.grid(row = 7, column = 1, ipady = 5, pady = 5, padx = 10)
#reset button
reset_btn = Button(frame, text = "Reset", font = ("monospace 10 bold"), bd = 5, command = clear_input)
reset_btn.grid(row = 7, column = 2, columnspan = 3, ipady = 5, ipadx = 8, padx = 10, sticky = W)
main_window.mainloop()