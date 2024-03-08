import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400 # Taille des canvas


root = tk.Tk() # Initialise la fenetre

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x = CANVAS_WIDTH / 2
y1 = CANVAS_HEIGHT- 100
y0 = 100
canvas.create_line(x, y0, x,y1) # Créer une ligne de (X,Y) à (X1,Y)
canvas.create_oval(x - 50, y0 + 50, x + 50, y0 - 50) # Créer un oval de (X,Y) à (X'Y'), ici 
canvas.create_oval(x - 50, y1 +50, x + 50, y1 - 50)
canvas.create_oval(x - 50, (y1 + y0) / 2 + 50, x + 50 , (y1+y0)/2 - 50)
canvas.grid(row = 0, column= 0)

# Fin de votre code

canvas.grid()
root.mainloop()
