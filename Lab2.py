import hashlib
abc  = "abcdefghijklmnopqrstuvwxyz "
def get_desp(char):
    return (ord(char.upper())-66)

def CesarCifr(mensaje,n): #Funcion Cesar , recibe el mendasaje a cifrar y en n , este es la clave de cesar , en nuestro caso es 8
    cifrado =""
    for l in mensaje: 
            if l in abc:
                i = abc.find(l)
                i += n
                if i >=27 :
                    i -= 27
                cifrado += abc[i]

            else:
                    cifrado + l 
            
    return cifrado

def CesarDes(cifrado,n):
    mensaje =""
    for l in cifrado:
        if l in abc:
                e = abc.find(l)
                e -=n
                if e<0:
                    e+=27
                  
                mensaje += abc[e]
        else:
                mensaje+ l
    return mensaje

def vigenereCif(mensaje,clave):
    cifrado = ""
    for i in range(0,len(mensaje)):
        des = get_desp(clave[i % len(clave)]) #Desplazamiento de la clave
        cifrado+=(CesarCifr(mensaje[i],des)) #Usamos Cesar
    return cifrado

def vigenereDescif(mensaje,clave):
    cifrado = ""
    for i in range(0,len(mensaje)):
        des = get_desp(clave[i % len(clave)]) #Desplazamiento de la clave
        cifrado+=(CesarDes(mensaje[i],des)) #Usamos Cesar
    return cifrado

def Leer(documento):
    archivo = open(documento,'r')
    lectura = archivo.read()
    archivo.close()
    return lectura

def Escribir(nombre,cifrado):
    documento = open(nombre,'w')
    documento.write(cifrado)
    documento.close()
    return True


def main():
    texto = Leer("mensajeentrada.txt")
    #Hashear el mensaje de entrada antes de codificarlo
    str = hashlib.sha256(texto.encode('utf-8'))
    hash1 = str.hexdigest()
    #Cifrar el mensaje de entrada
    texto = CesarCifr(texto, 8)
    texto = vigenereCif(texto,"holamundo")
    print(texto)
    #Decifrar el mensaje de entrada
    texto2 = vigenereDescif(texto,"holamundo")
    texto2 = CesarDes(texto2, 8)
    print(texto2)
    #Crear el txt mensajeseguro y escribir el mensaje decifrado
    Escribir("mensajeseguro.txt", texto2)
    #Leer el mensajeseguro.txt
    texto2 = Leer("mensajeseguro.txt")
    #Hashear el mensaje del txt mensajeseguro
    str2 = hashlib.sha256(texto2.encode('utf-8'))
    hash2 = str2.hexdigest()
    #Comprarar los hash
    if ( hash1== hash2):
        print("Mensaje seguro")
    else:
        print("mensaje modificado, NO es seguro")


main()
