import common_model_lib
import dataframe
import numerical_feature_converter
import common_model_lib
import data_sampler
import model
import sqrt_distance_classifier
import abs_distance_classifier

# main brute force algorithm for different classification techniques:
def get_model(dataset):

    # get a converted dataframe and sampled data:
    df_raw = dataframe.get_dataframe(dataset)
    int_map = numerical_feature_converter.int_map(df_raw)
    df = numerical_feature_converter.convert_dataframe(df_raw, int_map)
    mean_map = common_model_lib.mean_map(df)
    sampled_data = data_sampler.sampled_dataframe(df, 1) # use 100% ratio (1) for testing purposes, downscale later when we want smaller models

    # get actual outputs:
    actual = []
    for point in df:
        actual.append(point[len(point) - 1])

    # test sqrt distance classifier:
    sqrt_distance_classifier_predictions = []
    for point in df:
        sqrt_distance_classifier_predictions.append(sqrt_distance_classifier.classify(point, mean_map))
    print('sqrt distance classifier accuracy: ' + str(common_model_lib.eval(actual, sqrt_distance_classifier_predictions)))

    # test abs distance classifier:
    abs_distance_classifier_predictions = []
    for point in df:
        abs_distance_classifier_predictions.append(abs_distance_classifier.classify(point, mean_map))
    print('abs distance classifier accuracy: ' + str(common_model_lib.eval(actual, abs_distance_classifier_predictions)))