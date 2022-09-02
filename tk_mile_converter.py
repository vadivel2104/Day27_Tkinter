import tkinter as tk

windows = tk.Tk()
windows.title("Km to Mile converter")
windows.minsize(width=500, height=300)
windows.config(padx=20, pady=20)



input = tk.Entry(width=3)
input.grid(column=0, row=1)

result = 0

def result_mile():
    km = float(input.get())
    mile = round(km/1.609, 2)
    ans_label.config(text= f"is equal to {mile}")

miles_label = tk.Label(text="KM",font=("Arial",10,"bold"))
miles_label.grid(column=1,row=1)

ans_label = tk.Label(text=f"is equal to {result}", font=("Arial", 10, "bold"))
ans_label.grid(column=1, row=2)

km_label = tk.Label(text="Miles", font=("Arial", 10, "bold"))
km_label.grid(column=3, row=2)

convert = tk.Button(text="convert", command=result_mile)
convert.grid(column=0, row=2)





windows.mainloop()


