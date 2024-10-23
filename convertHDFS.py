import json
import h5py

with open('books_raw.json', 'r') as f:
    data = json.load(f)

def save_to_hdf5(h5file, json_data, path='/'):
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

with h5py.File('books.h5', 'w') as h5file:
    h5file.create_group('/')
    save_to_hdf5(h5file, data)

with h5py.File('books.h5', 'r') as h5file:
    volume_info = h5file['/volumeInfo']
    title = volume_info.attrs['title']
    print("Title:", title)
    authors = [h5file[f'/volumeInfo/authors_{i}'][()] for i in range(len(volume_info.keys()) - 1)]
    print("Authors:", authors)
