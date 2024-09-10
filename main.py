from FileExtract import *
import subprocess

from runFile import run_file_1, run_file

try:
    student_ID = get_student_id()
    extract_zip(student_ID+'.zip',student_ID)

    # run_file_1(student_ID)

    total_files = get_total_files(student_ID)
    # for i in range(total_files):
        # run_file(student_ID,total_files[i+1], )

    run_file(student_ID,2,11)

    # delete_file("program.exe")
    # delete_zip(student_ID+'.zip')
    delete_folder_with_contents(student_ID)
except Exception as e:
    print(e)






