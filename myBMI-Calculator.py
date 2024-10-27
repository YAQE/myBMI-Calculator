import numpy
from tkinter import *

window = Tk()
window.title("BMI")
window.minsize(200, 200)

my_label = Label(text="Welcome to myBMI Calculator App", font=('Arial', 20, "bold"))
my_label.pack()

my_weight = Label(text="Entry Your Weight (kg) : ")
my_weight.pack()

weight_entry = Entry(width=30)
weight_entry.pack()

my_height = Label(text="Enter Your Height (cm) : ")
my_height.pack()

height_entry = Entry(width=30)
height_entry.pack()

resoult = Label()
resoult.pack()


def submitbutton_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight > 0 and height > 0:
                BMI = weight / (height / 100 * height / 100)
                if BMI <= 18.4:
                    resoult.config(text=f"Your BMI: {round(BMI, 2)} You are Underweight.")
                elif 18.5 <= BMI <= 24.9:
                    resoult.config(text=f"Your BMI: {round(BMI, 2)} You are Normal.")
                elif 25.0 <= BMI <= 39.9:
                    resoult.config(text=f"Your BMI: {round(BMI, 2)} You are Overweight.")
                else:
                    resoult.config(text=f"Your BMI: {round(BMI, 2)} You are Obese.")
        else:
            resoult.config(text="Please enter only POSITIVE NUMBERS value")
    except ValueError:
        resoult.config(text="Please enter only NUMBERS value")

submitb = Button(text="Calculate", command=submitbutton_clicked)
submitb.pack()

















window.mainloop()