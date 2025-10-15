import unicodedata
import numpy as np

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

def contaminar_con_na(data, porcentaje=0.10, columnas_excluir=['price']):
    '''
    Contamina un DataFrame con valores NA en un porcentaje específico de filas
    para todas las columnas excepto las especificadas
    
    Args:
        data: pd.DataFrame: DataFrame original
        porcentaje: float: Porcentaje de datos a contaminar (default 0.10 = 10%)
        columnas_excluir: list: Lista de columnas que no se deben contaminar
    
    Returns:
        pd.DataFrame: DataFrame con valores NA añadidos
    '''
    # Crear una copia para no modificar el original
    data_contaminado = data.copy()
    
    # Obtener todas las columnas excepto las que se deben excluir
    columnas_a_contaminar = [col for col in data.columns if col not in columnas_excluir]
    
    print(f"Contaminando {len(columnas_a_contaminar)} columnas con {porcentaje*100}% de valores NA...")
    
    # Para cada columna a contaminar
    for col in columnas_a_contaminar:
        # Calcular el número de valores a contaminar
        n_contaminar = int(len(data) * porcentaje)
        
        # Seleccionar índices aleatorios
        indices_aleatorios = np.random.choice(
            data.index, 
            size=n_contaminar, 
            replace=False
        )
        
        # Asignar NA a esos índices
        data_contaminado.loc[indices_aleatorios, col] = np.nan
        
        print(f"  - Columna '{col}': {n_contaminar} valores contaminados")
    
    print(f"Contaminación completada. Total de columnas afectadas: {len(columnas_a_contaminar)}")
    
    return data_contaminado
