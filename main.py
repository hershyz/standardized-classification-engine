import training_engine
import prediction_engine
import dataframe
import data_sampler

# train
dataset = 'benchmark-data/stars.csv' # (change according to test)
model = training_engine.get_model(dataset)

# test
print('---')
df_raw = dataframe.get_dataframe(dataset)
df_test = data_sampler.sampled_dataframe(df_raw, 0.1) # (change ratio according to test)
correct = 0
for point in df_test:
    expected = point[len(point) - 1]
    prediction = prediction_engine.predict(point, model)
    print(str(point) + ', prediction: ' + prediction)
    if str(prediction) == str(expected):
        correct += 1
print('testing accuracy (' + str(model.algorithm) + '): ' + str(correct / len(df_test)))