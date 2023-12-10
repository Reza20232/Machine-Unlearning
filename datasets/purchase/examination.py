import os
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from scipy.sparse import load_npz

data1 = load_npz('data1.npz').toarray()
data2 = load_npz('data2.npz').toarray()
print(len(data1))
print(len(data2))
