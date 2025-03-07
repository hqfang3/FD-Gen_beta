# import toolkits
import numpy as np
from MRND import *
from global_parm import *
import itertools

"Part 1: To generate field parameter - FIRE SOURCE LOCATION"
# define the class of parameters FIRE_ROOM
class FIRE_SOURCE_LOCATION_DICT:
    def __init__(self, FIRE_SOURCE_LOCATION_INFO):
        if len(FIRE_SOURCE_LOCATION_INFO) == 13:
            fire_source_location_info=FIRE_SOURCE_LOCATION_INFO
            self.ID=fire_source_location_info[0]
            self.GENERATOR_ID=fire_source_location_info[1]
            self.FYI=fire_source_location_info[2]
            self.XB=fire_source_location_info[3]
            self.FIRE_BURNER_SIZE=fire_source_location_info[4]
            self.MODIFIED_ROOM_COORDINATES=fire_source_location_info[5]
            self.MESH_SIZE=fire_source_location_info[6]
            self.RANDOM_SEEDS=fire_source_location_info[7]
            self.SHUFFLE_STATES=fire_source_location_info[8]
            self.SHUFFLE_RANDOM_SEEDS=fire_source_location_info[9]
            self.NUMBER_OF_SAMPLES=fire_source_location_info[10]
            self.SAMPLES=fire_source_location_info[11]
            self.PRODUCT=fire_source_location_info[12]
        else:
            raise ValueError(f"FIRE_SOURCE_LOCATION_INFO for ID '{self.ID}' must contain at least 13 elements.")
    
    def to_list(self):
        return [self.ID, self.GENERATOR_ID, self.FYI, self.XB, self.FIRE_BURNER_SIZE, self.MODIFIED_ROOM_COORDINATES, self.MESH_SIZE, self.RANDOM_SEEDS, self.SHUFFLE_STATES, self.SHUFFLE_RANDOM_SEEDS, self.NUMBER_OF_SAMPLES, self.SAMPLES, self.PRODUCT]
    
    def to_dict(self):
        return  self.__dict__
    
    def __str__(self):
        result = ""
        room_size = self.XB
        if room_size == 'N/A':
            room_length = 'N/A'
            room_width = 'N/A'
            room_height = 'N/A'
        else:
            room_length = room_size[1] - room_size[0]
            room_width = room_size[3] - room_size[2]
            room_height = room_size[5] - room_size[4]
        result += (f"ID: {self.ID} \n"
                    f"Generator ID: {self.GENERATOR_ID} \n"
                    f"FYI: {self.FYI} \n"
                    f"Room Length: {room_length} m,\n"
                    f"Room Width: {room_width} m,\n"
                    f"Room Height: {room_height} m,\n"
                    f"Burner size: {self.FIRE_BURNER_SIZE} m,\n"
                    f"Random Seeds: {self.RANDOM_SEEDS}, \n"
                    f"Shuffle State: {self.SHUFFLE_STATES}, \n"
                    f"Shuffle Random Seeds: {self.SHUFFLE_RANDOM_SEEDS}, \n"
                    f"Number of Samples: {self.NUMBER_OF_SAMPLES}, \n"
                    f"Fire Source Location Samples: {self.SAMPLES} "
                    )
        return result


