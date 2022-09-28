# returns a converted point from a dataframe 
def convert_point(point, int_map):
    converted = []
    for x in point:
        if x in int_map:
            converted.append(int_map[x])
        else:
            converted.append(x)
    return converted