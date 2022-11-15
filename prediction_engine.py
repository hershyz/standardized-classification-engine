import sqrt_distance_classifier
import abs_distance_classifier
import percent_distance_classifier
import stddev_classifier
import knn

# returns a converted point from a dataframe 
def convert_point(point, int_map):
    converted = []
    for x in point:
        if x in int_map:
            converted.append(int_map[x])
        else:
            converted.append(x)
    return converted


# predict function
def predict(point, model):
    
    converted = convert_point(point, model.int_map)

    if model.algorithm == 'sqrt_distance_classifier':
        return sqrt_distance_classifier.classify(converted, model.mean_map)
    
    if model.algorithm == 'abs_distance_classifier':
        return abs_distance_classifier.classify(converted, model.mean_map)
    
    if model.algorithm == 'percent_distance_classifier':
        return percent_distance_classifier.classify(converted, model.mean_map)
    
    if model.algorithm == 'stddev_distance_classifier':
        return stddev_classifier.classify(converted, model.stddev_map, model.mean_map)
    
    if model.algorithm == 'knn':
        return knn.classify(converted, model.df_sampled)