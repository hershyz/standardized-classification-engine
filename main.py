from cProfile import label
import dataframe
import numerical_feature_converter
import common_model

raw = dataframe.get_dataframe('data/healthcare-dataset-stroke-data.csv')
label_map = numerical_feature_converter.int_map(raw)
df = numerical_feature_converter.convert_dataframe(raw, label_map)
mean_map = common_model.mean_map(df)
print('mean map: ' + str(mean_map))