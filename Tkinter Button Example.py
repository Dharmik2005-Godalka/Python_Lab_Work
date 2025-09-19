import tkinter as tk

def say_hello():
    print("Hello, Tkinter!")

root = tk.Tk()
btn = tk.Button(root, text="Click Me", command=say_hello)
btn.pack()
root.mainloop()
