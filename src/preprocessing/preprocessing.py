import pandas as pd
from src.packages.utils import eliminar_tildes, contaminar_con_na

def get_bronze_data():
    '''
    Get the bronze data from the data folder
    Args:
        None
    Returns:
        pd.DataFrame: The bronze data
    '''
    return pd.read_excel('data/bronze/car_raw.xlsx')

def write_gold_data(data):
    '''
    Write the gold data to the data folder
    Args:
        data: pd.DataFrame: The gold data
    Returns:
        None
    '''
    data.to_excel('data/gold/car_gold.xlsx', index=False)

def clean_date_column(data):
    print("Cleaning date column...")
    data['_created'] = data['_created'].str[:10]
    data['_created'] = pd.to_datetime(data['_created'], format='%Y-%m-%d')
    return data

def create_new_columns(data):
    print("Creating new columns...")
    data['vehicle_brand'] = data['product'].str.split(" ").str[0]
    data['vehicle_line'] = data['product'].str.split(" ").str[1]
    data['brand_line'] = data['vehicle_brand'] + "-" + data['vehicle_line']
    data['antiguedad'] = data['_created'].dt.year - data['years']
    return data

def clean_text_column(data):
    print("Cleaning text column...")
    lista_columnas = ["location_state", 
                      "location_city", 
                      "vehicle_brand", 
                      "vehicle_line", 
                      "brand_line"]
    for col in lista_columnas:
        print(f"Cleaning {col} column...")
        data[col] = data[col].str.lower().str.replace(" ", "_")
        data[col] = data[col].apply(eliminar_tildes)
    return data


def main():
    print("Starting preprocessing...")
    data_bronze = get_bronze_data()
    print("Data bronze loaded")
    data_gold = clean_date_column(data_bronze)
    data_gold = create_new_columns(data_gold)
    data_gold = clean_text_column(data_gold)
    data_gold = contaminar_con_na(data_gold) ## Warning!!: This is not a good practice, it is just for the example
    print("Data gold created")
    write_gold_data(data_gold)