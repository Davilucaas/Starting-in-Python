import random as rd

def jogar():

    mensagem_abertura()
    palavra_secreta = palavra_aleatoria()
    lista = iniciar_lista(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print("A palavra tem {} letras: \n{}".format(len(lista),lista))

    while not enforcou and not acertou:

        chute = pedir_chute()

        if chute in palavra_secreta:
            marcar_chute_correto(chute, lista, palavra_secreta)
        else:
            erros +=1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in lista
        print(lista)

    if enforcou:
       print_perdeu(palavra_secreta)
    else:
        print_ganhou()

def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

def palavra_aleatoria():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = rd.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def iniciar_lista(palavra):
    return ["_" for letra in palavra]

def pedir_chute():
    chute = input("Qual letra você quer tentar?").strip().upper()
    return chute

def marcar_chute_correto(chute, lista, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            lista.pop(index)
            lista.insert(index, letra)
            print("Encontrei a letra {} na posição {}".format(letra, index))
        index += 1

def print_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def print_ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()