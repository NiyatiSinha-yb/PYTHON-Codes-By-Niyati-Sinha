
def find_max(list):
    max=list[0]
    for item in list:
        if max<item:
            max=item
    return max
