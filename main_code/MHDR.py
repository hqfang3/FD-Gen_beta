import numpy as np
import os
import shutil
import global_parm
from global_parm import *
import script_engine_wrapper as SEW
import QUTP

"Part 1: giving the basic case information."
def MHDR_MAIN(PROJECT_NAME, NUMBER_OF_CASES, SEEDS=1):
    global_parm._INIT()
    print('===========  Basic INFO ================')
    DEFINE_PROJECT_NAME(PROJECT_NAME)
    DEFINE_PATH()
    DEFINE_NUMBER_OF_CASES(NUMBER_OF_CASES)
    DEFINE_SEEDS(SEEDS)
    print('========================================')
    return
    
    
# define project name.
def DEFINE_PROJECT_NAME(PROJECT_NAME):
    project_name=str(PROJECT_NAME)
    formatted_name = 'PROJECT_NAME'[:21].ljust(21)+'==>'
    print_info = formatted_name +' '+project_name
    print(print_info)
    SET_VALUE('PROJECT_NAME', project_name)
    return 

# define path name
def DEFINE_PATH():
    PATH = os.getcwd()
    path=PATH + "\\" + GET_VALUE('PROJECT_NAME')
    formatted_name = 'CURRENT PATH'[:21].ljust(21)+'==>'
    print_info = formatted_name +' '+path
    print(print_info)
    # Check if the directory exists
    if os.path.exists(path):
     # If it exists, remove it
        shutil.rmtree(path)
    # Create the new directory
    os.makedirs(path)
    SET_VALUE('PATH',path)
    return

# number of cases to be generated.
def DEFINE_NUMBER_OF_CASES(NUMBER_OF_CASES):
    number_of_cases=NUMBER_OF_CASES
    formatted_name = 'NUMBER_OF_CASES'[:21].ljust(21)+'==>'
    print_info = formatted_name +' '+str(number_of_cases)
    print(print_info)
    SET_VALUE('NUMBER_OF_CASES',number_of_cases)
    return


# defines on integer pair used to determine random number seeds for distributions.
def DEFINE_SEEDS(SEEDS):
    seeds=SEEDS
    np.random.seed(seeds)
    random_seeds_list = np.random.randint(0, 100, size=200)
    formatted_name = 'SEEDS'[:21].ljust(21)+'==>'
    print_info = formatted_name +' '+str(seeds)
    print(print_info)
    SET_VALUE('SEEDS_NUMBER',seeds)
    SET_VALUE('SEEDS',random_seeds_list)
    return


# The seed number is saved to original path with a .txt file outputted.
def SAVE_SEEDS():
    
    save_seed_path=GET_VALUE('PATH')+"\\" + "SEEDS_FOLDER"
    # Check if the directory exists
    if os.path.exists(save_seed_path):
     # If it exists, remove it
        shutil.rmtree(save_seed_path)
    # Create the new directory
    os.makedirs(save_seed_path)
    os.chdir(save_seed_path)
    # write SAVE_SEEDS .text file
    with open(save_seed_path+"\\"+'SAVE_SEEDS_file.txt', 'w') as save_seed_file:
        save_seed_file.write(f"The seed number is: {GET_VALUE('SEEDS_NUMBER')}\n")
        save_seed_file.write(f"The number of cases is: {GET_VALUE('NUMBER_OF_CASES')}\n")
        
    print(f"SAVE_SEEDS file created successfully.\n")
    
    return 


"Part 2: parameter and case files output."
# output a Summary file of the generated cases including their file names and parameter values for inputs varied for each FDS scenario in the set of generated FDS cases.
def PARAMETER_FILE(PARAMETERS_OUTPUT, PARAMETER_SAMPLE_GENERATOR_OUTPUTS):
    
    number_of_case=GET_VALUE('NUMBER_OF_CASES')
    parameter_file_path=GET_VALUE('PATH')+"\\" + "PARAMETER_FILE_FOLDER"
    parameter_brief_name='param_brief.txt'
    generator_info_name='generator_info.txt'
    parameter_spreadsheet_name='parameter_outputs.xlsx'
    # Check if the directory exists
    if os.path.exists(parameter_file_path):
     # If it exists, remove it
        shutil.rmtree(parameter_file_path)
    # Create the new directory
    os.makedirs(parameter_file_path)
    os.chdir(parameter_file_path)
    # write PARAMETER_FILE .csv file
    file_parameter_brief=QUTP.PRINT_PARAMETER_BRIEF_INFO(PARAMETERS_OUTPUT, parameter_file_path, parameter_brief_name)
    file_generator_info=QUTP.PRINT_GENERATOR_INFO(PARAMETER_SAMPLE_GENERATOR_OUTPUTS, parameter_file_path, generator_info_name)
    file_parameter_spreadsheet=QUTP.PRINT_PARAMETER_SPREADSHEET(number_of_case, PARAMETERS_OUTPUT, parameter_file_path, parameter_spreadsheet_name)
    
    print(f"*****PARAMETER_FILE file created successfully.")
    
    return 


# output the set of FDS inputs file and this folder creates the path where the FDS input files to be run.
def CASE_FOLDER(USER_SCRIPT, parameter_outputs):
    filename=GET_VALUE('PROJECT_NAME')
    work_folder_path=GET_VALUE('PATH')+"\\" + "CASE_FOLDER"
    # Check if the directory exists
    if os.path.exists(work_folder_path):
     # If it exists, remove it
        shutil.rmtree(work_folder_path)
    # Create the new directory
    os.makedirs(work_folder_path)
    os.chdir(work_folder_path)
    # write WORK_FOLDER .fds file
    file=SEW.replace_FDS_base_script(USER_SCRIPT, filename=filename, parameter_outputs=parameter_outputs)
    
    print(f"*****CASE_FOLDER file created successfully.")
    
    return 
    
"Part 3: output file output."
def OUTPUT_FOLDER():
    
    output_folder_path=GET_VALUE('PATH')+"\\" + "OUTPUT_FOLDER"
    # Check if the directory exists
    if os.path.exists(output_folder_path):
     # If it exists, remove it
        shutil.rmtree(output_folder_path)
    # Create the new directory
    os.makedirs(output_folder_path)
    os.chdir(output_folder_path)

    return 
