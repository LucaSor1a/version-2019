from vigenere import vigenere


def interfaz(mensaje):
    resultado = vigenere(mensaje)
    return resultado



def main():
    mensaje = input("Ingrese el mensaje a codificar: ")
    main.resultado = interfaz(mensaje)
    print(main.resultado)


'''
while True:
    main()
    if main.resultado != "":
        break
'''