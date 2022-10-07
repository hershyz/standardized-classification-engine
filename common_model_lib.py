# return a map of means of position arguments per unique category
def mean_map(df):
    
    # initialize the map
    n_features = len(df[0]) - 1
    cat_freqs = {}

    for i in range(0, len(df)):
        curr_cat = df[i][len(df[0]) - 1]
        if curr_cat in cat_freqs:
            cat_freqs[curr_cat] += 1
        if curr_cat not in cat_freqs:
            cat_freqs[curr_cat] = 0

    init_arr = []
    for i in range(0, n_features):
        init_arr.append(0)
    
    map = {}
    for cat in cat_freqs:
        map[cat] = init_arr
    

    # sum values in the map
    for point in df:
        curr_cat = point[len(point) - 1]
        arr = map[curr_cat]
        for i in range(0, len(point) - 1):
            arr[i] += float(point[i])
        map[curr_cat] = arr
    

    # divide by frequencies of unique categories to find averages
    for cat in map:
        arr = map[cat]
        for i in range(0, len(arr)):
            arr[i] /= cat_freqs[cat]
        map[cat] = arr
    
    return map