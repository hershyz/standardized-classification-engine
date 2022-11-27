import common_model_lib
import prediction_engine

model = common_model_lib.parse_model('drug200.mlmodel')
point = '23,F,HIGH,HIGH,25.355'.split(',')

'''
input features:
point[0] = age
point[1] = sex
point[2] = bp
point[3] = cholesterol
point[4] = na_to_k (ratio)
real output: DrugY
'''
point = ['23', 'F', 'HIGH', 'HIGH', '25.355']
print(prediction_engine.predict(point, model))