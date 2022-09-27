# get the feature map for conversion (arguments: dataframe):
def int_map(df):
    n = 0
    map = {}
    for point in df:
        for i in range(0, len(point) - 1):
            feature = point[i]
            try:
                num = float(feature)
            except:
                if feature not in map:
                    map[feature] = n
                    n += 1
    
    return map

# use feature map to convert dataframe (argunments: dataframe, map):
def convert_dataframe(df, map):
    df_converted = []
    for point in df:
        converted_point = []
        for feature in point:
            if feature in map:
                converted_point.append(map[feature])
            else:
                converted_point.append(feature)
        df_converted.append(converted_point)

    return df_converted