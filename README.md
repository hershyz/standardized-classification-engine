<p align="center">
  <img src="https://raw.githubusercontent.com/hershyz/standardized-classification-engine/main/images/logo.png" width=600px>
</p>

<h4>Overview</h4>
<p>
  Lightweight, standardized classification engine for general machine learning tasks.<br>
  (GSMST Senior Capstone Maker Project)
</p>

<h4>Purpose</h4>
<p>
  The end goal of this project is to create an all encompassing ML algorithm that automatically finds the best classification method for an individual dataset, serving as a standalone module for instantaneous predictions and lightweight model retraining, having lower runtimes and resource utilization than existing frameworks (TensorFlow, PyTorch, SKLearn), while maintaining similar levels of classification accuracy.<br>
  Such a system eliminates the need for human trial and error when choosing a classification technique, allowing for an automatic classification algorithm switch as a dataset grows through the use of a standardized model.<br>
  Finally, this system removes the overhead of large inferencing frameworks, making for faster classifications and model training times without the need for GPU acceleration.
</p>

<h4>Dependencies for tests (pip)</h4>
<pre>
numpy
pandas
sklearn
tensorflow
keras
</pre>

<h4>Model Metadata</h4>
<pre>
mean per input feature, parameterized by output feature
int/float mapping (label serialization) for non-numerical input features
standard deviation per input feature
sampled raw data, for knn classifications
max accuracy classification algorithm
</pre>

<h4>Standardized Classification Algorithms</h4>
<pre>
sqrt distance classifier
absolute distance classifier
percent distance classifier
standard deviation distance classifier
knn (k-nearest neighbors) classifier
</pre>

<h4>Package Modules</h4>
<pre>
abs_distance_classifier
percent_distance_classifier
sqrt_distance_classifier
stddev_classifier
common_model_lib
knn
data_sampler
dataframe
model
numerical_feature_converter
prediction_engine
training_engine
</pre>

<h4>Train and cache model</h4>
<pre>
import training_engine
import common_model_lib

model = training_engine.get_model('data/drug200.csv')
common_model_lib.cache(model, 'drug200')
</pre>
<pre>
(terminal output)
sqrt distance classifier accuracy: 0.38
abs distance classifier accuracy: 0.44
percent distance classifier accuracy: 0.615
stddev classifier accuracy: 0.64
knn accuracy: 0.94
---
training complete: 0.04366495800059056s elapsed
max training accuracy: knn (0.94)
</pre>

<h4>Parse a cached model and predict</h4>
<pre>
import common_model_lib
import prediction_engine

model = common_model_lib.parse_model('drug200.mlmodel')

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
</pre>
<pre>
(terminal output)
DrugY
</pre>