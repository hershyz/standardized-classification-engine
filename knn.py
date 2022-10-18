import math

def classify(point, df):

    distances = []

    for row in df:
        curr_distance = 0
        for i in range(0, len(row) - 1):
            curr_distance += abs(float(row[i]) - float(point[i])) ** 2
        curr_distance = math.sqrt(curr_distance)
        distances.append([curr_distance, row[len(row) - 1]])
    
    distances = sorted(distances, key=lambda x : x[0])

    freqs = {}
    for i in range(0, 5): # k = 5
        if distances[i][1] in freqs:
            freqs[distances[i][1]] += 1
        else:
            freqs[distances[i][1]] = 1

    max = 0
    max_cat = ''
    for cat in freqs:
        if freqs[cat] > max:
            max = freqs[cat]
            max_cat = cat
    
    return max_cat