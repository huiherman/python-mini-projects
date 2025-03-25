
import os
import glob

# Step 1: Get all .txt files in a folder
folder_path = './sample_files'  # Create and place .txt files here
os.makedirs(folder_path, exist_ok=True)
files = glob.glob(os.path.join(folder_path, '*.txt'))

# Step 2: Rename each file
for file in files:
    directory, filename = os.path.split(file)
    new_name = os.path.join(directory, 'renamed_' + filename)
    os.rename(file, new_name)
    print(f'Renamed: {file} → {new_name}')
