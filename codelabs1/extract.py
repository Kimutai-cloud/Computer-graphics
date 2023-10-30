import json
import pandas as pd
import glob
import os

# Get the parent folder where "1.0" and "Codes" folders are located
parent_folder = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Define the paths to the JSONL files and the pivot file
jsonl_folder = os.path.join(parent_folder, 'Cat1', 'data')
jsonl_files = glob.glob(os.path.join(jsonl_folder, '*.jsonl'))
output_folder = os.path.join(parent_folder, 'Cat1', 'output')

pivot_file = os.path.join(jsonl_folder, 'en-US.jsonl')

# Initialize an empty DataFrame to store data from all files
pivot_data = []

with open(pivot_file, 'r', encoding='utf-8') as pivot_file:
    for line in pivot_file:
        item = json.loads(line)
        id_value = item.get('id', None)
        utt_value = item.get('utt', None)
        annot_utt_value = item.get('annot_utt', None)

        if id_value is not None:
            pivot_data.append({'id': id_value, 'utt': utt_value, 'annot-utt': annot_utt_value})

pivot_df = pd.DataFrame(pivot_data)

# Check if 'annot-utt' exists in the pivot DataFrame
if 'annot-utt' not in pivot_df.columns:
    pivot_df['annot-utt'] = ""

# Iterate through the other JSONL files and create separate Excel files
for jsonl_file in jsonl_files:
    if jsonl_file != pivot_file:  # Skip processing the pivot file again
        file_data = []

        with open(jsonl_file, 'r', encoding='utf-8') as file:
            for line in file:
                item = json.loads(line)
                id_value = item.get('id', None)
                utt_value = item.get('utt', None)
                annot_utt_value = item.get('annot_utt', None)

                if id_value is not None:
                    file_data.append({'id': id_value, 'utt': utt_value, 'annot-utt': annot_utt_value})

        file_df = pd.DataFrame(file_data)

        # Merge the data into the combined DataFrame based on 'id' with a suffix for duplicate columns
        merged_df = pd.merge(pivot_df, file_df, on='id', how='left')

        # Get the language code from the JSONL filename
        language_code = os.path.splitext(os.path.basename(jsonl_file))[0]

        # Write to Excel file with a filename in the format "en-xx.xlsx"
        excel_filename = f'en-{language_code}.xlsx'
excel_file = os.path.join(output_folder, excel_filename)
merged_df.to_excel(excel_file, index=False, engine='openpyxl')

# You can skip writing the pivot data to a separate Excel file by removing this part.

print("Excel files created successfully!")
