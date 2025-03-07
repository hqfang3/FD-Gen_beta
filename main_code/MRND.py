# import library
import numpy as np
import math
from scipy.stats import uniform
from scipy.stats import norm
from scipy.stats import lognorm
from scipy.stats import triang
from global_parm import *


" This is the module for random data sampling and refining."
# define the class of generator
class SAMPLE_GENERATOR_DICT:
    def __init__(self, SAMPLE_GENERATOR_INFO=None):
        self.GENERATOR_ID = {}
        self.PARM_ID = {}
        self.FYI = {}
        self.DISTRIBUTION_TYPE = {}
        self.RANDOM_SEEDS = {}
        self.CONSTANT = {}
        self.MINIMUM = {}
        self.PEAK = {}
        self.MAXIMUM = {}
        self.MEAN = {}
        self.STDEV = {}
        self.INCREASE = {}
        self.VALUE_TYPE = {}
        self.APPROX_VALUE = {}
        self.LOGICAL_VALUE = {}
        self.SHUFFLE_STATES = {}
        self.SHUFFLE_RANDOM_SEEDS = {}
        self.NUMBER_OF_SAMPLES = {}
        self.SAMPLES = {}
        
        if SAMPLE_GENERATOR_INFO is not None:
            for GENERATOR_ID in SAMPLE_GENERATOR_INFO:
                generator_info=SAMPLE_GENERATOR_INFO[GENERATOR_ID]
                if len(generator_info) == 18:
                    self.GENERATOR_ID[GENERATOR_ID] = GENERATOR_ID
                    self.PARM_ID[GENERATOR_ID] = generator_info[0]
                    self.FYI[GENERATOR_ID] = generator_info[1]
                    self.DISTRIBUTION_TYPE[GENERATOR_ID] = generator_info[2]
                    self.RANDOM_SEEDS[GENERATOR_ID] = generator_info[3]
                    self.CONSTANT[GENERATOR_ID] = generator_info[4]
                    self.MINIMUM[GENERATOR_ID] = generator_info[5]
                    self.PEAK[GENERATOR_ID] = generator_info[6]
                    self.MAXIMUM[GENERATOR_ID] = generator_info[7]
                    self.MEAN[GENERATOR_ID] = generator_info[8]
                    self.STDEV[GENERATOR_ID] = generator_info[9]
                    self.INCREASE[GENERATOR_ID] = generator_info[10]
                    self.VALUE_TYPE[GENERATOR_ID] = generator_info[11]
                    self.APPROX_VALUE[GENERATOR_ID] = generator_info[12]
                    self.LOGICAL_VALUE[GENERATOR_ID] = generator_info[13]
                    self.SHUFFLE_STATES[GENERATOR_ID] = generator_info[14]
                    self.SHUFFLE_RANDOM_SEEDS[GENERATOR_ID] = generator_info[15]
                    self.NUMBER_OF_SAMPLES[GENERATOR_ID] = generator_info[16]
                    self.SAMPLES[GENERATOR_ID] = generator_info[17]
                else:
                    raise ValueError(f"MRND for GENERATOR_ID '{GENERATOR_ID}' must contain necessary elements.")
    
    def to_list(self):
        sample_generator_list=[]
        for GENERATOR_ID in self.GENERATOR_ID:
            sample_generator=[self.GENERATOR_ID[GENERATOR_ID], self.PARM_ID[GENERATOR_ID], self.FYI[GENERATOR_ID], self.DISTRIBUTION_TYPE[GENERATOR_ID], self.RANDOM_SEEDS[GENERATOR_ID], self.CONSTANT[GENERATOR_ID], self.MINIMUM[GENERATOR_ID], self.PEAK[GENERATOR_ID], self.MAXIMUM[GENERATOR_ID], self.MEAN[GENERATOR_ID], self.STDEV[GENERATOR_ID], self.INCREASE[GENERATOR_ID], self.VALUE_TYPE[GENERATOR_ID], self.APPROX_VALUE[GENERATOR_ID], self.LOGICAL_VALUE[GENERATOR_ID], self.SHUFFLE_STATES[GENERATOR_ID], self.SHUFFLE_RANDOM_SEEDS[GENERATOR_ID], self.NUMBER_OF_SAMPLES[GENERATOR_ID], self.SAMPLES[GENERATOR_ID]]
            sample_generator_list.append(sample_generator)
        return sample_generator_list
    
    def to_dict(self):
        return self.__dict__
                           
    def __str__(self):      
        result = ""
        for GENERATOR_ID in self.GENERATOR_ID:
            result += (f"GENERATOR_ID: {GENERATOR_ID}\n"
                       f"1 Parameter ID: {self.PARM_ID[GENERATOR_ID]},\n"
                       f"2 FYI: {self.FYI[GENERATOR_ID]},\n"
                       f"3 Distribution Type: {self.DISTRIBUTION_TYPE[GENERATOR_ID]},\n"
                       f"4 Random Seeds: {self.RANDOM_SEEDS[GENERATOR_ID]},\n"
                       f"5 Constant: {self.CONSTANT[GENERATOR_ID]},\n"
                       f"6 Minimum: {self.MINIMUM[GENERATOR_ID]},\n"
                       f"7 Peak: {self.PEAK[GENERATOR_ID]},\n"
                       f"8 Maximum: {self.MAXIMUM[GENERATOR_ID]},\n"
                       f"9 Mean: {self.MEAN[GENERATOR_ID]},\n"
                       f"10 Stdev: {self.STDEV[GENERATOR_ID]},\n"
                       f"11 Increase: {self.INCREASE[GENERATOR_ID]},\n"
                       f"12 Value Type: {self.VALUE_TYPE[GENERATOR_ID]},\n"
                       f"13 Approx Value: {self.APPROX_VALUE[GENERATOR_ID]},\n"
                       f"14 Logical Value: {self.LOGICAL_VALUE[GENERATOR_ID]},\n"
                       f"15 Shuffle State: {self.SHUFFLE_STATES[GENERATOR_ID]},\n"
                       f"16 Shuffle Random Seeds: {self.SHUFFLE_RANDOM_SEEDS[GENERATOR_ID]},\n"
                       f"17 Number of Samples: {self.NUMBER_OF_SAMPLES[GENERATOR_ID]},\n"
                       f"18 Samples: {self.SAMPLES[GENERATOR_ID]}\n"
                       f"\n")   
        return result


