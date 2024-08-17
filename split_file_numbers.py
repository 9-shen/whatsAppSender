import os
import pandas as pd
import math

import config


# Function to split the CSV file
def split_csv_file(file_path, output_dir, num_splits=20, encoding='ISO-8859-1'):
    try:
        # Read the CSV file with specified encoding
        df = pd.read_csv(file_path, encoding=encoding)

        # Calculate the number of rows per split
        rows_per_split = math.ceil(len(df) / num_splits)

        # Split the file and save the parts
        for i in range(num_splits):
            start_row = i * rows_per_split
            end_row = min((i + 1) * rows_per_split, len(df))

            split_df = df.iloc[start_row:end_row]

            output_file = os.path.join(output_dir, f"{os.path.basename(file_path).replace('.csv', '')}_part{i + 1}.csv")
            split_df.to_csv(output_file, index=False, encoding=encoding)

    except UnicodeDecodeError:
        print(f"Encoding error while processing {file_path}. Trying with 'latin1' encoding.")
        try:
            # Retry with 'latin1' encoding
            df = pd.read_csv(file_path, encoding='latin1')
            rows_per_split = math.ceil(len(df) / num_splits)

            for i in range(num_splits):
                start_row = i * rows_per_split
                end_row = min((i + 1) * rows_per_split, len(df))

                split_df = df.iloc[start_row:end_row]

                output_file = os.path.join(output_dir,
                                           f"{os.path.basename(file_path).replace('.csv', '')}_part{i + 1}.csv")
                split_df.to_csv(output_file, index=False, encoding=encoding)
        except Exception as e:
            print(f"Failed to process {file_path} with alternative encoding: {e}")
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")


# Directory containing the CSV files
source_dir = config.Contacts

# Loop through each file in the source directory
for file_name in os.listdir(source_dir):
    if file_name.endswith('.csv'):
        # Create a new folder with the same name as the file (without extension)
        file_base_name = os.path.splitext(file_name)[0]
        output_dir = os.path.join(source_dir, file_base_name)
        os.makedirs(output_dir, exist_ok=True)

        # Full path to the source file
        file_path = os.path.join(source_dir, file_name)

        # Split the file and save the parts into the new folder
        split_csv_file(file_path, output_dir)
