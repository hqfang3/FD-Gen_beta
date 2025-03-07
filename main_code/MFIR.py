# import toolkits
import numpy as np
import math
from MRND import *
from global_parm import *
import itertools

"Part 1: To generate fire parameter - FIRE TIME DURATION"
# define the class of parameters FIRE TIME DURATION
class FIRE_TIME_DURATION_DICT:
    def __init__(self, FIRE_TIME_DURATION_INFO):
        if len(FIRE_TIME_DURATION_INFO) == 16:
            fire_time_duration_info=FIRE_TIME_DURATION_INFO
            self.ID=fire_time_duration_info[0]
            self.GENERATOR_ID=fire_time_duration_info[1]
            self.FYI=fire_time_duration_info[2]
            self.START_TIME=fire_time_duration_info[3]
            self.END_TIME=fire_time_duration_info[4]
            self.INCIPIENT_TIME=fire_time_duration_info[5]
            self.FIRE_GROWTH_TIME=fire_time_duration_info[6]
            self.FIRE_GROWTH_RATE=fire_time_duration_info[7]
            self.PEAK_TIME=fire_time_duration_info[8]
            self.DECAY_TIME=fire_time_duration_info[9]
            self.FIRE_DECAY_RATE=fire_time_duration_info[10]
            self.RANDOM_SEEDS=fire_time_duration_info[11]
            self.SHUFFLE_STATES=fire_time_duration_info[12]
            self.SHUFFLE_RANDOM_SEEDS=fire_time_duration_info[13]
            self.NUMBER_OF_SAMPLES=fire_time_duration_info[14]
            self.SAMPLES=fire_time_duration_info[15]
        else:
            raise ValueError(f"FIRE_SOURCE_LOCATION_INFO for ID '{self.ID}' must contain at least 15 elements.")
    
    def to_list(self):
        return [self.ID, self.GENERATOR_ID, self.FYI, self.START_TIME, self.END_TIME, self.INCIPIENT_TIME, self.FIRE_GROWTH_TIME, self.FIRE_GROWTH_RATE, self.PEAK_TIME, self.DECAY_TIME, self.FIRE_DECAY_RATE, self.RANDOM_SEEDS, self.SHUFFLE_STATES, self.SHUFFLE_RANDOM_SEEDS, self.NUMBER_OF_SAMPLES, self.SAMPLES]
    
    def to_dict(self):
        return  self.__dict__
    
    def __str__(self):
        result = ""
        result += (f"ID: {self.ID} \n"
                    f"Generator ID: {self.GENERATOR_ID} \n"
                    f"FYI: {self.FYI} \n"
                    f"Start Time: {self.START_TIME},\n"
                    f"End Time: {self.END_TIME},\n"
                    f"Incipient Time: {self.INCIPIENT_TIME},\n"
                    f"Fire Growth Time: {self.FIRE_GROWTH_TIME},\n"
                    f"Fire Growth Rate: {self.FIRE_GROWTH_RATE},\n"
                    f"Peak Time: {self.PEAK_TIME},\n"
                    f"Decay Time: {self.DECAY_TIME},\n"
                    f"Fire Decay Rate: {self.FIRE_DECAY_RATE},\n"
                    f"Random Seeds: {self.RANDOM_SEEDS}, \n"
                    f"Shuffle State: {self.SHUFFLE_STATES}, \n"
                    f"Shuffle Random Seeds: {self.SHUFFLE_RANDOM_SEEDS}, \n"
                    f"Number of Samples: {self.NUMBER_OF_SAMPLES}, \n"
                    f"Fire Time Duration Samples: {self.SAMPLES} "
                    )
        return result
    

