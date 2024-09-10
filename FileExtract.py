import zipfile
import tarfile
import rarfile
import shutil
import os
import subprocess
import time


def get_student_id():
    result = subprocess.run('dir', shell=True, text=True, capture_output=True)
    result = str(result.stdout)
    results = result.split()
    for i in results:
        if i.find(".zip") != -1:
            return i.split('.')[0]


def extract_zip(zip_file_path, extract_to='.'):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted all files to {os.path.abspath(extract_to)}")


def extract_tar_gz(tar_gz_file_path, extract_to='.'):
    with tarfile.open(tar_gz_file_path, 'r:gz') as tar_ref:
        tar_ref.extractall(extract_to)
    print(f"Extracted all files to {os.path.abspath(extract_to)}")


def extract_rar(rar_file_path, extract_to='.'):
    with rarfile.RarFile(rar_file_path, 'r') as rar_ref:
        rar_ref.extractall(extract_to)
    print(f"Extracted all files to {os.path.abspath(extract_to)}")


def delete_folder_with_contents(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Deleted folder and all its contents: {folder_path}")
    except OSError as e:
        print(f"Error: {e.strerror} - {e.filename}")

def delete_zip(zip_path):
    try:
        os.remove(zip_path)
        print(f"Deleted .zip file: {zip_path}")
    except OSError as e:
        print(f"Error: {e.strerror} - {e.filename}")

def delete_file(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error: {e.strerror} - {e.filename}")
def get_total_files(student_ID):
    dir_path = f'./{student_ID}/{student_ID}'
    count = 0
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count
#
# student_ID = '6630300521'
#
# try:
#     zip_file_path = student_ID+'.zip'
#     extract_zip(zip_file_path, '.')
#
#     tar_gz_file_path = student_ID +'.tar.gz'
#     extract_tar_gz(tar_gz_file_path, '.')
#
#     rar_file_path = student_ID +'.rar'
#     extract_rar(rar_file_path, '.')
#
#
#
# except Exception as e:
#     print(e)
#
#
# time.sleep(5)
# folder_path = student_ID
# delete_folder_with_contents(folder_path)
#
# folder_path = '__MACOSX'
# delete_folder_with_contents(folder_path)
#
# zip_path = student_ID + '.zip'
# delete_zip(zip_path)


