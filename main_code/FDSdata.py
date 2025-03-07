import script_engine_main
import sys

def FDSdata(path):
    script_file = path
    with open(script_file, 'rb') as file:
        user_script = file.readlines()
    
    "Step 1 basic information."
    print('\n')
    print('**********************************************')
    print('* Fire Data Generator (FD-Gen) Version 1.0.0 *')
    print('********** upgraded date 12/6/2024 ***********')
    print('**********************************************')
    print('\n')
    print('========================================')
    script_engine_main.execute_MHDR_script(user_script)
    print('========================================\n')
    
    "Step 2 main program."
    print('\n')
    print('========================================')
    script_engine_main.execute_checking_script(user_script)
    print('========================================\n')
    user_input = input("Do you want to proceed to the SAMPLING step? (Y/N): ").strip().lower()
    if user_input == 'y':
        print('\n')
        print('\n')
        parameter_outputs, parameter_sample_generator_outputs=script_engine_main.execute_sampling_script(user_script)
        print('\n')
        user_input = input("Do you want to proceed to the WRAPPING step? (Y/N): ").strip().lower()
        
        if user_input == 'y':
            print('\n')
            print('\n')
            script_engine_main.execute_wrapping_script(user_script, parameter_outputs)
        elif user_input == 'n':
            print("Operation aborted.") 
            sys.exit()  
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            sys.exit()  
    elif user_input == 'n':
        print("Operation aborted.")
        sys.exit()  
        
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        sys.exit()  
        
        
    "Step 3 Plot the data."
    print('\n')
    print('========================================')
    script_engine_main.execute_plotting_script(user_script, parameter_outputs, parameter_sample_generator_outputs)
    print('========================================\n')
    

    return


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python FDSData.py <script_file_path>")
        sys.exit(1)
    
    script_file_path = sys.argv[1]
    FDSdata(script_file_path)
