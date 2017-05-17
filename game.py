import random
import massa_teste
import campaign

saved_games = []

def main_menu():
    print("**************")
    print("****RPGZÃO****")
    print("**************")
    print("\n\n")
    print("\t1\t-\tIniciar Campanha (Novo Jogo)")
    print("\t2\t-\tCarregar Jogo")
    print("\t3\t-\tOpções")
    print("\t4\t-\tCréditos")
    print("\n\n\n\t0\t-\tSair")

    return int(input("Escolha uma opção:"))

def register_game():
    new_game_number = int(input("Escolha um número para o seu personagem(esse número será registrado no sistema para que você possa acessar seu personagem futuramente): "))
    new_game_character = input("Qual o nome do seu personagem?\n")
    new_game_force = int(input("Quanto de força ele tem?\n"))
    new_game_inteligence = int(input("Quanto de inteligência?\n"))
    new_game_dexterity = int(input("Destreza?"))
    new_game = [new_game_number, new_game_character, new_game_force, new_game_inteligence, new_game_dexterity]
    saved_games.append(new_game)

def credits():
    print("\n\n")
    print("*****************")
    print("*****CREDITS*****")
    print("*****************")

    print("\n\n")

    print("Desenvolvido por Kayo Anderson e Ranieri Wellyson\n\n")

    __main__()

def __main__():
    x = main_menu()
    if x == 1:
        register_game()
        campaign.cap1()

    elif x == 2:
        load_game()

    elif x == 3:
        options()

    elif x == 4:
        credits()

    elif x == 0:
        pass

    else:
        main_menu()


__main__()
