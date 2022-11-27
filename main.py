import common_model_lib
import dataframe
import numerical_feature_converter

model = common_model_lib.parse_model('drug200.mlmodel')
df_raw = dataframe.get_dataframe('data/drug200.csv')
int_map = numerical_feature_converter.int_map(df_raw)
df_converted = numerical_feature_converter.convert_dataframe(df_raw, int_map)
print(df_converted)
test_accuracy = common_model_lib.test_model(model, df_converted)
print('test accuracy: ' + str(test_accuracy))