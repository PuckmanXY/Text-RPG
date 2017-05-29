import pickle
import campaign
import characters

def main_menu():
    print("***********************")
    print("****Fighting Beasts****")
    print("***********************")
    print("\n")
    print("\t1\t-\tIniciar Campanha (Novo Jogo)")
    print("\t2\t-\tCarregar Jogo")
    print("\t3\t-\tCréditos")
    print("\n\n\n\t0\t-\tSair")

    return int(input("Escolha uma opção:"))


def load_games():
    arq = open('personagens.pck', 'rb')
    characters.saved_games = pickle.load(arq)
    arq.close()

def load_game():
    for i in range (len(characters.saved_games)):
        print(characters.saved_games[i][0],"-" ,characters.saved_games[i][1], end = "\n")
    num = int(input("Qual é o número do seu personagem?\n"))
    for character in characters.saved_games:
        if num == int(character[0]):
            campaign.current_session = character
            campaign.what_to_do()


def credits():
    print("\n\n")
    print("*****************")
    print("*****CREDITS*****")
    print("*****************")

    print("\n\n")

    print("Desenvolvido por Kayo Anderson e Ranieri Wellyson\n\n")

    __main__()

def __main__():
    characters.ff()
    load_games()
    x = main_menu()
    if x == 1:
        characters.register_character()

    elif x == 2:
        load_game()

    elif x == 3:
        credits()

    elif x == 0:
        return 0

    else:
        main_menu()
