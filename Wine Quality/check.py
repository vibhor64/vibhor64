from joblib import dump, load
import numpy as np
model = load('wine.joblib') 
features = np.array([[5.9, 0.645, 0.12, 2, 0.075, 32, 44, 0.99547, 3.57, 0.71, 10.2
]])
a = model.predict(features)
print(a)