from tkinter import *

window = Tk()
window.title('Mile to KM Converter')
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# takes mile input
miles_input = Entry()
miles_input.grid(column=1, row=0)

# displays miles
miles_label = Label(text='miles', font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)

# displays is equal to
is_equal_to = Label(text='is equal to', font=("Arial", 10, "bold"))
is_equal_to.grid(column=0, row=1)

# displays result
kilometer_result_label = Label(text='0', font=("Arial", 10, "bold"))
kilometer_result_label.grid(column=1, row=1)

# displays km
kilometer_label = Label(text='km', font=("Arial", 10, "bold"))
kilometer_label.grid(column=2, row=1)


# Converter
def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.6093
    kilometer_result_label.config(text=f"{km}")


# displays calculate button
calculate_button = Button(text='Calculate', command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()
