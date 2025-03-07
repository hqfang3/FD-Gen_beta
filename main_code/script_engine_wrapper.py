from global_parm import *
import parse_syntax as PS

"Part 2: to replace the value."
def replace_FDS_base_script(script, filename, parameter_outputs):
    
    def write_lines(line_content, line_content_replaced):
        if line_content_replaced==[]:
            file.writelines(str.encode(line_content).decode('UTF-8').rstrip('\r\n')+'\n')
        else:
            for lines in line_content_replaced:
                file.writelines(str.encode(lines).decode('UTF-8').rstrip('\r\n')+'\n')
        return 
    
    # number of input files and read 
    number_of_input_files=GET_VALUE("NUMBER_OF_CASES")
    # break script
    valid_line_grouped_list, valid_lines=PS.break_script(script)
    # data generator namelist
    FDG_name_lists= {'PFSL', 'PHRC', 'PPSD', 'MAIN','MRND','IFSL','IVTP','IDWT','IRXB','IOTH','IFTD','IMHR','IHRC','GFSL','GVTP','GDWT','GRXB','GOTH','GFTD','GMHR','GHRC'}
    
    # write each input file
    for case_num in range(number_of_input_files):
        # create file name
        fds_input_file_name=str(filename+'_'+'{:05}'.format(case_num)+'.fds')
        # go through FDS data generator script
        with open(fds_input_file_name, 'w') as file:
            for line_content, line_num in zip(script, range(len(script))):
                line_content=line_content.decode('UTF-8')
                line_content_replaced=[]
                if line_content[0] == '&' or line_content[:6] == '      ':
                    if any(line_num in grouped_line for grouped_line in valid_line_grouped_list):
                        index=next((index for index, grouped_line in enumerate(valid_line_grouped_list) if line_num in grouped_line),None)
                        valid_line_function_name, valid_line_args = PS.parse_script_lines(valid_lines[index]) 
                        if valid_line_function_name not in FDG_name_lists:
                            # ===================== HEAD ===========================
                            if valid_line_function_name == 'HEAD':
                                function_name, args = PS.parse_script_lines(line_content) 
                                case_name=str(filename+'_'+'{:05}'.format(case_num))
                                if 'CHID' in args:
                                    index=next((index for index, parm_name in enumerate(args) if parm_name == 'CHID'),None)
                                    if index+1 == len(args):
                                        replaced_after_args=None
                                    else:
                                        replaced_after_args=list(args)[index+1]
                                    line_content_replaced=[PS.replace_value(line_content, replaced_args='CHID', replaced_after_args=replaced_after_args, replaced_value=[case_name])]
                                write_lines(line_content, line_content_replaced)
                            # ===================== OBST ===========================
                            elif valid_line_function_name == 'OBST':
                                # fire source location
                                line_content_replaced_FSL=replace_FSL_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # door or window open time 
                                line_content_replaced_DWT_OBST=replace_DWT_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # XB
                                line_content_replaced_RXB=replace_RXB_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # OTHERS
                                line_content_replaced_OTH=replace_OTH_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # write into the input file
                                line_content_replaced=next((x for x in [line_content_replaced_FSL, line_content_replaced_DWT_OBST, line_content_replaced_RXB, line_content_replaced_OTH] if x != []), [])
                                write_lines(line_content, line_content_replaced)
                            # ===================== VENT ===========================
                            elif valid_line_function_name == 'VENT':
                                # vent position
                                line_content_replaced_VTP=replace_VTP_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # XB
                                line_content_replaced_RXB=replace_RXB_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # OTHERS
                                line_content_replaced_OTH=replace_OTH_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # write into the input file
                                line_content_replaced=next((x for x in [line_content_replaced_VTP, line_content_replaced_RXB, line_content_replaced_OTH] if x != []), [])
                                write_lines(line_content, line_content_replaced)
                            # ===================== DEVC ===========================
                            elif valid_line_function_name == 'DEVC':
                                # door or window open time 
                                line_content_replaced_DWT_DEVC=replace_DWT_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # XB
                                line_content_replaced_RXB=replace_RXB_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # OTHERS
                                line_content_replaced_OTH=replace_OTH_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # write into the input file
                                line_content_replaced=next((x for x in [line_content_replaced_DWT_DEVC, line_content_replaced_RXB, line_content_replaced_OTH] if x != []), [])
                                write_lines(line_content, line_content_replaced)
                            # ===================== HOLE ===========================
                            elif valid_line_function_name == 'HOLE':
                                # door or window open time 
                                line_content_replaced_DWT_OBST=replace_DWT_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # XB
                                line_content_replaced_RXB=replace_RXB_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # OTHERS
                                line_content_replaced_OTH=replace_OTH_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # write into the input file
                                line_content_replaced=next((x for x in [line_content_replaced_RXB, line_content_replaced_OTH, line_content_replaced_DWT_OBST] if x != []), [])
                                write_lines(line_content, line_content_replaced)
                            # ===================== SURF ===========================
                            elif valid_line_function_name == 'SURF':
                                # XB
                                line_content_replaced_FHRC=replace_HRC_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # OTHERS
                                line_content_replaced_OTH=replace_OTH_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # write into the input file
                                line_content_replaced=next((x for x in [line_content_replaced_FHRC, line_content_replaced_OTH] if x != []), [])
                                write_lines(line_content, line_content_replaced)
                            # ===================== OTHERS ===========================
                            else:
                                # OTHERS
                                line_content_replaced_OTH=replace_OTH_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs)
                                # write into the input file
                                line_content_replaced=next((x for x in [line_content_replaced_OTH] if x != []), [])
                                write_lines(line_content, line_content_replaced)
                    else:
                        write_lines(line_content, line_content_replaced)
                else:
                    write_lines(line_content, line_content_replaced)

    return file