# create sample generator.
def INPUT_SAMPLE_GENERATOR_INFO(SAMPLE_GENERATOR_INFO, GENERATOR_ID, PRE_PARM_INFO_ID=None, FYI=None, DISTRIBUTION_TYPE=None, RANDOM_SEEDS=None, CONSTANT=None, MINIMUM=None, PEAK=None, MAXIMUM=None, MEAN=None, STDEV=None, INCREASE=None, VALUE_TYPE=None, APPROX_VALUE=None, LOGICAL_VALUE=None, SHUFFLE_STATES=True, SHUFFLE_RANDOM_SEEDS=None, NUMBER_OF_SAMPLES=None, SAMPLES=None):

    if SAMPLES is not None:
        SAMPLES=np.array(SAMPLES)
    else:
        SAMPLES=np.array([])
    
    if SAMPLE_GENERATOR_INFO is not None:
        for key, value in SAMPLE_GENERATOR_INFO.items():
            FYI = value[1] if value[1] is not None else FYI
            DISTRIBUTION_TYPE = value[2] if value[2] is not None else DISTRIBUTION_TYPE
            RANDOM_SEEDS = value[3] if value[3] is not None else RANDOM_SEEDS
            CONSTANT = value[4] if value[4] is not None else CONSTANT
            MINIMUM = value[5] if value[5] is not None else MINIMUM
            PEAK = value[6] if value[6] is not None else PEAK
            MAXIMUM = value[7] if value[7] is not None else MAXIMUM
            MEAN = value[8] if value[8] is not None else MEAN
            STDEV = value[9] if value[9] is not None else STDEV
            INCREASE = value[10] if value[10] is not None else INCREASE
            VALUE_TYPE = value[11] if value[11] is not None else VALUE_TYPE
            APPROX_VALUE = value[12] if value[12] is not None else APPROX_VALUE
            LOGICAL_VALUE = value[13] if value[13] is not None else LOGICAL_VALUE
            SHUFFLE_STATES = value[14] if value[14] is not True else SHUFFLE_STATES
            SHUFFLE_RANDOM_SEEDS = value[15] if value[15] is not None else SHUFFLE_RANDOM_SEEDS
            NUMBER_OF_SAMPLES = value[16] if value[16] is not None else NUMBER_OF_SAMPLES
            SAMPLES = value[17] if value[17] is not None else SAMPLES

    
    
    sample_generator_info={str(GENERATOR_ID): [PRE_PARM_INFO_ID, FYI, DISTRIBUTION_TYPE, RANDOM_SEEDS, CONSTANT, MINIMUM, PEAK, MAXIMUM, MEAN, STDEV, INCREASE, VALUE_TYPE, APPROX_VALUE, LOGICAL_VALUE, SHUFFLE_STATES, SHUFFLE_RANDOM_SEEDS, NUMBER_OF_SAMPLES, SAMPLES]}
    
    return sample_generator_info


