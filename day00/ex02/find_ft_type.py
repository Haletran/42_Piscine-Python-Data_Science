def all_thing_is_obj(object: any) -> int:
    if isinstance(object, str):
        print(f"{object} is in the kitchen : <class 'str'>")
    elif isinstance(object, (list, tuple, set, dict)):
        if (type(object) is list):    
            print(f"List : {type(object)}")
        elif (type(object) is tuple):
            print(f"Tuple : {type(object)}")
        elif (type(object) is set):
            print(f"Set : {type(object)}")
        elif (type(object) is dict):
            print(f"Dict : {type(object)}")
    else:
        print("Type not found")
        return 42
    return 0