# determine the index of parameter_outputs
def find_pra_index(parameter_ID_name, target_arg_name):
    for pra_index, ID_name in enumerate(parameter_ID_name):
        if isinstance(ID_name, list):
           if target_arg_name in ID_name:
               return pra_index
        else:
            if target_arg_name == ID_name:
                return pra_index
     
# fire source location
def replace_FSL_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs):
    # collect the fire source location ID namelist
    parameters_list=parameter_outputs['FSL']
    parameter_ID_name=[]
    identify_arg_name=['ID']
    for parameter in parameters_list:
        parameter_ID_name.append(parameter.ID)
    line_content_replaced=[]
    # find the exact position for replacement 
    if any(args in identify_arg_name for args in valid_line_args):
        arg_name_index=next((index for index, surf_name in enumerate(identify_arg_name) if surf_name in valid_line_args),None)
        if valid_line_args[identify_arg_name[arg_name_index]] in parameter_ID_name:
            pra_index=find_pra_index(parameter_ID_name, valid_line_args[identify_arg_name[arg_name_index]])
            if valid_line_function_name == 'OBST':
                # write sampled fire source location coordinates
                coordinate_x_0=parameters_list[pra_index].SAMPLES[0][case_num]
                coordinate_x_1=coordinate_x_0+parameters_list[pra_index].FIRE_BURNER_SIZE[0]
                coordinate_y_0=parameters_list[pra_index].SAMPLES[1][case_num]
                coordinate_y_1=coordinate_y_0+parameters_list[pra_index].FIRE_BURNER_SIZE[1]
                coordinate_z_0=parameters_list[pra_index].SAMPLES[2][case_num]
                coordinate_z_1=coordinate_z_0+parameters_list[pra_index].FIRE_BURNER_SIZE[2]
                coordinate_FSL=[coordinate_x_0,coordinate_x_1,coordinate_y_0,coordinate_y_1,coordinate_z_0,coordinate_z_1]
                # replace at certain position
                function_name, args = PS.parse_script_lines(line_content) 
                if 'XB' in args:
                    index=next((index for index, parm_name in enumerate(args) if parm_name == 'XB'),None)
                    if index+1 == len(args):
                        replaced_after_args=None
                    else:
                        replaced_after_args=list(args)[index+1]
                    line_content_replaced=[PS.replace_value(line_content, replaced_args='XB', replaced_after_args=replaced_after_args, replaced_value=coordinate_FSL)]
        
    return line_content_replaced
            
            
