import random

def menu():
    menu = """
    Bienvenido a ¡Adivina el numero!
    Ingrese la dificultad...
    1- Dificil (5 vidas)
    2- Normal (7 vidas)
    3- Facil (10 vidas)
    4- Salir del juego
    Opcion: """

    opcion = input(menu)

    while opcion != '4':
        if opcion == '1':
            vidas = 5
            adivina_numero(vidas)
        elif opcion == '2':
            vidas = 7
            adivina_numero(vidas)
        elif opcion == '3':
            vidas = 10
            adivina_numero(vidas)
        else:
            print("Opcion no valida, volve a intentarlo")
        
        opcion = input(menu)
    print("Gracias por jugar :)")


def adivina_numero(vidas):
    numero_random = random.randint(1, 100)
    numero_usuario = int(input("Ingresa un numero entre 1 y 100: "))
    while vidas > 1:
        if numero_usuario == numero_random:
            print("¡Felicidades adivinaste el numero!")
            break
        elif numero_usuario > numero_random:
            print("Te pasaste, elegi uno mas chico")
            vidas -= 1
            print(f'Te quedan {vidas} vidas')
            numero_usuario = int(input("Ingresa un numero entre 1 y 100: "))
        else:
            print("Te quedaste corto, elegi uno mas grande")
            vidas -= 1
            print(f'Te quedan {vidas} vidas')
            numero_usuario = int(input("Ingresa un numero entre 1 y 100: "))

    print(f'Lo siento perdiste :( el numero correcto era {numero_random}')



def main():
    menu()

if __name__ == "__main__":
    main()