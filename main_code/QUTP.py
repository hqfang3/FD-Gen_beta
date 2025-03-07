# import library
import os
import pandas as pd

"Part 1: print parameter brief information."
def PRINT_PARAMETER_BRIEF_INFO(PARAMETERS_OUTPUT, parameter_file_path, parameter_brief_name):
    parameter_outputs=PARAMETERS_OUTPUT
    os.chdir(parameter_file_path)
    
    with open(parameter_brief_name, 'w') as file:
    
        file.write('=================================================\n')
        file.write('==========  Fire source location (FSL) ==========\n')
        if parameter_outputs['FSL'] != []:
            for number, i in enumerate(parameter_outputs['FSL']):
                file.write('FSL No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('=============  Vent position (VTP) ==============\n')
        if parameter_outputs['VTP'] != []:
            for number, i in enumerate(parameter_outputs['VTP']):
                file.write('VTP No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('=====  Door and window open time (DWT) ==========\n')
        if parameter_outputs['DWT'] != []:
            for number, i in enumerate(parameter_outputs['DWT']):
                file.write('DWT No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('==========  Obstruction position (RXB) ==========\n')
        if parameter_outputs['RXB'] != []:
            for number, i in enumerate(parameter_outputs['RXB']):
                file.write('RXB No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('==========  Other information (OTH) =============\n')
        if parameter_outputs['OTH'] != []:
            for number, i in enumerate(parameter_outputs['OTH']):
                file.write('OTH No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('==========  Fire time duration (FTD) ============\n')
        if parameter_outputs['FTD'] != []:
            for number, i in enumerate(parameter_outputs['FTD']):
                file.write('FTD No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('==========  Fire time duration (MHR) ============\n')
        if parameter_outputs['MHR'] != []:
            for number, i in enumerate(parameter_outputs['MHR']):
                file.write('MHR No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('===============  HRR curve (HRC) ================\n')
        if parameter_outputs['HRC'] != []:
            for number, i in enumerate(parameter_outputs['HRC']):
                file.write('HRC No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
    
    return file
    


"Part 2: print generator information."
def PRINT_GENERATOR_INFO(PARAMETER_SAMPLE_GENERATOR_OUTPUTS, parameter_file_path, generator_info_name):
    parameter_sample_generator_outputs=PARAMETER_SAMPLE_GENERATOR_OUTPUTS
    os.chdir(parameter_file_path)
    
    with open(generator_info_name, 'w') as file:
        file.write('=================================================\n')
        file.write('==========  Fire source location (FSL) ==========\n')
        if parameter_sample_generator_outputs['FSL'] != []:
            for number, i in enumerate(parameter_sample_generator_outputs['FSL']):
                file.write('FSL No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('=============  Vent position (VTP) ==============\n')
        if parameter_sample_generator_outputs['VTP'] != []:
            for number, i in enumerate(parameter_sample_generator_outputs['VTP']):
                file.write('VTP No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('=====  Door and window open time (DWT) ==========\n')
        if parameter_sample_generator_outputs['DWT'] != []:
            for number, i in enumerate(parameter_sample_generator_outputs['DWT']):
                file.write('DWT No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('==========  Obstruction position (RXB) ==========\n')
        if parameter_sample_generator_outputs['RXB'] != []:
            for number, i in enumerate(parameter_sample_generator_outputs['RXB']):
                file.write('RXB No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('==========  Other information (OTH) =============\n')
        if parameter_sample_generator_outputs['OTH'] != []:
            for number, i in enumerate(parameter_sample_generator_outputs['OTH']):
                file.write('OTH No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('==========  Fire time duration (FTD) ============\n')
        if parameter_sample_generator_outputs['FTD'] != []:
            for number, i in enumerate(parameter_sample_generator_outputs['FTD']):
                file.write('FTD No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        
        file.write('=================================================\n')
        file.write('=================  MAX HRR (MHR) ================\n')
        if parameter_sample_generator_outputs['MHR'] != []:
            for number, i in enumerate(parameter_sample_generator_outputs['MHR']):
                file.write('MHR No.' + str(number+1)+'\n')
                file.write(str(i)+'\n')
        else:
            file.write('No parameter sampled.\n')
        file.write('=================================================\n')
        file.write('\n')
        


"Part 3: print parameter spreadsheet."
def PRINT_PARAMETER_SPREADSHEET(number_of_case, PARAMETERS_OUTPUT, parameter_file_path, parameter_spreadsheet_name):
    parameter_outputs=PARAMETERS_OUTPUT
    os.chdir(parameter_file_path)
    
    C_cases=list(range(number_of_case))
    spreadsheet_data = {'Cases': C_cases}
    # FSL spreadsheet
    if parameter_outputs['FSL'] != []:
        for number, data_dic in enumerate(parameter_outputs['FSL']):
            name='<FSL> OBST_ID -   ' + data_dic.ID
            FSL_data=[]
            for case_num in range(number_of_case):
                # write sampled fire source location coordinates
                coordinate_x_0=data_dic.SAMPLES[0][case_num]
                coordinate_x_1=coordinate_x_0+data_dic.FIRE_BURNER_SIZE[0]
                coordinate_y_0=data_dic.SAMPLES[1][case_num]
                coordinate_y_1=coordinate_y_0+data_dic.FIRE_BURNER_SIZE[1]
                coordinate_z_0=data_dic.SAMPLES[2][case_num]
                coordinate_z_1=coordinate_z_0+data_dic.FIRE_BURNER_SIZE[2]
                coordinate_FSL=[coordinate_x_0,coordinate_x_1,coordinate_y_0,coordinate_y_1,coordinate_z_0,coordinate_z_1]
                FSL_data.append(coordinate_FSL)
            spreadsheet_data.update({name:FSL_data})
    
    # VTP spreadsheet
    if parameter_outputs['VTP'] != []:
        for number, data_dic in enumerate(parameter_outputs['VTP']):
            name='<VTP> VENT_ID - ' + data_dic.ID
            VTP_data=[]
            for case_num in range(number_of_case):
                # write sampled vent position coordinates
                if data_dic.PLANE== 'X':
                    vent_size=[0, data_dic.VENT_SIZE[0], data_dic.VENT_SIZE[1]]
                if data_dic.PLANE== 'Y':
                    vent_size=[data_dic.VENT_SIZE[0], 0, data_dic.VENT_SIZE[1]]
                if data_dic.PLANE== 'Z':
                    vent_size=[data_dic.VENT_SIZE[0], data_dic.VENT_SIZE[1], 0]
                coordinate_x_0=data_dic.SAMPLES[0][case_num]
                coordinate_x_1=coordinate_x_0+vent_size[0]
                coordinate_y_0=data_dic.SAMPLES[1][case_num]
                coordinate_y_1=coordinate_y_0+vent_size[1]
                coordinate_z_0=data_dic.SAMPLES[2][case_num]
                coordinate_z_1=coordinate_z_0+vent_size[2]
                coordinate_VTP=[coordinate_x_0,coordinate_x_1,coordinate_y_0,coordinate_y_1,coordinate_z_0,coordinate_z_1]
                VTP_data.append(coordinate_VTP)
            spreadsheet_data.update({name:VTP_data})
    
    # DWT spreadsheet
    if parameter_outputs['DWT'] != []:
        for number, data_dic in enumerate(parameter_outputs['DWT']):
            name_0='<DWT> OBST_ID - ' + '_'.join(map(str, data_dic.OBST_ID))
            name_1='<DWT> DEVC_ID - ' + '_'.join(map(str, data_dic.DEVC_ID))
            DWT_data_0=[]
            DWT_data_1=[]
            for case_num in range(number_of_case):
                # write sampled door window open time
                XB_coordinate=data_dic.XB
                timer_DWT=[]
                for index in range(len(data_dic.DEVC_ID)):
                    timer=data_dic.SAMPLES[index][case_num]
                    timer_DWT.append(timer)
                DWT_data_0.append(XB_coordinate)
                DWT_data_1.append(timer_DWT) 
            spreadsheet_data.update({name_0:DWT_data_0})
            spreadsheet_data.update({name_1:DWT_data_1})
    
    # RXB spreadsheet
    if parameter_outputs['RXB'] != []:
        for number, data_dic in enumerate(parameter_outputs['RXB']):
            name='<RXB> OBST_ID - ' + data_dic.ID
            RXB_data=[]
            for case_num in range(number_of_case):
                # write sampled random XB coordinates
                initial_point=data_dic.INITIAL_POINT
                coordinate_x_0=initial_point[0]
                coordinate_x_1=initial_point[0]+data_dic.SAMPLES[0][case_num]
                coordinate_y_0=initial_point[1]
                coordinate_y_1=initial_point[1]+data_dic.SAMPLES[1][case_num]
                coordinate_z_0=initial_point[2]
                coordinate_z_1=initial_point[2]+data_dic.SAMPLES[2][case_num]
                coordinate_RXB=[coordinate_x_0,coordinate_x_1,coordinate_y_0,coordinate_y_1,coordinate_z_0,coordinate_z_1]
                RXB_data.append(coordinate_RXB)
            spreadsheet_data.update({name:RXB_data})
    
    # OTH spreadsheet
    if parameter_outputs['OTH'] != []:
        for number, data_dic in enumerate(parameter_outputs['OTH']):
            name='<OTH> ID - ' + data_dic.ID
            OTH_data=[]
            for case_num in range(number_of_case):
                # write OTH information
                other_value=data_dic.SAMPLES[0][case_num]
                OTH_data.append(other_value)
            spreadsheet_data.update({name:OTH_data})
    
    # FTD spreadsheet
    if parameter_outputs['FTD'] != []:
        for number, data_dic in enumerate(parameter_outputs['FTD']):
            name0='<FTD> ID - ' + data_dic.ID + ' .Incipient'
            FTD_incipient=[]
            name1='<FTD> ID - ' + data_dic.ID + ' .Growth'
            FTD_growth=[]
            name2='<FTD> ID - ' + data_dic.ID + ' .Peak'
            FTD_peak=[]
            name3='<FTD> ID - ' + data_dic.ID + ' .Decay'
            FTD_decay=[]
            for case_num in range(number_of_case):
                FTD_incipient.append(data_dic.SAMPLES[0][case_num])
                FTD_growth.append(data_dic.SAMPLES[1][case_num])
                FTD_peak.append(data_dic.SAMPLES[2][case_num])
                FTD_decay.append(data_dic.SAMPLES[3][case_num])
            spreadsheet_data.update({name0:FTD_incipient})
            spreadsheet_data.update({name1:FTD_growth})
            spreadsheet_data.update({name2:FTD_peak})
            spreadsheet_data.update({name3:FTD_decay})
            
    # FTD spreadsheet
    if parameter_outputs['MHR'] != []:
        for number, data_dic in enumerate(parameter_outputs['MHR']):
            name0='<MHR> ID - ' + data_dic.ID + ' .Incipient'
            MHR_incipient=[]
            name1='<MHR> ID - ' + data_dic.ID + ' .Peak'
            MHR_peak=[]
            name2='<MHR> ID - ' + data_dic.ID + ' .Decay'
            MHR_decay=[]
            for case_num in range(number_of_case):
                MHR_incipient.append(data_dic.SAMPLES[0][case_num])
                MHR_peak.append(data_dic.SAMPLES[1][case_num])
                MHR_decay.append(data_dic.SAMPLES[2][case_num])
            spreadsheet_data.update({name0:MHR_incipient})
            spreadsheet_data.update({name1:MHR_peak})
            spreadsheet_data.update({name2:MHR_decay})
    
    # HRC spreadsheet
    if parameter_outputs['HRC'] != []:
        for number, data_dic in enumerate(parameter_outputs['HRC']):
            name0='<HRC> ID - ' + data_dic.ID + ' .Fire time duration'
            HRC_fire_time_duration=[]
            name1='<HRC> ID - ' + data_dic.ID + ' .HRR samples'
            HRC_hrr_samples=[]
            for case_num in range(number_of_case):
                HRC_fire_time_duration.append(data_dic.TIME_SLICE_SAMPLES[case_num])
                HRC_hrr_samples.append(data_dic.HRR_SAMPLES[case_num])
            spreadsheet_data.update({name0:HRC_fire_time_duration})
            spreadsheet_data.update({name1:HRC_hrr_samples})
            
    # Create a DataFrame from the data
    df = pd.DataFrame(spreadsheet_data)

    # Write the DataFrame to an Excel file
    output_file = parameter_spreadsheet_name
    df.to_excel(output_file, index=False)
    
    
    return

    
    
    