# Vent position
def replace_VTP_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs):
    # collect the fire source location ID namelist
    parameters_list=parameter_outputs['VTP']
    parameter_ID_name=[]
    identify_arg_name=['ID']
    for parameter in parameters_list:
        parameter_ID_name.append(parameter.ID)
    line_content_replaced=[]
    # find the exact position for replacement 
    if any(args in identify_arg_name for args in valid_line_args):
        arg_name_index=next((index for index, surf_name in enumerate(identify_arg_name) if surf_name in valid_line_args),None)
        if valid_line_args[identify_arg_name[arg_name_index]] in parameter_ID_name:
            pra_index=find_pra_index(parameter_ID_name, valid_line_args[identify_arg_name[arg_name_index]])
            if valid_line_function_name == 'VENT':
                # write sampled vent position coordinates
                if parameters_list[pra_index].PLANE== 'X':
                    vent_size=[0, parameters_list[pra_index].VENT_SIZE[0], parameters_list[pra_index].VENT_SIZE[1]]
                if parameters_list[pra_index].PLANE== 'Y':
                    vent_size=[parameters_list[pra_index].VENT_SIZE[0], 0, parameters_list[pra_index].VENT_SIZE[1]]
                if parameters_list[pra_index].PLANE== 'Z':
                    vent_size=[parameters_list[pra_index].VENT_SIZE[0], parameters_list[pra_index].VENT_SIZE[1], 0]
                coordinate_x_0=parameters_list[pra_index].SAMPLES[0][case_num]
                coordinate_x_1=coordinate_x_0+vent_size[0]
                coordinate_y_0=parameters_list[pra_index].SAMPLES[1][case_num]
                coordinate_y_1=coordinate_y_0+vent_size[1]
                coordinate_z_0=parameters_list[pra_index].SAMPLES[2][case_num]
                coordinate_z_1=coordinate_z_0+vent_size[2]
                coordinate_VTP=[coordinate_x_0,coordinate_x_1,coordinate_y_0,coordinate_y_1,coordinate_z_0,coordinate_z_1]
                # replace at certain position
                function_name, args = PS.parse_script_lines(line_content) 
                if 'XB' in args:
                    index=next((index for index, parm_name in enumerate(args) if parm_name == 'XB'),None)
                    if index+1 == len(args):
                        replaced_after_args=None
                    else:
                        replaced_after_args=list(args)[index+1]
                    line_content_replaced=[PS.replace_value(line_content, replaced_args='XB', replaced_after_args=replaced_after_args, replaced_value=coordinate_VTP)]
                
    return line_content_replaced


# door window open time
def replace_DWT_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs):
    # collect the door window open time ID namelist
    parameters_list=parameter_outputs['DWT']
    parameter_ID_name=[]
    parameter_OBST_ID_name=[]
    parameter_DEVC_ID_name=[]
    identify_arg_name=['ID']
    for parameter in parameters_list:
        parameter_ID_name.append(parameter.ID)
    for parameter in parameters_list:
        parameter_OBST_ID_name.append(parameter.OBST_ID)
    for parameter in parameters_list:
        parameter_DEVC_ID_name.append(parameter.DEVC_ID)
    line_content_replaced=[]
    # find the exact position for replacement - OBST and DEVC
    if any(args in identify_arg_name for args in valid_line_args):
        arg_name_index=next((index for index, surf_name in enumerate(identify_arg_name) if surf_name in valid_line_args),None)
        target_arg_name=valid_line_args[identify_arg_name[arg_name_index]]
        if any(target_arg_name == ID_name for ID_name in parameter_ID_name) or \
            any(target_arg_name == i for OBST_ID_name in parameter_OBST_ID_name for i in OBST_ID_name) or \
            any(target_arg_name == j for DEVC_ID_name in parameter_DEVC_ID_name for j in DEVC_ID_name):
            # write sampled door or window open time information- OBST
            if valid_line_function_name == 'OBST' or valid_line_function_name == 'HOLE':
                pra_index=find_pra_index(parameter_OBST_ID_name, target_arg_name)
                OBST_ID_index = next((index for index, parm_value in enumerate(parameters_list[pra_index].OBST_ID) if parm_value == target_arg_name),None)
                function_name, args = PS.parse_script_lines(line_content) 
                if ('XB' in args) or ('DEVC_ID' in args):
                    # replace XB
                    if 'XB' in args:
                        index=next((index for index, parm_name in enumerate(args) if parm_name == 'XB'),None)
                        if index+1 == len(args):
                            replaced_after_args=None
                        else:
                            replaced_after_args=list(args)[index+1]  
                        line_content_replaced_XB=PS.replace_value(line_content, replaced_args='XB', replaced_after_args=replaced_after_args, replaced_value=parameters_list[pra_index].XB[OBST_ID_index])
                    else:
                        line_content_replaced_XB=line_content
                    # replace DEVC_ID
                    if 'DEVC_ID' in args:
                        index=next((index for index, parm_name in enumerate(args) if parm_name == 'DEVC_ID'),None)
                        if index+1 == len(args):
                            replaced_after_args=None
                        else:
                            replaced_after_args=list(args)[index+1]
                        line_content_replaced_DEVC_ID=PS.replace_value(line_content_replaced_XB, replaced_args='DEVC_ID', replaced_after_args=replaced_after_args, replaced_value=[parameters_list[pra_index].DEVC_ID[OBST_ID_index]])
                        line_content_replaced=[line_content_replaced_DEVC_ID]
                    else:
                        line_content_replaced=[line_content_replaced_XB]
                
            # write sampled door or window open time information- DEVC
            if valid_line_function_name == 'DEVC':
                pra_index=find_pra_index(parameter_DEVC_ID_name, target_arg_name)
                DEVC_ID_index = next((index for index, parm_value in enumerate(parameters_list[pra_index].DEVC_ID) if parm_value == target_arg_name),None)
                function_name, args = PS.parse_script_lines(line_content) 
                if ('QUANTITY' in args) or ('SETPOINT' in args):
                    # replace XB
                    if 'QUANTITY' in args:
                        index=next((index for index, parm_name in enumerate(args) if parm_name == 'QUANTITY'),None)
                        if index+1 == len(args):
                            replaced_after_args=None
                        else:
                            replaced_after_args=list(args)[index+1]  
                        line_content_replaced_QUAN=PS.replace_value(line_content, replaced_args='QUANTITY', replaced_after_args=replaced_after_args, replaced_value=[parameters_list[pra_index].QUANTITY_NAME])
                    else:
                        line_content_replaced_QUAN=line_content
                    # replace DEVC_ID
                    if 'SETPOINT' in args:
                        index=next((index for index, parm_name in enumerate(args) if parm_name == 'SETPOINT'),None)
                        if index+1 == len(args):
                            replaced_after_args=None
                        else:
                            replaced_after_args=list(args)[index+1]
                        line_content_replaced_SETP=PS.replace_value(line_content_replaced_QUAN, replaced_args='SETPOINT', replaced_after_args=replaced_after_args, replaced_value=[parameters_list[pra_index].SAMPLES[DEVC_ID_index][case_num]])
                        line_content_replaced=[line_content_replaced_SETP]
                    else:
                        line_content_replaced=[line_content_replaced_QUAN]
                                    
    return line_content_replaced        


