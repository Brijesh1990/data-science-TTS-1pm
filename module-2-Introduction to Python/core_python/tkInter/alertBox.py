import tkinter as tk
import tkinter.messagebox as messagebox
# create a function to show alert box
def show_alert():
    # print("Alert Button Clicked!")
    return tk.messagebox.showinfo("Alert", "This is an Brijesh!")

# Create the main application window
root = tk.Tk()
root.title("Alert Box Example")
root.geometry("400x300")
# Create a label widget
label = tk.Label(root, text="This is an alert box example using Tkinter.", font=("Arial", 14))
label.pack(pady=20)  # set a position with some padding top to bottom
# create a button
button=tk.Button(root, text="click on button", command=show_alert, font=('Arial', 14))
button.pack(pady=20)  # set a position with some padding top to bottom


# main loop to run the application
root.mainloop()