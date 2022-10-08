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


# caches the model as a file (given the best classification algorithm):
def cache(model, name):

    # create file and specify classificaiton algorithm:
    f = open(name+'.mlmodel', 'w')
    f.write('algorithm: ' + model.algorithm + '\n')

    # write mean map data:
    f.write('mean_map:\n')
    mean_map = model.mean_map
    for cat in mean_map:
        data = cat + ','
        means = mean_map[cat]
        for i in range(0, len(means)):
            data += str(means[i])
            if i != len(means) - 1:
                data += ','
        f.write(data + '\n')
    
    # write int map conversion data:
    f.write('int_map:\n')
    int_map = model.int_map
    for data in int_map:
        f.write(data + ',' + str(int_map[data]) + '\n')
    
    # write df sampled data:
    f.write('df_sampled:\n')
    df_sampled = model.df_sampled
    for i in range(0, len(df_sampled)):
        point = str(df_sampled[i])
        point = str.replace(point, '[', '')
        point = str.replace(point, ']', '')
        point = str.replace(point, '\'', '')
        f.write(point + '\n')