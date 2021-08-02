


import pandas as pd


# In[2]:


wine = pd.read_csv("winequality-red.csv")


# In[3]:


# wine.head()


# # In[4]:


# wine.info()


# # In[5]:


# wine['alcohol'].value_counts()


# # In[6]:


# wine['quality'].value_counts()


# # In[7]:


# wine.describe()


# In[8]:


# import matplotlib.pyplot as plt
# wine.hist(bins=50, figsize=(20, 15))


# ## Train Test Splitting

# In[9]:


from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(wine, test_size = 0.2, random_state = 42)
# print(len(train_set))
# print(len(test_set))


# In[10]:


from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size = 0.2, random_state = 42)
for train_index, test_index in split.split(wine, wine['quality']):
    strat_train_set = wine.loc[train_index]
    strat_test_set = wine.loc[test_index]


# In[11]:


# strat_test_set['quality'].value_counts()


# # In[12]:


# strat_train_set['quality'].value_counts()


# In[13]:


wine = strat_train_set.copy()


# ## Correlations

# In[14]:


corr_matrix = wine.corr()
corr_matrix['quality'].sort_values(ascending=False)


# In[15]:


# from pandas.plotting import scatter_matrix
# attributes = ["quality", "alcohol", "volatile acidity", "residual sugar"]
# scatter_matrix(wine[attributes], figsize = (12,8))


# In[16]:


# wine.plot(kind="scatter", x="alcohol", y="quality", alpha=0.8)


# In[17]:


wine = strat_train_set.drop("quality", axis=1)
wine_labels = strat_train_set["quality"].copy()


# ## Pipeline

# In[18]:


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
my_pipeline = Pipeline([
    ('std_scaler', StandardScaler()),
])


# In[19]:


wine_num_tr = my_pipeline.fit_transform(wine)


# In[20]:


wine_num_tr.shape


# ## Selecting a model

# In[21]:


from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor


# In[22]:


# pipelines = []
# pipelines.append(('ScaledLR', Pipeline([('Scaler', StandardScaler()),('LR',LinearRegression())])))
# pipelines.append(('ScaledLASSO', Pipeline([('Scaler', StandardScaler()),('LASSO', Lasso())])))
# pipelines.append(('ScaledEN', Pipeline([('Scaler', StandardScaler()),('EN', ElasticNet())])))
# pipelines.append(('ScaledKNN', Pipeline([('Scaler', StandardScaler()),('KNN', KNeighborsRegressor())])))
# pipelines.append(('ScaledCART', Pipeline([('Scaler', StandardScaler()),('CART', DecisionTreeRegressor())])))
# pipelines.append(('ScaledGBM', Pipeline([('Scaler', StandardScaler()),('GBM', GradientBoostingRegressor())])))
# pipelines.append(('ScaledRDF', Pipeline([('Scaler', StandardScaler()),('RDF', RandomForestRegressor())])))

# results = []
# names = []
# for name, model in pipelines:
#     kfold = KFold(n_splits=10)
#     cv_results = cross_val_score(model, wine_num_tr, wine_labels, scoring="neg_mean_squared_error", cv=10)
#     results.append(cv_results)
#     names.append(name)
#     msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
#     print(msg)


# In[23]:


model = RandomForestRegressor()
# model = GradientBoostingRegressor()
model.fit(wine_num_tr, wine_labels)


# ## Evaluation

# In[24]:


from sklearn.metrics import mean_squared_error
import numpy as np
wine_predictions = model.predict(wine_num_tr)
mse = mean_squared_error(wine_labels, wine_predictions)
rmse = np.sqrt(mse)


# In[25]:


# rmse


# ## Cross Validation Evaluation

# In[26]:


from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, wine_num_tr, wine_labels, scoring="neg_mean_squared_error", cv=10)
rmse_scores = np.sqrt(-scores)
# rmse_scores


# In[27]:


def print_scores(scores):
    print("Scores:", scores)
    print("Mean: ", scores.mean())
    print("Standard deviation: ", scores.std())


# In[28]:


print_scores(rmse_scores)


# In[29]:


from joblib import dump, load
dump(model, 'Wine.joblib') 


# ## Test On Data

# In[30]:


X_test = strat_test_set.drop("quality", axis=1)
Y_test = strat_test_set["quality"].copy()
X_test_prepared = my_pipeline.transform(X_test)
final_predictions = model.predict(X_test_prepared)
final_mse = mean_squared_error(Y_test, final_predictions)
final_rmse = np.sqrt(final_mse)
print(final_predictions, list(Y_test))


# In[31]:


final_rmse


# ## Using the model

# In[32]:


# from joblib import dump, load
# import numpy as np
# model = load('wine.joblib') 
# features = np.array([[5.9, 0.645, 0.12, 2, 0.075, 32, 44, 0.99547, 3.57, 0.71, 10.2
# ]])
# model.predict(features)


# In[ ]:




