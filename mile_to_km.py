from tkinter import *

km = 0


def button_clicked():
    new_text = miles_input.get()
    miles_value.config(text=int(float(new_text) * 1.60934))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Input Box for Miles
miles_input = Entry()
miles_input.grid(column=2, row=1)

# "Miles" text
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=3, row=1)

# "is equal to " text
miles_label = Label(text="is equal to", font=("Arial", 10))
miles_label.grid(column=1, row=2)

# "value "km text
miles_value = Label(text=km, font=("Arial", 10))
miles_value.grid(column=2, row=2)

# "km" text
miles_label = Label(text="Km", font=("Arial", 10))
miles_label.grid(column=3, row=2)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()
