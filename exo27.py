# Créer un jeu simple où l'utilisateur peut choisir pierre, papier ou ciseaux et jouer contre l'ordinateur.
# Afficher le score et l'historique des coups

import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.geometry('850x750')
fenetre.resizable(width=False, height=False)
fenetre.configure(bg="#F1F1F1")
fenetre.title("Pierre - Papier - Ciseaux")

# Fonction qui choisi au hasard pour l'ordinateur
def computer_choice():
    choices = ["Pierre", "Papier", "Ciseaux"]
    return random.choice(choices)


# Fonction qui permet de lancer le jeu
def play(user_choice):
    nbDeCoups.set(nbDeCoups.get() + 1) # Ajoute 1 au nombre de coups
    print("Nombre de coups : " + str(nbDeCoups.get()))
    computer = computer_choice() #Fait appel à la fonction qui choisi aléatoirement pour le PC

    # Logique pour déterminer le gagnant
    if user_choice == computer:
        result_var.set("Egalité !")
    elif (
        (user_choice == "Pierre" and computer == "Ciseaux") 
        or (user_choice == "Papier" and computer == "Pierre")
        or (user_choice == "Ciseaux" and computer == "Papier")
        ): 
        result_var.set("Vous avez gagné !")
        player_score_var.set(player_score_var.get() + 1)
    else:
        result_var.set("Vous avez perdu !")
        computer_score_var.set(computer_score_var.get() + 1)
    
    # Charger les images correspondantes aux choix
    user_img_label.config(image=get_image(user_choice))
    computer_img_label.config(image=get_image(computer))

    # Ajouter les choix à l'historique (du plus récent au plus ancien)
    history_listbox.insert(0, f"Vous : {user_choice} - Ordinateur : {computer}")

    verify_victory()

# Permet de savoir si l'utilisateur peut continuer à jouer
def verify_victory():
    # Test si le nombre de coups est > 10
    if nbDeCoups.get() >= 10:
        # Comparer les scores pour déterminer le gagnant
        if player_score_var.get() > computer_score_var.get():
            result_var.set("Félicitation, vous avez gagné la partie !")
        elif player_score_var.get() < computer_score_var.get():
            result_var.set("Dommage, l'ordinateur a gagné")
        else:
            result_var.set("Match nul !")

        # Désactiver les boutons pour empêcher de jouer
        rock_button.config(state=tk.DISABLED)
        paper_button.config(state=tk.DISABLED)
        scissors_button.config(state=tk.DISABLED)

        # Bouton pour réinitialiser les scores et continuer à jouer
        reset_button.place(x=300 ,y=20)

def reset_scores():
    # Réinitialiser toutes les variables à 0 ou à ""
    nbDeCoups.set(0)
    result_var.set("")
    player_score_var.set(0)
    computer_score_var.set(0)
    history_listbox.delete(0, tk.END)

    user_img_label.config(image=empty_img)
    computer_img_label.config(image=empty_img)

    # Réactiver les boutons
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)

    # Supprimer le bouton reset
    reset_button.place_forget()


# Afficher une image en fonction du choix
def get_image(choice):
    if choice == "Pierre":
        return rock_img
    elif choice == "Papier":
        return paper_img
    else:
        return scissors_img
    
# Fonction à appeler lors de l'appui de la touche P
def on_key_press(e):
    if nbDeCoups.get() < 10:
        if e.char.lower() == "p":
            play("Papier")
        if e.char.lower() == "r":
            play("Pierre")
        if e.char.lower() == "c":
            play("Ciseaux")
    
# Associer la fonction on_key_press à l'évènement <Key>
fenetre.bind('<Key>', on_key_press)
    
# Définition des variables
result_var = tk.StringVar()
player_score_var = tk.IntVar()
computer_score_var = tk.IntVar()
nbDeCoups = tk.IntVar(value=0)
    
# Charger les images
rock_img = ImageTk.PhotoImage(Image.open("./pierre.gif"))
paper_img = ImageTk.PhotoImage(Image.open("./papier.gif"))
scissors_img = ImageTk.PhotoImage(Image.open("./ciseaux.gif"))
# Création image vide en taille 0x0 transparente
empty_img = ImageTk.PhotoImage(Image.new("RGBA", (0, 0), (0, 0, 0, 0)))

# Création des widget avec les images
user_label = tk.Label(fenetre, text="Choisissez : ")
user_label.place(x=70, y=20)

rock_button = tk.Button(fenetre, image=rock_img, command=lambda : play("Pierre"))
rock_button.place(x=40, y=60)
              
paper_button = tk.Button(fenetre, image=paper_img, command=lambda : play("Papier"))
paper_button.place(x=40, y=260)

scissors_button = tk.Button(fenetre, image=scissors_img, command=lambda : play("Ciseaux"))
scissors_button.place(x=40, y=460)

# Etiquettes pour afficher les images jouées
user_img_label = tk.Label(fenetre, image=None) # Pas d'image de départ
user_img_label.place(x=300, y=60)

computer_img_label = tk.Label(fenetre, image=None) # Pas d'image de départ
computer_img_label.place(x=300, y=200)

result_label = tk.Label(fenetre, textvariable=result_var)
result_label.place(x=500, y=180)

# Création d'une frame pour les score
score_frame = tk.Frame(fenetre)
score_frame.place(x=290, y=400)

player_score_label = tk.Label(score_frame, text="Score J1 :", font=("Verdana 10"), fg='#6f9fbd')
player_score_label.pack(side=tk.LEFT, padx=10)

player_score_display = tk.Label(score_frame, textvariable=player_score_var, font=("Verdana 10 bold"), fg='#6f9fbd')
player_score_display.pack(side=tk.LEFT, padx=10)

computer_score_label = tk.Label(score_frame, text="Score Ordinateur :", font=("Verdana 10"), fg='#6f9fbd')
computer_score_label.pack(side=tk.LEFT, padx=10)

computer_score_display = tk.Label(score_frame, textvariable=computer_score_var, font=("Verdana 10 bold"), fg='#6f9fbd')
computer_score_display.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(fenetre, text="Nouvelle partie", command=reset_scores, bg='#6f9fbd', fg='white')

# Gestion de l'historique et de l'affichage
history_label = tk.Label(fenetre, text="Historique des coups : ", fg='black', font=("Verdana 12 bold"))
history_label.place(x=300, y=440)

history_listbox = tk.Listbox(fenetre, width=40, height=6, bg='#6f9fbd', fg='white')
history_listbox.place(x=300, y=470)


fenetre.mainloop()