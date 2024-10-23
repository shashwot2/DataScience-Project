import json
import h5py

with open('books_raw.json', 'r') as f:
    data = json.load(f)

def save_to_hdf5(h5file, json_data, path='/'):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if isinstance(value, dict):
                grp = h5file.create_group(path + key)
                save_to_hdf5(h5file, value, path + key + '/')
            elif isinstance(value, list):
                for idx, item in enumerate(value):
                    if isinstance(item, dict):
                        grp = h5file.create_group(f"{path}{key}_{idx}")
                        save_to_hdf5(h5file, item, f"{path}{key}_{idx}/")
                    else:
                        h5file.create_dataset(f"{path}{key}_{idx}", data=item)
            else:
                h5file[path].attrs[key] = value
    elif isinstance(json_data, list):
        for idx, item in enumerate(json_data):
            if isinstance(item, dict):
                grp = h5file.create_group(f"{path}book_{idx}")
                save_to_hdf5(h5file, item, f"{path}book_{idx}/")
            else:
                h5file.create_dataset(f"{path}book_{idx}", data=item)

with h5py.File('books.h5', 'w') as h5file:
    save_to_hdf5(h5file, data)

with h5py.File('books.h5', 'r') as h5file:
    for book_key in h5file.keys():
        if 'volumeInfo' in h5file[book_key]:
            volume_info = h5file[f'{book_key}/volumeInfo']
            
            title = volume_info.attrs.get('title', 'No Title Found')
            print("Title:", title)

            authors = []
            for key in volume_info.keys():
                if key.startswith('authors_'):
                    authors.append(volume_info[key][()])

            print("Authors:", authors)
        else:
            print(f"No 'volumeInfo' found in '{book_key}'.")