# obstruction position
def replace_RXB_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs):
    # collect the fire source location ID namelist
    parameters_list=parameter_outputs['RXB']
    parameter_ID_name=[]
    identify_arg_name=['ID']
    for parameter in parameters_list:
        parameter_ID_name.append(parameter.ID)
    line_content_replaced=[]
    # find the exact position for replacement 
    if any(args in identify_arg_name for args in valid_line_args):
        arg_name_index=next((index for index, surf_name in enumerate(identify_arg_name) if surf_name in valid_line_args),None)
        if valid_line_args[identify_arg_name[arg_name_index]] in parameter_ID_name:
            pra_index=find_pra_index(parameter_ID_name, valid_line_args[identify_arg_name[arg_name_index]])
            if valid_line_function_name == parameters_list[pra_index].NAMELIST:
                # write sampled random XB coordinates
                initial_point=parameters_list[pra_index].INITIAL_POINT
                coordinate_x_0=initial_point[0]
                coordinate_x_1=initial_point[0]+parameters_list[pra_index].SAMPLES[0][case_num]
                coordinate_y_0=initial_point[1]
                coordinate_y_1=initial_point[1]+parameters_list[pra_index].SAMPLES[1][case_num]
                coordinate_z_0=initial_point[2]
                coordinate_z_1=initial_point[2]+parameters_list[pra_index].SAMPLES[2][case_num]
                coordinate_OBS=[coordinate_x_0,coordinate_x_1,coordinate_y_0,coordinate_y_1,coordinate_z_0,coordinate_z_1]
                # replace at certain position
                function_name, args = PS.parse_script_lines(line_content) 
                if 'XB' in args:
                    index=next((index for index, parm_name in enumerate(args) if parm_name == 'XB'),None)
                    if index+1 == len(args):
                        replaced_after_args=None
                    else:
                        replaced_after_args=list(args)[index+1]
                    line_content_replaced=[PS.replace_value(line_content, replaced_args='XB', replaced_after_args=replaced_after_args, replaced_value=coordinate_OBS)]
        
    return line_content_replaced


