def main ():
    usuarios = []

    print ("digite os usuarios que deseja cadastrar (digite s pra sair)")

    while True: 
        user = input("usuairo: ")

        if user.upper() == "S":
            break

        if user :
            usuarios.append(user)
        else:
            print ("por favor digite um usuario valido")
    print ("-------usuario cadastrado-------")
    for usuario in usuarios:
        print(f"{usuario.upper()} | {usuario.lower()}")

if __name__=="__main__":
    main()        

