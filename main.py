import training_engine
import common_model_lib

# train
dataset = 'data/drug200.csv' # (change according to test)
model = training_engine.get_model(dataset)
common_model_lib.cache(model, 'test')


common_model_lib.parse_model('test.mlmodel')