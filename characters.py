import campaign
import pickle
import tkinter as tk


global cont_chars
cont_chars = 1

saved_games = [0, "Chico", 40, 5, 5, 5, 0]

def ff():
    arq = open('contagem.pck', 'rb')
    globals()["cont_chars"] = pickle.load(arq)
    arq.close()


def register_character():
    atributes = 15

    def save_char():
        if (str(strenght_entry.get()).isnumeric()) and (str(dexterity_entry.get()).isnumeric()) and (str(intelligence_entry.get()).isnumeric()) and (not(str(name_entry.get()).isnumeric())):
            str_int = int(strenght_entry.get())
            dex_int = int(dexterity_entry.get())
            int_int = int(intelligence_entry.get())
            if str_int + dex_int + int_int <= atributes:
                new_game = [globals()["cont_chars"], name_entry.get(), 30, 1, str_int, dex_int, int_int, 0, 1]
                saved_games.append(new_game)
                campaign.current_session = new_game
                globals()["cont_chars"] += 1
                arq = open('contagem.pck', 'wb')
                pickle.dump(globals()["cont_chars"], arq)
                arq.close()
                win.destroy()
                campaign.what_to_do()
            else:
                print("Vá com calma! Seu personagem está muito forte, tente diminuir alguns atributos!")
        else:
            print("Entrada inválida! Tente novamente")
            win.destroy()
            register_character()


    win = tk.Tk()
    win.title("Ficha")
    win.geometry("355x125")

    name = tk.Label(win, text="Nome: ")
    name.grid(column=0, row=0)
    name_entry = tk.Entry(win)
    name_entry.grid(column=1, row=0)

    strenght = tk.Label(win, text="Força: ")
    strenght.grid(column=0, row=1)
    strenght_entry = tk.Entry(win)
    strenght_entry.grid(column=1, row=1)

    dexterity = tk.Label(win, text="Dextreza: ")
    dexterity.grid(column=0, row=2)
    dexterity_entry = tk.Entry(win)
    dexterity_entry.grid(column=1, row=2)

    intelligence = tk.Label(win, text="Inteligência: ")
    intelligence.grid(column=0, row=3)
    intelligence_entry = tk.Entry(win)
    intelligence_entry.grid(column=1, row=3)

    warning = tk.Label(win, text="Você tem 15 pontos para distribuir\nentre os atributos! Escolha com sabedoria!")
    warning.grid(column=0, row=4)

    save = tk.Button(win, width=10, text="Confirmar", command=save_char)
    save.grid(column=1, row=4)

    win.mainloop()
