import tkinter as tk
# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter Window")
# Set the window size
root.geometry("300x200")
# Create a label widget
label = tk.Label(root, text="Hello, Brijesh!", font=("Arial", 24))
label.pack(pady=20) #set a position with some padding top to bottom
# print a windows message
root.mainloop()
