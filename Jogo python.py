## Projeto de jogo em python

char_name = input("Digite o nome do seu heroi: ")
print("Bem vindo ao jogo!")


char_class = int(input("Escolha a classe do seu heroi: \n 1 - Batman \n 2 - Superman \n 3 - Mulher Maravilha \n 4 - Flash \n "))
hp = 10 
strengh = 10 
speed = 10 
smartness = 10

if char_class == 1:
    print("Voce escolheu Batman!")
    hp += 2
    strengh += 1
    speed -= 2
    smartness += 4
    char_class = "Batman"
elif char_class == 2:
    print("Voce escolheu Superman!")
    hp += 3
    strengh += 7
    speed += 1
    smartness -= 2
    char_class = "Superman"
elif char_class == 3:
    print("Voce escolheu Mulher Maravilha!")
    hp += 5
    strengh += 3
    speed -= 3
    smartness += 2
    char_class = "Mulher Maravilha"
elif char_class == 4:
    print("Voce escolheu Flash!")
    hp -= 2
    strengh += 2
    speed += 8
    smartness += 1
    char_class = "Flash"
else:
    print("Classe invalida! Escolha novamente.")
    char_class = input("Escolha a classe do seu heroi: \n 1 - Batman \n 2 - Superman \n 3 - Mulher Maravilha \n 4 - Flash \n ")

print(f"Voce escolheu a classe {char_class} com os seguintes atributos: \n HP: {hp} \n Forca: {strengh} \n Velocidade: {speed} \n Inteligencia: {smartness}")

print ("Sua missão é salvar o mundo do Coringa!" \
       "Ele roubou uma bomba nuclear e pretende destruir uma mina de escavação!" \
       "Você deve encontrar a bomba e desativá-la antes que seja tarde demais!" \
       "Boa sorte, herói", char_name, "!")
action = int(input("O que você quer fazer? \n 1 - entrar na caverna pela frente  \n 2 - entrar por cima  \n 3- desistir da missão\n "))
while action not in [1, 2, 3]:
    action = int(input("Opção inválida. O que você quer fazer? \n 1 - entrar na caverna pela frente  \n 2 - entrar por cima  \n 3- desistir da missão"))

# Superman Death
if action == 1 and char_class == 2:
    print("Você entrou na caverna pela frente e foi surpreendido por um grupo de capangas do Coringa com Kriptonita!" \
          "Eles te capturaram e levaram para o covil do Coringa!" \
          "Infelizmente, sua missão falhou!")

#Game continuation in the situation 1 if u are not the superman
elif action == 1 and char_class != 2:
    print("Você entrou na caverna pela frente e conseguiu derrotar os capangas do Coringa! Eles sabem que você está aqui.")
    action = int(input("Voce encontrou um inimigo! O que você quer fazer? \n 1 - Atacar \n 2 - Fugir\n "))
    if action == 1 and char_class.hp() > 0:
        print("Você atacou o inimigo e conseguiu derrotá-lo! Porém, você sofreu 1 ponto de dano.")
        char_class.hp(-1)
        print(f"Seu HP atual é {hp}.")
        action = int(input("Voce encontrou o Coringa e a bomba! O que você quer fazer? \n 1 - Atacar \n 2 - Desativar a bomba\n "))
        if action == 1:
            print("Você atacou o Coringa e conseguiu derrotá-lo! E voce achou dois controles com ele ou seja tem uma bomba a mais para desativar.")
    elif action == 2:
        print("Você fugiu do combate e conseguiu escapar! Porém, a bomba vai detonar e não há como desativá-la a tempo!" \
              "Infelizmente, sua missão falhou!")
#Game continuation in the situation 2 
elif action == 2:
    print("Você entrou na caverna por cima e conseguiu evitar os capangas do Coringa!")
elif action == 3:
    print("Você desistiu da missão e o Coringa conseguiu destruir a mina de escavação!" \
          "Infelizmente, sua missão falhou! \n Game Over!")
