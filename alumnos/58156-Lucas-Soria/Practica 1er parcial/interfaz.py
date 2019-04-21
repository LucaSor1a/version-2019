from vigenere import vigenere


def interfaz(mensaje):
    resultado = vigenere(mensaje)
    return resultado



def main():
    mensaje = input("Ingrese el mensaje a codificar: ")
    resultado = interfaz(mensaje)
    print(resultado)



main()