# generating the samples
def GENERATING_SAMPLES(SAMPLE_GENERATOR_INFO):
    for key, value in SAMPLE_GENERATOR_INFO.items(): 
        SAMPLE_GENERATOR_INFO[key][0]=[]
    sample_generator = SAMPLE_GENERATOR_DICT(SAMPLE_GENERATOR_INFO)
    for GENERATOR_ID in sample_generator.GENERATOR_ID:
        distribution_type=sample_generator.DISTRIBUTION_TYPE[GENERATOR_ID]
        random_seeds=sample_generator.RANDOM_SEEDS[GENERATOR_ID]
        constant=sample_generator.CONSTANT[GENERATOR_ID]
        minimum=sample_generator.MINIMUM[GENERATOR_ID]
        peak=sample_generator.PEAK[GENERATOR_ID]
        maximum=sample_generator.MAXIMUM[GENERATOR_ID]
        mean=sample_generator.MEAN[GENERATOR_ID]
        stdev=sample_generator.STDEV[GENERATOR_ID]
        increase=sample_generator.INCREASE[GENERATOR_ID]
        value_type=sample_generator.VALUE_TYPE[GENERATOR_ID]
        approx_value=sample_generator.APPROX_VALUE[GENERATOR_ID]
        logical_value=sample_generator.LOGICAL_VALUE[GENERATOR_ID]
        shuffle_states=sample_generator.SHUFFLE_STATES[GENERATOR_ID]
        shuffle_random_seeds=sample_generator.SHUFFLE_RANDOM_SEEDS[GENERATOR_ID]
        number_of_samples=sample_generator.NUMBER_OF_SAMPLES[GENERATOR_ID]
        samples=sample_generator.SAMPLES[GENERATOR_ID]

        if samples.size == 0: 
            # adjust the value
            # default distribution type
            if distribution_type is None:
                distribution_type = "LINEAR"
                sample_generator.DISTRIBUTION_TYPE[GENERATOR_ID] = distribution_type
            
            if distribution_type == "CONSTANT" and constant is None:
                constant=(minimum+maximum)/2
                sample_generator.CONSTANT[GENERATOR_ID] = constant
                
            # maximum and minimum value
            if constant != None:
                minimum=None
                maximum=None
                sample_generator.MINIMUM[GENERATOR_ID] = minimum
                sample_generator.MAXIMUM[GENERATOR_ID] = maximum
            
            # create sampling random seeds
            if random_seeds is None:
                random_seeds_list=GET_VALUE('SEEDS')
                random_seeds=random_seeds_list[0]
                sample_generator.RANDOM_SEEDS[GENERATOR_ID] = random_seeds
                SET_VALUE('SEEDS', random_seeds_list[1:])
                
            # create shuffle random seeds
            if shuffle_states is True:
                if shuffle_random_seeds is None:
                    random_seeds_list=GET_VALUE('SEEDS')
                    shuffle_random_seeds = random_seeds_list[0]
                    SET_VALUE('SEEDS',random_seeds_list[1:])
            sample_generator.SHUFFLE_RANDOM_SEEDS[GENERATOR_ID] = shuffle_random_seeds
            
            # refine the sample with value type
            if value_type is None:
                value_type = "APPROX"
                sample_generator.VALUE_TYPE[GENERATOR_ID] = value_type
                approx_value = float(0.01)
                sample_generator.APPROX_VALUE[GENERATOR_ID] = approx_value
                
            # retrieve parameters
            if number_of_samples is None:
                number_of_samples=GET_VALUE("NUMBER_OF_CASES")
                sample_generator.NUMBER_OF_SAMPLES[GENERATOR_ID] = number_of_samples
            
            # sample generation process
            np.random.seed(random_seeds)
            # Distribution name list
            distribution_namelist={"CONSTANT", "LINEAR", "UNIFORM", "TRIANGLE", "NORMAL", "LOG_NORMAL", "USER_DEFINE"}
            # Iterate through the distribution names and apply the corresponding function
            for distribution_name in distribution_namelist:
                if distribution_type == distribution_name:
                    sample_generator.SAMPLES[GENERATOR_ID] = distribution_functions[distribution_name](constant, minimum, peak, maximum, mean, stdev, increase, samples, number_of_samples)
                    print("GENERATOR_ID =", GENERATOR_ID)
                    print(f"{distribution_name}: Successfully applied")
                    found = True
                    break 
            if not found:
                print("No function found for the given distribution type")
            
            # sample refining and shuffling process
            samples=sample_generator.SAMPLES[GENERATOR_ID]
            # value type name list
            value_type_namelist={"INTEGER", "APPROX", "REAL", "STRING", "LOGICAL"}
            # Iterate through the value type names and apply the corresponding function
            for value_type_name in value_type_namelist:
                if value_type == value_type_name:
                    samples_after_refine = value_type_functions[value_type_name](samples, approx_value, logical_value)
                    if shuffle_states is not True:
                        samples_after_refine
                    else:
                        np.random.seed(shuffle_random_seeds)
                        np.random.shuffle(samples_after_refine)
                    sample_generator.SAMPLES[GENERATOR_ID] = samples_after_refine
                    print(f"{value_type_name}: Successfully applied")
                    found = True
                    break 
            if not found:
                print("No function found for the given value type")
            
        
    return sample_generator


