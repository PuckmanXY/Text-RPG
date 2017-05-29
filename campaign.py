import battle
import pickle
import characters
import game

xpToLU = 5

inimigos = [[1, "Cachorro", 35, 3, 4, 4, 2], [2, "Kobolt", 40, 4, 5, 5, 3], [3, "Ogro", 50, 5, 6, 4, 5],
            [4, " Kayo, The Guardian Ogro", 70, 6, 5, 5, 6]]

current_session = []

def what_to_do():
    print("\n\nO que você deseja fazer?\n")
    print("\t1\t-\tIr para a próxima batalha")
    print("\t2\t-\tSubir de nível")
    print("\t3\t-\tLutar uma batalha passada")
    print("\t4\t-\tIniciar o tutorial")
    print("\t5\t-\tSalvar progresso")
    x = input()
    if x == '1':
        wich_battle(current_session[8])
    if x == '2':
        level_up(current_session[3])
    if x == '3':
        choose_enemy()
    if x == '4':
        introduction()
    if x == '5':
        save_game()

def save_game():
    arq = open('personagens.pck', 'wb')
    for i in characters.saved_games:
        if current_session[0] == i[0]:
            characters.saved_games.remove(i)
            characters.saved_games.append(current_session)
    pickle.dump(characters.saved_games, arq)
    arq.close()
    game.__main__()


def choose_enemy():
    for i in range (len(inimigos)):
        print(inimigos[i][0], "-", inimigos[i][1], end="\n")
    c = input("Contra que inimigo deseja lutar?\n")
    for enemy in inimigos:
        if int(c) == enemy[0]:
            wich_battle(c)
        else:
            pass


def wich_battle(enemy):
    for possible_enemy in inimigos:
        if int(enemy) == possible_enemy[0]:
            cur_enemy = possible_enemy
            battle.battle(current_session[1], current_session[2],current_session[3], current_session[4],current_session[5], cur_enemy[0], cur_enemy[1], cur_enemy[2], cur_enemy[3], cur_enemy[4], cur_enemy[5], cur_enemy[6])
        else:
            pass


def level_up(level):
    def up_level():
        print("\nVocê pode aumentar um dos atributos abaixo:")
        print("1\t-\tForça(+4)")
        print("2\t-\tDextreza(+3)")
        print("3\t-\tInteligência(+4)")
        print("4\t-\tHP (+10)")
        x=int(input("Que atributo deseja aumentar?"))
        if x == 1:
            current_session[4] += 4
            print("Agora o seu personagem " + current_session[1] + " tem " + str(current_session[4]) + " de FORÇA!")
            what_to_do()

        if x ==2:
            current_session[5] += 3
            print("Agora o seu personagem " + current_session[1] + " tem " + str(current_session[5]) + " de DEXTREZA!")
            what_to_do()

        if x == 3:
            current_session[6] += 4
            print("Agora o seu personagem " + current_session[1] + " tem " + str(current_session[6]) + " de INTELIGÊNCIA!")
            what_to_do()

        if x == 4:
            current_session[2] += 10
            print("Agora o seu personagem " + current_session[1] + " tem " + str(current_session[2]) + " de HP!")
            what_to_do()

    if current_session[7] >= int(xpToLU * level):
        current_session[3] += 1
        current_session[7] = 0
        up_level()

    else:
        print("VOCÊ PRECISA DE " + str(xpToLU * level - current_session[7]) + " XP PARA AVANÇAR DE NÍVEL!")
        what_to_do()


def introduction():
    print("\n\n\t\t\tBem-vindo ao sistema de batalhas de Fighting Beasts")
    print("A partir de agora, você irá batalhar contra oponentes poderosos e terá de derrotar todos até chegar no Guardião Ogro")
    print("A recompensa por isso é vários nadas")
    x = input("\nGostaria de iniciar o tutorial? (Y/N)")
    if x == 'y' or x == 'Y':
        tutorial()
    if x == 'n' or x == 'N':
        print("Você escolheu sair do tutorial!\n\n")
        what_to_do()
    else:
        print("Erro de entrada de dados!")
        introduction()


def tutorial():
    print("\n\n***********************")
    print("*******TUTORIAL********")
    print("***********************")

    print("\nO sistema de batalhas é bastante simples: você lutará contra um inimigo por vez até chegar no boss final!")
    print("Lembre-se de planejar bem cada ataque!")
    x = input("Vamos começar com uma batalha de treino!\n(PRESSIONE ENTER)")
    battle.battle("Chico", 40, 5, 5, 5, 0, "Ogro", 20, 3, 3, 1, 0)
