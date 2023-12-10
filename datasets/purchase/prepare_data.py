'import modules for work with files in ubuntu, load data for work and from zip files , and learn data and 
'module/library for work with files
import os
'module for work with loaded data containers
import numpy as np
'modules to learn data
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
'load data from zip file npz
from scipy.sparse import load_npz 

'here we read the data available. The data consist from shapes and each from these shapes has 600 dimensions
data = np.concatenate([load_npz('data1.npz').toarray(), load_npz('data2.npz').toarray()]).astype(int)

'here we setup the complexity of learning eg count of classes we predict from the data
num_class = 2

'here we add the results of learning to the main data
if not os.path.exists(f'{num_class}_kmeans.npy'):
    kmeans = KMeans(n_clusters=num_class, random_state=0, n_init=10).fit(data)
    label = kmeans.labels_
    np.save(f'{num_class}_kmeans.npy', label)
else:
    label = np.load(f'{num_class}_kmeans.npy')

'here we create tran and test samples based on the learn data. 
if not os.path.exists(f'purchase{num_class}_train.npy'):
    X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.2)
    np.save(f'purchase{num_class}_train.npy', {'X': X_train, 'y': y_train})
    np.save(f'purchase{num_class}_test.npy', {'X': X_test, 'y': y_test})
