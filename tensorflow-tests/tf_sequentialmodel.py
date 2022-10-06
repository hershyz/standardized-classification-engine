import pandas as pd
import numpy as np

np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf
import keras.api._v2.keras as keras

drug = pd.read_csv('drug200_tf.csv')
drug_features = drug.copy()
drug_labels = drug_features.pop('Drug')

inputs = {}
for name, column in drug_features.items():
    dtype = column.dtype
    if dtype == object:
        dtype = tf.string
    else:
        dtype = tf.float32
    
    inputs[name] = tf.keras.Input(shape=(1,), name=name, dtype=dtype)

numeric_inputs = {name:input for name,input in inputs.items() if input.dtype==tf.float32}
x = keras.layers.Concatenate()(list(numeric_inputs.values()))
norm = keras.layers.Normalization()
norm.adapt(np.array(drug[numeric_inputs.keys()]))
all_numeric_inputs = norm(x)

preprocessed_inputs = [all_numeric_inputs]

for name, input in inputs.items():
    if input.dtype == tf.float32:
        continue

    lookup = keras.layers.StringLookup(vocabulary=np.unique(drug_features[name]))
    one_hot = keras.layers.CategoryEncoding(num_tokens=lookup.vocabulary_size())

    x = lookup(input)
    x = one_hot(x)
    preprocessed_inputs.append(x)

preprocessed_inputs_cat = keras.layers.Concatenate()(preprocessed_inputs)
drug_preprocessing = tf.keras.Model(inputs, preprocessed_inputs_cat)

drug_features_dict = {name: np.array(value) for name, value in drug_features.items()}
features_dict = {name:values[:1] for name, values in drug_features_dict.items()}
drug_preprocessing(features_dict)

def drug_model(preprocessing_head, inputs):
    body = tf.keras.Sequential([
        keras.layers.Dense(64),
        keras.layers.Dense(1)
    ])

    preprocessed_inputs = preprocessing_head(inputs)
    result = body(preprocessed_inputs)
    model = tf.keras.Model(inputs, result)

    model.compile(loss=tf.losses.BinaryCrossentropy(from_logits=True), optimizer=tf.optimizers.Adam(), metrics=['accuracy'])
    return model

drug_model = drug_model(drug_preprocessing, inputs)
drug_model.fit(x=drug_features_dict, y=drug_labels, epochs=10)
print(drug_model.summary())