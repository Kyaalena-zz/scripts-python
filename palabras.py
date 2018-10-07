import unicodedata

ARCHIVO = 'palabras.py'
DICCIONARIO = 'diccionario.txt'
REDUCIR = 'reducir.txt'
SEPARADOR = '#'
PROCESADO = 'diccionarioPesos.txt'
STR_PREMIADO = 'MANTENER'
STR_NO_PREMIADO = 'REDUCIR'
EXPORT = 'datos.txt'


def convert_to_ascii(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')



def lee_fichero(file):
    resultado = []
    with open(file,'r') as f:
        for line in f:
            resultado.append({
                'original': line[:-1] if line[-1] == '\n' else line,
                'convertida': convert_to_ascii(line[:-1].upper())
            })
    return resultado


def identifica_premiado(termino, lista_palabras):
    for palabra in termino.split(' '):
        if palabra in lista_palabras:
            return True
    return False


conceptos = lee_fichero(DICCIONARIO)
pal_reducir = lee_fichero(REDUCIR)

#del archivo de palabras a reducir nos queddamos solo con las palabr
#as en ascii y las ponemos en un arreglo ~ lista

lista_reducir = [ concepto.get('convertida') for concepto in pal_reducir ]
lista_export = []
for concepto in conceptos:
    premiado = identifica_premiado(concepto.get('convertida'), lista_reducir)
    premio = STR_NO_PREMIADO if premiado else STR_PREMIADO
    lista_export += ['{}{}{}\n'.format(concepto.get('original'), SEPARADOR, premio)]
with open(EXPORT, 'w') as export:
    export.writelines(lista_export)
    export.close()

quit()