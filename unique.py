def unique_values(x):
    y = set(x)

    if len(y) == len(x):
        return True
    if len(y) != len(x):
        return False