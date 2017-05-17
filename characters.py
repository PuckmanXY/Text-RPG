import random as rd
import tkinter as tk
from tkinter import ttk

def register_character():

    # def character_name():
    #     win = tk.Tk()
    #     win.title("Ficha")
    #
    #     ttk.Label(win, text="Qual o nome do seu personagem?").grid(column=0, row=0)
    #
    #     char_name = tk.StringVar()
    #     ent = ttk.Entry(win, width=50, textvariable=char_name)
    #     ent.grid(column=1, row=0)
    #     ent.focus()
    #     ttk.Label(win, text="\t\t\t\t\t\tATRIBUTOS\t\t").grid(column=0, row=1)
    #     ttk.Label(win, text=":{30s}".format('strenght')).grid(column=0, row=2)
    #     ttk.Label(win, text="Dextreza").grid(column=0, row=3)
    #     ttk.Label(win, text="Inteligência").grid(column=0, row=4)
    #
    #     win.mainloop()

    # character_name()

    new_game_number = int(input("Escolha um número para o seu personagem(esse número será registrado no sistema para que você possa acessar seu personagem futuramente): "))
    new_game_character = input("Qual o nome do seu personagem?\n")
    new_game_force = int(input("Quanto de força ele tem?\n"))
    new_game_inteligence = int(input("Quanto de inteligência?\n"))
    new_game_dexterity = int(input("Destreza?"))
    new_game = [new_game_number, new_game_character, new_game_force, new_game_inteligence, new_game_dexterity]
    saved_games.append(new_game)
