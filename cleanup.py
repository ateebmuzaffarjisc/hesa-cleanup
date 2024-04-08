import os
import pandas as pd

username = os.getlogin()
file_name= f'C:\\Users\\{username}\\Jisc\\HESA Official statistics - Documents\\'

def get_files_sorted_by_size(directory):
    # List all files in the directory recursively
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append((file_path, os.path.getsize(file_path), os.path.getmtime(file_path)))

    # Sort files by size in descending order
    sorted_files = sorted(all_files, key=lambda x: x[1], reverse=True)
    return sorted_files

def bytes_to_mb(size_in_bytes):
    # Convert bytes to megabytes
    return size_in_bytes / (1024 * 1024)

def extract_date(timestamp):
    # Extract only the date part from the timestamp
    return pd.to_datetime(timestamp, unit='s').date()

def main():
    directory = file_name
    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return

    # Get files sorted by size
    files_sorted_by_size = get_files_sorted_by_size(directory)

    # Create a DataFrame
    data = []
    for file_path, size, modified_time in files_sorted_by_size[:20]:
        size_mb = bytes_to_mb(size)
        modified_date = extract_date(modified_time)
        data.append([file_path, size_mb, modified_date])

    df = pd.DataFrame(data, columns=['File Path', 'File Size (MB)', 'Last Modified Date'])

    # Return the DataFrame
    return df


if __name__ == "__main__":
    # Assign the returned DataFrame to a variable in the global scope
    top_10_files_df = main()