import tkinter as tk

root = tk.Tk()

root.title("Mon dessin")

canva_longeur, canva_largeur = (400,400)
frame_button = tk.Frame(root)

def cercle():
    canva_1.create_oval(  ((canva_longeur // 2) -50    , (canva_largeur //2) -50     )   , ( (canva_largeur //2) + 50  , (canva_largeur //2) + 50 )   , width = 5, outline = "Blue")
    #canva_1.grid(row = 1, column= 1)

btn_couleur = tk.Button(root, text = "Choisir une couleur")
btn_cercle = tk.Button(frame_button, text = "Cerlce", foreground= "Blue", font= ("Helvetica",12, "bold"), command= cercle)
btn_carre = tk.Button(frame_button, text = "Carré", foreground= "Green")
btn_croix = tk.Button(frame_button, text = "Croix", foreground= "Red", font= ("italic", 12))
canva_1 = tk.Canvas(root, bg = "white", width= canva_largeur, height= canva_longeur, relief = "sunken",borderwidth = 10, highlightthickness=10, highlightbackground="brown")

frame_button.grid(row = 1, column=0)
btn_couleur.grid(row = 0, column= 1)
btn_cercle.grid(pady=20)
btn_carre.grid(pady=20)
btn_croix.grid(pady=20)
canva_1.grid(row = 1, column= 1)
root.mainloop()