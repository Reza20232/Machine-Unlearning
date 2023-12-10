'load the required libraries for work to work with arrays in python and with system files
import numpy as np
import os

'load the prepared test and train data files to implement different splitting method on it
pwd = os.path.dirname(os.path.realpath(__file__))

train_data = np.load(os.path.join(pwd, 'purchase2_train.npy'), allow_pickle=True)
test_data = np.load(os.path.join(pwd, 'purchase2_test.npy'), allow_pickle=True)

'here we reduce the dimensionality of the data by reshaping it
train_data = train_data.reshape((1,))[0]
test_data = test_data.reshape((1,))[0]

'here we transform the data in to the required formats
'so the shapes were transformed into digital information in float32 format
'and the classes were presented as numbers of each class in int64 format
X_train = train_data['X'].astype(np.float32)
X_test = test_data['X'].astype(np.float32)
y_train = train_data['y'].astype(np.int64)
y_test = test_data['y'].astype(np.int64)

'here we test the class of the data we have
if not isinstance(X_train, np.ndarray):
    raise TypeError("X_train must be a NumPy array")

if not isinstance(X_test, np.ndarray):
    raise TypeError("X_test must be a NumPy array")

'here is the function we use to load the data with only required indices from the arrays
'to filter this data from other modules of framework.
def load(indices, category='train'):
    if category == 'train':
        return X_train[indices], y_train[indices]
    elif category == 'test':
        return X_test[indices], y_test[indices]

