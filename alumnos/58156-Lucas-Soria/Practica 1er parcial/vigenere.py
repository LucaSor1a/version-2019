class Exception_corto(Exception):
    pass

class Exception_numero(Exception):
    pass

class Exception_simbolo(Exception):
    pass


letras = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7,
    'i' : 8,
    'j' : 9,
    'k' : 10,
    'l' : 11,
    'm' : 12,
    'n' : 13,
    'ñ' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26
}

codigo = ['c','o','d','i','g','o']

def vigenere(mensaje):
    mensaje = mensaje.replace(" ","")
    result = ''
    c = 0
    if len(mensaje) < len(codigo):
        raise Exception_corto("{} es mas corto que el codigo establecido".format(mensaje))
    else:
        for x in mensaje:
            if x.isdigit():
                raise Exception_numero("{} es un numero, esto no esta permitido".format(x))
            elif x not in letras:
                raise Exception_simbolo("{} es un simbolo, esto no esta permitido".format(x))
            else:
                a = letras[x] + letras[codigo[c]]
                if a <= 26:
                    for key, value in letras.items():   
                        if value == a:
                            result += key
                else:
                    a = (letras[codigo[c]] - 13) + (letras[x] - 14)
                    for key, value in letras.items():
                        if value == a:
                            result += key
                c +=1
                if c == len(codigo):
                    c = 0
    return result