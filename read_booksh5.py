import h5py

file_path = 'books.h5'

with h5py.File(file_path, 'r') as h5file:
    print("\nGlobal Metadata:")
    for attr, value in h5file.attrs.items():
        print(f"{attr}: {value}")

    print("\nBooks Data:")
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
