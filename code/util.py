def parsed_arguments_dict(my_args):
    keys = [key for key in dir(my_args) if key[0] != '_']
    dict = {}
    for key in keys:
        dict[key] = eval('my_args.' + str(key))
    return dict
