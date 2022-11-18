import training_engine

# train
dataset = 'data/diabetes_data.csv' # (change according to test)
model = training_engine.get_model(dataset)