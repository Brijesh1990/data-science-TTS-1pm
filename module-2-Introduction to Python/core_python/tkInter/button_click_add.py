import tkinter as tk
import tkinter.messagebox as messagebox
# create a function 
def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    return tk.messagebox.showinfo("Result", f"The sum is: {result}")

#create a window
root = tk.Tk()
root.title("Add Two Numbers")
root.geometry("400x300")
# create labels and entry widgets for two numbers
label1 = tk.Label(root, text="Enter first number:")
label1.pack(pady=10)
entry1 = tk.Entry(root)
entry1.pack(pady=10)   

label2 = tk.Label(root, text="Enter second number:")
label2.pack(pady=10)
entry2 = tk.Entry(root)
entry2.pack(pady=10 )

# create a button to perform addition
button = tk.Button(root, text="Add", command=add)
button.pack(pady=20)

# start the main event loop
root.mainloop()