import re

"Part 1: General syntax algorithm."
# break the script
def break_script(script):
    output_namelist_lines=[]
    for line,num in zip(script,range(len(script))):
        line=line.decode('UTF-8').strip()
        pattern = r'^&(\w+)\s*(.*)'
        match = re.match(pattern, line)
        if match:
            if len(match.group(1)) != 4:
                raise ValueError(f"Invalid syntax found.")
            else:
                output_namelist_lines.append(num)
    
    # output grouped lines
    valid_line_grouped_list = []
    for index in range(1,len(output_namelist_lines)):
        valid_line_grouped_list.append(list(range(output_namelist_lines[index-1], output_namelist_lines[index])))
    valid_line_grouped_list.append(list(range(output_namelist_lines[-1], len(script))))
    
    # output valid script
    valid_script=[]
    for grouped_lines in valid_line_grouped_list:
        lines=[script[i].decode('UTF-8').strip() for i in grouped_lines]
        temp_script='\n'.join(lines)
        temp_script = temp_script.replace("\n", ", ").strip()
        valid_script.append(temp_script)
    
    return valid_line_grouped_list, valid_script


# parse the valid script lines
def parse_script_lines(line):
    # parse custom syntax using regular expressions
    pattern1 = r'^&(\w+)\s*(.*)'
    match1 = re.match(pattern1, line)
    pattern2 = r'^\s(\s{4})'
    match2 = re.match(pattern2, line)
    
    if match1:
        function_name = match1.group(1)
        params_str = match1.group(2)
        if '/' in params_str:
            params_str=params_str.split('/')[0]
        params = parse_params(params_str)
        # modify
        if 'ID' in params: 
            if isinstance(params['ID'], list):
                params['ID'] =''.join(params['ID'])
        if 'FYI' in params: 
            if isinstance(params['FYI'], list):
                params['FYI'] =''.join(params['FYI'])
        return function_name, params
    
    elif match2:
        function_name = '    '
        params_str = line[5:]
        if '/' in params_str:
            params_str=params_str.split('/')[0]
        params = parse_params(params_str)
        # modify
        if 'ID' in params: 
            if isinstance(params['ID'], list):
                params['ID'] =''.join(params['ID'])
        if 'FYI' in params: 
            if isinstance(params['FYI'], list):
                params['FYI'] =''.join(params['FYI'])
        return function_name, params
    
    else:
        raise ValueError("Invalid script line format")


def parse_params(params_str):
    # Parse parameter pair strings -- key-value pairs
    params = {}
    params_str=re.sub(r'\s*=\s*', '=', params_str)
    parts = re.findall(r'\b[\w():,]+=.*?(?=\s*\b[\w():,]+=|\s*$)', params_str)
    for part in parts:
        part = part.split('=')
        key = part[0].strip()
        space_indices=[]
        quota_indices=[]
        space_indices = [index for index, char in enumerate(part[1]) if char == ' ']
        quota_indices = [index for index, char in enumerate(part[1]) if char == "'"]
        groups_quota_indices = [quota_indices[i:i + 2] for i in range(0, len(quota_indices), 2)]   
        for s_index in space_indices:
            result = any(pair[0]<=s_index<= pair[1] for pair in groups_quota_indices)
            if result is True:
                part[1][s_index]
            else:
                part[1][s_index].replace(' ', '')
        string_value=part[1]
        split_string_value = string_value.split(',')
        # Convert to a list of appropriate types
        mapping = {
            '.FALSE.':'.FALSE.',
            '.TRUE.':'.TRUE.',
            "T":'T',
            "F":'F',
            "None": None,
            "true": True,
            "false": False,
            "True": True,
            "False": False,
            "FALSE": False,
            "TRUE": True
            }
        values=[]
        for value in split_string_value:
            if "'" in value:
                match = re.search(r"'([^']*)'", value)
                if match:
                    value = match.group(1)  # Extracted part
                values.append(value)
            elif value.strip():
                if value in mapping:
                    values.append(mapping[value])
                else:
                    try:
                        if '.' in value:
                            value = float(value)
                        else:
                            value = int(value)
                        values.append(value)
                    except ValueError:
                        pass 
        if len(values)==1:
            values=values[0]
        params[key] = values
    
    return params

"Part 2: replace the potential sentence."
def replace_value(line_content, replaced_args, replaced_after_args, replaced_value):
    # prepare the replaced syntax 
    line_content_replaced=line_content
    replaced_value_str=str(replaced_value)[1:-1]+','+' '
    combined_str = replaced_args + '=' + replaced_value_str
    current_length = len(combined_str)
    
    index_start = line_content.find(replaced_args)
    if replaced_after_args is not None:
        index_end = line_content.find(replaced_after_args)
        spaces_to_add=len(line_content_replaced[index_start:index_end])-current_length
        final_str = combined_str + ' ' * spaces_to_add
        line_content_replaced=line_content_replaced[:index_start]+final_str+line_content_replaced[index_end:]
    else:
        index_end = line_content.find('/')
        if index_end != -1:
            spaces_to_add=len(line_content_replaced[index_start:index_end+1])-current_length
            final_str = combined_str + ' ' * spaces_to_add
            line_content_replaced=line_content_replaced[:index_start]+final_str+line_content_replaced[index_end:]
        else:
            spaces_to_add=len(line_content_replaced[index_start:])-current_length
            final_str = combined_str + ' ' * spaces_to_add
            line_content_replaced=line_content_replaced[:index_start]+final_str
    
    return line_content_replaced
