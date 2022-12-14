from copy import deepcopy
import data_sampler
import prediction_engine
import model


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
        arr = deepcopy(map[curr_cat])
        for i in range(0, len(point) - 1):
            arr[i] += float(point[i])
        map[curr_cat] = arr
    

    # divide by frequencies of unique categories to find averages
    for cat in map:
        arr = deepcopy(map[cat])
        for i in range(0, len(arr)):
            arr[i] /= cat_freqs[cat]
        map[cat] = arr
    
    return map


# return a map of standard deviations per feature
def stddev_map(df):

    mean_map = {}
    map = {}

    # iterate features
    for feature in range(0, len(df[0]) - 1):
        curr_total = 0
        # iterate down the rows
        for row in range(0, len(df)):
            curr_total += float(df[row][feature])
        mean_map[feature] = curr_total / len(df)
    
    # iterate features
    for feature in range(0, len(df[0]) - 1):
        total_diff = 0
        # iterate down the rows
        for row in range(0, len(df)):
            diff = abs(float(df[row][feature]) - mean_map[feature])
            total_diff += diff
        map[feature] = total_diff / len(df)
    
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
    
    # write std dev map data:
    f.write('stddev_map:\n')
    stddev_map = model.stddev_map
    for feature in stddev_map:
        f.write(str(feature) + ',' + str(stddev_map[feature]) + '\n')
    
    # write df sampled data:
    f.write('df_sampled:\n')
    df_sampled = model.df_sampled
    for i in range(0, len(df_sampled)):
        point = str(df_sampled[i])
        point = str.replace(point, '[', '')
        point = str.replace(point, ']', '')
        point = str.replace(point, '\'', '')
        f.write(point + '\n')
    

# parse model:
def parse_model(path):

    f = open(path)
    raw = f.readlines()
    lines = []
    for line in raw:
        line = line.replace('\n', '')
        lines.append(line)

    # get algorithm:
    algorithm = lines[0].split(': ')[1]
    
    # get mean map:
    mean_map = {}
    index = 2
    while lines[index] != 'int_map:':
        raw_arr = lines[index].split(',')
        key = raw_arr[0]
        point_arr = []
        for i in range(1, len(raw_arr)):
            point_arr.append(float(raw_arr[i]))
        mean_map[key] = point_arr
        index += 1
    
    # get int map:
    int_map = {}
    index += 1
    while lines[index] != 'stddev_map:':
        raw_arr = lines[index].split(',')
        key = raw_arr[0]
        num = float(raw_arr[1])
        int_map[key] = num
        index += 1
    
    # get stddev map:
    stddev_map = {}
    index += 1
    while lines[index] != 'df_sampled:':
        raw_arr = lines[index].split(',')
        key = float(raw_arr[0])
        num = float(raw_arr[1])
        stddev_map[key] = num
        index += 1
    
    # get sampled df:
    df_sampled = []
    index += 1
    for i in range(index, len(lines)):
        if len(lines[i]) == 0:
            break
        raw_arr = lines[i].split(',')
        point_arr = []
        for j in range(0, len(raw_arr) - 1):
            point_arr.append(float(raw_arr[j]))
        point_arr.append(raw_arr[len(raw_arr) - 1])
        df_sampled.append(point_arr)
    
    parsed_model = model.Model(mean_map, int_map, stddev_map, df_sampled, algorithm)
    return parsed_model


# evaluate accuracy:
def eval(actual, predicted):
    total = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            total += 1
    return total / len(actual)


# evaluate model:
def test_model(model, df_converted):
    df_sampled = data_sampler.sampled_dataframe(df_converted, 0.2)
    correct = 0
    for point in df_sampled:
        actual = point[len(point) - 1]
        predicted = prediction_engine.predict(point, model)
        if str(predicted) == str(actual):
            correct += 1
    return correct / len(df_sampled)