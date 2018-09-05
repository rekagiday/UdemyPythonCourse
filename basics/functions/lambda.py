import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# def say_hello():
#     print("Hello!")

button = tk.Button(frame,
                   text = "Click me!",
                   fg = "blue",
                   bg = "yellow",
                   # command = say_hello) #instead of calling a function we defined elsewhere, we use inline lamba function
                   command = lambda: print('HELLO!') )

button.pack(side = tk.LEFT)
root.mainloop()
