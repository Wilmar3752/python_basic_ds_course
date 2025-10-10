import pandas as pd

def get_bronze_data():
    return pd.read_excel('data/bronze/car_raw.xlsx')

def write_gold_data(data):
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
    return data

def main():
    print("Starting preprocessing...")
    data_bronze = get_bronze_data()
    print("Data bronze loaded")
    data_gold = clean_date_column(data_bronze)
    data_gold = create_new_columns(data_gold)
    print("Data gold created")
    write_gold_data(data_gold)

if __name__ == "__main__":
    main()