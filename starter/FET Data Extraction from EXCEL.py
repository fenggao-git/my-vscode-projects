import pandas as pd
import os
from glob import glob

# Change this to your folder path
folder_path = '/Users/edison/Downloads/411-25-1PBS'  # e.g., r'C:\Users\YourName\Documents\ExcelFiles'

# Get list of all Excel files in the folder (can filter by .xlsx or .xls)
excel_files = glob(os.path.join(folder_path, '*.xlsx'))

# Initialize an empty DataFrame
combined_df = pd.DataFrame()

for file in excel_files:
    # Extract file name without extension
    file_name = os.path.splitext(os.path.basename(file))[0]
    print(f"Processing: {file}")
    # Read only the first column
    df = pd.read_excel(file, usecols=[0])
    
    # Rename the column to the file name
    df.columns = [file_name]
    
    # Combine all data (align by index)
    combined_df = pd.concat([combined_df, df], axis=1)

# Save to new Excel file
combined_df.to_excel(os.path.join(folder_path, 'combined_first_columns.xlsx'), index=False)
print("✅ All files combined successfully. Done!")

print("update on this windows")

print("1111")