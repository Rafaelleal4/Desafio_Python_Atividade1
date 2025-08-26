
# Importa o módulo random para gerar números aleatórios
import random

print("Bem-vindo ao DC Heroes!\nEste é um jogo de aventura em texto,\nonde suas escolhas determinarão o destino da sua jornada.")

# Solicita o nome do personagem ao jogador
char_name = input("Digite o nome do seu herói: ")


# Escolha do modo de jogo
modo = 0
while modo not in [1, 2]:
    try:
        print("Atenção: No modo Hardcore, a senha da bomba é gerada aleatoriamente e você tem apenas o seu HP de tentativas para desativá-la!")
        modo = int(input("Escolha o modo de jogo: \n 1 - Fácil \n 2 - Hardcore\n"))
    except ValueError:
        print("Digite apenas 1 ou 2.")


# Define a senha da bomba conforme o modo
if modo == 1:
    senha_correta = 3090
else:
    senha_correta = random.randint(1000, 9999)

print(f"Você acorda em mais um dia da sua vida patética até que de repente aparece uma mulher misteriosa em seu quarto, que aparenta ser uma heroína poderosa que usa magia. \nZATANA: Olá, {char_name}, me chamo Zatanna. Todos os heróis do planeta estão lutando com o Darkseid nesse momento, eu não tenho muito tempo, já tenho que voltar e ajudar eles. Precisamos de você, o Coringa plantou uma bomba em uma mina de escavação aqui perto!")
print("ZATANA: Não consigo explicar mais, meu tempo aqui está acabando, você precisa ir impedir ele. Vou te dar alguns atributos dos melhores heróis do mundo!")

# Escolha da classe do personagem
char_class = 0
while char_class not in [1, 2, 3, 4]:
    try:
        char_class = int(input("Escolha a classe do seu herói: \n 1 - Batman \n 2 - Superman \n 3 - Mulher Maravilha \n 4 - Flash\n"))
        if char_class not in [1, 2, 3, 4]:
            print("Classe inválida. Por favor, escolha um número entre 1 e 4.")
    except ValueError:
        print("Por favor, insira um número válido.")


# Atributos iniciais do personagem
hp = 10
strength = 10
speed = 10
smartness = 10


# Ajusta os atributos conforme a classe escolhida
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


# Exibe os atributos finais e introduz a missão
print(f"Com os seguintes atributos: \n HP: {hp} \n Força: {strength} \n Velocidade: {speed} \n Inteligência: {smartness}")
print("Sua missão é salvar o mundo do Coringa! \nEle roubou uma bomba nuclear e pretende destruir uma mina de escavação! \nVocê deve encontrar a bomba e desativá-la antes que seja tarde demais!")
print(f"Boa sorte, herói {char_name}!")


# Variáveis de controle para a parte da bomba
encontrou_bomba = False
acao_bomba = 0


# Loop principal de escolhas do jogador
while True:
    if smartness >= 14:
        action = int(input("O que você quer fazer? \n 1 - Entrar na caverna pela frente  \n 2 - Entrar por cima  \n 3 - Desistir da missão\n"))
        while action not in [1, 2, 3]:
            action = int(input("Opção inválida. O que você quer fazer? \n 1 - Entrar na caverna pela frente  \n 2 - Entrar por cima  \n 3 - Desistir da missão\n"))
    else:
        action = int(input("O que você quer fazer? \n 1 - Entrar na caverna pela frente  \n 2 - Desistir da missão\n"))
        while action not in [1, 3]:
            action = int(input("Opção inválida. O que você quer fazer? \n 1 - Entrar na caverna pela frente  \n 2 - Desistir da missão\n"))


    # Caso especial para Superman
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
            print("Você encontrou um bilhete com números da senha da bomba")
            print(int(senha_correta/100))
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


# Lógica para desarmar as bombas
if encontrou_bomba:
    if acao_bomba == 1:
        print("Você escolheu desarmar a bomba 1!")
        while hp > 0:
            try:
                tentativa = int(input("Digite a senha de 4 dígitos da bomba: "))
                if len(str(tentativa).zfill(4)) != 4:
                    print("Senha inválida! Digite exatamente 4 números (ex: 0423).")
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
                if senha_correta > tentativa:
                    print("A senha correta é maior do que a tentativa.")
                else:
                    print("A senha correta é menor do que a tentativa.")
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
                    print("Senha inválida! Digite exatamente 4 números (ex: 1234).")
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
                if senha_correta > tentativa:
                    print("A senha correta é maior do que a tentativa.")
                else:
                    print("A senha correta é menor do que a tentativa.")
        if hp == 0:
            print("Você errou todas as tentativas! A bomba explodiu! Game Over.")
