# Jeu pierre papier ciseaux

* Utilisation de Tkinter sur Python
* Jeu entre un utilisateur et un ordinateur
* If... else, image, widgets, fonctions, labels, frames
* Historique des coups joués

## Énoncé de l'exercice

* Créer un jeu simple où l'utilisateur peut choisir pierre, papier ou ciseaux et jouer contre l'ordinateur.
* Afficher le score et l'historique des coups

## Visuel v1

![Aperçu de la fenêtre Tkinter](visuel-v1.jpg)

## Amélioration du visuel

![Aperçu de la fenêtre Tkinter version 2](visuel-v2.jpg)

* Mis en place de chaque élément avec ``.place`` au lieu de ``.pack``
* Mise en forme du texte et de la Listbox

## Prise en compte de la victoire et de la défaite

* Phrase qui permet de dire si la partie est gagnée ou perdue
* Désactivation des boutons
* Apparition d'un bouton pour lancer une nouvelle partie

## Nouvelle fonctionnalité

* Possibilité de jouer avec les touches du clavier : 
    * "c" : ciseaux
    * "r" : pierre
    * "p" : papier