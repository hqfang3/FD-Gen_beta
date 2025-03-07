def _INIT():
    global _global_dict
    _global_dict = {}
    return
    
def SET_VALUE(key,value):
    _global_dict[key] = value
    return
    
def GET_VALUE(key, defValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue
    