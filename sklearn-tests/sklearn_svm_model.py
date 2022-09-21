# init timer
import time
start = time.perf_counter()

# other library imports
import numpy as np
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

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
# label_mapping = {
#     'DrugY': 1,
#     'drugC': 2,
#     'drugX': 3,
#     'drugB': 4,
#     'drugA': 5
# }
# y['Drug'] = y['Drug'].map(label_mapping)
# y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = svm.SVC()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
acc = accuracy_score(y_test, predictions)
print('accuracy: ' + str(acc))

elapsed = time.perf_counter() - start
print('time elapsed: ' + str(elapsed) + ' s')