import tkinter as tk
# import button_func as bf
#
# action = bf.BUTTONS()

windows = tk.Tk()
windows.title("My First GUI")
windows.minsize(width=500, height=300)
windows.config(padx=20, pady=20)

my_lable = tk.Label(text="Header", font=("Arial",24,"bold"))
# my_lable.pack(side="top")
my_lable.grid(column=100,row=10)

input = tk.Entry()
# input.pack()
input.grid(column=0,row=0)


def display():
    my_lable.config(text=input.get())


button_1 = tk.Button(text="click", command=display)
# button_1.pack()
button_1.grid(column=0,row=50)







windows.mainloop()
