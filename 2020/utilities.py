def input_to_list(fname):
    """
    Parses the input file fname into a list of strings with newline stripped.
    User is responsible for casting into the appropriate format.
    :param fname:
    :return:
    """
    with open(f'input_files/{fname}') as f:
        data = f.read().strip().splitlines()
    return data
