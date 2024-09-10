import subprocess
import time

def run_file_1(student_ID):
    try:
        cpp_file = f'./{student_ID}/{student_ID}/{student_ID}_1.cpp'
        subprocess.run(f'g++ {cpp_file} -o program', check=True)
        result = subprocess.run('./program', input='4', text=True, capture_output=True)
        print(result.stdout)
    except Exception as e:
        print(e)

def run_file(student_ID,number,Input):
    try:
        cpp_file = f'./{student_ID}/{student_ID}/{student_ID}_{number}.cpp'
        subprocess.run(f'g++ {cpp_file} -o program', check=True)
        result = subprocess.run('./program', input=f'{Input}', text=True, capture_output=True)
        print(result.stdout)
    except Exception as e:
        print(e)
# def run_file_1(student_ID):
#     try:
#         # Correct path to the C++ file
#         cpp_file = f'D:/Projects/Grader/{student_ID}/{student_ID}/{student_ID}_1.cpp'
#
#         # Compile the C++ file
#         subprocess.run(f'g++ {cpp_file} -o program', shell=True, check=True)
#
#         # Run the compiled program and capture the output
#         result = subprocess.run('./program', input='4', text=True, capture_output=True)
#
#         # Print the output
#         print(result.stdout)
#     except Exception as e:
#         print(e)
