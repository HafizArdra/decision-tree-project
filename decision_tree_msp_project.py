# -*- coding: utf-8 -*-
"""Decision Tree MSP_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14RsPgD2Ey3e2F8yLtriWPVHEyxlRiUnB
"""

# First Dataset - Drug Dataset
# Dapat di download : https://www.kaggle.com/datasets/pablomgomez21/drugs-a-b-c-x-y-for-decision-trees

from google.colab import files

# Pilih file yang ingin diupload
uploaded = files.upload()

# Pastikan file berhasil diupload
for filename in uploaded.keys():
    print('File berhasil diupload: "{name}" dengan ukuran {length} bytes'.format(
        name=filename, length=len(uploaded[filename])))

# Second Dataset - Credit Risk Dataset
# Dapat di download : https://www.kaggle.com/datasets/laotse/credit-risk-dataset

from google.colab import files

# Pilih file yang ingin diupload
uploaded = files.upload()

# Pastikan file berhasil diupload
for filename in uploaded.keys():
    print('File berhasil diupload: "{name}" dengan ukuran {length} bytes'.format(
        name=filename, length=len(uploaded[filename])))

# Import Library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# importing the classes where DT is implemented
from sklearn.tree import DecisionTreeClassifier as DTC, DecisionTreeRegressor as DTR

# importing Drugs dataset
drugs = pd.read_csv('drug200.csv')
drugs

sns.pairplot(data=drugs, hue='Drug');

# let's see some info about the data
drugs.info()

# let's see the categorical features
drugs.describe(include='O')

# We have some categorical features let's encode them
# we can use one_hot_encodeing
# or we can use label_encoding
# let's chooce label_encoding for this problem
from sklearn.preprocessing import LabelEncoder

# initiating the class
label_enc = LabelEncoder()

# columns that are categorical
cols = drugs.select_dtypes(include='O').columns
# looping on each column in the dataset
for col in cols:
    # Label encoding each column
    drugs[col] = label_enc.fit_transform(drugs[col])

# displaying the data after encoding
drugs

# dividing the data into X, y
# X: the features
# y : the target 🎯
X = drugs.drop(columns='Drug')
y = drugs['Drug']

# let's see our data X, y
display(X.head(3), y.head(3))

# now we need to split the data into train set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=42)

# Building the model
tree_clf0 = DTC()
# Fitting the model
tree_clf0.fit(X_train,y_train)

# let's see the model score (acc) on the training set
tree_clf0.score(X_train, y_train)

# let's see the model score on the test set
tree_clf0.score(X_test, y_test)

# another way of calculating the accuracy
from sklearn.metrics import accuracy_score, classification_report
y_pred = tree_clf0.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
accuracy

# third way using more than one metric
report = classification_report(y_test, y_pred)
print(report)

# visualsing👀 the Decision Tree🌳
from sklearn.tree import plot_tree
plt.figure(figsize=(10, 8), dpi=200)
plot_tree(tree_clf0, feature_names=drugs.columns, filled=True);
# Optinal parameters
# feature_names=drugs.columns, filled=True
# filled=True  colors

# reading the dataset
risk = pd.read_csv('credit_risk_dataset.csv')
risk.head(4)

# data size
risk.shape

# some info
risk.info()

# describing the dataset
risk.describe()

# describing the dataset object features
risk.describe(include='O')

risk.isnull().sum()

# dealing with the messing data
'''
person_emp_length              895  /32581
loan_int_rate                 3116  /32581
'''
# we need to understand more about these features
sns.pairplot(data=risk, hue='loan_status')

sns.pairplot(data=risk[['person_emp_length', 'loan_int_rate', 'loan_status']], hue='loan_status')

# let's see the correlation
correlation = risk.corr()
plt.figure(figsize=(10,7))
corr_map = sns.heatmap(correlation, annot=True, cmap="Spectral")

