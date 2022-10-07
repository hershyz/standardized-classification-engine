import dataframe
import numerical_feature_converter
import data_sampler
import common_model_lib
import prediction_engine

df = dataframe.get_dataframe('data/drug200.csv')
int_map = numerical_feature_converter.int_map(df)
df_converted = numerical_feature_converter.convert_dataframe(df, int_map)
df_sampled = data_sampler.sampled_dataframe(df_converted, 0.2)
for point in df_sampled:
    print(point)