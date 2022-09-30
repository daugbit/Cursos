def dados(info):
    if not info.isdigit() or info == '':
        return False
    else:
        return float(info)
