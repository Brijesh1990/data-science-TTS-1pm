import tkinter as tk
import tkinter.messagebox as messagebox
# create a function
def input_user():
    user_input = entry.get()
    print("User name is :", user_input)
    # return tk.messagebox.showinfo("User Input", f"Hello, {user_input}!")
# create a window
root = tk.Tk()
root.title("Input User Window")
root.geometry("400x300")
# create a label
label = tk.Label(root, text="Enter your name:", font=("Arial", 14)) 
label.pack(pady=20)  # set a position with some padding top to bottom
# create an entry widget
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)  # set a position with some padding top to bottom   

# create a button and attach the function to it
button = tk.Button(root, text="Submit", command=input_user)
button.pack(pady=20)  # set a position with some padding top to bottom
# run the application
root.mainloop()