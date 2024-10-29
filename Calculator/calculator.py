
from tkinter import *

def calc_click(number):
	# calculator_Input.delete(0, END)
	current = calculator_Input.get()
	calculator_Input.delete(0 , END)
	calculator_Input.insert(0, str(current) + str(number))

def calc_add():
	num1 = calculator_Input.get()
	remove = calculator_Input.delete(0, END)
	global f_num
	global math
	math = "addition"
	f_num = int(num1)
	calculator_Input.delete(0, END)

def calc_sub():
	num1 = calculator_Input.get()
	remove = calculator_Input.delete(0, END)
	global f_num
	global math
	math = "subtraction"
	f_num = int(num1)
	calculator_Input.delete(0, END)

def calc_multi():
	num1 = calculator_Input.get()
	remove = calculator_Input.delete(0, END)
	global f_num
	global math
	math = "multiplication"
	f_num = int(num1)
	calculator_Input.delete(0, END)

def calc_divide():
	num1 = calculator_Input.get()
	remove = calculator_Input.delete(0, END)
	global f_num
	global math
	math = "division"
	f_num = int(num1)
	calculator_Input.delete(0, END)

def calc_equal():
	num2 = calculator_Input.get()
	calculator_Input.delete(0, END)
	if math == "addition":
		calculator_Input.insert(0, f_num + int(num2))

	if math == "subtraction":
		calculator_Input.insert(0, f_num - int(num2))

	if math == "multiplication":
		calculator_Input.insert(0, f_num * int(num2))

	if math == "division":
		calculator_Input.insert(0, f_num / int(num2))

def calc_clear():
	calculator_Input.delete(0, END)

def calculator_screen():
	global screen
	global calculator_Input
	screen = Tk()
	screen.title("Basic Calculator")
	calculator_Input = Entry( screen, width = 40, borderwidth = 5, font = ("none 10 bold"))
	calculator_Input.grid(row = 0, column = 0, columnspan =3, padx = 10, ipady = 5, pady = 10)

# calculator button number
	button_1 = Button(screen, text = "1", padx = 40, pady = 20, command =lambda: calc_click(1))
	button_2 = Button(screen, text = "2", padx = 40, pady = 20, command = lambda: calc_click(2))
	button_3 = Button(screen, text = "3", padx = 40, pady = 20, command = lambda: calc_click(3))
	button_4 = Button(screen, text = "4", padx = 40, pady = 20, command = lambda: calc_click(4))
	button_5 = Button(screen, text = "5", padx = 40, pady = 20, command = lambda: calc_click(5))
	button_6 = Button(screen, text = "6", padx = 40, pady = 20, command = lambda: calc_click(6))
	button_7 = Button(screen, text = "7", padx = 40, pady = 20, command = lambda: calc_click(7))
	button_8 = Button(screen, text = "8", padx = 40, pady = 20, command = lambda: calc_click(8))
	button_9 = Button(screen, text = "9", padx = 40, pady = 20, command = lambda: calc_click(9))
	button_0 = Button(screen, text = "0", padx = 40, pady = 20, command = lambda: calc_click(0))
	button_add = Button(screen, text = "+", padx = 39, pady = 20, command = calc_add)
	button_equal = Button(screen, text = "=", padx = 87, pady = 20, command = calc_equal)
	button_clear = Button(screen, text = "Clear", padx = 77, pady = 20, command = calc_clear)

	button_sub = Button(screen, text = "-", padx = 41, pady = 20, command = calc_sub)
	button_multi = Button(screen, text = "*", padx = 40, pady = 20, command = calc_multi)
	button_divide = Button(screen, text = "/", padx = 41, pady = 20, command = calc_divide)


# number positioning

	button_1.grid(row = 3, column = 0)
	button_2.grid(row = 3, column = 1)
	button_3.grid(row = 3, column = 2)

	button_4.grid(row = 2, column = 0)
	button_5.grid(row = 2, column = 1)
	button_6.grid(row = 2, column = 2)

	button_7.grid(row = 1, column = 0)
	button_8.grid(row = 1, column = 1)
	button_9.grid(row = 1, column = 2)

	button_0.grid(row = 4, column = 0)
	button_add.grid(row = 5, column = 0)
	button_equal.grid(row = 5, column = 1, columnspan =2)
	button_clear.grid(row = 4, column = 1, columnspan =2)

	button_sub.grid(row = 6, column = 0)
	button_multi.grid(row = 6, column = 1)
	button_divide.grid(row = 6, column = 2)



	screen.mainloop()

calculator_screen()