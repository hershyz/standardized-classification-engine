# init timer
import time
start = time.perf_counter()

# other library imports
import numpy as np
import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

csv_path = 'C:/Users/bagal/OneDrive/Desktop/src/standardized-classification-engine/data/drug200.csv'
data = pd.read_csv(csv_path)

# set all input features as X
X = data[[
    'Age',
    'Sex',
    'BP',
    'Cholesterol',
    'Na_to_K'
]].values

# set output as Y
y = data[['Drug']]

# convert features to numerical
Le = LabelEncoder()
for i in range(len(X[0])):
    X[:, i] = Le.fit_transform(X[:, i])

# label mapping Y
label_mapping = {
    'DrugY': 1,
    'drugC': 2,
    'drugX': 3,
    'drugB': 4,
    'drugA': 5
}
y['Drug'] = y['Drug'].map(label_mapping)
y = np.array(y)

# create model
knn = neighbors.KNeighborsClassifier(n_neighbors=10, weights='uniform')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
knn.fit(X_train, y_train)

# make predictions
predictions = knn.predict(X_test)
accuracy = metrics.accuracy_score(y_test, predictions)
print('accuracy: ' + str(accuracy))
elapsed = time.perf_counter() - start
print('time elapsed: ' + str(elapsed) + ' s')