mask_up = np.triu(np.ones_like(correlation, dtype=bool))
plt.figure(figsize=(10,7))
sns.heatmap(correlation, cmap='Spectral', mask=mask_up, annot=True)
'''
np.ones_like(correlation, dtype=bool) creates a boolean matrix of the same shape as correlation.
It sets all elements to True initially because we're going to use this as a mask.

np.triu(...) stands for "upper triangle" and is a NumPy function that zeros out (sets to False) all
the elements below the main diagonal of the matrix. In other words, it keeps only the upper triangle intact.

1 2 3
4 5 6
7 8 9

Applying np.triu(...) would give you:

1 2 3
0 5 6
0 0 9
'''

# dealing with the messing data
'''
person_emp_length              895  /32581
loan_int_rate                 3116  /32581
'''
risk.person_emp_length.value_counts()

# The Question here "Which to use Mean or Median"?
# Create a histogram using Seaborn
# main code
plt.figure(figsize=(12, 6))
sns.histplot(risk['person_emp_length'].dropna(), bins=20, kde=True)
# --------------------end of the important code -----------------#

# Calculate mean and median
mean_value = risk['person_emp_length'].mean()
median_value = risk['person_emp_length'].median()

# plt.figure(figsize=(10, 7))
# Add vertical lines for mean and median
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label='Mean')
plt.axvline(median_value, color='green', linestyle='dashed', linewidth=2, label='Median')

# Add labels and legend
plt.xlabel('person_emp_length')
plt.ylabel('Frequency')
plt.legend()
# it won't make a difference in this case
# use median if the data  skewed or contains outliers,
# The median is less sensitive to extreme values (outliers) than the mean.
# Choose the mean if the distribution is approximately symmetric

# filing using the median
risk['person_emp_length'].fillna(risk['person_emp_length'].median(), inplace=True)

# checking
risk.isnull().sum()

# loan interset rate
plt.figure(figsize=(12, 6))
sns.histplot(risk['loan_int_rate'].dropna(), bins=20, kde=True)

# ploting the mean and median
mean, median = risk['loan_int_rate'].mean(), risk['loan_int_rate'].median()

plt.axvline(mean, color='red')
plt.axvline(median, color ='green')

print(mean, median)
# almost the same

# filling with the mean
risk['loan_int_rate'].fillna(risk['loan_int_rate'].mean(), inplace=True)

risk.isnull().sum()
# perfect ✅

# now let's encode the data
# What columns need encoding
risk.select_dtypes(include='O').info()

cols = risk.select_dtypes(include='O').columns
cols

for col in cols:
    print("="*50, col)
    print(risk[col].value_counts())

# let's label encode this features
lenc = LabelEncoder()

# loop over each column with the type 'object' => string
for col in cols:
    # fit_transform
    risk[col] = lenc.fit_transform(risk[col])

# displaying
risk

risk.info()

# 🌳 very intersting thing about the tree it doesn't need scaling the data
# the alogrithms that need sclaing mostly depend on distance or using variance
# but here the true work based on the purity of a node
# that is why also I prefered to use label encoding
# it's perfect with using classes and sepreating them
# and OneHotEncoding make more columns which mean larger trees🌴🌴
# Let's Split the data to => X features (input for the model) , y the target (output)
X = risk.drop(columns='loan_status')
y = risk['loan_status']

# Spliting the data into train and test data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)

# let's fit the tree
tree_clf1 = DTC()

# fitting the model
tree_clf1.fit(X_train, y_train)

plt.figure(figsize=(15, 9))
plot_tree(tree_clf1, feature_names=risk.columns, filled=True);

# depth of the tree
tree_clf1.get_depth()

# n of leaves
tree_clf1.get_n_leaves()

# features ✨
features = tree_clf1.feature_names_in_
features

# features importance ✨
importance = tree_clf1.feature_importances_
importance

plt.figure(figsize=(10,7))
plt.bar(features, importance)
plt.title('Feature Importance')
plt.xticks(rotation=90);

# parameter of the model
tree_clf1.get_params()

# getting the score✨
print(f"Training accuracy : {tree_clf1.score(X_train, y_train)}")
print(f"Test accuracy {tree_clf1.score(X_test, y_test)}")

