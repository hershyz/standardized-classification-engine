import training_engine
import common_model_lib
import prediction_engine

model = common_model_lib.parse_model('test.mlmodel')
point = '33,3.0,18.0,2.0,?,?,?,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,?,?,0,129,0,0,1,1,1,1'
print(prediction_engine.predict(point.split(','), model))