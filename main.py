from FileExtract import *
import subprocess

from runFile import run_file_1, run_file
times = [1,2,1,1]
Input = [4, [4, 11], "", ""]

try:
    student_ID = get_student_id()
    extract_zip(student_ID+'.zip',student_ID)

    # run_file_1(student_ID)

    total_files = get_total_files(student_ID)
    # total_files = 2
    for i in range(1,total_files):
        for j in range(times[i]):
            if times[i] > 1:
                run_file(student_ID, i+1, Input[i][j])
                # print(f"Input is {Input[j]}")
            else:
                run_file(student_ID,i+1,Input[i])
                # print(f"Input is {Input}")

    # run_file(student_ID,4,"")

    # delete_file("program.exe")
    # delete_zip(student_ID+'.zip')
    delete_folder_with_contents(student_ID)
except Exception as e:
    print(e)






