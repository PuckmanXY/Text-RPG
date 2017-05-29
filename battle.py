import campaign
import random as rd
import tkinter as tk
import time

global_char_cur_hp = 0
global_enemy_cur_hp = 0

def versus(char_hp, enemy_hp):
    global global_char_cur_hp
    global_char_cur_hp = char_hp
    global global_enemy_cur_hp
    global_enemy_cur_hp = enemy_hp


def battle(char_name, char_hp, char_str, char_dex, char_int, enemy_number, enemy_name, enemy_hp, enemy_str, enemy_dex, enemy_int, xp_if_win):

    versus(char_hp, enemy_hp)

    def update_values(char_cur_hp, enemy_cur_hp):
        global global_char_cur_hp
        global_char_cur_hp = char_cur_hp
        global global_enemy_cur_hp
        global_enemy_cur_hp = enemy_cur_hp

    def win_battle(xp_if_win):
        print("\n\n\nPARABÉNS! Você ganhou a batalha! Você acaba de receber " + str(xp_if_win) + " de experiência")
        campaign.current_session[7] += xp_if_win
        if campaign.current_session[8] <= enemy_number:
            campaign.current_session[8] += 1
        bat_win.destroy()
        time.sleep(3)
        campaign.what_to_do()

    def lose_battle():
        print("\n\n\nVOCÊ PERDEU!")
        bat_win.destroy()
        time.sleep(3)
        campaign.what_to_do()


    def atack(who, cur_hp, strenght, dexterity, aim):
        x = rd.randint(1,10)
        if x >=8:
            damage = strenght + dexterity + rd.randint(int(cur_hp/5), int(cur_hp/3))
            print(who + " TEM ACERTO CRÍTICO E CAUSA " + str(damage) + " DE DANO EM " + aim)
        else:
            damage = strenght + dexterity
            print(who + " CAUSA " + str(damage) + " DE DANO EM " + aim, "!")
        return damage


    def cure(who, cur_hp, dexterity, intelligence):
        will_cure = rd.randint(1,10)
        cure_points = 0
        if will_cure>=7:
            cure_points = dexterity + intelligence / 4
            print(who + " SE CURA EM " + str(cure_points))
        else:
            print(who + " TENTA SE CURAR, MAS NÃO OBTÉM SUCESSO")
        return cure_points

    def action():
        char_cur_hp = global_char_cur_hp
        enemy_cur_hp = global_enemy_cur_hp
        print("\n\nO que você deseja fazer?\n")
        print("1\t-\t Atacar")
        print("2\t-\t Curar")
        print("3\t-\t Desistir")
        x = input()
        if str(x).isnumeric():
            if x == '1':
                enemy_cur_hp -= atack(char_name, char_cur_hp, char_str, char_dex, enemy_name)
                if enemy_cur_hp <= 0:
                    win_battle(xp_if_win)
                enemy_hp_lb["text"]= enemy_cur_hp
                time.sleep(3)
                et = rd.randint(1,10)
                if et >= 8:
                    enemy_cur_hp += cure(enemy_name, enemy_cur_hp, enemy_dex, enemy_int)
                    enemy_hp_lb["text"] = enemy_cur_hp
                else:
                    char_cur_hp -= atack(enemy_name, enemy_cur_hp, enemy_str, enemy_dex, char_name)
                    char_hp_lb["text"] = char_cur_hp
                    if char_cur_hp <= 0:
                        lose_battle()
            if x == '2':
                char_cur_hp += cure(char_name, char_cur_hp, char_dex, char_int)
                if char_cur_hp > char_hp:
                    char_cur_hp = char_hp
                char_hp_lb["text"] = char_cur_hp
                time.sleep(3)
                et = rd.randint(1, 10)
                if et >= 8:
                    enemy_cur_hp += cure(enemy_name, enemy_cur_hp, enemy_dex, enemy_int)
                    enemy_hp_lb["text"] = enemy_cur_hp
                else:
                    char_cur_hp -= atack(enemy_name, enemy_cur_hp, enemy_str, enemy_dex, char_name)
                    if char_cur_hp <= 0:
                        lose_battle()
                    char_hp_lb["text"] = char_cur_hp
            if x =='3':
                lose_battle()
        else:
            print("ERRO! Tente novamente!")
        update_values(char_cur_hp, enemy_cur_hp)


    bat_win = tk.Tk()
    bat_win.title("Battle against " + enemy_name)
    bat_win.geometry("190x75")

    char_name_lb = tk.Label(bat_win, text=char_name)
    char_name_lb.grid(column=0, row=0)
    char_hp_lb = tk.Label(bat_win, text=char_hp)
    char_hp_lb.grid(column=0, row=1)

    enemy_name_lb = tk.Label(bat_win, text=enemy_name)
    enemy_name_lb.grid(column=2, row=0)
    enemy_hp_lb = tk.Label(bat_win, text=enemy_hp)
    enemy_hp_lb.grid(column=2, row=1)

    act_bt = tk.Button(bat_win, width=16, text="AGIR", command=action)
    act_bt.grid(column=1, row=3)

    print("Seu inimigo é " + enemy_name + "! Boa sorte!")

    bat_win.mainloop()
