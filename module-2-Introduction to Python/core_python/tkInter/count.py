import tkinter as tk
import tkinter.messagebox as messagebox
#create a window
root = tk.Tk()
root.title("Count a number")
root.geometry("300x400")
# initalize count 
count=0
# create a function 
# function to update label
def upd_label():
   label.config(text=str(count))
# increment
def increment():
   global count
   count+=1
   upd_label()
def decrement():
   global count
   count-=1
   upd_label()

def reset():
   global count
   count=0
   upd_label()

   
# defined label 
label=tk.Label(root,text="0",font=("Arial",25))
label.pack(pady=20)
 
# create a button to perform addition
button = tk.Button(root, text="+", command=increment,font=("Arial",25))
button.pack(pady=20)

button = tk.Button(root, text="-", command=decrement,font=("Arial",25))
button.pack(pady=20)


button = tk.Button(root, text="Reset", command=reset,font=("Arial",20))
button.pack(pady=20)

# start the main event loop
root.mainloop()