import h5py

file_path = 'books.h5'

with h5py.File(file_path, 'r') as h5file:
    print("\nGlobal Metadata:")
    for attr, value in h5file.attrs.items():
        print(f"{attr}: {value}")

    print("\nBooks Data:")
    for book_key in h5file.keys():
        book_group = h5file[book_key]

        if 'volumeInfo' in book_group:
            volume_info = book_group['volumeInfo']

            title = volume_info.attrs.get('title', 'No Title Found')
            print("\nTitle:", title)

            authors = []
            for key in volume_info:
                if key.startswith('authors_'):
                    author = volume_info[key][()].decode('utf-8') 
                    authors.append(author)

            print("Authors:", ', '.join(authors))

            published_date = volume_info.get('publishedDate', 'N/A')
            if isinstance(published_date, h5py.Dataset):
                published_date = published_date[()].decode('utf-8')  
            print("Published Date:", published_date)

            categories = []
            for key in volume_info:
                if key.startswith('categories_'):
                    category = volume_info[key][()].decode('utf-8')
                    categories.append(category)

            print("Categories:", ', '.join(categories))
        else:
            print(f"\nNo 'volumeInfo' found in '{book_key}'.")
