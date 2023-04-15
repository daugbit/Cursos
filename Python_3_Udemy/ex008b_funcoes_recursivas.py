import bip39


def recursiva(end=0, __v1=0, __v2=1):
    print(__v1)
    __v1 += __v2
    __v2, __v1 = __v1, __v2
    if __v1 > end:
        return None
    return recursiva(end, __v1, __v2)


recursiva(1000000)
