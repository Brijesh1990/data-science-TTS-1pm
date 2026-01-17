import tkinter as tk
import datetime
# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter Window")
# Set the window size
root.geometry("300x200")
# Create a label widget
label = tk.Label(root, text="just print date & time", font=("Arial", 18))
label.pack(pady=20) #set a position with some padding top to bottom
# print date & time
print("the date time is :",datetime.datetime.now())
 
# print a windows message
root.mainloop()
