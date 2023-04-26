def is_isogram(string):
    new_arr = []

    for val in list(string):
        if not val.isalpha():
            continue

        val = val.lower()
        if val not in new_arr:
            new_arr.append(val)
        else:
            return False

    return True