# input fire source location information
def INPUT_FIRE_TIME_DURATION_INFO(PRE_PARM_INFO_ID, FYI=None, INCIPIENT_TIME=[None,None], FIRE_GROWTH_TIME=[None,None], FIRE_GROWTH_RATE=[None,None], PEAK_TIME=[None,None], DECAY_TIME=[None,None], FIRE_DECAY_RATE=[None,None]):
    
    # default_variable
    START_TIME='N/A'
    END_TIME='N/A'
    GENERATOR_ID=[]
    RANDOM_SEEDS=[]
    SHUFFLE_STATES=[]
    SHUFFLE_RANDOM_SEEDS=[]
    NUMBER_OF_SAMPLES=[]
    SAMPLES=[]
    
    
    # request the format of the input
    filtered_input_list = [x for x in [INCIPIENT_TIME, FIRE_GROWTH_TIME, FIRE_GROWTH_RATE, PEAK_TIME, DECAY_TIME, FIRE_DECAY_RATE] if x != [None,None]]
    if len(filtered_input_list) == 4:
        fire_time_duration_info=[PRE_PARM_INFO_ID, GENERATOR_ID, FYI, START_TIME, END_TIME, INCIPIENT_TIME, FIRE_GROWTH_TIME, FIRE_GROWTH_RATE, PEAK_TIME, DECAY_TIME, FIRE_DECAY_RATE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES]
        # extract information
        id=fire_time_duration_info[0]
        incipient_time=fire_time_duration_info[5]
        fire_growth_time=fire_time_duration_info[6]
        fire_growth_rate=fire_time_duration_info[7]
        peak_time=fire_time_duration_info[8]
        decay_time=fire_time_duration_info[9]
        fire_decay_rate=fire_time_duration_info[10]
            
        # decode fire time duration list
        fire_time_duration_list = [incipient_time, fire_growth_time, fire_growth_rate, peak_time, decay_time, fire_decay_rate]
        for item, i in zip(fire_time_duration_list, range(len(fire_time_duration_list))):
            if item == [None,None]:
                fire_time_duration_list[i] = [None]
            else:
                if item[0]==item[1]:
                    fire_time_duration_list[i] = [item[0]]
               
        # output sample generator information
        fire_time_duration={id:fire_time_duration_info}
        sample_generator_info_FTD_S1=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_I', DISTRIBUTION_TYPE=None if len(fire_time_duration_list[0]) == 2 else 'CONSTANT',
                                                                CONSTANT=None if len(fire_time_duration_list[0]) == 2 else fire_time_duration_list[0], 
                                                                MINIMUM=fire_time_duration_list[0][0] if len(fire_time_duration_list[0]) == 2 else None, PEAK=None, 
                                                                MAXIMUM=fire_time_duration_list[0][1] if len(fire_time_duration_list[0]) == 2 else None, MEAN=None)
        
        sample_generator_info_FTD_S2=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_G', DISTRIBUTION_TYPE=None if len(fire_time_duration_list[1]) == 2 else 'CONSTANT', 
                                                                CONSTANT = None if (fire_time_duration_list[1] != [None] and len(fire_time_duration_list[1]) == 2) else (fire_time_duration_list[1] if fire_time_duration_list[1] != [None] else [0]), 
                                                                MINIMUM=fire_time_duration_list[1][0] if (fire_time_duration_list[1] != [None] and len(fire_time_duration_list[1]) == 2) else None, PEAK=None, 
                                                                MAXIMUM=fire_time_duration_list[1][1] if (fire_time_duration_list[1] != [None] and len(fire_time_duration_list[1]) == 2) else None, MEAN=None)
        
        sample_generator_info_FTD_S2_R=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_GR', DISTRIBUTION_TYPE=None if len(fire_time_duration_list[2]) == 2 else 'CONSTANT', 
                                                                CONSTANT = None if (fire_time_duration_list[2] != [None] and len(fire_time_duration_list[2]) == 2) else (fire_time_duration_list[2] if fire_time_duration_list[2] != [None] else [0]), 
                                                                MINIMUM=fire_time_duration_list[2][0] if (fire_time_duration_list[2] != [None] and len(fire_time_duration_list[2]) == 2) else None, PEAK=None, 
                                                                MAXIMUM=fire_time_duration_list[2][1] if (fire_time_duration_list[2] != [None] and len(fire_time_duration_list[2]) == 2) else None, MEAN=None)
        
        sample_generator_info_FTD_S3=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_P', DISTRIBUTION_TYPE=None if len(fire_time_duration_list[3]) == 2 else 'CONSTANT',
                                                                CONSTANT=None if len(fire_time_duration_list[3]) == 2 else fire_time_duration_list[3], 
                                                                MINIMUM=fire_time_duration_list[3][0] if len(fire_time_duration_list[3]) == 2 else None, PEAK=None, 
                                                                MAXIMUM=fire_time_duration_list[3][1] if len(fire_time_duration_list[3]) == 2 else None, MEAN=None)
        
        sample_generator_info_FTD_S4=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_D', DISTRIBUTION_TYPE=None if len(fire_time_duration_list[4]) == 2 else 'CONSTANT',
                                                                CONSTANT = None if (fire_time_duration_list[4] != [None] and len(fire_time_duration_list[4]) == 2) else (fire_time_duration_list[4] if fire_time_duration_list[4] != [None] else [0]), 
                                                                MINIMUM=fire_time_duration_list[4][0] if (fire_time_duration_list[4] != [None] and len(fire_time_duration_list[4]) == 2) else None, PEAK=None, 
                                                                MAXIMUM=fire_time_duration_list[4][1] if (fire_time_duration_list[4] != [None] and len(fire_time_duration_list[4]) == 2) else None, MEAN=None)
        
        sample_generator_info_FTD_S4_R=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_DR', DISTRIBUTION_TYPE=None if len(fire_time_duration_list[5]) == 2 else 'CONSTANT',
                                                                CONSTANT = None if (fire_time_duration_list[5] != [None] and len(fire_time_duration_list[5]) == 2) else (fire_time_duration_list[5] if fire_time_duration_list[5] != [None] else [0]), 
                                                                MINIMUM=fire_time_duration_list[5][0] if (fire_time_duration_list[5] != [None] and len(fire_time_duration_list[5]) == 2) else None, PEAK=None, 
                                                                MAXIMUM=fire_time_duration_list[5][1] if (fire_time_duration_list[5] != [None] and len(fire_time_duration_list[5]) == 2) else None, MEAN=None)
        
    else:
        raise ValueError("The input format of the fire time duration information is wrong.")
        
    return fire_time_duration, fire_time_duration_list, sample_generator_info_FTD_S1, sample_generator_info_FTD_S2, sample_generator_info_FTD_S2_R, sample_generator_info_FTD_S3, sample_generator_info_FTD_S4, sample_generator_info_FTD_S4_R


