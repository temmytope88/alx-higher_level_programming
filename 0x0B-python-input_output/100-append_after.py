""" module of a function that appends to a
    specific line
"""
def append_after(filename="", search_string="", new_string=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        search_string (str, optional): _description_. Defaults to "".
        new_string (str, optional): _description_. Defaults to "".
    """
    with open(filename, "a+", encoding="utf-8") as f:
        data = f.readline()
        for line in data:
            print(line)
            if search_string in line:
                f.write(new_string)
