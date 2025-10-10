import unicodedata

def maximo(lista):
    max_val = lista[0]
    for num in lista:
        print(f"probando con {num}")
        if num > max_val:
            max_val = num
        print(f"hasta ahora el maximo es :{max_val}")
    return max_val


def eliminar_tildes(texto):
    if isinstance(texto, str):
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )
    return texto