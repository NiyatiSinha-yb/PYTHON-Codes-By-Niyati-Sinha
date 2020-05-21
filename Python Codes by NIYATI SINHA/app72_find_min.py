
def find_min(list):
    min=list[0]
    for item in list:
        if min>item:
            min=item
    return min
