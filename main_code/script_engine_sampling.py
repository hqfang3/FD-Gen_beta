from global_parm import *
import MRND
import MFLD
import MFIR
import parse_syntax as PS
import itertools
import numpy as np


"Part 1: to execute FDS generator script."
# execute script - main
def execute_script(script):
    
    # namespace
    namespace_MRND = {'MRND': MRND.INPUT_SAMPLE_GENERATOR_INFO}
    namespace_MFLD = {
        'IFSL': MFLD.INPUT_FIRE_SOURCE_LOCATION_INFO,
        'GFSL': MFLD.GENERATING_FIRE_SOURCE_LOCATION_SAMPLES,
        'IVTP': MFLD.INPUT_VENT_POSITION_INFO,
        'GVTP': MFLD.GENERATING_VENT_POSITION_SAMPLES,
        'IDWT': MFLD.INPUT_DOOR_OR_WINDOW_OPEN_TIME_INFO,
        'GDWT': MFLD.GENERATING_DOOR_OR_WINDOW_OPEN_TIME_SAMPLES,
        'IRXB': MFLD.INPUT_OBSTRUCTIONS_INFO,
        'GRXB': MFLD.GENERATING_OBSTRUCTIONS_SAMPLES,
        'IOTH': MFLD.INPUT_OTHERS_INFO,
        'GOTH': MFLD.GENERATING_OTHERS_SAMPLES,
        }
    namespace_MFIR = {
        'IFTD': MFIR.INPUT_FIRE_TIME_DURATION_INFO,
        'GFTD': MFIR.GENERATING_FIRE_TIME_DURATION_SAMPLES,
        'IMHR': MFIR.INPUT_MAX_HRR_INFO,
        'GMHR': MFIR.GENERATING_MAX_HRR_SAMPLES,
        'GHRC': MFIR.GENERATING_HRR_CURVE,
        }
    # output parameters
    parameter_pre_inputs_info={'FSL':[],'VTP':[],'DWT':[],'RXB':[],'OTH':[],'FTD':[],'MHR':[],'HRC':[]}
    parameter_pre_outputs_info={'FSL':[],'VTP':[],'DWT':[],'RXB':[],'OTH':[],'FTD':[],'MHR':[],'HRC':[]}
    parameter_sample_generator_info=[]
    parameter_outputs = {'FSL':[],'VTP':[],'DWT':[],'RXB':[],'OTH':[],'FTD':[],'MHR':[],'HRC':[]}
    parameter_sample_generator_outputs = {'FSL':[],'VTP':[],'DWT':[],'RXB':[],'OTH':[],'FTD':[],'MHR':[],'HRC':[]}
    
    # analyze the script
    valid_line_grouped_list, valid_lines=PS.break_script(script)
    
    # parameter pre-info inputs
    for line in valid_lines:
        function_name, args = PS.parse_script_lines(line) 
        # Under the MFLD namelist 
        if function_name == 'IFSL':
            fire_source_location, generator_info_X, generator_info_Y, generator_info_Z = namespace_MFLD[function_name](**args)
            # save the data
            parameter_pre_outputs_info['FSL'].append(fire_source_location)
            parameter_pre_inputs_info['FSL'].append(generator_info_X)
            parameter_pre_inputs_info['FSL'].append(generator_info_Y)
            parameter_pre_inputs_info['FSL'].append(generator_info_Z)
            
        if function_name == 'IVTP':
            vent_position, generator_info_VP_X, generator_info_VP_Y, generator_info_VP_Z = namespace_MFLD[function_name](**args)
            # save the data
            parameter_pre_outputs_info['VTP'].append(vent_position)
            parameter_pre_inputs_info['VTP'].append(generator_info_VP_X)
            parameter_pre_inputs_info['VTP'].append(generator_info_VP_Y)
            parameter_pre_inputs_info['VTP'].append(generator_info_VP_Z)
                       
        # door or window open time
        if function_name == 'IDWT':
            door_or_window_open_time, generated_info_variables = namespace_MFLD[function_name](**args)
            # save the data
            parameter_pre_outputs_info['DWT'].append(door_or_window_open_time)
            for info in generated_info_variables:
                parameter_pre_inputs_info['DWT'].append(info)
                       
        # obstruction size sampling
        if function_name == 'IRXB':
            obstructions, generator_info_obst_length, generator_info_obst_width, generator_info_obst_height = namespace_MFLD[function_name](**args)
            # save the data
            parameter_pre_outputs_info['RXB'].append(obstructions)
            parameter_pre_inputs_info['RXB'].append(generator_info_obst_length)
            parameter_pre_inputs_info['RXB'].append(generator_info_obst_width)
            parameter_pre_inputs_info['RXB'].append(generator_info_obst_height)
            
        # others sampling
        if function_name == 'IOTH':
            others, generator_info_others = namespace_MFLD[function_name](**args)
            # save the data
            parameter_pre_outputs_info['OTH'].append(others)
            parameter_pre_inputs_info['OTH'].append(generator_info_others)


        # Under the MFIR namelist 
        # fire time duration sampling
        if function_name == 'IFTD':
            fire_time_duration, fire_time_duration_list, sample_generator_info_FTD_S1, sample_generator_info_FTD_S2, sample_generator_info_FTD_S2_R, sample_generator_info_FTD_S3, sample_generator_info_FTD_S4, sample_generator_info_FTD_S4_R = namespace_MFIR[function_name](**args)
            # save the data
            parameter_pre_outputs_info['FTD'].append(fire_time_duration)
            FTD_sample_generator_list=[sample_generator_info_FTD_S1, sample_generator_info_FTD_S2, sample_generator_info_FTD_S2_R, sample_generator_info_FTD_S3, sample_generator_info_FTD_S4, sample_generator_info_FTD_S4_R]
            none_indices = [index for index, value in enumerate(fire_time_duration_list) if value == [None]]
            filtered_FTD_sample_generator_list = [value for index, value in enumerate(FTD_sample_generator_list) if index not in none_indices]
            for info in filtered_FTD_sample_generator_list:
                parameter_pre_inputs_info['FTD'].append(info)
        
        # max HRR sampling
        if function_name == 'IMHR':
            heat_release_rate, generator_info_HRR_incipient, generator_info_HRR_peak, generator_info_HRR_decay = namespace_MFIR[function_name](**args)
            # save the data
            parameter_pre_outputs_info['MHR'].append(heat_release_rate)
            parameter_pre_inputs_info['MHR'].append(generator_info_HRR_incipient)
            parameter_pre_inputs_info['MHR'].append(generator_info_HRR_peak)
            parameter_pre_inputs_info['MHR'].append(generator_info_HRR_decay)

    
    # obtain the list of pre-input info for the generator
    parameter_IDs={'FSL':[],'VTP':[],'DWT':[],'RXB':[],'OTH':[],'FTD':[],'MHR':[],'HRC':[]}
    for namelist, items in parameter_pre_inputs_info.items():
        for i in items:
            for key, value in i.items():
                parameter_IDs[namelist].append(i[key][0])
    

    # create generator info
    for line in valid_lines:
        function_name, args = PS.parse_script_lines(line) 
        # Under the MRND namelist 
        if function_name == 'MRND':
            if 'PRE_PARM_INFO_ID' in args:
                namelist = [namelist for namelist, parameter_ID in parameter_IDs.items() if args['PRE_PARM_INFO_ID'] in parameter_ID]
                if namelist ==[]:
                    raise ValueError(f"Did NOT find the matching 'PRE_PARM_INFO_ID' with arguments '{args}'.")
                for number, parameter_value in enumerate(parameter_IDs[namelist[-1]]):
                    if parameter_value == args['PRE_PARM_INFO_ID']:
                        info=namespace_MRND[function_name](SAMPLE_GENERATOR_INFO=parameter_pre_inputs_info[namelist[-1]][number],**args)
                        parameter_sample_generator_info.append(info)
                        break
                else:
                    raise ValueError(f"PRE_PARM_INFO_ID for '{args['ID']}' is NOT found.")
            else:
                info=namespace_MRND[function_name](SAMPLE_GENERATOR_INFO=None,**args)
                parameter_sample_generator_info.append(info)
            
                
    # generating samples
    for line in valid_lines:
        function_name, args = PS.parse_script_lines(line) 
        
        # MFLD sample generation
        if function_name == 'GFSL':
            print(f"========================================")
            print(f"== Parameter (fire source location) - {args['ID']} ==")
            print(f"==> Generating samples...")
            parameter, sample_generator=namespace_MFLD[function_name](PARAMETER_PRE_OUTPUTS_INFO=parameter_pre_outputs_info['FSL'], PARAMETER_SAMPLE_GENERATOR_INFO=parameter_sample_generator_info, **args)
            parameter_sample_generator_outputs['FSL'].append(sample_generator)
            parameter_outputs['FSL'].append(parameter)
            print('==> Data samples generated Successfully.')
            print(f"========================================\n")
        
        if function_name == 'GVTP':
            print(f"========================================")
            print(f"== Parameter (vent position) - {args['ID']} ==")
            print(f"==> Generating samples...")
            parameter, sample_generator=namespace_MFLD[function_name](PARAMETER_PRE_OUTPUTS_INFO=parameter_pre_outputs_info['VTP'], PARAMETER_SAMPLE_GENERATOR_INFO=parameter_sample_generator_info, **args)
            parameter_sample_generator_outputs['VTP'].append(sample_generator)
            parameter_outputs['VTP'].append(parameter)
            print('==> Data samples generated Successfully.')
            print(f"========================================\n")
        
        if function_name == 'GDWT':
            print(f"========================================")
            print(f"== Parameter (door or window open time) - {args['ID']} ==")
            print(f"==> Generating samples...")
            parameter, sample_generator=namespace_MFLD[function_name](PARAMETER_PRE_OUTPUTS_INFO=parameter_pre_outputs_info['DWT'], PARAMETER_SAMPLE_GENERATOR_INFO=parameter_sample_generator_info, **args)
            parameter_sample_generator_outputs['DWT'].append(sample_generator)
            parameter_outputs['DWT'].append(parameter)
            print('==> Data samples generated Successfully.')
            print(f"========================================\n")
        
        if function_name == 'GRXB':
            print(f"========================================")
            print(f"== Parameter (door or window open time) - {args['ID']} ==")
            print(f"==> Generating samples...")
            parameter, sample_generator=namespace_MFLD[function_name](PARAMETER_PRE_OUTPUTS_INFO=parameter_pre_outputs_info['RXB'], PARAMETER_SAMPLE_GENERATOR_INFO=parameter_sample_generator_info, **args)
            parameter_sample_generator_outputs['RXB'].append(sample_generator)
            parameter_outputs['RXB'].append(parameter)
            print('==> Data samples generated Successfully.')
            print(f"========================================\n")

        if function_name == 'GOTH':
            print(f"========================================")
            print(f"== Parameter (others) - {args['ID']} ==")
            print(f"==> Generating samples...")
            parameter, sample_generator=namespace_MFLD[function_name](PARAMETER_PRE_OUTPUTS_INFO=parameter_pre_outputs_info['OTH'], PARAMETER_SAMPLE_GENERATOR_INFO=parameter_sample_generator_info, **args)
            parameter_sample_generator_outputs['OTH'].append(sample_generator)
            parameter_outputs['OTH'].append(parameter)
            print('==> Data samples generated Successfully.')
            print(f"========================================\n")
            
        # MFIR sample generation
        if function_name == 'GFTD':
            print(f"========================================")
            print(f"== Parameter (fire time duration) - {args['ID']} ==")
            print(f"==> Generating samples...")
            parameter, sample_generator=namespace_MFIR[function_name](PARAMETER_PRE_OUTPUTS_INFO=parameter_pre_outputs_info['FTD'], PARAMETER_SAMPLE_GENERATOR_INFO=parameter_sample_generator_info, **args)
            parameter_sample_generator_outputs['FTD'].append(sample_generator)
            parameter_outputs['FTD'].append(parameter)       
            print('==> Data samples generated Successfully.')
            print(f"========================================\n")
            
        if function_name == 'GMHR':
            print(f"========================================")
            print(f"== Parameter (max HRR) - {args['ID']} ==")
            print(f"==> Generating samples...")
            parameter, sample_generator=namespace_MFIR[function_name](PARAMETER_PRE_OUTPUTS_INFO=parameter_pre_outputs_info['MHR'], PARAMETER_SAMPLE_GENERATOR_INFO=parameter_sample_generator_info, **args)
            parameter_sample_generator_outputs['MHR'].append(sample_generator)
            parameter_outputs['MHR'].append(parameter)       
            print('==> Data samples generated Successfully.')
            print(f"========================================\n")
    
    # generating fire curves
    for line in valid_lines:
        function_name, args = PS.parse_script_lines(line) 
        # HRR curve generation
        if function_name == 'GHRC':
            print(f"========================================")
            print(f"== Parameter (fire HRR curve) - {args['ID']} ==")
            print(f"==> Generating samples...")
            HRR_curve = namespace_MFIR[function_name](PARAMETER_OUTPUTS=[parameter_outputs['FTD'], parameter_outputs['MHR']], **args)
            parameter_outputs['HRC'].append(HRR_curve) 
            print('==> Data samples generated Successfully.')
            print(f"========================================\n")
    
    # Go through the samples and check Cartesian product iteration
    ALL_product_combinations=[]
    parameter_generator_for_product_exc_HRC=[]
    parameter_generator_for_product_HRC=[]
    parameter_generator_for_product_FTD=[]
    parameter_generator_for_product_MHR=[]
    PRODUCT_list=[]
    for parameters_name, parameters_value in parameter_outputs.items():
        for parameter_item in parameters_value:
            if parameters_name in ['FTD']:
                parameter_generator_for_product_FTD.append(parameter_item)
            elif parameters_name in ['MHR']:
                parameter_generator_for_product_MHR.append(parameter_item)
            else:
                PRODUCT_list.append(parameter_item.PRODUCT)
                if parameter_item.PRODUCT is True:
                    if parameters_name in ['FSL', 'VTP', 'DWT', 'RXB', 'OTH']:
                        parameter_generator_for_product_exc_HRC.append(parameter_item)
                        ALL_product_combinations.append(list(range(parameter_item.NUMBER_OF_SAMPLES[0])))
                    else:
                        parameter_generator_for_product_HRC.append(parameter_item)
                        ALL_product_combinations.append(list(range(parameter_item.NUMBER_OF_SAMPLES)))
                            
    PRODUCT_sample_combinations = list(itertools.product(*ALL_product_combinations))
    
    # save into samples
    global_number_of_samples=GET_VALUE("NUMBER_OF_CASES")
    if True in PRODUCT_list:
        if global_number_of_samples <= len(PRODUCT_sample_combinations):
        
            for num, generator_for_product in enumerate(parameter_generator_for_product_exc_HRC):
                for feature in range(len(generator_for_product.SAMPLES)):
                    generator_product_samples_index=[]
                    for sample_num in range(len(PRODUCT_sample_combinations)):
                        generator_product_samples_index.append(PRODUCT_sample_combinations[sample_num][num])   
                    generator_for_product.SAMPLES[feature] = np.array([generator_for_product.SAMPLES[feature][i] for i in generator_product_samples_index])
                    generator_for_product.SAMPLES[feature] = generator_for_product.SAMPLES[feature][:global_number_of_samples]
                    generator_for_product.NUMBER_OF_SAMPLES[feature]=len(PRODUCT_sample_combinations)
            
            for num, generator_for_product in enumerate(parameter_generator_for_product_HRC):
                generator_product_samples_index=[]
                for sample_num in range(len(PRODUCT_sample_combinations)):
                    generator_product_samples_index.append(PRODUCT_sample_combinations[sample_num][len(parameter_generator_for_product_exc_HRC)+num])   
                generator_for_product.HRR_SAMPLES = [generator_for_product.HRR_SAMPLES[i] for i in generator_product_samples_index]
                generator_for_product.HRR_SAMPLES = generator_for_product.HRR_SAMPLES[:global_number_of_samples]
                generator_for_product.TIME_SLICE_SAMPLES = [generator_for_product.TIME_SLICE_SAMPLES[i] for i in generator_product_samples_index]
                generator_for_product.TIME_SLICE_SAMPLES = generator_for_product.TIME_SLICE_SAMPLES[:global_number_of_samples]
                generator_for_product.NUMBER_OF_SAMPLES = len(generator_for_product.HRR_SAMPLES) 
            
            for num, generator_for_product in enumerate(parameter_generator_for_product_FTD):
                for feature in range(len(generator_for_product.SAMPLES)):
                    generator_product_samples_index=[]
                    for sample_num in range(len(PRODUCT_sample_combinations)):
                        generator_product_samples_index.append(PRODUCT_sample_combinations[sample_num][len(parameter_generator_for_product_exc_HRC)]) 
                    generator_for_product.SAMPLES[feature] = np.array([generator_for_product.SAMPLES[feature][i] for i in generator_product_samples_index])
                    generator_for_product.SAMPLES[feature] = generator_for_product.SAMPLES[feature][:global_number_of_samples]
                    generator_for_product.NUMBER_OF_SAMPLES[feature]=len(PRODUCT_sample_combinations)  
            
            for num, generator_for_product in enumerate(parameter_generator_for_product_MHR):
                for feature in range(len(generator_for_product.SAMPLES)):
                    generator_product_samples_index=[]
                    for sample_num in range(len(PRODUCT_sample_combinations)):
                        generator_product_samples_index.append(PRODUCT_sample_combinations[sample_num][len(parameter_generator_for_product_exc_HRC)]) 
                    generator_for_product.SAMPLES[feature] = np.array([generator_for_product.SAMPLES[feature][i] for i in generator_product_samples_index])
                    generator_for_product.SAMPLES[feature] = generator_for_product.SAMPLES[feature][:global_number_of_samples]
                    generator_for_product.NUMBER_OF_SAMPLES[feature]=len(PRODUCT_sample_combinations)  
        
        else:
            raise ValueError(f"Parameter samples less than global NUMBER_OF_CASES.")
    
    else:
        for parameters_name, parameters_value in parameter_outputs.items():
            if parameters_name in ['FSL', 'VTP', 'DWT', 'RXB', 'OTH']:
                for parameter_item in parameters_value:
                    if parameter_item.NUMBER_OF_SAMPLES[0]<global_number_of_samples:
                        raise ValueError(f"Parameter samples less than global NUMBER_OF_CASES.")
            if parameters_name in ['HRC']:
                for parameter_item in parameters_value:
                    if parameter_item.NUMBER_OF_SAMPLES<global_number_of_samples:
                        raise ValueError(f"Parameter samples less than global NUMBER_OF_CASES.")
        
      
    return parameter_outputs, parameter_sample_generator_outputs