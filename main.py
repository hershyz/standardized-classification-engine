import training_engine
import common_model_lib

model = training_engine.get_model('data/drug200.csv')
common_model_lib.cache(model, 'drug200')