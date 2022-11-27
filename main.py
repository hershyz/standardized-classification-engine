import training_engine
import common_model_lib
import dataframe
import numerical_feature_converter

dataset = 'benchmark-data/stars.csv'

# train:
model = training_engine.get_model(dataset)

# test:
df_raw = dataframe.get_dataframe(dataset)
int_map = numerical_feature_converter.int_map(df_raw)
df_converted = numerical_feature_converter.convert_dataframe(df_raw, int_map)
test_accuracy = common_model_lib.test_model(model, df_converted)
print('testing accuracy: ' + str(test_accuracy))