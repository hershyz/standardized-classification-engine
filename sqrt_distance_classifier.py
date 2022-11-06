import math

def classify(point, mean_map):

    dists = {}

    for cat in mean_map:
        mean_point = mean_map[cat]
        cat_dist = 0
        for i in range(len(mean_point)):
            cat_dist += abs((float(mean_point[i]) - float(point[i])) ** 2)
        dists[cat] = math.sqrt(cat_dist)

    min = 10000000000
    min_cat = ''
    for cat in dists:
        if dists[cat] < min:
            min_cat = cat
            min = dists[cat]
    
    return min_cat


def classify_std(point, stddev_map, mean_map):

    dists = {}

    index = 0
    for cat in mean_map:
        mean_point = mean_map[cat]
        cat_dist = 0
        for i in range(len(mean_point)):
            cat_dist += abs((float(mean_point[i]) - float(point[i])) ** 2) * (1 / stddev_map[index])
        index += 1
        dists[cat] = math.sqrt(cat_dist)
    
    min = 10000000000
    min_cat = ''
    for cat in dists:
        if dists[cat] < min:
            min_cat = cat
            min = dists[cat]
    
    return min_cat