from vigenere import vigenere


def interfaz(mensaje):
    interfaz.resultado = vigenere(mensaje)
    return interfaz.resultado



def main():
    mensaje = input("Ingrese el mensaje a codificar: ")
    interfaz(mensaje)
    print(interfaz.resultado)

while True:
    main()
    if interfaz.resultado != "Ingresaste un caracter no permitido":
        break
