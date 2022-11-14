# imports
import common_model_lib
import dataframe
import numerical_feature_converter
import common_model_lib
import data_sampler
import model
import sqrt_distance_classifier
import abs_distance_classifier
import percent_distance_classifier
import stddev_classifier
import knn


# main brute force algorithm for different classification techniques:
def get_model(dataset):


    # get a converted dataframe and sampled data:
    df_raw = dataframe.get_dataframe(dataset)
    int_map = numerical_feature_converter.int_map(df_raw)
    df = numerical_feature_converter.convert_dataframe(df_raw, int_map)
    mean_map = common_model_lib.mean_map(df)
    stddev_map = common_model_lib.stddev_map(df)
    sampled_data = data_sampler.sampled_dataframe(df, 1) # use 100% ratio (1) for testing purposes, downscale later when we want smaller models


    # get actual outputs:
    actual = []
    for point in df:
        actual.append(point[len(point) - 1])

    # test sqrt distance classifier:
    sqrt_distance_classifier_predictions = []
    for point in df:
        sqrt_distance_classifier_predictions.append(sqrt_distance_classifier.classify(point, mean_map))
    sqrt_distance_accuracy = common_model_lib.eval(actual, sqrt_distance_classifier_predictions)
    print('sqrt distance classifier accuracy: ' + str(sqrt_distance_accuracy))

    # test abs distance classifier:
    abs_distance_classifier_predictions = []
    for point in df:
        abs_distance_classifier_predictions.append(abs_distance_classifier.classify(point, mean_map))
    abs_distance_accuracy = common_model_lib.eval(actual, abs_distance_classifier_predictions)
    print('abs distance classifier accuracy: ' + str(abs_distance_accuracy))

    # test percent distance classifier:
    percent_distance_classifier_predictions = []
    for point in df:
        percent_distance_classifier_predictions.append(percent_distance_classifier.classify(point, mean_map))
    percent_distance_accuracy = common_model_lib.eval(actual, percent_distance_classifier_predictions)
    print('percent distance classifier accuracy: ' + str(percent_distance_accuracy))

    # test stddev classifier:
    steddev_classifier_predictions = []
    for point in df:
        steddev_classifier_predictions.append(stddev_classifier.classify(point, stddev_map, mean_map))
    stddev_distance_accuracy = common_model_lib.eval(actual, steddev_classifier_predictions)
    print('stddev classifier accuracy: ' + str(stddev_distance_accuracy))

    # test knn:
    knn_predictions = []
    for point in df:
        knn_predictions.append(knn.classify(point, sampled_data))
    knn_accuracy = common_model_lib.eval(actual, knn_predictions)
    print('knn accuracy: ' + str(knn_accuracy))


    # find max accuracy:
    acc_map = {}
    acc_map['sqrt_distance_classifier'] = sqrt_distance_accuracy
    acc_map['abs_distance_classifier'] = abs_distance_accuracy
    acc_map['percent_distance_classifier'] = percent_distance_accuracy
    acc_map['stddev_classifier_accuracy'] = stddev_distance_accuracy
    acc_map['knn'] = knn_accuracy

    max = 0
    max_algo = ''
    for algo in acc_map:
        if acc_map[algo] > max:
            max = acc_map[algo]
            max_algo = algo
    
    print('max accuracy: ' + max_algo + ' (' + str(acc_map[max_algo]) + ')')