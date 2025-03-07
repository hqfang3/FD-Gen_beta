import MHDR
import MSTT
import parse_syntax as PS
import script_engine_checking as SEC
import script_engine_sampling as SES


def execute_MHDR_script(script):
    # namespace
    namespace_MHDR = {'MAIN': MHDR.MHDR_MAIN}
    # processing MHDR input
    valid_line_grouped_list, valid_lines=PS.break_script(script)
    for line in valid_lines:
        function_name, args = PS.parse_script_lines(line) 
    # basic information 
        if function_name == 'MAIN':
            namespace_MHDR[function_name](**args)
            MHDR.SAVE_SEEDS()
    return

def execute_checking_script(script):
    print('=========  Script checking =============')
    print('\n')
    FDS_script_line_len, data_generator_script_line_len=SEC.checking_script_line_length(script)
    MHDR_name, pre_parm_id, generator_id, generator_pair_id=SEC.extract_id_name(script)
    SEC.check_PRE_PARM_INFO_ID_info(pre_parm_id)
    SEC.check_GENERATOR_ID_info(generator_pair_id)
    SEC.check_matched_info(script, pre_parm_id, generator_id)
    print('========================================')
    
    return

def execute_sampling_script(script):
    print('========================================')
    print('======  Parameter data sampling ========')
    parameter_outputs, parameter_sample_generator_outputs=SES.execute_script(script)
    MHDR.PARAMETER_FILE(parameter_outputs, parameter_sample_generator_outputs)
    print('========================================')
    print('========================================')
    
    return parameter_outputs, parameter_sample_generator_outputs

def execute_wrapping_script(script, parameter_outputs):
    print('========================================')
    print('======  Parameter data wrapping ========')
    print('\n')
    MHDR.CASE_FOLDER(script, parameter_outputs)
    print('========================================')
    print('========================================')
    
    return 

def execute_plotting_script(script, parameter_outputs, parameter_sample_generator_outputs):
    print('======  Parameter data plotting ========')
    namespace_MSTT = {'PFSL': MSTT.PLOT_FIRE_SOURCE_LOCATIONS,
                      'PHRC': MSTT.PLOT_HRR_CURVES,
                      'PPSD': MSTT.PLOT_GENERATOR_SAMPLINGS}
    MHDR.OUTPUT_FOLDER()

    valid_line_grouped_list, valid_lines=PS.break_script(script)
    for line in valid_lines:
        function_name, args = PS.parse_script_lines(line) 

        if function_name == 'PFSL':
            namespace_MSTT[function_name](**args, PARAMETERS_OUTPUT=parameter_outputs)
        if function_name == 'PHRC':
            namespace_MSTT[function_name](**args, PARAMETERS_OUTPUT=parameter_outputs)
        if function_name == 'PPSD':
            namespace_MSTT[function_name](**args, SAMPLE_GENERATOR_OUTPUTS=parameter_sample_generator_outputs)
    
    print('\n')
    print(f"*****OUTPUT_FOLDER file created successfully.")
    print('========================================')
    
    return 
    
