import random

char_name = input("Digite o nome do seu herói: ")
print("Bem-vindo ao jogo!")

modo = 0
while modo not in [1, 2]:
    try:
        print("Ateção: No modo Hardcore, a senha da bomba é gerada aleatoriamente e você tem apenas o seu HP de tentativas para desativá-la!")
        modo = int(input("Escolha o modo de jogo: \n 1 - Fácil \n 2 - Hardcore\n"))
    except ValueError:
        print("Digite apenas 1 ou 2.")

if modo == 1:
    senha_correta = 3090
else:
    senha_correta = random.randint(0, 9999)

char_class = 0
while char_class not in [1, 2, 3, 4]:
    try:
        char_class = int(input("Escolha a classe do seu herói: \n 1 - Batman \n 2 - Superman \n 3 - Mulher Maravilha \n 4 - Flash\n"))
        if char_class not in [1, 2, 3, 4]:
            print("Classe inválida. Por favor, escolha um número entre 1 e 4.")
    except ValueError:
        print("Por favor, insira um número válido.")

hp = 10
strength = 10
speed = 10
smartness = 10

if char_class == 1:
    print("Você escolheu Batman!")
    hp += 2
    strength += 1
    speed -= 2
    smartness += 4
    char_class = "Batman"
elif char_class == 2:
    print("Você escolheu Superman!")
    hp += 3
    strength += 7
    speed += 1
    smartness -= 2
    char_class = "Superman"
elif char_class == 3:
    print("Você escolheu Mulher Maravilha!")
    hp += 5
    strength += 3
    speed -= 3
    smartness += 2
    char_class = "Mulher Maravilha"
elif char_class == 4:
    print("Você escolheu Flash!")
    hp -= 2
    strength += 2
    speed += 8
    smartness += 1
    char_class = "Flash"

print(f"Com os seguintes atributos: \n HP: {hp} \n Força: {strength} \n Velocidade: {speed} \n Inteligência: {smartness}")
print("Sua missão é salvar o mundo do Coringa! \nEle roubou uma bomba nuclear e pretende destruir uma mina de escavação! \nVocê deve encontrar a bomba e desativá-la antes que seja tarde demais!")
print(f"Boa sorte, herói {char_name}!")

# Separa codigo da bomba
encontrou_bomba = False
acao_bomba = 0

