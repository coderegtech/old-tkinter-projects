# import tkinter library
from tkinter import *
from tkinter import messagebox
from data import Data

main_window = Tk()
main_win_width = main_window.winfo_screenwidth()
main_win_height = main_window.winfo_screenheight()
main_window.geometry("%dx%d+-8+-5" % (main_win_width, main_win_height))
main_window.resizable(True, True)
main_window.title("ENROLLMENT SYSTEM")

#database
db = Data("StudentRecords.db")

#System Title
sys_title = Label(main_window, width = "100", text = "ENROLLMENT SYSTEM",
                  bg = "#111", fg = "white", font = ("calibri 20 bold"), anchor = CENTER)
sys_title.grid(row = 0, column = 0, columnspan = 2, ipady = 10, sticky = W+E)

def select_item(event):
    try:
        global selected_item
        index = record_list.curselection()[0]
        selected_item = record_list.get(index)
    except IndexError:
        pass

def show_in_query():
    record_list.delete(0, END)
    for rec in db.show_query():
        record_list.insert(END, rec)

# add to record
def add_record():
    if student_lrn_entry.get() == '' or student_lname_entry.get() == '' or student_fname_entry.get() == '' or \
            student_address_entry.get() == ''or student_guardian_entry.get() == '' or guardian_tel_no_entry.get() == '' or  \
            student_bday_entry.get() == '' or student_bplace_entry.get() == ''or sex.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(
        student_lrn_entry.get(),student_lname_entry.get(),student_fname_entry.get(),student_address_entry.get(),
        student_guardian_entry.get(),guardian_tel_no_entry.get(), student_bday_entry.get(),student_bplace_entry.get(),
        sex.get()
    )
    show_in_query()
    clear()

def delete_rec():
    db.remove(selected_item[0])
    show_in_query()


def clear():
    student_lrn_entry.delete(0, END)
    student_lname_entry.delete(0, END)
    student_fname_entry.delete(0, END)
    student_address_entry.delete(0, END)
    student_guardian_entry.delete(0, END)
    guardian_tel_no_entry.delete(0, END)
    student_bday_entry.delete(0, END)
    student_bplace_entry.delete(0, END)
    sex.set("NULL")

#==================================================================================
#SHOW RECORDS
show_frame = LabelFrame(main_window, bd = 15, bg = "#ccc")
show_frame.grid(row = 1, column = 1, columnspan = 1, padx = 20, pady = 15, sticky = W)
#==================================================================================
#record list
record_list = Listbox(show_frame, width = 90, height = 18, bd = 0, font = ("calibri 13"))
record_list.grid(row = 0, column = 0, rowspan = 10, padx = 20, pady = 35)
#scrollbar_y for record list
scroll_y = Scrollbar(show_frame)
scroll_y.grid(row = 0, column = 1, rowspan = 10, padx = 20, ipady = 30)
#set record list to scrollbar_y
record_list.configure(yscrollcommand = scroll_y.set)
scroll_y.configure(command = record_list.yview)
#scrollbar_x for record list
scroll_x = Scrollbar(show_frame, orient = HORIZONTAL)
scroll_x.grid(row = 9, column = 0, rowspan = 10, padx = 20, ipadx = 30)
#set record list to scrollbar_x
record_list.configure(xscrollcommand = scroll_x.set)
scroll_x.configure(command = record_list.xview)
#bind
record_list.bind('<<ListboxSelect>>', select_item)

#==================================================================================
#frame for register form
form_frame = LabelFrame(main_window, bd = 15, bg = "#ccc")
form_frame.grid(row = 1, column = 0, padx = 15, pady = 15,
                 ipady =  20, ipadx = 8, sticky = W)
#==================================================================================
form_title = Label(form_frame, width = "30", text = "REGISTER STUDENT", bg = "#111", fg = "white",
                   font = ("calibri 15 bold"), anchor = CENTER)