def SAVE_SAMPLING_SAMPLES(PARAMETER_OUTPUTS, SAMPLE_GENERATOR):
    
    Parameter_outputs = PARAMETER_OUTPUTS
    # Update information from SAMPLE_GENERATOR
    for key, value in SAMPLE_GENERATOR.GENERATOR_ID.items(): 
            Parameter_outputs.GENERATOR_ID.append(value)
    for key, value in SAMPLE_GENERATOR.RANDOM_SEEDS.items(): 
            Parameter_outputs.RANDOM_SEEDS.append(value)
    for key, value in SAMPLE_GENERATOR.SHUFFLE_STATES.items(): 
            Parameter_outputs.SHUFFLE_STATES.append(value)
    for key, value in SAMPLE_GENERATOR.SHUFFLE_RANDOM_SEEDS.items(): 
            Parameter_outputs.SHUFFLE_RANDOM_SEEDS.append(value)
    for key, value in SAMPLE_GENERATOR.NUMBER_OF_SAMPLES.items(): 
            Parameter_outputs.NUMBER_OF_SAMPLES.append(value)
    for key, value in SAMPLE_GENERATOR.SAMPLES.items(): 
            Parameter_outputs.SAMPLES.append(value)
    for key, value in SAMPLE_GENERATOR.PARM_ID.items(): 
            value.append(Parameter_outputs.ID)
        
    return 
            
        
# =====data sampling methods========
# LHS_uniform 
def UNIFORM(constant, minimum, peak, maximum, mean, stdev, increase, samples, number_of_samples):
    "This function generates N uniformly distributed samples in the interval [MINIMUM, MAXIMUM]."
    "Args: MINIMUM: The lower bound of the interval.  MAXIMUM: The upper bound of the interval. NUMBER_OF_SAMPLES: The number of samples to generate."
    if minimum == maximum:
        raise ValueError(f"DISTRIBUTION_TYPE should be CONSTANT when MINIMUM equals to MAXIMUM.")
    else:
        x = np.zeros(number_of_samples)
        sample = np.zeros(number_of_samples)
        interval = (1-0)/number_of_samples
        r = np.random.rand(number_of_samples)
        for i in range(number_of_samples):
            x[i] = (i + r[i]) * interval
            sample[i] = uniform.ppf(x[i],loc=minimum, scale=maximum-minimum)
            uniform_samples=sample

    return uniform_samples


# LHS_uniform_discrete
def LINEAR(constant, minimum, peak, maximum, mean, stdev, increase, samples, number_of_samples):
    "This function generates N uniformly distributed samples in the interval [L, H] in a linear form."
    "Args: MINIMUM: The lower bound of the interval.  MAXIMUM: The upper bound of the interval. NUMBER_OF_SAMPLES: The number of samples to generate."
    if increase==None:
        sample = np.linspace(minimum, maximum, number_of_samples)
        linear_samples=sample
    else:
        sample = np.arange(minimum, maximum + 1/(10**15), increase) 
        linear_samples=sample
        
    return linear_samples


# LHS_normal
def NORMAL(constant, minimum, peak, maximum, mean, stdev, increase, samples, number_of_samples):
    "This function generates NUMBER_OF_SAMPLES normally distributed samples in the interval [MINIMUM, MAXIMUM]."
    "Args: MINIMUM: The lower bound of the interval.  MAXIMUM: The upper bound of the interval." 
    "Args: MEAN is the mean; and STDEV is the standard deviation; NUMBER_OF_SAMPLES is the number of samples to generate." 
    
    x=np.zeros(number_of_samples)
    sample=np.zeros(number_of_samples)
    PLL=norm.cdf(minimum,mean,stdev)
    PUL=norm.cdf(maximum,mean,stdev)
    Interval=(PUL-PLL)/number_of_samples

    r=np.random.rand(number_of_samples)

    for i in range(number_of_samples):
        x[i]=PLL+(i+r[i])*Interval
        sample[i]=norm.ppf(x[i],mean,stdev)
        norm_samples=sample
        
    return norm_samples


