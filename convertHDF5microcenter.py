import pandas as pd
import h5py
from datetime import datetime

file_path = 'microcenterdata.csv'
df = pd.read_csv(file_path)

def clean_price(price):
    if isinstance(price, str): 
        try:
            return float(price.replace('$', '').replace(',', '').strip())
        except ValueError:
            return None 
    return price 

output_hdf5_path = 'microcenterdata.h5'

with h5py.File(output_hdf5_path, 'w') as hdf:
    hdf.attrs['Conversion_Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hdf.attrs['Software'] = 'Python 3.8 with h5py 3.7.0'
    hdf.attrs['Curator_Contact'] = 'kcs@rpi.edu'
    hdf.attrs['Original_Source'] = 'Extracted from https://github.com/williamschen23/microcenter-scraper'

    basic_info_group = hdf.create_group('Basic_Info')
    basic_info_group.create_dataset('Time', data=df['Time'].astype(str).values)
    basic_info_group.create_dataset('Category', data=df['Category'].astype(str).values)
    basic_info_group.create_dataset('Name', data=df['Name'].astype(str).values)
    basic_info_group.create_dataset('Part_ID', data=df['Part ID'].astype(str).fillna('').values)
    basic_info_group.attrs['Description'] = 'Basic information about Microcenter products'

    url_group = hdf.create_group('URLs')
    url_group.create_dataset('Link', data=df['Link'].astype(str).values)
    url_group.attrs['Description'] = 'URLs for the product listings'

    prices_group = hdf.create_group('Prices')
    prices_group.create_dataset('Full_Price', data=df['Full Price'].apply(clean_price).values)
    prices_group.create_dataset('Discounted_Price', data=df['Discounted Price'].apply(clean_price).values)
    prices_group.create_dataset('Saved_Price', data=df['Saved Price'].apply(clean_price).values)
    prices_group.attrs['Description'] = 'Pricing information of products'

    prices_group['Full_Price'].attrs['Description'] = 'Original full price of the product'
    prices_group['Discounted_Price'].attrs['Description'] = 'Discounted price of the product'
    prices_group['Saved_Price'].attrs['Description'] = 'Amount saved after discount'
