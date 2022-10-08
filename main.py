import dataframe
import numerical_feature_converter
import data_sampler
import common_model_lib
import prediction_engine
import model

# get neccesary components
df = dataframe.get_dataframe('data/drug200.csv')
int_map = numerical_feature_converter.int_map(df)
df_converted = numerical_feature_converter.convert_dataframe(df, int_map)
mean_map = common_model_lib.mean_map(df_converted)
df_sampled = data_sampler.sampled_dataframe(df_converted, 0.2)

# create and cache model
model = model.Model(mean_map, int_map, df_sampled, 'test-debug')
common_model_lib.cache(model, 'testmodel')