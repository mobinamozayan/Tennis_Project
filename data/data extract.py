import pandas as pd
import os


def process_parquet_files(base_path):
    dataframes_par = dict()
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.parquet'):
                file_path = os.path.join(os.getcwd(), root, file)
                file_name = file[:file.rfind("_")]
                if file_name not in dataframes_par:
                    dataframes_par[file_name] = pd.read_parquet(file_path)
                else:
                    dataframes_par[file_name] = pd.concat([dataframes_par[file_name], pd.read_parquet(file_path)],
                                                          ignore_index=True)
    return dataframes_par


extract_dir = 'path_to_extract_directory'
extraxt_path = os.path.join(os.getcwd(), extract_dir)
data_frames = process_parquet_files(extraxt_path)

output_dir = 'output_directory'
os.makedirs(output_dir, exist_ok=True)

for name, df in data_frames.items():
    csv_path = os.path.join(os.getcwd(), output_dir, f'{name}.csv')
    df.to_csv(csv_path, index=False)

print("Data frames have been saved as Parquet and CSV files.")