# input fire source location information
def INPUT_FIRE_SOURCE_LOCATION_INFO(PRE_PARM_INFO_ID, XB, FIRE_BURNER_SIZE, FYI=None, MESH_SIZE=[None,None,None]):
    
    # default_variable
    GENERATOR_ID=[]
    MODIFIED_ROOM_COORDINATES=None
    RANDOM_SEEDS=[]
    SHUFFLE_STATES=[]
    SHUFFLE_RANDOM_SEEDS=[]
    NUMBER_OF_SAMPLES=[]
    SAMPLES=[]
    PRODUCT=None
    
    # request the format of the input
    if len(XB) == 6 and len(FIRE_BURNER_SIZE) == 3:
        fire_source_location_info=[PRE_PARM_INFO_ID, GENERATOR_ID, FYI, XB, FIRE_BURNER_SIZE, MODIFIED_ROOM_COORDINATES, MESH_SIZE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        # extract information
        id=fire_source_location_info[0]
        room_coordinates=fire_source_location_info[3]
        fire_burner_size=fire_source_location_info[4]
        modified_room_coordinates=fire_source_location_info[5]
        mesh_size=fire_source_location_info[6]
        
        # decode MODIFIED_ROOM_COORDINATES: adjust the sampling room area excluding fire burner size
        if modified_room_coordinates is None:
            modified_room_coordinates=room_coordinates.copy()
            modified_room_coordinates[1] = room_coordinates[1]-fire_burner_size[0] # maximum X direction
            modified_room_coordinates[3] = room_coordinates[3]-fire_burner_size[1] # maximum Y direction
            modified_room_coordinates[5] = room_coordinates[5]-fire_burner_size[2] # maximum Z direction
            fire_source_location_info[5] = modified_room_coordinates
        
        # decode MESH_SIZE
        if mesh_size is not [None, None, None]:
            value_type_FSL_X = "APPROX" if mesh_size[0] is not None else None
            approx_value_FSL_X = mesh_size[0] if mesh_size[0] is not None else None

            value_type_FSL_Y = "APPROX" if mesh_size[1] is not None else None
            approx_value_FSL_Y = mesh_size[1] if mesh_size[1] is not None else None

            value_type_FSL_Z = "APPROX" if mesh_size[2] is not None else None
            approx_value_FSL_Z = mesh_size[2] if mesh_size[2] is not None else None
        else:
            value_type_FSL_X = None
            approx_value_FSL_X = None
            value_type_FSL_Y = None
            approx_value_FSL_Y = None
            value_type_FSL_Z = None
            approx_value_FSL_Z = None
        
        # output sample generator information
        fire_source_location={id:fire_source_location_info}
        sample_generator_pre_info_FSL_X=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_X', MINIMUM=modified_room_coordinates[0], MAXIMUM=modified_room_coordinates[1], VALUE_TYPE=value_type_FSL_X, APPROX_VALUE=approx_value_FSL_X)
        sample_generator_pre_info_FSL_Y=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_Y', MINIMUM=modified_room_coordinates[2], MAXIMUM=modified_room_coordinates[3], VALUE_TYPE=value_type_FSL_Y, APPROX_VALUE=approx_value_FSL_Y)
        sample_generator_pre_info_FSL_Z=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_Z', MINIMUM=modified_room_coordinates[4], MAXIMUM=modified_room_coordinates[5], VALUE_TYPE=value_type_FSL_Z, APPROX_VALUE=approx_value_FSL_Z)
        
    else:
        raise ValueError("The input format of the fire source location information is wrong.")
    
    return fire_source_location, sample_generator_pre_info_FSL_X, sample_generator_pre_info_FSL_Y, sample_generator_pre_info_FSL_Z


def GENERATING_FIRE_SOURCE_LOCATION_SAMPLES(ID, GENERATOR_ID, PARAMETER_PRE_OUTPUTS_INFO, PARAMETER_SAMPLE_GENERATOR_INFO, PRE_PARM_INFO_ID=None, PRODUCT=False, FYI=None):
    # extract the data from parameter dictionary
    id=ID
    if isinstance(GENERATOR_ID, list):
        generator_id=GENERATOR_ID
    else:
        generator_id=[GENERATOR_ID]
    if len(generator_id)!=3:
        raise ValueError(f"GENERATOR_ID for GFSL ID = '{id}' requires 3 ID names.")
    number_of_samples=GET_VALUE("NUMBER_OF_CASES")
    
    para_info_id=PRE_PARM_INFO_ID
    parameter_id_list=[]
    for parameter in PARAMETER_PRE_OUTPUTS_INFO:
        if parameter is not None:
            for key in parameter:
                parameter_id_list.append(parameter[key][0])
    
    # save the parameter 
    fire_source_location_info={}
    for generator_value in PARAMETER_SAMPLE_GENERATOR_INFO:
        for key,value in generator_value.items():
            if key in generator_id:
                fire_source_location_info.update(generator_value)
    sample_generator=GENERATING_SAMPLES(fire_source_location_info)
    
    # product samples
    product_combinations = []
    for _, value in sample_generator.SAMPLES.items():
        if len(value) != number_of_samples:
            product_combinations = [v for v in sample_generator.SAMPLES.values()]
            sample_product_combinations = list(itertools.product(*product_combinations))
            for index, (key, value) in enumerate(sample_generator.SAMPLES.items()):
                generator_product_samples=[]
                for i in range(len(sample_product_combinations)):
                    generator_product_samples.append(sample_product_combinations[i][index])
                sample_generator.SAMPLES[key] = np.array(generator_product_samples)
                sample_generator.NUMBER_OF_SAMPLES[key]=len(generator_product_samples)
            break
    
    # if para_info already exists
    if para_info_id in parameter_id_list:
        # Write the parameter dictionary
        index = [i for i, x in enumerate(parameter_id_list) if x == para_info_id]
        parameter=PARAMETER_PRE_OUTPUTS_INFO[index[-1]]
        GENERATOR_ID=[]
        XB=parameter[para_info_id][3]
        FIRE_BURNER_SIZE=parameter[para_info_id][4]
        MODIFIED_ROOM_COORDINATES=parameter[para_info_id][5]
        MESH_SIZE=parameter[para_info_id][6]
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
            
        fire_source_location_info_dic=[id, GENERATOR_ID, FYI, XB, FIRE_BURNER_SIZE, MODIFIED_ROOM_COORDINATES, MESH_SIZE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        parameter = FIRE_SOURCE_LOCATION_DICT(fire_source_location_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
    
    else:
        # Write the parameter dictionary
        GENERATOR_ID=[]
        XB='N/A'
        FIRE_BURNER_SIZE='N/A'
        MODIFIED_ROOM_COORDINATES='N/A'
        MESH_SIZE='N/A'
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
            
        fire_source_location_info_dic=[id, GENERATOR_ID, FYI, XB, FIRE_BURNER_SIZE, MODIFIED_ROOM_COORDINATES, MESH_SIZE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        parameter = FIRE_SOURCE_LOCATION_DICT(fire_source_location_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
            
    return parameter, sample_generator



"Part 2: To generate field parameter - VENT_POSITION"
# define the class of parameters DOOR_OR_WINDOW_OPEN_TIME
class VENT_POSITION_DICT:
    def __init__(self, VENT_POSITION_INFO):
        if len(VENT_POSITION_INFO) == 13:
            vent_position_info=VENT_POSITION_INFO
            self.ID=vent_position_info[0]
            self.GENERATOR_ID=vent_position_info[1]
            self.FYI=vent_position_info[2]
            self.PLANE=vent_position_info[3]
            self.MOVE_RANGE=vent_position_info[4]
            self.VENT_SIZE=vent_position_info[5]
            self.MESH_SIZE=vent_position_info[6]
            self.RANDOM_SEEDS=vent_position_info[7]
            self.SHUFFLE_STATES=vent_position_info[8]
            self.SHUFFLE_RANDOM_SEEDS=vent_position_info[9]
            self.NUMBER_OF_SAMPLES=vent_position_info[10]
            self.SAMPLES=vent_position_info[11]
            self.PRODUCT=vent_position_info[12]
        else:
            raise ValueError(f"VENT_POSITION_INFO for ID '{self.ID}' must contain at least 11 elements.")
    
    def to_list(self):
        return [self.ID, self.GENERATOR_ID, self.FYI, self.PLANE, self.MOVE_RANGE, self.VENT_SIZE, self.MESH_SIZE, self.RANDOM_SEEDS, self.SHUFFLE_STATES, self.SHUFFLE_RANDOM_SEEDS, self.NUMBER_OF_SAMPLES, self.SAMPLES, self.PRODUCT]
    
    def to_dict(self):
        return  self.__dict__
    
    def __str__(self):
        result = ""
        result += (f"ID: {self.ID} \n"
                   f"Generator ID: {self.GENERATOR_ID}, \n"
                   f"FYI: {self.FYI}, \n"
                   f"Plane: {self.PLANE}, \n"
                   f"Move Range: {self.MOVE_RANGE}, \n"
                   f"Vent Size: {self.VENT_SIZE}, \n"
                   f"Mesh Size: {self.MESH_SIZE}, \n"
                   f"Random Seeds: {self.RANDOM_SEEDS}, \n"
                   f"Shuffle State: {self.SHUFFLE_STATES}, \n"
                   f"Shuffle Random Seeds: {self.SHUFFLE_RANDOM_SEEDS}, \n"
                   f"Number of Samples: {self.NUMBER_OF_SAMPLES}, \n"
                   f"Door and Window Open Time Samples: {self.SAMPLES} "
                   )
        return result
    
    
# input fire source location information
def INPUT_VENT_POSITION_INFO(PRE_PARM_INFO_ID, PLANE, MOVE_RANGE, VENT_SIZE, FYI=None, MESH_SIZE=[None,None,None]):
    
    # default_variable
    GENERATOR_ID=[]
    RANDOM_SEEDS=[]
    SHUFFLE_STATES=[]
    SHUFFLE_RANDOM_SEEDS=[]
    NUMBER_OF_SAMPLES=[]
    SAMPLES=[]
    PRODUCT=None
    
    # request the format of the input
    if len(PLANE) == 1 and len(MOVE_RANGE) == 6 and len(VENT_SIZE) == 2:
        vent_position_info=[PRE_PARM_INFO_ID, GENERATOR_ID, FYI, PLANE, MOVE_RANGE, VENT_SIZE, MESH_SIZE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        # extract information
        id=vent_position_info[0]
        plane=vent_position_info[3]
        move_range=vent_position_info[4]
        vent_size=vent_position_info[5]
        mesh_size=vent_position_info[6]

        
        # adjust the sampling area excluding vent size
        modified_sample_coordinates=[0,0,0,0,0,0]
        if plane == 'X':
            if MOVE_RANGE[0]==MOVE_RANGE[1]:
                modified_sample_coordinates[0] = move_range[0]
                modified_sample_coordinates[1] = move_range[1]
                modified_sample_coordinates[2:]=move_range[2:]
                modified_sample_coordinates[3] = modified_sample_coordinates[3]-VENT_SIZE[0]
                modified_sample_coordinates[5] = modified_sample_coordinates[5]-VENT_SIZE[1]
                if modified_sample_coordinates[2]>modified_sample_coordinates[3]:
                    modified_sample_coordinates[3]=modified_sample_coordinates[2]
                if modified_sample_coordinates[4]>modified_sample_coordinates[5]:
                    modified_sample_coordinates[5]=modified_sample_coordinates[4]
            else:
                raise ValueError(f"MOVE_RANGE remains the same within a plane.")
            
        if plane == 'Y':
            if MOVE_RANGE[2]==MOVE_RANGE[3]:
                modified_sample_coordinates[0:2] = move_range[0:2]
                modified_sample_coordinates[2] = move_range[2]
                modified_sample_coordinates[3] = move_range[3]
                modified_sample_coordinates[4:] = move_range[4:]
                modified_sample_coordinates[1] = modified_sample_coordinates[1]-VENT_SIZE[0]
                modified_sample_coordinates[5] = modified_sample_coordinates[5]-VENT_SIZE[1]
                if modified_sample_coordinates[0]>modified_sample_coordinates[1]:
                    modified_sample_coordinates[1]=modified_sample_coordinates[0]
                if modified_sample_coordinates[4]>modified_sample_coordinates[5]:
                    modified_sample_coordinates[5]=modified_sample_coordinates[4]
            else:
                raise ValueError(f"MOVE_RANGE remains the same within a plane.")
                
        if plane == 'Z':
            if MOVE_RANGE[4]==MOVE_RANGE[5]:
                modified_sample_coordinates[0:4] = move_range[0:4]
                modified_sample_coordinates[4] = move_range[4]
                modified_sample_coordinates[5] = move_range[5]
                modified_sample_coordinates[1] = modified_sample_coordinates[1]-VENT_SIZE[0]
                modified_sample_coordinates[3] = modified_sample_coordinates[3]-VENT_SIZE[1]
                if modified_sample_coordinates[0]>modified_sample_coordinates[1]:
                    modified_sample_coordinates[1]=modified_sample_coordinates[0]
                if modified_sample_coordinates[2]>modified_sample_coordinates[3]:
                    modified_sample_coordinates[3]=modified_sample_coordinates[2]
            else:
                raise ValueError(f"MOVE_RANGE remains the same within a plane.")
        
        # decode MESH_SIZE
        if mesh_size is not [None, None, None]:
            value_type_VP_X = "APPROX" if mesh_size[0] is not None else None
            approx_value_VP_X = mesh_size[0] if mesh_size[0] is not None else None

            value_type_VP_Y = "APPROX" if mesh_size[1] is not None else None
            approx_value_VP_Y = mesh_size[1] if mesh_size[1] is not None else None

            value_type_VP_Z = "APPROX" if mesh_size[2] is not None else None
            approx_value_VP_Z = mesh_size[2] if mesh_size[2] is not None else None
        else:
            value_type_VP_X = None
            approx_value_VP_X = None
            value_type_VP_Y = None
            approx_value_VP_Y = None
            value_type_VP_Z = None
            approx_value_VP_Z = None
        
        # output sample generator information
        vent_position={id:vent_position_info}
        sample_generator_pre_info_VP_X=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_X', MINIMUM=modified_sample_coordinates[0], MAXIMUM=modified_sample_coordinates[1], VALUE_TYPE=value_type_VP_X, APPROX_VALUE=approx_value_VP_X)
        sample_generator_pre_info_VP_Y=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_Y', MINIMUM=modified_sample_coordinates[2], MAXIMUM=modified_sample_coordinates[3], VALUE_TYPE=value_type_VP_Y, APPROX_VALUE=approx_value_VP_Y)
        sample_generator_pre_info_VP_Z=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_Z', MINIMUM=modified_sample_coordinates[4], MAXIMUM=modified_sample_coordinates[5], VALUE_TYPE=value_type_VP_Z, APPROX_VALUE=approx_value_VP_Z)
        
    else:
        raise ValueError("The input format of the vent position information is wrong.")
    
    return vent_position, sample_generator_pre_info_VP_X, sample_generator_pre_info_VP_Y, sample_generator_pre_info_VP_Z
    


def GENERATING_VENT_POSITION_SAMPLES(ID, GENERATOR_ID, PARAMETER_PRE_OUTPUTS_INFO, PARAMETER_SAMPLE_GENERATOR_INFO, PRE_PARM_INFO_ID=None, PRODUCT=False, FYI=None):
    # extract the data from parameter dictionary
    id=ID
    if isinstance(GENERATOR_ID, list):
        generator_id=GENERATOR_ID
    else:
        generator_id=[GENERATOR_ID]
    if len(generator_id)!=3:
        raise ValueError(f"GENERATOR_ID for GVTP ID = '{id}' requires 3 ID names.")
    number_of_samples=GET_VALUE("NUMBER_OF_CASES")
    
    para_info_id=PRE_PARM_INFO_ID
    parameter_id_list=[]
    for parameter in PARAMETER_PRE_OUTPUTS_INFO:
        if parameter is not None:
            for key in parameter:
                parameter_id_list.append(parameter[key][0])
    
    # save the parameter
    vent_position_info={}
    for generator_value in PARAMETER_SAMPLE_GENERATOR_INFO:
        for key,value in generator_value.items():
            if key in generator_id:
                vent_position_info.update(generator_value)
    sample_generator=GENERATING_SAMPLES(vent_position_info)
    
    # product samples
    product_combinations = []
    for _, value in sample_generator.SAMPLES.items():
        if len(value) != number_of_samples:
            product_combinations = [v for v in sample_generator.SAMPLES.values()]
            sample_product_combinations = list(itertools.product(*product_combinations))
            for index, (key, value) in enumerate(sample_generator.SAMPLES.items()):
                generator_product_samples=[]
                for i in range(len(sample_product_combinations)):
                    generator_product_samples.append(sample_product_combinations[i][index])
                sample_generator.SAMPLES[key] = np.array(generator_product_samples)
                sample_generator.NUMBER_OF_SAMPLES[key]=len(generator_product_samples)
            break
    
    # if para_info already exists
    if para_info_id in parameter_id_list:
        # Write the parameter dictionary
        index = [i for i, x in enumerate(parameter_id_list) if x == para_info_id]
        parameter=PARAMETER_PRE_OUTPUTS_INFO[index[-1]]
        GENERATOR_ID=[]
        PLANE=parameter[para_info_id][3]
        MOVE_RANGE=parameter[para_info_id][4]
        VENT_SIZE=parameter[para_info_id][5]
        MESH_SIZE=parameter[para_info_id][6]
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
        vent_position_info_dic=[id, GENERATOR_ID, FYI, PLANE, MOVE_RANGE, VENT_SIZE, MESH_SIZE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        parameter = VENT_POSITION_DICT(vent_position_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
    
    else:
        # Write the parameter dictionary
        GENERATOR_ID=[]
        PLANE='N/A'
        MOVE_RANGE='N/A'
        VENT_SIZE='N/A'
        MESH_SIZE='N/A'
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
        vent_position_info_dic=[id, GENERATOR_ID, FYI, PLANE, MOVE_RANGE, VENT_SIZE, MESH_SIZE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        parameter = VENT_POSITION_DICT(vent_position_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
            
    return parameter, sample_generator
 


"Part 3: To generate field parameter - DOOR_OR_WINDOW_OPEN_TIME"
# define the class of parameters DOOR_OR_WINDOW_OPEN_TIME
class DOOR_OR_WINDOW_OPEN_TIME_DICT:
    def __init__(self, DOOR_OR_WINDOW_OPEN_TIME_INFO):
        if len(DOOR_OR_WINDOW_OPEN_TIME_INFO) == 16:
            door_or_window_open_time_info=DOOR_OR_WINDOW_OPEN_TIME_INFO
            self.ID=door_or_window_open_time_info[0]
            self.GENERATOR_ID=door_or_window_open_time_info[1]
            self.FYI=door_or_window_open_time_info[2]
            self.OBST_ID=door_or_window_open_time_info[3]
            self.XB=door_or_window_open_time_info[4]
            self.OPEN_DIRECTION=door_or_window_open_time_info[5]
            self.QUANTITY_NAME=door_or_window_open_time_info[6]
            self.PORTION=door_or_window_open_time_info[7]
            self.DEVC_ID=door_or_window_open_time_info[8]
            self.DOOR_OR_WINDOW_OPEN_TIME_RANGE=door_or_window_open_time_info[9]
            self.RANDOM_SEEDS=door_or_window_open_time_info[10]
            self.SHUFFLE_STATES=door_or_window_open_time_info[11]
            self.SHUFFLE_RANDOM_SEEDS=door_or_window_open_time_info[12]
            self.NUMBER_OF_SAMPLES=door_or_window_open_time_info[13]
            self.SAMPLES=door_or_window_open_time_info[14]
            self.PRODUCT=door_or_window_open_time_info[15]
        else:
            raise ValueError(f"DOOR_OR_WINDOW_OPEN_TIME_INFO for ID '{self.ID}' must contain at least 14 elements.")
    
    def to_list(self):
        return [self.ID, self.GENERATOR_ID, self.FYI, self.OBST_ID, self.XB, self.OPEN_DIRECTION, self.QUANTITY_NAME, self.PORTION, self.DEVC_ID, self.DOOR_OR_WINDOW_OPEN_TIME_RANGE, self.RANDOM_SEEDS, self.SHUFFLE_STATES, self.SHUFFLE_RANDOM_SEEDS, self.NUMBER_OF_SAMPLES, self.SAMPLES, self.PRODUCT]
    
    def to_dict(self):
        return  self.__dict__
    
    def __str__(self):
        result = ""
        result += (f"ID: {self.ID} \n"
                   f"Generator ID: {self.GENERATOR_ID}, \n"
                   f"FYI: {self.FYI}, \n"
                   f"OBST_ID: {self.OBST_ID}, \n"
                   f"XB: {self.XB}, \n"
                   f"Open direction: {self.OPEN_DIRECTION}, \n"
                   f"Quantity Name: {self.QUANTITY_NAME}, \n"
                   f"Portion: {self.PORTION}, \n"
                   f"Timer ID: {self.DEVC_ID}, \n"
                   f"Door or Window Open Time Range: {self.DOOR_OR_WINDOW_OPEN_TIME_RANGE}, \n"
                   f"Random Seeds: {self.RANDOM_SEEDS}, \n"
                   f"Shuffle State: {self.SHUFFLE_STATES}, \n"
                   f"Shuffle Random Seeds: {self.SHUFFLE_RANDOM_SEEDS}, \n"
                   f"Number of Samples: {self.NUMBER_OF_SAMPLES}, \n"
                   f"Door and Window Open Time Samples: {self.SAMPLES} "
                   )
        return result
    
    
# input fire source location information
def INPUT_DOOR_OR_WINDOW_OPEN_TIME_INFO(PRE_PARM_INFO_ID, OBST_ID, XB, QUANTITY_NAME, DEVC_ID, DOOR_OR_WINDOW_OPEN_TIME_RANGE, OPEN_DIRECTION='X+', PORTION=1, FYI=None):
    
    # default_variable
    GENERATOR_ID=[]
    RANDOM_SEEDS=[]
    SHUFFLE_STATES=[]
    SHUFFLE_RANDOM_SEEDS=[]
    NUMBER_OF_SAMPLES=[]
    SAMPLES=[]
    PRODUCT=None
    
    # request the format of the input
    if isinstance(PORTION, list):
        portion=PORTION
    else:
        portion=[PORTION]
    if isinstance(OBST_ID, list):
        obst_id=OBST_ID
    else:
        obst_id=[OBST_ID]
    if isinstance(DEVC_ID, list):
        devc_id=DEVC_ID
    else:
        devc_id=[DEVC_ID]
    if OPEN_DIRECTION not in ['X+','X-','Y+','Y-','Z+','Z-']:
        raise ValueError("The input format of the door or window open time information is wrong.")
    if len(portion)==len(DOOR_OR_WINDOW_OPEN_TIME_RANGE)/2 and len(obst_id) and len(devc_id):
        # extract information
        id=PRE_PARM_INFO_ID
        open_direction=OPEN_DIRECTION
        # determine xyz of XB of door and window
        XB_list = [XB[:] for _ in range(len(portion))]
        if open_direction == 'X+':
            arr = np.linspace(XB[0], XB[1], len(portion)+1)
            arr = arr.tolist()
            XB_x = [[arr[i], arr[i + 1]] for i in range(len(arr) - 1)]
            for i in range(len(portion)):
                XB_list[i][0]=XB_x[i][0]
                XB_list[i][1]=XB_x[i][1]
        if open_direction == 'X-':
            arr = np.linspace(XB[0], XB[1], len(portion)+1)
            arr = arr.tolist()
            XB_x = [[arr[i], arr[i + 1]] for i in range(len(arr) - 1)]
            XB_x = XB_x[::-1]
            for i in range(len(portion)):
                XB_list[i][0]=XB_x[i][0]
                XB_list[i][1]=XB_x[i][1]
        if open_direction == 'Y+':
            arr = np.linspace(XB[2], XB[3], len(portion)+1)
            arr = arr.tolist()
            XB_y = [[arr[i], arr[i + 1]] for i in range(len(arr) - 1)]
            for i in range(len(portion)):
                XB_list[i][2]=XB_y[i][0]
                XB_list[i][3]=XB_y[i][1]
        if open_direction == 'Y-':
            arr = np.linspace(XB[2], XB[3], len(portion)+1)
            arr = arr.tolist()
            XB_y = [[arr[i], arr[i + 1]] for i in range(len(arr) - 1)]
            XB_y = XB_y[::-1]
            for i in range(len(portion)):
                XB_list[i][2]=XB_y[i][0]
                XB_list[i][3]=XB_y[i][1]
        if open_direction == 'Z+':
            arr = np.linspace(XB[4], XB[5], len(portion)+1)
            arr = arr.tolist()
            XB_z = [[arr[i], arr[i + 1]] for i in range(len(arr) - 1)]
            for i in range(len(portion)):
                XB_list[i][4]=XB_z[i][0]
                XB_list[i][5]=XB_z[i][1]
        if open_direction == 'Z-':
            arr = np.linspace(XB[4], XB[5], len(portion)+1)
            arr = arr.tolist()
            XB_z = [[arr[i], arr[i + 1]] for i in range(len(arr) - 1)]
            XB_z = XB_z[::-1]
            for i in range(len(portion)):
                XB_list[i][4]=XB_z[i][0]
                XB_list[i][5]=XB_z[i][1]
                
        quantity_name=QUANTITY_NAME
        door_or_window_open_time_range=[DOOR_OR_WINDOW_OPEN_TIME_RANGE[i:i+2] for i in range(0, len(DOOR_OR_WINDOW_OPEN_TIME_RANGE), 2)]
        door_or_window_open_time_info=[id, GENERATOR_ID, FYI, obst_id, XB_list, open_direction, quantity_name, portion, devc_id, door_or_window_open_time_range, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        # output sample generator information
        door_or_window_open_time={id:door_or_window_open_time_info}
        generated_info_variables =[]
        if len(door_or_window_open_time_range)!=1:
            for time_range, num in zip(door_or_window_open_time_range, range(len(door_or_window_open_time_range))):
                locals()['sample_generator_info_door_or_window_open_time_'+str(num)]=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_'+str(num+1), MINIMUM=time_range[0], MAXIMUM=time_range[1])
                generated_info_variables.append(locals()['sample_generator_info_door_or_window_open_time_'+str(num)])
        else:
            locals()['sample_generator_info_door_or_window_open_time_'+str(0)]=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id, MINIMUM=door_or_window_open_time_range[0][0], MAXIMUM=door_or_window_open_time_range[0][1])
            generated_info_variables.append(locals()['sample_generator_info_door_or_window_open_time_'+str(0)])
    else:
        raise ValueError("The input format of the door or window open time information is wrong.")
    
    return door_or_window_open_time, generated_info_variables


def GENERATING_DOOR_OR_WINDOW_OPEN_TIME_SAMPLES(ID, GENERATOR_ID, PARAMETER_PRE_OUTPUTS_INFO, PARAMETER_SAMPLE_GENERATOR_INFO, PRE_PARM_INFO_ID=None, PRODUCT=False, FYI=None):
    # extract the data from parameter dictionary
    id=ID
    if isinstance(GENERATOR_ID, list):
        generator_id=GENERATOR_ID
    else:
        generator_id=[GENERATOR_ID]
    
    para_info_id=PRE_PARM_INFO_ID
    parameter_id_list=[]
    for parameter in PARAMETER_PRE_OUTPUTS_INFO:
        if parameter is not None:
            for key in parameter:
                parameter_id_list.append(parameter[key][0])
    number_of_samples=GET_VALUE("NUMBER_OF_CASES")
    
    # save the parameter 
    door_window_open_time_info={}
    for generator_value in PARAMETER_SAMPLE_GENERATOR_INFO:
        for key,value in generator_value.items():
            if key in generator_id:
                door_window_open_time_info.update(generator_value)
    sample_generator=GENERATING_SAMPLES(door_window_open_time_info)
    
    # product samples
    product_combinations = []
    for _, value in sample_generator.SAMPLES.items():
        if len(value) != number_of_samples:
            product_combinations = [v for v in sample_generator.SAMPLES.values()]
            sample_product_combinations = list(itertools.product(*product_combinations))
            for index, (key, value) in enumerate(sample_generator.SAMPLES.items()):
                generator_product_samples=[]
                for i in range(len(sample_product_combinations)):
                    generator_product_samples.append(sample_product_combinations[i][index])
                sample_generator.SAMPLES[key] = np.array(generator_product_samples)
                sample_generator.NUMBER_OF_SAMPLES[key]=len(generator_product_samples)
            break
    
    # if para_info already exists
    if para_info_id in parameter_id_list:
        # check the input
        index = [i for i, x in enumerate(parameter_id_list) if x == para_info_id]
        parameter=PARAMETER_PRE_OUTPUTS_INFO[index[-1]]  
                 
        if len(parameter[para_info_id][7]) == len(generator_id):
                
            # Write the parameter dictionary
            GENERATOR_ID=[]
            OBST_ID=parameter[para_info_id][3]
            XB=parameter[para_info_id][4]
            OPEN_DIRECTION=parameter[para_info_id][5]
            QUANTITY_NAME=parameter[para_info_id][6]
            PORTION=parameter[para_info_id][7]
            DEVC_ID=parameter[para_info_id][8]
            DOOR_OR_WINDOW_OPEN_TIME_RANGE=parameter[para_info_id][9]
            RANDOM_SEEDS=[]
            SHUFFLE_STATES=[]
            SHUFFLE_RANDOM_SEEDS=[]
            NUMBER_OF_SAMPLES=[]
            SAMPLES=[]
            door_or_window_open_time_info_dic=[id, GENERATOR_ID, FYI, OBST_ID, XB, OPEN_DIRECTION, QUANTITY_NAME, PORTION, DEVC_ID, DOOR_OR_WINDOW_OPEN_TIME_RANGE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
            parameter = DOOR_OR_WINDOW_OPEN_TIME_DICT(door_or_window_open_time_info_dic)
            SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
        else:
            raise ValueError("GENERATOR_ID for ID '{self.ID}' has different lengths as designed.")
     
    else:
        # Write the parameter dictionary
        GENERATOR_ID=[]
        OBST_ID='N/A'
        XB='N/A'
        OPEN_DIRECTION='N/A'
        QUANTITY_NAME='N/A'
        PORTION='N/A'
        DEVC_ID='N/A'
        
        open_time_range_min=[]
        open_time_range_max=[]
        for key, value in sample_generator.MINIMUM.items():
            open_time_range_min.append(value if value != None else sample_generator.CONSTANT[key])
        for key, value in sample_generator.MAXIMUM.items():
            open_time_range_max.append(value if value != None else sample_generator.CONSTANT[key])
        DOOR_OR_WINDOW_OPEN_TIME_RANGE=[[open_time_range_min[i], open_time_range_max[i]] for i in range(len(open_time_range_min))]
        
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
        door_or_window_open_time_info_dic=[id, GENERATOR_ID, FYI, OBST_ID, XB, OPEN_DIRECTION, QUANTITY_NAME, PORTION, DOOR_OR_WINDOW_OPEN_TIME_RANGE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        parameter = DOOR_OR_WINDOW_OPEN_TIME_DICT(door_or_window_open_time_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
            
    return parameter, sample_generator



"Part 4: To generate field parameter - RANDOM XB"
# define the class of parameters OBSTRUCTIONS
class OBSTRUCTIONS_DICT:
    def __init__(self, OBSTRUCTIONS_INFO):
        if len(OBSTRUCTIONS_INFO) == 14:
            obstructions_info=OBSTRUCTIONS_INFO
            self.ID=obstructions_info[0]
            self.GENERATOR_ID=obstructions_info[1]
            self.FYI=obstructions_info[2]
            self.NAMELIST=obstructions_info[3]
            self.INITIAL_POINT=obstructions_info[4]
            self.LENGTH_RANGE=obstructions_info[5]
            self.WIDTH_RANGE=obstructions_info[6]
            self.HEIGHT_RANGE=obstructions_info[7]
            self.RANDOM_SEEDS=obstructions_info[8]
            self.SHUFFLE_STATES=obstructions_info[9]
            self.SHUFFLE_RANDOM_SEEDS=obstructions_info[10]
            self.NUMBER_OF_SAMPLES=obstructions_info[11]
            self.SAMPLES=obstructions_info[12]
            self.PRODUCT=obstructions_info[13]
        else:
            raise ValueError(f"OBSTRUCTIONS_INFO for ID '{self.ID}' must contain at least 12 elements.")
    
    def to_list(self):
        return [self.ID, self.GENERATOR_ID, self.FYI, self.NAMELIST, self.INITIAL_POINT, self.LENGTH_RANGE, self.WIDTH_RANGE, self.HEIGHT_RANGE, self.RANDOM_SEEDS, self.SHUFFLE_STATES, self.SHUFFLE_RANDOM_SEEDS, self.NUMBER_OF_SAMPLES, self.SAMPLES, self.PRODUCT]
    
    def to_dict(self):
        return  self.__dict__
    
    def __str__(self):
        result = ""
        result += (f"ID: {self.ID} \n"
                   f"Generator ID: {self.GENERATOR_ID}, \n"
                   f"FYI: {self.FYI}, \n"
                   f"Namelist: {self.NAMELIST}, \n"
                   f"Initial point: {self.INITIAL_POINT}, \n"
                   f"OBST Length Range: {self.LENGTH_RANGE}, \n"
                   f"OBST Width Range: {self.WIDTH_RANGE}, \n"
                   f"OBST Height Range: {self.HEIGHT_RANGE}, \n"
                   f"Random Seeds: {self.RANDOM_SEEDS}, \n"
                   f"Shuffle State: {self.SHUFFLE_STATES}, \n"
                   f"Shuffle Random Seeds: {self.SHUFFLE_RANDOM_SEEDS}, \n"
                   f"Number of Samples: {self.NUMBER_OF_SAMPLES}, \n"
                   f"Obstruction Samples: {self.SAMPLES} "
                   )
        return result
    
    
# input obstruction information
def INPUT_OBSTRUCTIONS_INFO(PRE_PARM_INFO_ID, NAMELIST, INITIAL_POINT, LENGTH_RANGE, WIDTH_RANGE, HEIGHT_RANGE, FYI=None):
    
    # default_variable
    GENERATOR_ID=[]
    RANDOM_SEEDS=[]
    SHUFFLE_STATES=[]
    SHUFFLE_RANDOM_SEEDS=[]
    NUMBER_OF_SAMPLES=[]
    SAMPLES=[]
    PRODUCT=None
    
    if len(INITIAL_POINT)==3 and len(LENGTH_RANGE)==2 and len(WIDTH_RANGE)==2 and len(HEIGHT_RANGE)==2:
        # request the format of the input
        obstructions_info=[PRE_PARM_INFO_ID, GENERATOR_ID, FYI, NAMELIST, INITIAL_POINT, LENGTH_RANGE, WIDTH_RANGE, HEIGHT_RANGE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        # extract information
        id=obstructions_info[0]
        initial_point=obstructions_info[4]
        length_range=obstructions_info[5]
        width_range=obstructions_info[6]
        height_range=obstructions_info[7]

        # output sample generator information
        obstructions={id:obstructions_info}
        sample_generator_info_obst_length=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_L', MINIMUM=length_range[0], MAXIMUM=length_range[1])
        sample_generator_info_obst_width=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_W', MINIMUM=width_range[0], MAXIMUM=width_range[1])
        sample_generator_info_obst_height=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_H', MINIMUM=height_range[0], MAXIMUM=height_range[1])
    else:
        raise ValueError("The input format of the obstruction information is wrong.")
      
    return obstructions, sample_generator_info_obst_length, sample_generator_info_obst_width, sample_generator_info_obst_height


def GENERATING_OBSTRUCTIONS_SAMPLES(ID, GENERATOR_ID, PARAMETER_PRE_OUTPUTS_INFO, PARAMETER_SAMPLE_GENERATOR_INFO, PRE_PARM_INFO_ID=None, PRODUCT=False, FYI=None):
    # extract the data from parameter dictionary
    id=ID
    if isinstance(GENERATOR_ID, list):
        generator_id=GENERATOR_ID
    else:
        generator_id=[GENERATOR_ID]
    if len(generator_id)!=3:
        raise ValueError(f"GENERATOR_ID for GRXB ID = '{id}' requires 3 ID names.")
    number_of_samples=GET_VALUE("NUMBER_OF_CASES")
    
    para_info_id=PRE_PARM_INFO_ID
    parameter_id_list=[]
    for parameter in PARAMETER_PRE_OUTPUTS_INFO:
        if parameter is not None:
            for key in parameter:
                parameter_id_list.append(parameter[key][0])
    
    obstructions_info={}
    for generator_value in PARAMETER_SAMPLE_GENERATOR_INFO:
        for key,value in generator_value.items():
            if key in generator_id:
                obstructions_info.update(generator_value)
    sample_generator=GENERATING_SAMPLES(obstructions_info)
    
    # product samples
    product_combinations = []
    for _, value in sample_generator.SAMPLES.items():
        if len(value) != number_of_samples:
            product_combinations = [v for v in sample_generator.SAMPLES.values()]
            sample_product_combinations = list(itertools.product(*product_combinations))
            for index, (key, value) in enumerate(sample_generator.SAMPLES.items()):
                generator_product_samples=[]
                for i in range(len(sample_product_combinations)):
                    generator_product_samples.append(sample_product_combinations[i][index])
                sample_generator.SAMPLES[key] = np.array(generator_product_samples)
                sample_generator.NUMBER_OF_SAMPLES[key]=len(generator_product_samples)
            break
    
    # save the parameter if para_info already exists
    if para_info_id in parameter_id_list:
        # Write the parameter dictionary
        index = [i for i, x in enumerate(parameter_id_list) if x == para_info_id]
        parameter=PARAMETER_PRE_OUTPUTS_INFO[index[-1]]
        GENERATOR_ID=[]
        NAMELIST=parameter[para_info_id][3]
        INITIAL_POINT=parameter[para_info_id][4]
        LENGTH_RANGE=parameter[para_info_id][5]
        WIDTH_RANGE=parameter[para_info_id][6]
        HEIGHT_RANGE=parameter[para_info_id][7]
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
        obstructions_info_dic=[id, GENERATOR_ID, FYI, NAMELIST, INITIAL_POINT, LENGTH_RANGE, WIDTH_RANGE, HEIGHT_RANGE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        parameter = OBSTRUCTIONS_DICT(obstructions_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
    
        # save the parameter if para_info NOT exists  
    else:
        obstructions_info={}
        for generator_value in PARAMETER_SAMPLE_GENERATOR_INFO:
            for key,value in generator_value.items():
                if key in generator_id:
                    obstructions_info.update(generator_value)
        sample_generator=GENERATING_SAMPLES(obstructions_info)
        # Write the parameter dictionary
        GENERATOR_ID=[]
        NAMELIST=[]
        INITIAL_POINT=[]
        LENGTH_RANGE=[sample_generator.MINIMUM[generator_id[0]],sample_generator.MAXIMUM[generator_id[0]]]
        WIDTH_RANGE=[sample_generator.MINIMUM[generator_id[1]],sample_generator.MAXIMUM[generator_id[1]]]
        HEIGHT_RANGE=[sample_generator.MINIMUM[generator_id[2]],sample_generator.MAXIMUM[generator_id[2]]]
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
        obstructions_info_dic=[id, GENERATOR_ID, FYI, NAMELIST, INITIAL_POINT, LENGTH_RANGE, WIDTH_RANGE, HEIGHT_RANGE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        parameter = OBSTRUCTIONS_DICT(obstructions_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
            
    return parameter, sample_generator


"Part 5: To generate field parameter - OTHER"
# define the class of parameters DOOR_OR_WINDOW_OPEN_TIME
class OTHERS_DICT:
    def __init__(self, OTHERS_INFO):
        if len(OTHERS_INFO) == 12:
            others_info=OTHERS_INFO
            self.ID=others_info[0]
            self.GENERATOR_ID=others_info[1]
            self.FYI=others_info[2]
            self.NAMELIST=others_info[3]
            self.ARG_NAME=others_info[4]
            self.OTHERS_RANGE=others_info[5]
            self.RANDOM_SEEDS=others_info[6]
            self.SHUFFLE_STATES=others_info[7]
            self.SHUFFLE_RANDOM_SEEDS=others_info[8]
            self.NUMBER_OF_SAMPLES=others_info[9]
            self.SAMPLES=others_info[10]
            self.PRODUCT=others_info[11]
        else:
            raise ValueError(f"OTHERS_INFO for ID '{self.ID}' must contain at least 10 elements.")
    
    def to_list(self):
        return [self.ID, self.GENERATOR_ID, self.FYI, self.NAMELIST, self.ARG_NAME, self.OTHERS_RANGE, self.RANDOM_SEEDS, self.SHUFFLE_STATES, self.SHUFFLE_RANDOM_SEEDS, self.NUMBER_OF_SAMPLES, self.SAMPLES, self.PRODUCT]
    
    def to_dict(self):
        return  self.__dict__
    
    def __str__(self):
        result = ""
        result += (f"ID: {self.ID} \n"
                   f"Generator ID: {self.GENERATOR_ID}, \n"
                   f"FYI: {self.FYI}, \n"
                   f"Namelist: {self.NAMELIST}, \n"
                   f"Argument Name: {self.ARG_NAME}, \n"
                   f"Other Parameter Range: {self.OTHERS_RANGE}, \n"
                   f"Random Seeds: {self.RANDOM_SEEDS}, \n"
                   f"Shuffle State: {self.SHUFFLE_STATES}, \n"
                   f"Shuffle Random Seeds: {self.SHUFFLE_RANDOM_SEEDS}, \n"
                   f"Number of Samples: {self.NUMBER_OF_SAMPLES}, \n"
                   f"Door and Window Open Time Samples: {self.SAMPLES} "
                   )
        return result
    
    
# input fire source location information
def INPUT_OTHERS_INFO(PRE_PARM_INFO_ID, NAMELIST, ARG_NAME, OTHERS_RANGE=[None,None], FYI=None):
    
    # default_variable
    GENERATOR_ID=[]
    RANDOM_SEEDS=[]
    SHUFFLE_STATES=[]
    SHUFFLE_RANDOM_SEEDS=[]
    NUMBER_OF_SAMPLES=[]
    SAMPLES=[]
    PRODUCT=None
    
    # request the format of the input
    others_info=[PRE_PARM_INFO_ID, GENERATOR_ID, FYI, NAMELIST, ARG_NAME, OTHERS_RANGE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
    # extract information
    id=others_info[0]
    other_range=others_info[5]
    # output sample generator information
    others={id:others_info}
    sample_generator_info_others=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id, MINIMUM=other_range[0],  MAXIMUM=other_range[1])
    
    return others, sample_generator_info_others


def GENERATING_OTHERS_SAMPLES(ID, GENERATOR_ID, PARAMETER_PRE_OUTPUTS_INFO, PARAMETER_SAMPLE_GENERATOR_INFO, PRE_PARM_INFO_ID=None, PRODUCT=False, FYI=None):
    # extract the data from parameter dictionary
    id=ID
    if isinstance(GENERATOR_ID, list):
        generator_id=GENERATOR_ID
    else:
        generator_id=[GENERATOR_ID]
    if len(generator_id)!=1:
        raise ValueError(f"GENERATOR_ID for GOTH ID = '{id}' requires 1 ID names.")
    number_of_samples=GET_VALUE("NUMBER_OF_CASES")
    
    para_info_id=PRE_PARM_INFO_ID
    parameter_id_list=[]
    for parameter in PARAMETER_PRE_OUTPUTS_INFO:
        if parameter is not None:
            for key in parameter:
                parameter_id_list.append(parameter[key][0])
    
    # save the parameter 
    others_info={}
    for generator_value in PARAMETER_SAMPLE_GENERATOR_INFO:
        for key,value in generator_value.items():
            if key in generator_id:
                others_info.update(generator_value)
    sample_generator=GENERATING_SAMPLES(others_info)
    
    # product samples
    product_combinations = []
    for _, value in sample_generator.SAMPLES.items():
        if len(value) != number_of_samples:
            product_combinations = [v for v in sample_generator.SAMPLES.values()]
            sample_product_combinations = list(itertools.product(*product_combinations))
            for index, (key, value) in enumerate(sample_generator.SAMPLES.items()):
                generator_product_samples=[]
                for i in range(len(sample_product_combinations)):
                    generator_product_samples.append(sample_product_combinations[i][index])
                sample_generator.SAMPLES[key] = np.array(generator_product_samples)
                sample_generator.NUMBER_OF_SAMPLES[key]=len(generator_product_samples)
            break
    
    if para_info_id in parameter_id_list:
        # Write the parameter dictionary
        index = [i for i, x in enumerate(parameter_id_list) if x == para_info_id]
        parameter=PARAMETER_PRE_OUTPUTS_INFO[index[-1]]
        GENERATOR_ID=[]
        namelist=parameter[para_info_id][3]
        arg_name=parameter[para_info_id][4]
        others_range=parameter[para_info_id][5]
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
        others_info_dic=[id, GENERATOR_ID, FYI, namelist, arg_name, others_range, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        parameter = OTHERS_DICT(others_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
    
    else:
        # Write the parameter dictionary
        GENERATOR_ID=[]
        namelist='N/A'
        arg_name='N/A'
        others_range=[sample_generator.MINIMUM[generator_id[0]],sample_generator.MAXIMUM[generator_id[0]]]
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
        others_info_dic=[id, GENERATOR_ID, FYI, arg_name, others_range, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES, PRODUCT]
        parameter = OTHERS_DICT(others_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
            
    return parameter, sample_generator

