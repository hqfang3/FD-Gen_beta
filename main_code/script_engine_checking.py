#
from global_parm import *
import parse_syntax as PS

"Part 1: estimate data generator line length."
def checking_script_line_length(script):
    FDG_name_lists= {'MRND','IFSL','IVTP','IDWT','IRXB','IOTH','IFTD','IMHR','IHRC','GFSL','GVTP','GDWT','GRXB','GOTH','GFTD','GMHR','GHRC'}
    valid_line_grouped_list, valid_lines=PS.break_script(script)
    data_generator_script_line_len=0
    FDS_script_line_len=0
    for line_content, line_num in zip(script, range(len(script))):
        line_content=line_content.decode('UTF-8')
        if line_content[0] == '&' or line_content[:6] == '      ':
            if any(line_num in grouped_line for grouped_line in valid_line_grouped_list):
                index=next((index for index, grouped_line in enumerate(valid_line_grouped_list) if line_num in grouped_line),None)
                valid_line_function_name, args = PS.parse_script_lines(valid_lines[index]) 
                # Analyzing the valid lines
                if valid_line_function_name in FDG_name_lists:
                    data_generator_script_line_len=data_generator_script_line_len+1
                else:
                    FDS_script_line_len=FDS_script_line_len+1
            else:
                FDS_script_line_len=FDS_script_line_len+1
        else:
            FDS_script_line_len=FDS_script_line_len+1
    
    # print the results
    print('=====> Check script length')
    formatted_name = 'FDS script total length: '[:36].ljust(36)
    print_info = formatted_name +' '+str(FDS_script_line_len)
    print(print_info)
    formatted_name = 'Data generator script total length: '[:36].ljust(36)
    print_info = formatted_name +' '+str(data_generator_script_line_len)
    print(print_info)
    print('\n')
    return FDS_script_line_len, data_generator_script_line_len

def extract_id_name(script):
    FDG_name_lists= {'MRND','IFSL','IVTP','IDWT','IRXB','IOTH','IFTD','IMHR','GFSL','GVTP','GDWT','GRXB','GOTH','GFTD','GMHR','GHRC'}
    valid_line_grouped_list, valid_lines=PS.break_script(script)
    
    MHDR_name=[]
    pre_parm_id={'IFSL':[],'IVTP':[],'IDWT':[],'IRXB':[],'IOTH':[],'IFTD':[],'IMHR':[]}
    generator_id=[]
    generator_pair_id=[]
    
    for line in valid_lines:
        function_name, args = PS.parse_script_lines(line) 
        if function_name in FDG_name_lists:
            # 1 basic information
            if function_name == 'MHDR':
                if 'PROJECT_NAME' in args and 'NUMBER_OF_CASES' in args and 'SEEDS' in args:
                    project_name = args['PROJECT_NAME']
                    number_of_cases = args['NUMBER_OF_CASES']
                    seeds = args['SEEDS']
                else:
                    print("One or more required arguments are missing in MHDR.")
                MHDR_name.append([project_name, number_of_cases, seeds])
            
            # 2 PRE-PRAM input information
            if function_name in ['IFSL']:
                if 'PRE_PARM_INFO_ID' in args:
                    id_name = args['PRE_PARM_INFO_ID']
                    pre_parm_id['IFSL'].append(id_name)
                else:
                    print("PRE_PARM_INFO_ID is missing in IFSL.")
            
            if function_name in ['IVTP']:
                if 'PRE_PARM_INFO_ID' in args:
                    id_name = args['PRE_PARM_INFO_ID']
                    pre_parm_id['IVTP'].append(id_name)
                else:
                    print("PRE_PARM_INFO_ID is missing in IVTP.")
            
            if function_name in ['IDWT']:
                if 'PRE_PARM_INFO_ID' in args:
                    id_name = args['PRE_PARM_INFO_ID']
                    pre_parm_id['IDWT'].append(id_name)
                else:
                    print("PRE_PARM_INFO_ID is missing in IDWT.")
                    
            if function_name in ['IRXB']:
                if 'PRE_PARM_INFO_ID' in args:
                    id_name = args['PRE_PARM_INFO_ID']
                    pre_parm_id['IRXB'].append(id_name)
                else:
                    print("PRE_PARM_INFO_ID is missing in IRXB.")
            
            if function_name in ['IOTH']:
                if 'PRE_PARM_INFO_ID' in args:
                    id_name = args['PRE_PARM_INFO_ID']
                    pre_parm_id['IOTH'].append(id_name)
                else:
                    print("PRE_PARM_INFO_ID is missing in IOTH.")
            
            if function_name in ['IFTD']:
                if 'PRE_PARM_INFO_ID' in args:
                    id_name = args['PRE_PARM_INFO_ID']
                    pre_parm_id['IFTD'].append(id_name)
                else:
                    print("PRE_PARM_INFO_ID is missing in IFTD.")
                    
            if function_name in ['IMHR']:
                if 'PRE_PARM_INFO_ID' in args:
                    id_name = args['PRE_PARM_INFO_ID']
                    pre_parm_id['IMHR'].append(id_name)
                else:
                    print("PRE_PARM_INFO_ID is missing in IMHR.")
            
            # 3 GENERATOR input information
            if function_name in ['MRND']:
                if 'GENERATOR_ID' in args:
                    generator_id_name = args['GENERATOR_ID']
                else:
                    print("ID is missing in GENERATOR_ID.")
                if 'PRE_PARM_INFO_ID' in args:
                    pre_info_id_in_MRND_name = args['PRE_PARM_INFO_ID']
                else:
                    pre_info_id_in_MRND_name = None
                    print("ID is missing in PRE_PARM_INFO_ID.")
                generator_id.append(generator_id_name)
                generator_pair_id.append([generator_id_name, pre_info_id_in_MRND_name])
                
                
    return MHDR_name, pre_parm_id, generator_id, generator_pair_id


