import random

# helper function, finds sample n with unique indices:
def get_sample_indices(n):
    indices = []
    while True:
        i = random.randint(0, n - 1)
        if i not in indices:
            indices.append(i)
        if len(indices) == n:
            return indices

# returns a sampled numerical dataframe with ratio*freq random instances of each category:
def sampled_dataframe(df_converted, ratio):

    # count instances
    freqs = {}
    points = {}
    for point in df_converted:
        cat = point[len(point) - 1]
        if cat in freqs:
            freqs[cat] += 1
            points[cat].append(point)
        else:
            freqs[cat] = 1
            points[cat] = [point]
    
    df_sampled = []
    for cat in freqs:
        size = int(ratio * freqs[cat])
        indices = get_sample_indices(size)
        for i in indices:
            df_sampled.append(points[cat][i])
    
    return df_sampled