while True:
    if smartness >= 14:
        action = int(input("O que você quer fazer? \n 1 - Entrar na caverna pela frente  \n 2 - Entrar por cima  \n 3 - Desistir da missão\n"))
        while action not in [1, 2, 3]:
            action = int(input("Opção inválida. O que você quer fazer? \n 1 - Entrar na caverna pela frente  \n 2 - Entrar por cima  \n 3 - Desistir da missão\n"))
    else:
        action = int(input("O que você quer fazer? \n 1 - Entrar na caverna pela frente  \n 3 - Desistir da missão\n"))
        while action not in [1, 3]:
            action = int(input("Opção inválida. O que você quer fazer? \n 1 - Entrar na caverna pela frente  \n 3 - Desistir da missão\n"))

    if action == 1 and char_class == "Superman":
        print("Você entrou na caverna pela frente e foi surpreendido por um grupo de capangas do Coringa com Kriptonita! "
              "Eles te capturaram e levaram para o covil do Coringa! "
              "Infelizmente, sua missão falhou!")
        break

    elif action == 1 and char_class != "Superman":
        print("Você entrou na caverna pela frente e conseguiu derrotar os capangas do Coringa! Eles sabem que você está aqui.")
        action = int(input("Você encontrou um inimigo! O que você quer fazer? \n 1 - Atacar \n 2 - Fugir\n"))
        if action == 1 and hp > 0:
            print("Você atacou o inimigo e conseguiu derrotá-lo! Porém, você sofreu 1 ponto de dano.")
            hp -= 1
            print(f"Seu HP atual é {hp}.")
            action = int(input("Você encontrou o Coringa e a bomba! O que você quer fazer? \n 1 - Atacar \n 2 - Fugir\n"))
            if action == 1:
                print("Você atacou o Coringa e conseguiu derrotá-lo! E você achou dois controles com ele, ou seja, tem uma bomba a mais para desativar.")
                acao_bomba = int(input("O que você quer fazer? \n 1 - Desativar a bomba 1 \n 2 - Desativar a bomba 2\n"))
                encontrou_bomba = True
            elif action == 2:
                print("Você fugiu do combate e conseguiu escapar! Porém, a bomba vai detonar e não há como desativá-la a tempo! "
                      "Infelizmente, sua missão falhou!")
        break

    elif action == 2:
        print("Você entrou na caverna por cima e conseguiu evitar os capangas do Coringa!")
        action = int(input("Você encontrou um inimigo! O que você quer fazer? \n 1 - Atacar \n 2 - Fugir\n"))
        if action == 1 and hp > 0:
            print("Você atacou o inimigo e conseguiu derrotá-lo! Porém, você sofreu 1 ponto de dano.")
            hp -= 1
            print(f"Seu HP atual é {hp}.")
            action = int(input("Você encontrou o Coringa e a bomba! O que você quer fazer? \n 1 - Atacar \n 2 - Fugir\n"))
            if action == 1:
                print("Você atacou o Coringa e conseguiu derrotá-lo! E você achou dois controles com ele, ou seja, tem uma bomba a mais para desativar.")
                acao_bomba = int(input("O que você quer fazer? \n 1 - Desativar a bomba 1 \n 2 - Desativar a bomba 2\n"))
                encontrou_bomba = True
            elif action == 2:
                print("Você fugiu do combate e conseguiu escapar! Porém, a bomba vai detonar e não há como desativá-la a tempo! "
                      "Infelizmente, sua missão falhou!")
        break

    elif action == 3:
        print("Você desistiu da missão e o Coringa conseguiu destruir a mina de escavação! "
              "Infelizmente, sua missão falhou! \nGame Over!")
        break

# Separa codigo da bomba
if encontrou_bomba:
    if acao_bomba == 1:
        print("Você escolheu desarmar a bomba 1!")

        
        while hp > 0:
            try:
                tentativa = int(input("Digite a senha de 4 dígitos da bomba: "))
                if len(str(tentativa).zfill(4)) != 4:  
                    print("Senha inválida! Digite menos de 4 números (ex: 0423).")
                    continue
            except ValueError:
                print("Senha inválida! Digite apenas números.")
                continue

            if tentativa == senha_correta:
                print("Bomba 1 desarmada com sucesso!")
                print("Mas a bomba 1 era falsa! Você perdeu tempo, e a bomba 2 (verdadeira) vai explodir!")
                break
            else:
                hp -= 1
                print(f"Senha incorreta! Tentativas restantes: {hp}")

        if hp == 0:
            print("Você errou todas as tentativas da bomba 1! Infelizmente, a bomba 2 (verdadeira) explodiu! Game Over.")
        else:
            print("A bomba 2 (verdadeira) explodiu! Infelizmente, sua missão falhou!")

    elif acao_bomba == 2:
        print("Você escolheu tentar desarmar a bomba 2!")
        while hp > 0:
            try:
                tentativa = int(input("Digite a senha de 4 dígitos da bomba 2: "))
                if len(str(tentativa).zfill(4)) != 4:
                    print("Senha inválida! Digite menos de 4 números (ex: 1234).")
                    continue
            except ValueError:
                print("Senha inválida! Digite apenas números.")
                continue

            if tentativa == senha_correta:
                print(f"Você desativou a bomba 2 com sucesso! O mundo está a salvo graças a você, {char_name}! Você é um verdadeiro herói!")
                break
            else:
                hp -= 1
                print(f"Senha incorreta! Tentativas restantes: {hp}")

        if hp == 0:
            print("Você errou todas as tentativas! A bomba explodiu! Game Over.")