def GENERATING_FIRE_TIME_DURATION_SAMPLES(ID, GENERATOR_ID, PARAMETER_PRE_OUTPUTS_INFO, PARAMETER_SAMPLE_GENERATOR_INFO, PRE_PARM_INFO_ID=None, FYI=None):
    # extract the data from parameter dictionary
    id=ID
    if isinstance(GENERATOR_ID, list):
        generator_id=GENERATOR_ID
    else:
        generator_id=[GENERATOR_ID]
    if len(generator_id)!=4:
        raise ValueError(f"GENERATOR_ID for GFTD ID = '{id}' requires 4 ID names.")
    number_of_samples=GET_VALUE("NUMBER_OF_CASES")
    
    para_info_id=PRE_PARM_INFO_ID
    parameter_id_list=[]
    for parameter in PARAMETER_PRE_OUTPUTS_INFO:
        if parameter is not None:
            for key in parameter:
                parameter_id_list.append(parameter[key][0])
    
    # save the parameter
    fire_time_duration_info={}
    for generator_value in PARAMETER_SAMPLE_GENERATOR_INFO:
        for key,value in generator_value.items():
            if key in generator_id:
                fire_time_duration_info.update(generator_value)
    sample_generator=GENERATING_SAMPLES(fire_time_duration_info)
    
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
        START_TIME=parameter[para_info_id][3]
        END_TIME=parameter[para_info_id][4]
        INCIPIENT_TIME=parameter[para_info_id][5]
        FIRE_GROWTH_TIME=parameter[para_info_id][6]
        FIRE_GROWTH_RATE=parameter[para_info_id][7]
        PEAK_TIME=parameter[para_info_id][8]
        DECAY_TIME=parameter[para_info_id][9]
        FIRE_DECAY_RATE=parameter[para_info_id][10]
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
        fire_time_duration_info_dic=[id, GENERATOR_ID, FYI, START_TIME, END_TIME, INCIPIENT_TIME, FIRE_GROWTH_TIME, FIRE_GROWTH_RATE, PEAK_TIME, DECAY_TIME, FIRE_DECAY_RATE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES]
        parameter = FIRE_TIME_DURATION_DICT(fire_time_duration_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
    
    else:
        # Write the parameter dictionary
        GENERATOR_ID=[]
        START_TIME='N/A'
        END_TIME='N/A'
        FIRE_GROWTH_RATE=[None, None]
        FIRE_DECAY_RATE=[None, None]
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
        if sample_generator.CONSTANT[generator_id[0]]==None:
            INCIPIENT_TIME=[sample_generator.MINIMUM[generator_id[0]],sample_generator.MAXIMUM[generator_id[0]]]
        else:
            INCIPIENT_TIME=[sample_generator.CONSTANT[generator_id[0]],sample_generator.CONSTANT[generator_id[0]]]
        if sample_generator.CONSTANT[generator_id[1]]==None:
            FIRE_GROWTH_TIME=[sample_generator.MINIMUM[generator_id[1]],sample_generator.MAXIMUM[generator_id[1]]]
        else:
            FIRE_GROWTH_TIME=[sample_generator.CONSTANT[generator_id[1]],sample_generator.CONSTANT[generator_id[1]]]
        if sample_generator.CONSTANT[generator_id[2]]==None:
            PEAK_TIME=[sample_generator.MINIMUM[generator_id[2]],sample_generator.MAXIMUM[generator_id[2]]]
        else:
            PEAK_TIME=[sample_generator.CONSTANT[generator_id[2]],sample_generator.CONSTANT[generator_id[2]]]
        if sample_generator.CONSTANT[generator_id[3]]==None:
            DECAY_TIME=[sample_generator.MINIMUM[generator_id[3]],sample_generator.MAXIMUM[generator_id[3]]]
        else:
            DECAY_TIME=[sample_generator.CONSTANT[generator_id[3]],sample_generator.CONSTANT[generator_id[3]]]
        fire_time_duration_info_dic=[id, GENERATOR_ID, FYI, START_TIME, END_TIME, INCIPIENT_TIME, FIRE_GROWTH_TIME, FIRE_GROWTH_RATE, PEAK_TIME, DECAY_TIME, FIRE_DECAY_RATE, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES]
        parameter = FIRE_TIME_DURATION_DICT(fire_time_duration_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
            
    return parameter, sample_generator



"Part 2: To generate fire parameter - MAX HRR"
# define the class of parameters HEAR_RELEASE_RATE
class MAX_HRR_DICT:
    def __init__(self, MAX_HRR_INFO):
        if len(MAX_HRR_INFO) == 11:
            heat_release_rate_info=MAX_HRR_INFO
            self.ID=heat_release_rate_info[0]
            self.GENERATOR_ID=heat_release_rate_info[1]
            self.FYI=heat_release_rate_info[2]
            self.INCIPIENT_MAX_HRR=heat_release_rate_info[3]
            self.PEAK_MAX_HRR=heat_release_rate_info[4]
            self.DECAY_MIN_HRR=heat_release_rate_info[5]
            self.RANDOM_SEEDS=heat_release_rate_info[6]
            self.SHUFFLE_STATES=heat_release_rate_info[7]
            self.SHUFFLE_RANDOM_SEEDS=heat_release_rate_info[8]
            self.NUMBER_OF_SAMPLES=heat_release_rate_info[9]
            self.SAMPLES=heat_release_rate_info[10]
        else:
            raise ValueError(f"MAX_HRR_INFO for ID '{self.ID}' must contain at least 9 elements.")
    
    def to_list(self):
        return [self.ID, self.GENERATOR_ID, self.FYI, self.INCIPIENT_MAX_HRR, self.PEAK_MAX_HRR, self.DECAY_MIN_HRR, self.RANDOM_SEEDS, self.SHUFFLE_STATES, self.SHUFFLE_RANDOM_SEEDS, self.NUMBER_OF_SAMPLES, self.SAMPLES]
    
    def to_dict(self):
        return  self.__dict__
    
    def __str__(self):
        result = ""
        result += (f"ID: {self.ID} \n"
                    f"Generator ID: {self.GENERATOR_ID}, \n"
                    f"FYI: {self.FYI}, \n"
                    f"Incipient MAX HRR: {self.INCIPIENT_MAX_HRR},\n"
                    f"Peak MAX HRR: {self.PEAK_MAX_HRR},\n"
                    f"Decay MIN HRR: {self.DECAY_MIN_HRR},\n"
                    f"Random Seeds: {self.RANDOM_SEEDS}, \n"
                    f"Shuffle State: {self.SHUFFLE_STATES}, \n"
                    f"Shuffle Random Seeds: {self.SHUFFLE_RANDOM_SEEDS}, \n"
                    f"Number of Samples: {self.NUMBER_OF_SAMPLES}, \n"
                    f"Max Heat Release Rate Samples: {self.SAMPLES} "
                    )
        return result


# input heat release rate information
def INPUT_MAX_HRR_INFO(PRE_PARM_INFO_ID, INCIPIENT_MAX_HRR, PEAK_MAX_HRR, DECAY_MIN_HRR, FYI=None):
    
    # default_variable
    GENERATOR_ID=[]
    RANDOM_SEEDS=[]
    SHUFFLE_STATES=[]
    SHUFFLE_RANDOM_SEEDS=[]
    NUMBER_OF_SAMPLES=[]
    SAMPLES=[]
    
    # request the format of the input
    if len([INCIPIENT_MAX_HRR, PEAK_MAX_HRR, DECAY_MIN_HRR]) == 3:
        heat_release_rate_info=[PRE_PARM_INFO_ID, GENERATOR_ID, FYI, INCIPIENT_MAX_HRR, PEAK_MAX_HRR, DECAY_MIN_HRR, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES]
        # extract information
        id=heat_release_rate_info[0]
        incipient_max_hrr=heat_release_rate_info[3]
        peak_max_hrr=heat_release_rate_info[4]
        decay_min_hrr=heat_release_rate_info[5]
            
        # decode heat release rate list
        heat_release_rate_list = [incipient_max_hrr,peak_max_hrr,decay_min_hrr]
        
        for item, i in zip(heat_release_rate_list, range(len(heat_release_rate_list))):
            if item[0]==item[1]:
               heat_release_rate_list[i] = [item[0]]
               
        # output sample generator information
        heat_release_rate={id:heat_release_rate_info}
        sample_generator_info_HRR_incipient=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_I', DISTRIBUTION_TYPE=None if len(heat_release_rate_list[0]) == 2 else 'CONSTANT', CONSTANT=None if len(heat_release_rate_list[0]) == 2 else heat_release_rate_list[0], MINIMUM=heat_release_rate_list[0][0] if len(heat_release_rate_list[0]) == 2 else None, PEAK=None, MAXIMUM=heat_release_rate_list[0][1] if len(heat_release_rate_list[0]) == 2 else None)
        sample_generator_info_HRR_peak=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_P', DISTRIBUTION_TYPE=None if len(heat_release_rate_list[1]) == 2 else 'CONSTANT', CONSTANT=None if len(heat_release_rate_list[1]) == 2 else heat_release_rate_list[1], MINIMUM=heat_release_rate_list[1][0] if len(heat_release_rate_list[1]) == 2 else None, PEAK=None, MAXIMUM=heat_release_rate_list[1][1] if len(heat_release_rate_list[1]) == 2 else None)
        sample_generator_info_HRR_decay=INPUT_SAMPLE_GENERATOR_INFO(None, GENERATOR_ID=None, PRE_PARM_INFO_ID=id+'_D', DISTRIBUTION_TYPE=None if len(heat_release_rate_list[2]) == 2 else 'CONSTANT', CONSTANT=None if len(heat_release_rate_list[2]) == 2 else heat_release_rate_list[2], MINIMUM=heat_release_rate_list[2][0] if len(heat_release_rate_list[2]) == 2 else None, PEAK=None, MAXIMUM=heat_release_rate_list[2][1] if len(heat_release_rate_list[2]) == 2 else None)
            
    else:
        raise ValueError("The input format of the heat release rate information is wrong.")
        
    return heat_release_rate, sample_generator_info_HRR_incipient, sample_generator_info_HRR_peak, sample_generator_info_HRR_decay



def GENERATING_MAX_HRR_SAMPLES(ID, GENERATOR_ID, PARAMETER_PRE_OUTPUTS_INFO, PARAMETER_SAMPLE_GENERATOR_INFO, PRE_PARM_INFO_ID=None, FYI=None):
    # extract the data from parameter dictionary
    id=ID
    
    if isinstance(GENERATOR_ID, list):
        generator_id=GENERATOR_ID
    else:
        generator_id=[GENERATOR_ID]
    if len(generator_id)!=3:
        raise ValueError(f"GENERATOR_ID for GMHR ID = '{id}' requires 3 ID names.")
    number_of_samples=GET_VALUE("NUMBER_OF_CASES")
    
    para_info_id=PRE_PARM_INFO_ID
    parameter_id_list=[]
    for parameter in PARAMETER_PRE_OUTPUTS_INFO:
        if parameter is not None:
            for key in parameter:
                parameter_id_list.append(parameter[key][0])
    
    # save the parameter 
    max_hrr_info={}
    for generator_value in PARAMETER_SAMPLE_GENERATOR_INFO:
        for key,value in generator_value.items():
            if key in generator_id:
                max_hrr_info.update(generator_value)
    sample_generator=GENERATING_SAMPLES(max_hrr_info)
    
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
        INCIPIENT_MAX_HRR=parameter[para_info_id][3]
        PEAK_MAX_HRR=parameter[para_info_id][4]
        DECAY_MIN_HRR=parameter[para_info_id][5]
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
        heat_release_rate_info_dic=[id, GENERATOR_ID, FYI, INCIPIENT_MAX_HRR, PEAK_MAX_HRR, DECAY_MIN_HRR, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES]
        parameter = MAX_HRR_DICT(heat_release_rate_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
    
    else:
        # Write the parameter dictionary
        GENERATOR_ID=[]
        INCIPIENT_MAX_HRR=[sample_generator.MINIMUM[generator_id[0]],sample_generator.MAXIMUM[generator_id[0]]]
        PEAK_MAX_HRR=[sample_generator.MINIMUM[generator_id[1]],sample_generator.MAXIMUM[generator_id[1]]]
        DECAY_MIN_HRR=[sample_generator.MINIMUM[generator_id[2]],sample_generator.MAXIMUM[generator_id[2]]]
        RANDOM_SEEDS=[]
        SHUFFLE_STATES=[]
        SHUFFLE_RANDOM_SEEDS=[]
        NUMBER_OF_SAMPLES=[]
        SAMPLES=[]
        heat_release_rate_info_dic=[id, GENERATOR_ID, FYI, INCIPIENT_MAX_HRR, PEAK_MAX_HRR, DECAY_MIN_HRR, RANDOM_SEEDS, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES]
        parameter = MAX_HRR_DICT(heat_release_rate_info_dic)
        SAVE_SAMPLING_SAMPLES(parameter, sample_generator)
            
    return parameter, sample_generator



"Part 3: To generate fire parameter - HRR curve"
# define the class of parameters BASELINE_HRR
class HRR_CURVE_DICT:
    def __init__(self, HRR_CURVE_INFO):
        if len(HRR_CURVE_INFO) == 14:
            baseline_hrr_info=HRR_CURVE_INFO
            self.ID=baseline_hrr_info[0]
            self.FIRE_TIME_DURATION_GENERATOR_ID=baseline_hrr_info[1]
            self.MAX_HRR_GENERATOR_ID=baseline_hrr_info[2]
            self.FIRE_PATTERN=baseline_hrr_info[3]
            self.FYI=baseline_hrr_info[4]
            self.TIME_FREQUENCY=baseline_hrr_info[5]
            self.START_TIME=baseline_hrr_info[6]
            self.END_TIME=baseline_hrr_info[7]
            self.HRR_FLUCTUATION=baseline_hrr_info[8]
            self.HRR_FLUCTUATION_RATE=baseline_hrr_info[9]
            self.NUMBER_OF_SAMPLES=baseline_hrr_info[10]
            self.TIME_SLICE_SAMPLES=baseline_hrr_info[11]
            self.HRR_SAMPLES=baseline_hrr_info[12]
            self.PRODUCT=baseline_hrr_info[13]
        else:
            raise ValueError(f"HRR_CURVE_INFO for ID '{self.ID}' must contain at least 13 elements.")
    
    def to_list(self):
        return [self.ID, self.FIRE_TIME_DURATION_GENERATOR_ID, self.MAX_HRR_GENERATOR_ID, self.FIRE_PATTERN, self.FYI, self.TIME_FREQUENCY, self.START_TIME, self.END_TIME, self.HRR_FLUCTUATION, self.HRR_FLUCTUATION_RATE, self.NUMBER_OF_SAMPLES, self.TIME_SLICE_SAMPLES, self.HRR_SAMPLES, self.PRODUCT]
    
    def to_dict(self):
        return  self.__dict__
    
    def __str__(self):
        result = ""
        result += (f"ID: {self.ID} \n"
                    f"Fire Time Duration Generator ID: {self.FIRE_TIME_DURATION_GENERATOR_ID}, \n"
                    f"Max HRR Generator ID: {self.MAX_HRR_GENERATOR_ID}, \n"
                    f"Fire Pattern: {self.FIRE_PATTERN}, \n"
                    f"FYI: {self.FYI}, \n"
                    f"Time Frequency: {self.TIME_FREQUENCY},\n"
                    f"Time Start: {self.START_TIME},\n"
                    f"Time End: {self.END_TIME},\n"
                    f"HRR Fluctuation: {self.HRR_FLUCTUATION}, \n"
                    f"HRR Fluctuation Rate: {self.HRR_FLUCTUATION_RATE}, \n"
                    f"Number of Samples: {self.NUMBER_OF_SAMPLES}, \n"
                    f"Time Slice Samples: {self.TIME_SLICE_SAMPLES}, \n"
                    f"Baseline HRR Samples: {self.HRR_SAMPLES} "
                    )
        return result
    

# Generating HRR baseline samples 
def GENERATING_HRR_CURVE(ID, FIRE_TIME_DURATION_GENERATOR_ID, MAX_HRR_GENERATOR_ID, PARAMETER_OUTPUTS, FIRE_PATTERN=[1,2,0,2], FYI=None, START_TIME=0,  END_TIME=1800, TIME_FREQUENCY=1, HRR_FLUCTUATION=False, HRR_FLUCTUATION_RATE=0, TIME_SLICE_SAMPLES=None, HRR_SAMPLES=None, PRODUCT=False):
    
    # transfer the sample format
    NUMBER_OF_SAMPLES=GET_VALUE("NUMBER_OF_CASES")
    if TIME_SLICE_SAMPLES is not None:
        TIME_SLICE_SAMPLES=np.array(TIME_SLICE_SAMPLES)
    else:
        TIME_SLICE_SAMPLES=np.array([])

    if HRR_SAMPLES is not None:
        HRR_SAMPLES=np.array(HRR_SAMPLES)
    else:
        HRR_SAMPLES=np.array([])
    
     # request the format of the input
    id=ID
    if isinstance(FIRE_TIME_DURATION_GENERATOR_ID, list):
        FTD_generator_id=FIRE_TIME_DURATION_GENERATOR_ID
    else:
        FTD_generator_id=[FIRE_TIME_DURATION_GENERATOR_ID]
    if isinstance(MAX_HRR_GENERATOR_ID, list):
        MHR_generator_id=MAX_HRR_GENERATOR_ID
    else:
        MHR_generator_id=[MAX_HRR_GENERATOR_ID]
        
    # input check
    if len(MHR_generator_id) != len(FTD_generator_id):
        raise ValueError(f"FIRE_TIME_DURATION_GENERATOR_ID and MAX_HRR_GENERATOR_ID for GHRC ID = '{id}' MUST have the same length.")
    if len(FIRE_PATTERN) != 4:
        raise ValueError(f"FIRE_PATTERN for GHRC ID = '{id}' MUST have 4 elements.")
    
    # save to dictionary 
    HRR_curve_info=[id, FTD_generator_id, MHR_generator_id, FIRE_PATTERN, FYI, TIME_FREQUENCY, START_TIME, END_TIME, HRR_FLUCTUATION, HRR_FLUCTUATION_RATE, NUMBER_OF_SAMPLES, TIME_SLICE_SAMPLES, HRR_SAMPLES, PRODUCT]
    HRR_curve = HRR_CURVE_DICT(HRR_curve_info)

    # extract information
    fire_pattern=HRR_curve.FIRE_PATTERN
    start_time=HRR_curve.START_TIME
    end_time=HRR_curve.END_TIME
    fire_frequency=HRR_curve.TIME_FREQUENCY
    hrr_fluctuation=HRR_curve.HRR_FLUCTUATION
    hrr_fluctuation_rate=HRR_curve.HRR_FLUCTUATION_RATE
    number_of_samples=HRR_curve.NUMBER_OF_SAMPLES
    time_slice_samples=HRR_curve.TIME_SLICE_SAMPLES
    hrr_curve_samples=HRR_curve.HRR_SAMPLES
    
    FTD_generators=[]
    MHR_generators=[]
    for parameter in PARAMETER_OUTPUTS[0]:
        if parameter.ID in FTD_generator_id:
            FTD_generators.append(parameter)
    for parameter in PARAMETER_OUTPUTS[1]:
        if parameter.ID in MHR_generator_id:
            MHR_generators.append(parameter)
        
    # Check whether need product
    product_check=[]
    for FTD_generator,MHR_generator in zip(FTD_generators,MHR_generators):
        if (FTD_generator.NUMBER_OF_SAMPLES[0] == number_of_samples) and (MHR_generator.NUMBER_OF_SAMPLES[0]==number_of_samples):
            all_match_FTD_MHR = True
        else:
            all_match_FTD_MHR = False
        product_check.append(all_match_FTD_MHR)
        
    # modify the sample with product
    list_number_of_samples=[]
    for index, product_result in enumerate(product_check):
        if product_result is False:
            number_of_samples_FTD=FTD_generators[index].NUMBER_OF_SAMPLES[0]
            number_of_samples_MHR=MHR_generators[index].NUMBER_OF_SAMPLES[0]
            for i in range(4):
                FTD_generators[index].SAMPLES[i]=np.array(FTD_generators[index].SAMPLES[i].tolist()*number_of_samples_MHR)
                FTD_generators[index].NUMBER_OF_SAMPLES[i]=len(FTD_generators[index].SAMPLES[i])
            for i in range(3):
                MHR_generators[index].SAMPLES[i]=np.array([element for element in MHR_generators[index].SAMPLES[i] for _ in range(number_of_samples_FTD)])
                MHR_generators[index].NUMBER_OF_SAMPLES[i]=len(MHR_generators[index].SAMPLES[i])
            list_number_of_samples.append(MHR_generators[index].NUMBER_OF_SAMPLES[i])
        else:
            list_number_of_samples.append(number_of_samples)
     
    if False in product_check:
        for i in range(4):
            ALL_product_combinations_FTD=[]
            for fire_time_duration_generator in FTD_generators:
                product_combinations_FTD=fire_time_duration_generator.SAMPLES[i]
                ALL_product_combinations_FTD.append(product_combinations_FTD)
            for index in range(len(FTD_generators)):
                sample_product_combinations = list(itertools.product(*ALL_product_combinations_FTD))
                generator_product_samples=[]
                for j in range(len(sample_product_combinations)):
                    generator_product_samples.append(sample_product_combinations[j][index])
                FTD_generators[index].SAMPLES[i] = np.array(generator_product_samples)
                FTD_generators[index].NUMBER_OF_SAMPLES[i]=len(sample_product_combinations)
                
        for i in range(3):
            ALL_product_combinations_MHR=[]
            for max_hrr_generator in MHR_generators:
                product_combinations_MHR=max_hrr_generator.SAMPLES[i]
                ALL_product_combinations_MHR.append(product_combinations_MHR)
            for index in range(len(MHR_generators)):
                sample_product_combinations = list(itertools.product(*ALL_product_combinations_MHR))
                generator_product_samples=[]
                for j in range(len(sample_product_combinations)):
                    generator_product_samples.append(sample_product_combinations[j][index])
                MHR_generators[index].SAMPLES[i] = np.array(generator_product_samples) 
                MHR_generators[index].NUMBER_OF_SAMPLES[i]=len(sample_product_combinations)
        
        number_of_samples=fire_time_duration_generator.NUMBER_OF_SAMPLES[0]
        
       
    # hrr curve samples
    if time_slice_samples.size == 0 and hrr_curve_samples.size == 0:
        
        time_slice_samples_list=[]
        hrr_curve_samples_list=[]
        
        for sample in range(number_of_samples):
            
            # calculating the curve
            time_accum=start_time
            time_slice_samples=[]
            hrr_curve_samples=[]
            decay_min_hrr=0
            
            for fire_time_duration_generator,max_hrr_generator in zip(FTD_generators,MHR_generators):
                # HRR baseline             
                # extract Fire time duration
                samples_fire_time_duration=[np.zeros(number_of_samples)] * 6
                samples_fire_time_duration[0]=fire_time_duration_generator.SAMPLES[0]
                if fire_time_duration_generator.FIRE_GROWTH_TIME != [None, None]:
                    samples_fire_time_duration[1] = fire_time_duration_generator.SAMPLES[1]
                if fire_time_duration_generator.FIRE_GROWTH_RATE != [None, None]:
                    samples_fire_time_duration[2] = fire_time_duration_generator.SAMPLES[1]
                samples_fire_time_duration[3]=fire_time_duration_generator.SAMPLES[2]
                if fire_time_duration_generator.DECAY_TIME != [None, None]:
                    samples_fire_time_duration[4] = fire_time_duration_generator.SAMPLES[3]
                if fire_time_duration_generator.FIRE_DECAY_RATE != [None, None]:
                    samples_fire_time_duration[5] = fire_time_duration_generator.SAMPLES[3]
                # extract max hrr 
                sample_max_hrr=max_hrr_generator.SAMPLES
                # extract hrr fluctuation
                hrr_fluctuation_rates=np.linspace(-hrr_fluctuation_rate,hrr_fluctuation_rate,number_of_samples)
                
                # incipient stage
                incipient_time_duration=samples_fire_time_duration[0][sample]
                incipient_time_num=round(incipient_time_duration/fire_frequency)
                incipient_max_hrr=sample_max_hrr[0][sample]
                if incipient_time_duration==0:
                    incipient_slope=0
                else:
                    incipient_slope=(incipient_max_hrr-decay_min_hrr)/((incipient_time_duration)**fire_pattern[0])
                incipient_time_slices=np.linspace(time_accum+1, time_accum+incipient_time_duration, incipient_time_num)
                incipient_hrr_samples= [decay_min_hrr+incipient_slope*(x**fire_pattern[0]) for x in [x - time_accum for x in incipient_time_slices]]
                time_accum=time_accum+incipient_time_duration
                    
                # fire growth stage
                peak_max_hrr=sample_max_hrr[1][sample]
                if samples_fire_time_duration[1][sample]!=0:
                    fire_growth_time_duration=samples_fire_time_duration[1][sample]
                    fire_growth_time_num=round(fire_growth_time_duration/fire_frequency)
                    fire_growth_rate=(peak_max_hrr-incipient_max_hrr)/((fire_growth_time_duration)**fire_pattern[1])
                else:
                    if samples_fire_time_duration[2][sample]!=0:
                        fire_growth_rate=samples_fire_time_duration[2][sample]
                        fire_growth_time_duration=((peak_max_hrr-incipient_max_hrr)/fire_growth_rate)**(1/fire_pattern[1])
                        fire_growth_time_num=round(fire_growth_time_duration/fire_frequency)
                    else:
                        fire_growth_rate=0
                        fire_growth_time_duration=0
                        fire_growth_time_num=0
                fire_growth_time_slices=np.linspace(time_accum+1, time_accum+fire_growth_time_duration, fire_growth_time_num)
                fire_growth_hrr_samples= [fire_growth_rate*(x**fire_pattern[1])+incipient_max_hrr for x in [x - time_accum for x in fire_growth_time_slices]]
                time_accum=time_accum+fire_growth_time_duration
                
                # peak stage
                peak_time_duration=samples_fire_time_duration[3][sample]
                peak_time_num=round(peak_time_duration/fire_frequency)
                peak_max_hrr=sample_max_hrr[1][sample]
                peak_time_slices=np.linspace(time_accum+1, time_accum+peak_time_duration, peak_time_num)
                peak_hrr_samples= [peak_max_hrr]*peak_time_num
                time_accum=time_accum+peak_time_duration        
                
                # decay stage
                peak_max_hrr=sample_max_hrr[1][sample]
                decay_min_hrr=sample_max_hrr[2][sample]
                if samples_fire_time_duration[4][sample]!=0:
                    decay_time_duration=samples_fire_time_duration[4][sample]
                    decay_time_num=round(decay_time_duration/fire_frequency)
                    fire_decay_rate=(peak_max_hrr-decay_min_hrr)/(decay_time_duration**fire_pattern[3])
                else:
                    if samples_fire_time_duration[5][sample]!=0:
                        fire_decay_rate=samples_fire_time_duration[5][sample]
                        decay_time_duration=((peak_max_hrr-decay_min_hrr)/fire_decay_rate)**(1/fire_pattern[3])
                        decay_time_num=round(decay_time_duration/fire_frequency)
                    else:
                        fire_decay_rate=0
                        decay_time_duration=0
                        decay_time_num=0
                decay_time_slices=np.linspace(time_accum+1, time_accum+decay_time_duration, decay_time_num)
                decay_hrr_samples= [decay_min_hrr+fire_decay_rate*(x**fire_pattern[3]) for x in [decay_time_duration - (x - time_accum) for x in decay_time_slices]]
                time_accum=time_accum+decay_time_duration
                
                time_slice_sample = np.concatenate((incipient_time_slices, fire_growth_time_slices, peak_time_slices, decay_time_slices))
                HRR_curve_sample = np.concatenate((incipient_hrr_samples, fire_growth_hrr_samples, peak_hrr_samples, decay_hrr_samples))
            
                time_slice_samples.append(time_slice_sample)
                hrr_curve_samples.append(HRR_curve_sample)
            
            time_slice_samples_per_case = [item for sublist in time_slice_samples for item in sublist]
            time_slice_samples_per_case=np.array(time_slice_samples_per_case)
            hrr_curve_samples_per_case = [item for sublist in hrr_curve_samples for item in sublist]
            hrr_curve_samples_per_case=np.array(hrr_curve_samples_per_case)
            time_slice_samples_list.append(time_slice_samples_per_case)
            hrr_curve_samples_list.append(hrr_curve_samples_per_case)
        
        
        # decide on fluctuation
        def all_elements_equal(lst):
            return all(np.array_equal(arr, lst[0]) for arr in lst)
        if all_elements_equal(time_slice_samples_list) and all_elements_equal(hrr_curve_samples_list):
            if hrr_fluctuation == True:
                for case,index in zip(hrr_curve_samples_list,range(len(hrr_curve_samples_list))):
                    hrr_curve_samples_list[index]=case*(1+hrr_fluctuation_rates[index])
        
        # trim the data with time end
        time_slice_samples_output=[]
        hrr_curve_samples_output=[]
        for sample in range(number_of_samples):
            curve_time_num=round(end_time/fire_frequency)-round(start_time/fire_frequency)
            if len(time_slice_samples_list[sample]) > curve_time_num:
                hrr_curve_samples_list[sample]=hrr_curve_samples_list[sample][:curve_time_num]
                time_slice_samples_list[sample]=time_slice_samples_list[sample][:curve_time_num]           
            time_slice_samples_output.append(time_slice_samples_list[sample])
            hrr_curve_samples_output.append(hrr_curve_samples_list[sample])
               
        HRR_curve.NUMBER_OF_SAMPLES = number_of_samples
        HRR_curve.TIME_SLICE_SAMPLES = time_slice_samples_output
        HRR_curve.HRR_SAMPLES = hrr_curve_samples_output
        
    return HRR_curve
                    
           