from tkinter import *
from Patient_db import PatientData

#database
db = PatientData('PatientRecord.db')


def back_to_main():
    wn2.destroy()
    main_menu()

def back_to_main2():
    wn3.destroy()
    main_menu()


def showInfo():
    return

def add_to_query():
    global records
    records = ""
    for cont in db.show_query():
        records += str(cont) + "\n"

def submit():
    db.insert(
        name_entry.get(), address_entry.get(), telephone_no_entry.get(), age_entry.get(), occupation_entry.get(), status_entry.get(),
        medical_his_entry.get(), general_health_entry.get(), headaches_entry.get(), allergies_entry.get(), bleeding_gums_entry.get(), heart_bp_entry.get(),
        family_his_entry.get()
    )
    clear_entry()
    add_to_query()

def delete_rec():
    db.remove(select_id.get())
    select_id.delete(0, END)
    add_to_query()
    records_label = Label(record_list, text = records)
    records_label.grid(row = 0, column = 3)



def clear_entry():
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



def addRecord_input():
    global wn2
    wn2 = Tk()
    wn2.title("REGISTER RECORD")
    wn2.geometry("650x400+380+150")
    wn2.resizable(False, False)
    wn2_title = Label(wn2, text = "REGISTER RECORD", bg = "#111", fg = "white", font = ("calibri 18 bold"))
    wn2_title.grid(row = 0,column = 0, columnspan = 3, ipadx = 205)
    #frame
    frame = Frame(wn2, bg = "#fefefe")
    frame.grid(row = 1, column = 0, columnspan = 4, ipadx = 10, ipady = 20, pady = 20)
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

    # globals
    global name_entry
    global address_entry
    global telephone_no_entry
    global age_entry
    global occupation_entry
    global status_entry
    global medical_his_entry
    global general_health_entry
    global headaches_entry
    global allergies_entry
    global bleeding_gums_entry
    global heart_bp_entry
    global family_his_entry

    #entry
    name_entry = Entry(frame)
    name_entry.grid(row = 0, column = 1, pady = 3)
    address_entry = Entry(frame)
    address_entry.grid(row=0, column=4, pady = 3)
    telephone_no_entry = Entry(frame)
    telephone_no_entry.grid(row=1, column=1, pady = 3)
    age_entry = Entry(frame)
    age_entry.grid(row=1, column=4, pady = 3)
    occupation_entry = Entry(frame)
    occupation_entry.grid(row=2, column=1, pady = 3)
    status_entry = Entry(frame)
    status_entry.grid(row=2, column=4, pady = 3)
    medical_his_entry = Entry(frame)
    medical_his_entry.grid(row=3, column=1, pady = 3)
    general_health_entry = Entry(frame)
    general_health_entry.grid(row=3, column=4, pady=3)
    headaches_entry = Entry(frame)
    headaches_entry.grid(row=4, column=1, pady=3)
    allergies_entry = Entry(frame)
    allergies_entry.grid(row=4, column=4, pady=3)
    bleeding_gums_entry = Entry(frame)
    bleeding_gums_entry.grid(row=5, column=1, pady=3)
    heart_bp_entry = Entry(frame)
    heart_bp_entry.grid(row=5, column=4, pady=3)
    family_his_entry = Entry(frame)
    family_his_entry.grid(row=6, column=1, pady=3)

    #add to record button
    add_to_record = Button(wn2, text = "Add To Record", command = submit)
    add_to_record.grid(row = 2, column = 0)
    #go back to menu
    back_to_menu = Button(wn2, text = "Menu", command = back_to_main)
    back_to_menu.grid(row = 2, column = 1)
    #exit program
    exit_program = Button(wn2, text = "Exit Program", command = wn2.destroy)
    exit_program.grid(row = 2, column = 2)

    wn.destroy()
    wn2.mainloop()


def showRecord():
    global wn3
    wn3 = Tk()
    wn3.title("SHOW ALL RECORDS")
    wn3.geometry("700x400+380+150")
    wn3.resizable(False, False)
    wn3_title = Label(wn3, text = "ALL PATIENT RECORDS", bg = "#111", fg = "white", font = ("calibri 15 bold"))
    wn3_title.grid(row = 0, column = 0, columnspan = 4, ipadx = 205, ipady = 10)

    global record_list
    record_list = LabelFrame(wn3)
    record_list.grid(row = 1, column = 0, columnspan = 4, ipadx = 180, ipady = 80, pady = 10)

    add_to_query()
    records_label = Label(record_list, text = records)
    records_label.grid(row = 0, column = 3)

    #select with ID no.
    select_label = Label(wn3, text = "Enter Patient ID: ")
    select_label.grid(row = 2, column = 1, pady = 8)
    global select_id
    select_id = Entry(wn3, bd = 2, width = 10)
    select_id.grid(row = 2, column = 2, pady = 8)
    # add to record button
    show_info_record = Button(wn3, text="Show Info", command=showInfo)
    show_info_record.grid(row=3, column=0)
    #go back to menu
    back_to_menu = Button(wn3, text = "Menu", command = back_to_main2)
    back_to_menu.grid(row = 3, column = 1)

    delete_record = Button(wn3, text="Delete", command=delete_rec)
    delete_record.grid(row=3, column=2)
    # exit program
    exit_program = Button(wn3, text="Exit Program", command=wn3.destroy)
    exit_program.grid(row=3, column=3)

    wn.destroy()
    wn3.mainloop()




def main_menu():
    global wn
    wn = Tk()
    wn.title("Patient Record")
    wn.geometry("400x300+500+200")
    wn.resizable(False, False)
    #title Label
    title_label = Label(wn, text = "PATEINT INFORMATION SYSTEM", bg = "#111", fg = "white", font = ("calibri 15 bold"))
    title_label.grid(row = 0, column = 0, columnspan = 3, ipadx = 13, ipady = 10, sticky = W+E)


    #Add record button
    Add_record_btn = Button(wn, text = "ADD RECORD", width = 30, bg = "#222", fg = "white", border = 1, command = addRecord_input)
    #Show record button
    Show_record_btn = Button(wn, text = "SHOW RECORD", width = 30, bg = "#222", fg = "white", border = 1, command = showRecord)
    #layout
    Add_record_btn.grid(row = 1, column = 0, columnspan = 3, pady = 30, ipady = 8)
    Show_record_btn.grid(row = 2, column = 0, columnspan = 3, ipady = 8)

    wn.mainloop()

#run main-window
main_menu()