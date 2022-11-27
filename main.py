import training_engine
import common_model_lib
import dataframe
import numerical_feature_converter

dataset = 'benchmark-data/stars.csv'

# train:
model = training_engine.get_model(dataset)