"Part 2-2: check PRE_PARM_INFO_ID and GENERATOR_ID have specific information."
def check_PRE_PARM_INFO_ID_info(pre_parm_id):
    # print the results
    print('=====>  Check PARAMETER PRE-INPUT information')
    for key, values in pre_parm_id.items():
        for value in values:
            formatted_name = 'PRE_PARM_INFO_ID: '+value[:21].ljust(21)+'==>'
            print_info = formatted_name +'     Namelist - '+ key
            print(print_info)
    print('\n')

    return


"Part 2-3: check I*** information have matches in MRND."
def check_GENERATOR_ID_info(generator_pair_id):
    # print the results
    print('=====>  Check SAMPLE GENERATOR information')
    for values in generator_pair_id:
        formatted_name = 'GENERATOR_ID: '+values[0][:21].ljust(21)+'==>'
        print_info = formatted_name +'     PRE_PARM_INFO_ID = '+ values[1]
        print(print_info)
    print('\n')

    return


"Part 2-4: check generator information have matches in G***."
"Part 2-5: check I*** information have matches in G***."
"Part 2-6: check FDS script have matched ID name."
def check_matched_info(script, pre_parm_id, generator_id):
    G_parm_name_lists= {'GFSL','GVTP','GDWT','GRXB','GOTH','GHRC'}
    MFLDandMFIR_parm_name_lists= {'GFSL','GVTP','GDWT','GRXB','GOTH','GFTD','GMHR','GHRC'}
    MFLDandMFIR_parm_name_lists_excludeGHRC= {'GFSL','GVTP','GDWT','GRXB','GOTH','GFTD','GMHR'}
    FDG_name_lists= {'MRND','IFSL','IVTP','IDWT','IRXB','IOTH','IFTD','IMHR','IHRC','GFSL','GVTP','GDWT','GRXB','GOTH','GFTD','GMHR','GHRC'}
    valid_line_grouped_list, valid_lines=PS.break_script(script)
    
    for line in valid_lines:
        generator_fds_para_match=0
        function_name, args = PS.parse_script_lines(line) 
        
        if function_name in MFLDandMFIR_parm_name_lists:
            if function_name in G_parm_name_lists:
                if 'ID' in args:
                    generator_parm_id = args['ID']
                    for line in valid_lines:
                        function_name_in, args_in = PS.parse_script_lines(line) 
                        if function_name_in not in FDG_name_lists:
                            if 'ID' in args_in:
                                fds_script_parm_id = args_in['ID']
                            else:
                                fds_script_parm_id = None
                            if generator_parm_id == fds_script_parm_id:
                                generator_fds_para_match=generator_fds_para_match+1
                    
                    formatted_name = 'ID: '+generator_parm_id[:21].ljust(21)+'==>'
                    print('=====> Check matched FDS ID')
                    if generator_fds_para_match==1:
                        if function_name == 'GDWT':
                            print_info_MATCH = formatted_name+'Match found (NOT applicable when multiple actions are involved)     FDS ID'
                            print(print_info_MATCH)
                        else:
                            print_info_MATCH = formatted_name+'Match found     FDS ID'
                            print(print_info_MATCH)
                    elif generator_fds_para_match==0:
                        if function_name == 'GDWT':
                            print_info_NO_MATCH = formatted_name+'NO Match found (NOT applicable when multiple actions are involved)     FDS ID'
                            print(print_info_NO_MATCH)
                        else:
                            print_info_NO_MATCH = formatted_name+'NO Match found     FDS ID'
                            print(print_info_NO_MATCH)
                            print('****************************************')
                            print('**************  WARNING  ***************')
                            print('\n')
                    else:
                        print_info_MORE_THAN_ONE = formatted_name+'More than one match     FDS ID'
                        print(print_info_MORE_THAN_ONE)     
                        print('****************************************')
                        print('**************  WARNING  ***************')
                        print('\n')             
                    
                else:
                    raise ValueError(f"ID name is missing in G***.")
            else:
                if 'ID' in args:
                    generator_parm_id = args['ID']
                    formatted_name = 'ID: '+generator_parm_id[:21].ljust(21)+'==>'
                    print_info = formatted_name+'NOT applicable     FDS ID'
                    print('=====> Check matched FDS ID')
                    print(print_info)  
                else:
                    raise ValueError(f"ID name is missing in G***.")              
            
            if function_name in MFLDandMFIR_parm_name_lists_excludeGHRC:
                if 'ID' in args:
                    generator_parm_id = args['ID']
                    print_info_MATCH=None
                    
                    # check PRE_PARM_INFO_ID
                    print('=====> Check matched PRE_PARM_INFO_ID')
                    if 'PRE_PARM_INFO_ID' in args:
                        generator_pre_parm_id = args['PRE_PARM_INFO_ID']
                        for key, values in pre_parm_id.items():
                            for item in values:
                                if generator_pre_parm_id == item:
                                    formatted_name = 'ID: '+generator_parm_id[:21].ljust(21)+'==>'
                                    print_info_MATCH = formatted_name+'Match found     '+'PRE_PARM_INFO_ID: '+item
                                    print(print_info_MATCH)
                        if print_info_MATCH is None:
                            formatted_name = 'ID: '+generator_parm_id[:21].ljust(21)+'==>'
                            print_info_MATCH = formatted_name+'NO Match found     '+'PRE_PARM_INFO_ID: '
                            print(print_info_MATCH)
                            print('****************************************')
                            print('**************  WARNING  ***************')
                            print('\n')
                    else:
                        formatted_name = 'ID: '+generator_parm_id[:21].ljust(21)+'==>'
                        print_info_MATCH = formatted_name+'NO Exist     '+'PRE_PARM_INFO_ID: '
                    
                    # check GENERATOR_ID
                    print('=====> Check matched GENERATOR_ID')
                    if 'GENERATOR_ID' in args:
                        parm_generator_id = args['GENERATOR_ID']
                        if not isinstance(parm_generator_id, list):
                            parm_generator_id = [parm_generator_id]
                        for value in parm_generator_id:
                            if generator_id.count(value) == 1:
                                formatted_name = 'ID: '+generator_parm_id[:21].ljust(21)+'==>'
                                print_info_MATCH = formatted_name+'Match found     '+'GENERATOR_ID: '+value
                                print(print_info_MATCH)
                            elif generator_id.count(value) == 0:
                                formatted_name = 'ID: '+generator_parm_id[:21].ljust(21)+'==>'
                                print_info_MATCH = formatted_name+'NO Match found     '+'GENERATOR_ID: '
                                print(print_info_MATCH)
                                print('****************************************')
                                print('**************  WARNING  ***************')
                                print('\n')
                            else: 
                                formatted_name = 'ID: '+generator_parm_id[:21].ljust(21)+'==>'
                                print_info_MATCH = formatted_name+'More than one match found    '+'GENERATOR_ID: '
                                print(print_info_MATCH)      
                                print('****************************************')
                                print('**************  WARNING  ***************')
                                print('\n')     
                else:
                    raise ValueError(f"ID name is missing in G***.")
            else:
                if 'ID' in args:
                    generator_parm_id = args['ID']
                    formatted_name = 'ID: '+generator_parm_id[:21].ljust(21)+'==>'
                    print_info_MATCH = formatted_name+'NOT applicable     PRE_PARM_INFO_ID'
                    print('=====> Check matched PRE_PARM_INFO_ID')
                    print(print_info_MATCH)            
                    print_info_MATCH = formatted_name+'NOT applicable     GENERATOR_ID'
                    print('=====> Check matched GENERATOR_ID')
                    print(print_info_MATCH)    
                else:
                    raise ValueError(f"ID name is missing in G***.")
            print('\n')
            
    return            
    
            
                    
