import tkinter as tk

root = tk.Tk()

root.title("Cible en couleur")

longeur, largeur = (400,400)

canva = tk.Canvas(root, width= longeur, height= largeur, bg = "black")
canva.grid()

# blue, green, black, yellow, magenta, red.

nbr_couleur = 0

def couleur():
    global nbr_couleur
    if nbr_couleur == 0:
        nbr_couleur =+ 1
        return "blue"
    elif nbr_couleur == 1:
        nbr_couleur += 1
        return "green"
    elif nbr_couleur == 2:
        nbr_couleur += 1
        return "black"
    elif nbr_couleur == 3:
        nbr_couleur += 1
        return "yellow"
    elif nbr_couleur ==4 :
        nbr_couleur += 1
        return "magenta"
    elif nbr_couleur == 5:
        nbr_couleur = 0
        return "red"
    
# Faire une liste et un modulo 
    
steps = 7

for i in range(steps, longeur//2, steps):
    canva.create_oval(  (  i  , i ), (  longeur - i  , longeur-i   ), outline= f"{couleur()}", width= steps)


root.mainloop()