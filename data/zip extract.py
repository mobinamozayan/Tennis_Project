from zipfile import ZipFile as zz
import os

zip_file_path = os.path.join(os.getcwd(),'data_raw','202405.zip')

extract_dir = 'path_to_extract_directory'
os.makedirs(extract_dir, exist_ok=True)

with zz(zip_file_path, 'r') as zip_read:
    zip_read.extractall(extract_dir)


def extract_nested_zips(base_path):
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if item.endswith('.zip'):
            with zz(item_path, 'r') as inner_zip_ref:
                inner_zip_ref.extractall(base_path)


extraxt_path = os.path.join(os.getcwd(),extract_dir)
extract_nested_zips(extraxt_path)