form_title.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 8)
#Registration form label
student_lrn = Label(form_frame, text = "LRN:", bg = "#ccc", fg = "#000", font = ("calibri 13 bold"))
student_lrn.grid(row = 1, column = 0, pady = 8, padx = 10, sticky = W)
student_lname = Label(form_frame, text = "LAST NAME:", bg = "#ccc", fg = "#000", font = ("calibri 13 bold"))
student_lname.grid(row = 2, column = 0, pady = 8, padx = 10, sticky = W)
student_fname = Label(form_frame, text = "FIRST NAME:", bg = "#ccc", fg = "#000", font = ("calibri 13 bold"))
student_fname.grid(row = 3, column = 0, pady = 8, padx = 10, sticky = W)
student_address = Label(form_frame, text = "ADDRESS:", bg = "#ccc", fg = "#000", font = ("calibri 13 bold"))
student_address.grid(row = 4, column = 0, pady = 8, padx = 10, sticky = W)
student_guardian = Label(form_frame, text = "GUARDIAN:", bg = "#ccc", fg = "#000", font = ("calibri 13 bold"))
student_guardian.grid(row = 5, column = 0, pady = 8, padx = 10, sticky = W)
guardian_tel_no = Label(form_frame, text = "TEL. NO.:", bg = "#ccc", fg = "#000", font = ("calibri 13 bold"))
guardian_tel_no.grid(row = 6, column = 0, pady = 8, padx = 10, sticky = W)
student_bday = Label(form_frame, text = "BIRTHDATE:", bg = "#ccc", fg = "#000", font = ("calibri 13 bold"))
student_bday.grid(row = 7, column = 0, pady = 8, padx = 10, sticky = W)
student_bplace = Label(form_frame, text = "BIRTH PLACE:", bg = "#ccc", fg = "#000", font = ("calibri 13 bold"))
student_bplace.grid(row = 8, column = 0, pady = 8, padx = 10, sticky = W)
student_sex = Label(form_frame, text = "SEX:", bg = "#ccc", fg = "#000", font = ("calibri 13 bold"))
student_sex.grid(row = 9, column = 0, pady = 8, padx = 10, sticky = W)
#==================================================================================
#form entry
student_lrn_entry = Entry(form_frame, width = 20 , fg = "#000", font = ("calibri 12"), bd = 3)
student_lrn_entry.grid(row = 1, column = 1, pady = 8)
student_lname_entry = Entry(form_frame, width = 20 , fg = "#000", font = ("calibri 12"), bd = 3)
student_lname_entry.grid(row = 2, column = 1, pady = 8)
student_fname_entry = Entry(form_frame, width = 20 , fg = "#000", font = ("calibri 12"), bd = 3)
student_fname_entry.grid(row = 3, column = 1, pady = 8)
student_address_entry = Entry(form_frame, width = 20 , fg = "#000", font = ("calibri 12"), bd = 3)
student_address_entry.grid(row = 4, column = 1, pady = 8)
student_guardian_entry = Entry(form_frame, width = 20 , fg = "#000", font = ("calibri 12"), bd = 3)
student_guardian_entry.grid(row = 5, column = 1, pady = 8)
guardian_tel_no_entry = Entry(form_frame, width = 20 , fg = "#000", font = ("calibri 12"), bd = 3)
guardian_tel_no_entry.grid(row = 6, column = 1, pady = 8)
student_bday_entry = Entry(form_frame, width = 20 , fg = "#000", font = ("calibri 12"), bd = 3)
student_bday_entry.grid(row = 7, column = 1, pady = 8)
student_bplace_entry = Entry(form_frame, width = 20 , fg = "#000", font = ("calibri 12"), bd = 3)
student_bplace_entry.grid(row = 8, column = 1, pady = 8)
#radio button for sudent sex
sex = StringVar()
sex.set("NULL")
Radiobutton(form_frame, text = "Male", variable = sex, value = "Male", bg = "#ccc").grid(row = 9, column = 0, pady = 8, columnspan = 2)
Radiobutton(form_frame, text = "Female", variable = sex, value = "Female", bg = "#ccc").grid(row = 9, column = 1, pady = 8, columnspan = 2)

#buttons
btns_frame = LabelFrame(main_window, bd =0)
btns_frame.grid(row = 2, column = 0, columnspan = 3)

#add to record button
add_rec = Button(btns_frame, text = "ADD RECORD", width = 25, font = ("calibri 14 bold"), bd = 5, command = add_record)
add_rec.grid(row = 1, column = 0, ipady = 5, sticky = W)
#add to record button
del_rec = Button(btns_frame, text = "DELETE RECORD", width = 25, font = ("calibri 14 bold"), bd = 5, command = delete_rec)
del_rec.grid(row = 1, column = 1, ipady = 5, padx = 3, sticky = W)
#add to record button
clear_entry = Button(btns_frame, text = "CLEAR", width = 25, font = ("calibri 14 bold"), bd = 5, command = clear)
clear_entry.grid(row = 1, column = 2, ipady = 5, padx = 3, sticky = W)
#add to record button
exit_prog = Button(btns_frame, text = "EXIT PROGRAM", width = 25, font = ("calibri 14 bold"), bd = 5, command = main_window.quit)
exit_prog.grid(row = 1, column = 3, ipady = 5, sticky = W)

show_in_query()
main_window.mainloop()