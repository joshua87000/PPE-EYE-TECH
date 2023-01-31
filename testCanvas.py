import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

arc = canvas.create_arc(50, 50, 250, 250, start=0, extent=90, width=0, fill="red")

root.mainloop()
