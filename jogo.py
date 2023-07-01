import time

def intro():
    print("Bem-vindo à Aventura no Castelo!")
    time.sleep(2)
    print("Você está em uma jornada para resgatar um tesouro escondido em um antigo castelo.")
    time.sleep(2)
    print("Prepare-se para uma aventura cheia de desafios e emoções!")
    time.sleep(2)
    player_name = input("Antes de começar, diga-nos o seu nome: ")
    print("Olá,", player_name + "! Prepare-se para começar sua aventura!")

def start_game():
    time.sleep(2)
    print("Você está parado em frente ao castelo. Há três portas à sua frente.")
    time.sleep(2)
    print("Uma é vermelha, a outra é azul e a terceira é verde.")
    time.sleep(2)
    print("Escolha com sabedoria!")

    while True:
        door_choice = input("Qual porta você escolhe? (vermelha/azul/verde): ")
        door_choice = door_choice.lower()

        if door_choice == "vermelha":
            room_red()
            break
        elif door_choice == "azul":
            room_blue()
            break
        elif door_choice == "verde":
            room_green()
            break
        else:
            print("Opção inválida. Tente novamente.")

def room_red():
    print("\nVocê entra na sala vermelha.")
    time.sleep(2)
    print("Há um grande baú no centro da sala.")
    time.sleep(2)
    print("O baú está trancado. Você precisa encontrar uma chave para abri-lo.")

    while True:
        choice = input("O que você faz? (procurar a chave/voltar para a entrada): ")
        choice = choice.lower()

        if choice == "procurar a chave":
            print("Você encontra uma chave brilhante debaixo do tapete.")
            time.sleep(2)
            print("Você desbloqueia o baú com a chave e encontra o tesouro!")
            time.sleep(2)
            print("Parabéns! Você venceu o jogo!")
            break
        elif choice == "voltar para a entrada":
            print("Você volta para a entrada do castelo.")
            start_game()
            break
        else:
            print("Opção inválida. Tente novamente.")

def room_blue():
    print("\nVocê entra na sala azul.")
    time.sleep(2)
    print("A sala está vazia, exceto por um espelho na parede.")
    time.sleep(2)
    print("Ao olhar no espelho, você é transportado para um mundo paralelo.")
    time.sleep(2)
    print("Você precisa resolver um enigma para voltar à sala anterior.")

    while True:
        answer = input("Qual é o que é, o que foi e o que será ao mesmo tempo? ")
        answer = answer.lower()

        if answer == "o tempo":
            print("Você responde corretamente!")
            time.sleep(2)
            print("Você é levado de volta à sala anterior.")
            start_game()
            break
        else:
            print("Resposta incorreta. Tente novamente.")

def room_green():
    print("\nVocê entra na sala verde.")
    time.sleep(2)
    print("A sala está cheia de plantas exuberantes.")
    time.sleep(2)
    print("Você nota uma placa com uma pergunta: 'Qual é a capital da Itália?'")

    while True:
        answer = input("Qual é a sua resposta? ")
        answer = answer.lower()

        if answer == "roma":
            print("Resposta correta!")
            time.sleep(2)
            print("Você ouve um barulho de porta abrindo.")
            time.sleep(2)
            print("Uma passagem secreta se revela e você entra nela.")
            time.sleep(2)
            print("Você continua sua jornada em busca do tesouro...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("Você encontrou o tesouro escondido! Parabéns!")
            break
        else:
            print("Resposta incorreta. Tente novamente.")

# Iniciar o jogo
intro()
start_game()


 