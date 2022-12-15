import bz2
import logging
import argparse
import urllib3
import tempfile
from google.cloud import storage

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def save_file_to_gcp(file_name, bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_name)


def download_file(url, bucket_name, output_file_name):
    logging.info(f"Downloading {output_file_name[:-4]}")
    http = urllib3.PoolManager()
    tmpdir = tempfile.gettempdir()
    with http.request('GET', url, preload_content=False) as response, open(f"{tmpdir}/{output_file_name}",
                                                                           'wb') as out_file:
        while True:
            data = response.read(1024)
            if not data:
                break
            out_file.write(data)
        save_file_to_gcp(f"{tmpdir}/{output_file_name}", bucket_name)


def decompress_file(file_name, bucket_name, output_file_name):
    logging.info(f"Decompressing {file_name}")
    tempdir = tempfile.gettempdir()
    temp_file = f"{tempdir}/{file_name}"
    with open(temp_file, 'rb') as file:
        data = file.read()
        decompressed_data = bz2.decompress(data)
    with open(f"{tempdir}/{output_file_name}", 'wb') as file:
        file.write(decompressed_data)
    save_file_to_gcp("dataset" + output_file_name, bucket_name)


def entry_point(request):
    bucket_name = "datalake-upb"

    datasets = {
        "1987": "https://dataverse.harvard.edu/api/access/datafile/:persistentId?persistentId=doi:10.7910/DVN/HG7NV7/IXITH2",
        "2008": "https://dataverse.harvard.edu/api/access/datafile/:persistentId?persistentId=doi:10.7910/DVN/HG7NV7/EIR0RA",
    }

    # Download the files
    for dataset_name, url in datasets.items():
        download_file(url, bucket_name, f"{dataset_name}.bz2")

    # Decompress the files
    for dataset_name, url in datasets.items():
        decompress_file(f"{dataset_name}.bz2", bucket_name, f"{dataset_name}.csv")
