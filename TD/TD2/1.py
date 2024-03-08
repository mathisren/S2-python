import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400 # Taille des canvas


root = tk.Tk() # Initialise la fenetre

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = CANVAS_WIDTH / 2
x1 = CANVAS_WIDTH - 100 # 500
y = 0 # 200
canvas.create_line(x0, y, x0, CANVAS_HEIGHT) # Créer une ligne de (X,Y) à (X1,Y)
canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50) # Créer un oval de (X,Y) à (X'Y'), ici 
canvas.create_oval(x0 - 50, (CANVAS_HEIGHT / 2) - 50, x0 + 50, CANVAS_HEIGHT / 2 + 50)
canvas.create_oval(x0 - 50, CANVAS_HEIGHT - 50, x0 + 50 , CANVAS_HEIGHT + 50)

# Fin de votre code

canvas.grid()
root.mainloop()
