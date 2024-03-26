import os
import shutil


def remove_files_in_directory(directory_path):
    try:

        shutil.rmtree(directory_path)
        os.makedirs(directory_path)

        print(f"All files removed successfully.")
    except Exception as e:
        print(f"Error removing files: {e}")


lis = ["/Report", "/Downloads","/Influ_downloads"]
for _ in lis:
    remove_files_in_directory(os.getcwd() + _)
