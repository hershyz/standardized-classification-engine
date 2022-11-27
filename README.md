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

<h4>Dependencies for Tests (pip)</h4>
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

<h4>Train and Cache Model</h4>
```
import training_engine
import common_model_lib

model = training_engine.get_model('data/drug200.csv')
common_model_lib.cache(model, 'drug200')
```