import json
import h5py
from datetime import datetime

with open('books_raw.json', 'r') as f:
    data = json.load(f)

# Function to save JSON data to HDF5 format
def save_to_hdf5(h5file, json_data, path='/'):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if isinstance(value, dict):
                grp = h5file.create_group(path + key)
                grp.attrs['Description'] = f"Group for '{key}' data"  # Add group metadata
                save_to_hdf5(h5file, value, path + key + '/')
            elif isinstance(value, list):
                for idx, item in enumerate(value):
                    if isinstance(item, dict):
                        grp = h5file.create_group(f"{path}{key}_{idx}")
                        grp.attrs['Description'] = f"Group for item '{key}_{idx}' in list"  # Add group metadata
                        save_to_hdf5(h5file, item, f"{path}{key}_{idx}/")
                    else:
                        h5file.create_dataset(f"{path}{key}_{idx}", data=item)
            else:
                h5file[path].attrs[key] = value
    elif isinstance(json_data, list):
        for idx, item in enumerate(json_data):
            if isinstance(item, dict):
                grp = h5file.create_group(f"{path}book_{idx}")
                grp.attrs['Description'] = f"Group for book '{idx}'"
                save_to_hdf5(h5file, item, f"{path}book_{idx}/")
            else:
                h5file.create_dataset(f"{path}book_{idx}", data=item)

output_hdf5_path = 'books.h5'
with h5py.File(output_hdf5_path, 'w') as h5file:
    h5file.attrs['Conversion_Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    h5file.attrs['Software'] = 'Python 3.8 with h5py 3.7.0'
    h5file.attrs['Curator_Contact'] = 'shashwot_07@hotmail.com'
    h5file.attrs['Original_Source'] = 'Extracted from Google Books API'
    
    save_to_hdf5(h5file, data)

with h5py.File(output_hdf5_path, 'r') as h5file:
    print("\nGlobal Metadata:")
    for attr, value in h5file.attrs.items():
        print(f"{attr}: {value}")
    
    for book_key in h5file.keys():
        if 'volumeInfo' in h5file[book_key]:
            volume_info = h5file[f'{book_key}/volumeInfo']
            
            title = volume_info.attrs.get('title', 'No Title Found')
            print("\nTitle:", title)

            authors = []
            for key in volume_info.keys():
                if key.startswith('authors_'):
                    authors.append(volume_info[key][()])

            print("Authors:", authors)
        else:
            print(f"\nNo 'volumeInfo' found in '{book_key}'.")
