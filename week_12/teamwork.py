import tkinter as tk
import math
from tkinter import Frame, Label, Button
from number_entry import FloatEntry

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Radius"
    lbl_age = Label(frm_main, text="Radius:")

    # Create an integer entry box where the user will enter her radius.
    ent_rad = FloatEntry(frm_main, width=4, lower_bound=12, upper_bound=90)

    # Create a label that displays "years"
    lbl_age_units = Label(frm_main, text="Centimeters")

    # Create a label that displays "Rates:"
    lbl_rates = Label(frm_main, text="Area:")

    # Create labels that will display the results.
    area = Label(frm_main, width=3)
    lbl_rate_units = Label(frm_main, text="Squared Centimeters")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_age.grid(      row=0, column=0, padx=3, pady=3)
    ent_rad.grid(      row=0, column=1, padx=3, pady=3)
    lbl_age_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_rates.grid(     row=1, column=0, padx=(30,3), pady=3)
    area.grid(      row=1, column=1, padx=3, pady=3)
    lbl_rate_units.grid(row=1, column=3, padx=0, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")

    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the user's radius.
            radius = ent_rad.get()
            pi = math.pi
            result = pi * (radius ** 2)
            area.config(text=f"{result:.2f}")

        except ValueError:
            # When the user deletes all the digits in the radius
            # entry box, clear the slowest and fastest labels.
            area.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_rad.clear()
        area.config(text="")
        ent_rad.focus()

    # Bind the calculate function to the radius entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_rad.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the radius entry box.
    ent_rad.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()