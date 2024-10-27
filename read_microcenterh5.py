import h5py

file_path = 'microcenterdata.h5'

with h5py.File(file_path, 'r') as h5file:
    print("\nGlobal Metadata:")
    for attr, value in h5file.attrs.items():
        print(f"{attr}: {value}")

    # Read Basic Info group
    if 'Basic_Info' in h5file:
        basic_info_group = h5file['Basic_Info']
        print("\nBasic Info:")
        for key in basic_info_group:
            data = basic_info_group[key][()]
            print(f"{key}: {data[:5]}")

    # Read URLs group
    if 'URLs' in h5file:
        url_group = h5file['URLs']
        print("\nURLs:")
        for key in url_group:
            data = url_group[key][()]
            print(f"{key}: {data[:5]}") 

    # Read Prices group
    if 'Prices' in h5file:
        prices_group = h5file['Prices']
        print("\nPrices:")
        for key in prices_group:
            data = prices_group[key][()]
            print(f"{key}: {data[:5]}")

    # Print metadata for Prices group
    print("\nPrices Group Metadata:")
    for attr, value in prices_group.attrs.items():
        print(f"{attr}: {value}")
