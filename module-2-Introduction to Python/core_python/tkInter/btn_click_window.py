import tkinter as tk
import tkinter.messagebox as messagebox
# create a function 
def hello_brijesh():
    # print("Hello, Brijesh!")
    return tk.messagebox.showinfo("Greeting", "Hello, Brijesh!")

#create a window
root = tk.Tk()
root.title("Button Click Window")
root.geometry("300x200")
# create a button and attach the function to it
button = tk.Button(root, text="Click Me", command=hello_brijesh) 

button.pack(pady=50) # set a position with some padding top to bottom
# run the application
root.mainloop()

