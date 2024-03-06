import tkinter as tk
import random

root = tk.Tk()

root.title("Mon dessin")

canva_longeur, canva_largeur = (400,400)
frame_button = tk.Frame(root)

couleur_dessin = "Blue"


def cercle():
    point_aleatoire_largeur = random.randint(0,canva_largeur)
    point_aleatoire_lonngeur = random.randint(0,canva_longeur)
    if (point_aleatoire_lonngeur ) -50   >= 0 and (point_aleatoire_largeur ) -50 >= 0 and (point_aleatoire_lonngeur ) +50 >= canva_longeur and (point_aleatoire_largeur ) + 50 >= canva_largeur:
        canva_1.create_oval(  ((point_aleatoire_lonngeur ) -50    , (point_aleatoire_largeur) -50     )   , ( (point_aleatoire_lonngeur) + 50  , (point_aleatoire_largeur) + 50 )   , width = 5, outline = couleur_dessin)
    else:
        while point_aleatoire_lonngeur  -50   <= 0 or point_aleatoire_largeur -50 <= 0 or point_aleatoire_lonngeur  +50 >= canva_longeur or point_aleatoire_largeur + 50 >= canva_largeur:
                point_aleatoire_largeur = random.randint(0,canva_largeur)
                point_aleatoire_lonngeur = random.randint(0,canva_longeur)
        canva_1.create_oval(  ((point_aleatoire_lonngeur ) -50    , (point_aleatoire_largeur ) -50     )   , ( (point_aleatoire_lonngeur ) + 50  , (point_aleatoire_largeur ) + 50 )   , width = 1, outline = couleur_dessin)


def carre():
    point_aleatoire_largeur = random.randint(0,canva_largeur)
    point_aleatoire_longeur = random.randint(0,canva_longeur)
    if point_aleatoire_largeur + 100 < canva_largeur and point_aleatoire_longeur + 100 < canva_longeur:
         canva_1.create_rectangle( (  point_aleatoire_largeur , point_aleatoire_longeur   )   ,  ( point_aleatoire_largeur  + 100, point_aleatoire_longeur  + 100 ), outline = couleur_dessin)
    else:
        while point_aleatoire_largeur + 100 > canva_largeur or point_aleatoire_longeur + 100 > canva_longeur:
            point_aleatoire_largeur = random.randint(0,canva_largeur)
            point_aleatoire_longeur = random.randint(0,canva_longeur)
        canva_1.create_rectangle( (  point_aleatoire_largeur , point_aleatoire_longeur   )   ,  ( point_aleatoire_largeur  + 100, point_aleatoire_longeur  + 100 ), outline = couleur_dessin)

def croix():
    point_aleatoire_largeur = random.randint(0,canva_largeur)
    point_aleatoire_longeur = random.randint(0,canva_longeur)
    point_A_1, point_A_2 = point_aleatoire_largeur - 50, point_aleatoire_longeur - 50
    point_B_1, point_B_2 = point_aleatoire_largeur - 50, point_aleatoire_longeur + 50
    point_C_1, point_C_2 = point_aleatoire_largeur + 50, point_aleatoire_longeur + 50
    point_D_1, point_D_2 = point_aleatoire_largeur + 50, point_aleatoire_longeur - 50
    if point_A_1 > 0 and point_A_2 > 0 and point_C_1 < canva_largeur and point_C_2 < canva_longeur:
         canva_1.create_line((point_A_1, point_A_2), (point_C_1, point_C_2), fill = couleur_dessin)
         canva_1.create_line((point_D_1, point_D_2), (point_B_1, point_B_2), fill = couleur_dessin)
    else:
         print("HORS")
         while point_A_1 <= 0 or point_A_2 <= 0 or point_C_1 >= canva_largeur or point_C_2 >= canva_longeur:
            point_aleatoire_largeur = random.randint(0,canva_largeur)
            point_aleatoire_longeur = random.randint(0,canva_longeur)
            point_A_1, point_A_2 = point_aleatoire_largeur - 50, point_aleatoire_longeur - 50
            point_B_1, point_B_2 = point_aleatoire_largeur - 50, point_aleatoire_longeur + 50
            point_C_1, point_C_2 = point_aleatoire_largeur + 50, point_aleatoire_longeur + 50
            point_D_1, point_D_2 = point_aleatoire_largeur + 50, point_aleatoire_longeur - 50
         canva_1.create_line((point_A_1, point_A_2), (point_C_1, point_C_2), fill = couleur_dessin)
         canva_1.create_line((point_D_1, point_D_2), (point_B_1, point_B_2), fill = couleur_dessin)


def couleur():
     global couleur_dessin
     nouvelle_couleur = input("Choissisez une nouvelle couleur :")
     if nouvelle_couleur in ("white", "black", "red", "green", "blue", "cyan", "yellow"):
          couleur_dessin = nouvelle_couleur
     else:
         print("Cette couleur n'est pas pris en charge")

btn_couleur = tk.Button(root, text = "Choisir une couleur", command = couleur)
btn_cercle = tk.Button(frame_button, text = "Cerlce", foreground= "Blue", font= ("Helvetica",12, "bold"), command= cercle)
btn_carre = tk.Button(frame_button, text = "Carré", foreground= "Green", command = carre)
btn_croix = tk.Button(frame_button, text = "Croix", foreground= "Red", font= ("italic", 12), command = croix)
canva_1 = tk.Canvas(root, bg = "white", width= canva_largeur, height= canva_longeur, relief = "sunken",borderwidth = 0, highlightthickness=0, highlightbackground="brown")

frame_button.grid(row = 1, column=0)
btn_couleur.grid(row = 0, column= 1)
btn_cercle.grid(pady=20)
btn_carre.grid(pady=20)
btn_croix.grid(pady=20)
canva_1.grid(row = 1, column= 1)
root.mainloop()