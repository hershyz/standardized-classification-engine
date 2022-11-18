import training_engine
import common_model_lib
import prediction_engine

model = common_model_lib.parse_model('test.mlmodel')
point_raw = '130.0,0.005,0.469,0.005,0.004,0.0,0.001,29.0,1.7,0.0,7.8,112.0,65.0,177.0,6.0,1.0,133.0,129.0,133.0,27.0,0.0,1.0'
print(prediction_engine.predict(point_raw.split(','), model))