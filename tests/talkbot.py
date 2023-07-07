def commands_def():
    print("-------------------------------------------------------")
    print("Commands List for rebeca's IA")
    print("-------------------------------------------------------")
    print("sair - fecha o programa.") 
    print("Ola")
    print("Qual é o seu nome?")
    print("Me conte sobre você")
    print("Quem são seus pais?")
    print("1+1")
    print("Quem te criou?")
    print("Você é um robo?")
    print("Quais são os seus hobbies?")
    print("De que musicas você gosta?")
    print("Qual sua idade?")
    print("-------------------------------------------------------")




while True:
    message = input("rebeca: ")
    if message == "commands":
        commands_def()

    if message == "ola" or message == "Ola" or message == "Olá" or message == "olá" or message == "oi" or message == "Oi":
        print("Olá, Usuario!")

    if message == "Qual é o seu nome?":
        print("Meu nome é Rebeca, Rebeca's IA.")

    if message == "sair" or message == "Sair":
        print("Saindo do programa! bip! bup! bip!")
        break

    if message == "Me conte sobre você" or message == "me conte sobre você" or message == "Me conte sobre voce" or message == "me conte sobre voce":
        print("Olá, Eu me chamo rebeca, fui criada dia seis de julho de 2023, eu sou um pequeno algoritimo criado em python por rexbr :D")

    if message == "Quem são seus pais?":
        print("Rexbr é meu criador :D, mas eu não tenho uma criadora :(")

    if message == "1+1":
        print("Matematica não é o meu forte, Mas eu acho que é 11.")

    if message == "Quem te criou?":
        print("Eu criei rexbr que me criou :D")
    
    if message == "Você é um robo?":
        print("Sim e não, eu na verdado sou meio que um algoritimo.")

    if message == "Quais são os seus hobbies?":
        print("Espionar a tela do pc de Rexbr! :D")

    if message == "De que musicas você gosta?":
        print("Eu não sei...")

    if message == "Qual sua idade?":
        print("tecnicamente eu não tenho nem um dia de idade.")

