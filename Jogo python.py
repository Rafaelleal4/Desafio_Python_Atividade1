## Projeto de jogo em python


char_name = input("Digite o nome do seu herói: ")
print("Bem-vindo ao jogo!")


char_class = 0
while char_class not in [1, 2, 3, 4]:
    try:
        char_class = int(input("Escolha a classe do seu herói: \n 1 - Batman \n 2 - Superman \n 3 - Mulher Maravilha \n 4 - Flash"))
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
else:
    print("Classe inválida! Escolha novamente.")
    char_class = input("Escolha a classe do seu herói: \n 1 - Batman \n 2 - Superman \n 3 - Mulher Maravilha \n 4 - Flash \n ")


print(f"Com os seguintes atributos: \n HP: {hp} \n Força: {strength} \n Velocidade: {speed} \n Inteligência: {smartness}")
print("Sua missão é salvar o mundo do Coringa! \n Ele roubou uma bomba nuclear e pretende destruir uma mina de escavação! \n Você deve encontrar a bomba e desativá-la antes que seja tarde demais! ")
print(f"Boa sorte, herói {char_name}!")

while True:
    # Se o personagem for inteligente o suficiente, pode escolher qualquer entrada
    if smartness >= 14:
        action = int(input("O que você quer fazer? \n 1 - Entrar na caverna pela frente  \n 2 - Entrar por cima  \n 3 - Desistir da missão\n "))
        while action not in [1, 2, 3]:
            action = int(input("Opção inválida. O que você quer fazer? \n 1 - Entrar na caverna pela frente  \n 2 - Entrar por cima  \n 3 - Desistir da missão\n "))
    # Se não for inteligente o suficiente, só pode entrar pela frente ou desistir
    else:
        action = int(input("O que você quer fazer? \n 1 - Entrar na caverna pela frente  \n 3 - Desistir da missão\n "))
        while action not in [1, 3]:
            action = int(input("Opção inválida. O que você quer fazer? \n 1 - Entrar na caverna pela frente  \n 3 - Desistir da missão\n "))

    # Morte do Superman
    if action == 1 and char_class == "Superman":
        print("Você entrou na caverna pela frente e foi surpreendido por um grupo de capangas do Coringa com Kriptonita! "
              "Eles te capturaram e levaram para o covil do Coringa! "
              "Infelizmente, sua missão falhou!")
        break

    # Continuação do jogo na situação 1 se não for o Superman
    elif action == 1 and char_class != "Superman":
        print("Você entrou na caverna pela frente e conseguiu derrotar os capangas do Coringa! Eles sabem que você está aqui.")
        action = int(input("Você encontrou um inimigo! O que você quer fazer? \n 1 - Atacar \n 2 - Fugir\n "))
        if action == 1 and hp > 0:
            print("Você atacou o inimigo e conseguiu derrotá-lo! Porém, você sofreu 1 ponto de dano.")
            hp -= 1
            print(f"Seu HP atual é {hp}.")
            action = int(input("Você encontrou o Coringa e a bomba! O que você quer fazer? \n 1 - Atacar \n 2 - Fugir\n "))
            if action == 1:
                print("Você atacou o Coringa e conseguiu derrotá-lo! E você achou dois controles com ele, ou seja, tem uma bomba a mais para desativar.")
                action = int(input("O que você quer fazer? \n 1 - Desativar a bomba 1 \n 2 - Desativar a bomba 2\n "))
                if action == 1:
                    print("Você tentou desativar a bomba 1, porém era uma bomba falsa! "
                          "Infelizmente, a bomba 2 vai detonar e não há como desativá-la a tempo!")
                elif action == 2:
                    print("Você desativou a bomba 2 com sucesso! A outra bomba era falsa. A mina de escavação está a salvo!")
            elif action == 2:
                print("Você fugiu do combate e conseguiu escapar! Porém, a bomba vai detonar e não há como desativá-la a tempo! "
                      "Infelizmente, sua missão falhou!")
        break

    # Continuação do jogo na situação 2
    elif action == 2:
        print("Você entrou na caverna por cima e conseguiu evitar os capangas do Coringa!")
        action = int(input("Você encontrou um inimigo! O que você quer fazer? \n 1 - Atacar \n 2 - Fugir\n "))
        if action == 1 and hp > 0:
            print("Você atacou o inimigo e conseguiu derrotá-lo! Porém, você sofreu 1 ponto de dano.")
            hp -= 1
            print(f"Seu HP atual é {hp}.")
            action = int(input("Você encontrou o Coringa e a bomba! O que você quer fazer? \n 1 - Atacar \n 2 - Fugir\n "))
            if action == 1:
                print("Você atacou o Coringa e conseguiu derrotá-lo! E você achou dois controles com ele, ou seja, tem uma bomba a mais para desativar.")
                action = int(input("O que você quer fazer? \n 1 - Desativar a bomba 1 \n 2 - Desativar a bomba 2\n "))
                if action == 1:
                    print("Você tentou desativar a bomba 1, porém era uma bomba falsa! "
                          "Infelizmente, a bomba 2 vai detonar e não há como desativá-la a tempo!")
                elif action == 2:
                    print("Você desativou a bomba 2 com sucesso! A outra bomba era falsa. A mina de escavação está a salvo!")
            elif action == 2:
                print("Você fugiu do combate e conseguiu escapar! Porém, a bomba vai detonar e não há como desativá-la a tempo! "
                      "Infelizmente, sua missão falhou!")
        break

    # Desistência da missão
    elif action == 3:
        print("Você desistiu da missão e o Coringa conseguiu destruir a mina de escavação! "
              "Infelizmente, sua missão falhou! \n Game Over!")
        break
    