# other information
def replace_OTH_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs):
    # collect the fire source location ID namelist
    parameters_list=parameter_outputs['OTH']
    parameter_ID_name=[]
    identify_arg_name=['ID']
    for parameter in parameters_list:
        parameter_ID_name.append(parameter.ID)
    line_content_replaced=[]
    # find the exact position for replacement 
    if any(args in identify_arg_name for args in valid_line_args):
        arg_name_index=next((index for index, surf_name in enumerate(identify_arg_name) if surf_name in valid_line_args),None)
        if valid_line_args[identify_arg_name[arg_name_index]] in parameter_ID_name:
            pra_index=find_pra_index(parameter_ID_name, valid_line_args[identify_arg_name[arg_name_index]])
            if valid_line_function_name == parameters_list[pra_index].NAMELIST:
                # write sampled other coordinates
                arg_name=parameters_list[pra_index].ARG_NAME
                # replace at certain position
                function_name, args = PS.parse_script_lines(line_content) 
                if arg_name in args:
                    index=next((index for index, parm_name in enumerate(args) if parm_name == arg_name),None)
                    if index+1 == len(args):
                        replaced_after_args=None
                    else:
                        replaced_after_args=list(args)[index+1]
                    line_content_replaced=[PS.replace_value(line_content, replaced_args=arg_name, replaced_after_args=replaced_after_args, replaced_value=[parameters_list[pra_index].SAMPLES[0][case_num]])]   

    return line_content_replaced


# other information
def replace_HRC_value(case_num, line_content, valid_line_function_name, valid_line_args, parameter_outputs):
    # collect the fire source location ID namelist
    parameters_list=parameter_outputs['HRC']
    parameter_ID_name=[]
    identify_arg_name=['ID']
    for parameter in parameters_list:
        parameter_ID_name.append(parameter.ID)
    line_content_replaced=[]
    # find the exact position for replacement 
    if any(args in identify_arg_name for args in valid_line_args):
        arg_name_index=next((index for index, surf_name in enumerate(identify_arg_name) if surf_name in valid_line_args),None)
        if valid_line_args[identify_arg_name[arg_name_index]] in parameter_ID_name:
            pra_index=find_pra_index(parameter_ID_name, valid_line_args[identify_arg_name[arg_name_index]])
            if valid_line_function_name == 'SURF':
                # write HRRPUA and RAMP_Q
                time_samples=parameters_list[pra_index].TIME_SLICE_SAMPLES
                hrr_samples=parameters_list[pra_index].HRR_SAMPLES
                hrrpua=max(hrr_samples[case_num])
                # replace at certain position
                function_name, args = PS.parse_script_lines(line_content) 
                # HRRPUA and RAMPS_Q
                if ('HRRPUA' in args) or ('RAMP_Q' in args):
                    if 'HRRPUA' in args:
                        index=next((index for index, parm_name in enumerate(args) if parm_name == 'HRRPUA'),None)
                        if index+1 == len(args):
                            replaced_after_args=None
                        else:
                            replaced_after_args=list(args)[index+1]
                        line_content_replaced_HRRPUA=PS.replace_value(line_content, replaced_args='HRRPUA', replaced_after_args=replaced_after_args, replaced_value=[hrrpua])
                    else:
                        line_content_replaced_HRRPUA=line_content
                    if 'RAMP_Q' in args:
                        index=next((index for index, parm_name in enumerate(args) if parm_name == 'RAMP_Q'),None)
                        if index+1 == len(args):
                            replaced_after_args=None
                        else:
                            replaced_after_args=list(args)[index+1]
                        line_content_replaced_RAMP=PS.replace_value(line_content_replaced_HRRPUA, replaced_args='RAMP_Q', replaced_after_args=replaced_after_args, replaced_value=[parameters_list[pra_index].ID+'_fireramp'])
                        line_content_replaced.append(line_content_replaced_RAMP)
                        line_content_replaced.append('\n')
                        # FIRERAMPS
                        T_value=time_samples[case_num]
                        F_value=hrr_samples[case_num]/hrrpua
                        for i in range(len(T_value)):
                            line_content_replaced_RAMP_value='&RAMP ID='+"'"+str(parameters_list[pra_index].ID)+'_fireramp'+"'"+', T='+str(T_value[i])+', F='+str(F_value[i])+' /'
                            line_content_replaced.append(line_content_replaced_RAMP_value)
                    else:
                        line_content_replaced=[line_content_replaced_HRRPUA]
                
    return line_content_replaced
