import tkinter as tk
import random



def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

root = tk.Tk()
root.title("Couleur")
frame_btn = tk.Frame(root)
canva = tk.Canvas(root, bg = "black", width=256, height= 256)

def draw_pixel(i, j, color):
    canva.create_rectangle(i,j, i,j, fill = color, width=0)

def ecran_aleatoire():
    for i in range(260):
        for j in range(260):
            color = get_color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            canva.create_rectangle(i,j,i,j, fill = color, width=0)

def degrade_gris ():
    for i in range(264):
        color = get_color(i, i, i)
        for j in range(264):
            canva.create_rectangle(i,j,i,j, fill = color, width=0)

def degrade_2D ():
    for i in range(264):
        color = get_color(255 - i, 0, 255-i)
        for j in range(264):
            canva.create_rectangle(i,j,i,j, fill = color, width=0)

btn_aleatoire = tk.Button(frame_btn, text = "Aléatoire", foreground= "blue", command= ecran_aleatoire)
btn_degrade = tk.Button(frame_btn, text = "Dégradé gris", foreground = "blue", command= degrade_gris)
btn_degrade_2D = tk.Button(frame_btn, text = "Dégradé 2D", foreground = "Blue", command= degrade_2D)


btn_aleatoire.grid(pady = 10)
btn_degrade.grid(pady =10)
btn_degrade_2D.grid(pady =10)
frame_btn.grid(column= 0, row= 0)
canva.grid(column= 1, row = 0)



#draw_pixel(100,100, get_color(255,255,255))

root.mainloop()