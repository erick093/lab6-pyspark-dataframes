import bz2
import logging
import argparse
import urllib3

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

def download_file(url, output_file_name):
    logging.info(f"Downloading {output_file_name[:-4]}")
    http = urllib3.PoolManager()
    with http.request('GET', url, preload_content=False) as response, open(output_file_name, 'wb') as out_file:
        while True:
            data = response.read(1024)
            if not data:
                break
            out_file.write(data)

def decompress_file(file_name, output_file_name):
    logging.info(f"Decompressing {file_name}")
    with open(file_name, 'rb') as file:
        data = file.read()
        decompressed_data = bz2.decompress(data)
    with open(output_file_name, 'wb') as file:
        file.write(decompressed_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Path to the output file", required=True)
    args = parser.parse_args()

    datasets = {
        "1987": "https://dataverse.harvard.edu/api/access/datafile/:persistentId?persistentId=doi:10.7910/DVN/HG7NV7/IXITH2",
        "2008": "https://dataverse.harvard.edu/api/access/datafile/:persistentId?persistentId=doi:10.7910/DVN/HG7NV7/EIR0RA",
    }

    # Download the files
    for dataset_name, url in datasets.items():
        download_file(url, f"{args.output}/{dataset_name}.bz2")

    # Decompress the files
    for dataset_name, url in datasets.items():
        decompress_file(f"{args.output}/{dataset_name}.bz2", f"{args.output}/{dataset_name}.csv")

