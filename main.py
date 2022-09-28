import dataframe
import numerical_feature_converter
import common_model
import prediction_engine

df = dataframe.get_dataframe('data/drug200.csv')
int_map = numerical_feature_converter.int_map(df)
print(int_map)
print('raw: ' + str(df[0]))
print('converted: ' + str(prediction_engine.convert_point(df[0], int_map)))