# LHS_lognormal
def LOG_NORMAL(constant, minimum, peak, maximum, mean, stdev, increase, samples, number_of_samples):
    "This function generates N lognormally distributed samples in the interval [MINIMUM, MAXIMUM]."
    "Args: MINIMUM: The lower bound of the interval.  MAXIMUM: The upper bound of the interval." 
    "Args: MEAN is the mean; and STDEV is the standard deviation; NUMBER_OF_SAMPLES is the number of samples to generate." 
    
    x=np.zeros(number_of_samples)
    sample=np.zeros(number_of_samples)
    PLL=lognorm.cdf(minimum, stdev, mean, math.exp(mean))
    PUL=lognorm.cdf(maximum, stdev, mean, math.exp(mean))
    Interval=(PUL-PLL)/number_of_samples

    r=np.random.rand(number_of_samples)
    
    for i in range(number_of_samples):
        x[i]=PLL+(i+r[i])*Interval
        sample[i]=lognorm.ppf(x[i], stdev, mean, math.exp(mean))
        lognorm_samples=sample
    
    return lognorm_samples


# LHS_triangular
def TRIANGLE(constant, minimum, peak, maximum, mean, stdev, increase, samples, number_of_samples):
    "This function generates N triangularlly distributed samples in the interval [MINIMUM, PEAK, MAXIMUM]."
    "Args: MINIMUM: The lower bound of the interval.  PEAK:The middle bound of the interval. MAXIMUM: The upper bound of the interval." 
    
    x=np.zeros(number_of_samples)
    sample=np.zeros(number_of_samples)
    Interval=(1-0)/number_of_samples
    
    r=np.random.rand(number_of_samples)
    
    for i in range(number_of_samples):
        x[i]=(i+r[i])*Interval
        sample[i] = triang.ppf(x[i], c=(peak-minimum)/(maximum-minimum), loc=minimum ,scale=maximum-minimum)
        triangular_samples=sample
    
    return triangular_samples
      
# user_define
def USER_DEFINE(constant, minimum, peak, maximum, mean, stdev, increase, samples, number_of_samples):
    "This function generates a distribution as user given."
    
    sample=samples
    user_define_samples=sample
    
    return user_define_samples


# constant
def CONSTANT(constant, minimum, peak, maximum, mean, stdev, increase, samples, number_of_samples):
    "This function generates a distribution with number of samples repetitions of the constant."
    
    sample = np.full(number_of_samples, constant)
    constant_samples=sample
    
    return constant_samples


# Create a mapping dictionary
distribution_functions = {
    "CONSTANT": CONSTANT,
    "LINEAR": LINEAR,
    "UNIFORM": UNIFORM,
    "TRIANGLE": TRIANGLE,
    "NORMAL": NORMAL,
    "LOG_NORMAL": LOG_NORMAL,
    "USER_DEFINE": USER_DEFINE
}


# =====value type methods========
# INTEGER
def INTEGER(SAMPLES, APPROX_VALUE, LOGICAL_VALUE):
    sample_after_refine=np.round(SAMPLES)
    return sample_after_refine


# APPROX
def APPROX(SAMPLES, APPROX_VALUE, LOGICAL_VALUE):
    sample_after_refine = []
    for num in SAMPLES:
        divided_by_approx_value = num / APPROX_VALUE
        rounded_integer = round(divided_by_approx_value)
        rounded_value = rounded_integer * APPROX_VALUE
        rounded_value = round(rounded_value, 10)
        sample_after_refine.append(rounded_value)
    sample_after_refine=np.array(sample_after_refine)
    return sample_after_refine


# REAL
def REAL(SAMPLES, APPROX_VALUE, LOGICAL_VALUE):
    sample_after_refine = np.round(SAMPLES, 10)
    return sample_after_refine


# STRING
def STRING(SAMPLES, APPROX_VALUE, LOGICAL_VALUE):
    sample_after_refine = [str(num) for num in SAMPLES]
    return sample_after_refine


# LOGICAL
def LOGICAL(SAMPLES, APPROX_VALUE, LOGICAL_VALUE):
    sample_after_refine = np.array([1 if num >= LOGICAL_VALUE else 0 for num in SAMPLES])
    return sample_after_refine


# Create a mapping dictionary
value_type_functions = {
    "INTEGER": INTEGER,
    "APPROX": APPROX,
    "REAL": REAL,
    "STRING": STRING,
    "LOGICAL": LOGICAL
}