# train the decision tree model with post-pruning
path = tree_clf1.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas = path.ccp_alphas
models = []
for i, ccp_alpha in enumerate(ccp_alphas):
    model = DTC(random_state=42, ccp_alpha=ccp_alpha)
    model.fit(X_train, y_train)
    print(f"Accuracy with pruning #{i+1}:", model.score(X_test, y_test))
    models.append(model)

# visualize the pruned decision tree
max_models = len(models)
choosen_models = [m for m in choosen_models if m < max_models]
for m in choosen_models:
    plt.figure(figsize=(30, 5))
    print(f"Model {m}")
    plot_tree(models[m], filled=True)
    plt.show()

# this model is overfitting
# doing well on the train (memorizing things not learning)
# to solve this problem we have to make the model more simplier
# by cuting or limiting the size of the tree🌳
# Pruning (post, pre)
path = tree_clf1.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities
fig, ax = plt.subplots()
ax.plot(ccp_alphas[:-1], impurities[:-1], marker="o", drawstyle="steps-post")
ax.set_xlabel("effective alpha")
ax.set_ylabel("total impurity of leaves")
ax.set_title("Total Impurity vs effective alpha for training set")

# train_scores = [clf.score(X_train, y_train) for clf in models]
# test_scores = [clf.score(X_test, y_test) for clf in models]

# fig, ax = plt.subplots()
# ax.set_xlabel("alpha")
# ax.set_ylabel("accuracy")
# ax.set_title("Accuracy vs alpha for training and testing sets")
# ax.plot(ccp_alphas, train_scores, marker="o", label="train", drawstyle="steps-post")
# ax.plot(ccp_alphas, test_scores, marker="o", label="test", drawstyle="steps-post")
# ax.legend()
# plt.show()

# let's build our fincal model
# you can try diferent values to cpp_alpha
# try 0.0001
# try 0.1 and other values as you like
tree_clf2 = DTC(ccp_alpha=0.001)

# fitting the model
tree_clf2.fit(X_train, y_train)

# train acc, test acc
tree_clf2.score(X_train, y_train), tree_clf2.score(X_test, y_test)

# ploting the tree
# train , test
# (0.9208980092957993, 0.9176470588235294)
plt.figure(figsize=(15, 7), dpi=250)
plot_tree(tree_clf2, feature_names=risk.columns, filled=True);

# using cross validation
from sklearn.model_selection import cross_val_score

# Perform 5-fold cross-validation (you can change the number of folds as needed)
cv_scores = cross_val_score(tree_clf1, X_train, y_train, cv=5)


# Print the cross-validation scores
print("Cross-Validation Scores:", cv_scores)
print("Mean CV Score:", cv_scores.mean())

# Perform 5-fold cross-validation (you can change the number of folds as needed)
cv_scores = cross_val_score(tree_clf2, X_train, y_train, cv=5)

# Print the cross-validation scores
print("Cross-Validation Scores:", cv_scores)
print("Mean CV Score:", cv_scores.mean())

tree_clf3 = DTC(max_depth=10)
# fiting the tree
tree_clf3.fit(X_train, y_train)
# cross val score
cv_scores = cross_val_score(tree_clf3, X_train, y_train, cv=5)

# Print the cross-validation scores
print("Cross-Validation Scores:", cv_scores)
print("Mean CV Score:", cv_scores.mean())

# test score
print("Test Score", tree_clf3.score(X_test, y_test))

# accuracy report
y_pred = tree_clf3.predict(X_test)
print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(y_test, y_pred)


plt.figure(figsize=(8, 6))
sns.set(font_scale=1.2)  # Adjust the font size as needed
sns.heatmap(conf_matrix, annot=True, fmt="d", linewidths=0.5, cbar=False, cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

from sklearn.model_selection import GridSearchCV

tree_clf4 = DTC()

param_grid = {
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
}

grid_search = GridSearchCV(tree_clf4, param_grid, cv=5, scoring='accuracy', n_jobs=-1)

grid_search.fit(X_train, y_train)

grid_search.best_params_

best_tree = grid_search.best_estimator_

best_tree

print(f"train score {best_tree.score(X_train, y_train)}")
print(f"test score {best_tree.score(X_test, y_test)}")

pd.DataFrame(grid_search.cv_results_).sample(5)