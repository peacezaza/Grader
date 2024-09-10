from FileExtract import *
import subprocess

from runFile import run_file_1

student_ID = get_student_id()
extract_zip(student_ID+'.zip',student_ID)
run_file_1(student_ID)
delete_file("program.exe")
# delete_zip(student_ID+'.zip')
delete_folder_with_contents(student_ID)







