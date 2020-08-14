import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.ensemble import ExtraTreesClassifier
import pickle

b_cell_epitope = pd.read_csv('input_bcell.csv')


cols = list(b_cell_epitope.columns)
b_cell_epitope.sort_values(by=cols, inplace=True, ignore_index=True)

b_cell_epitope.drop_duplicates(keep='last', inplace=True, ignore_index=True)

b_cell_epitope['parent_protein_id'] = b_cell_epitope['parent_protein_id'].astype(
    'category')
b_cell_epitope['parent_protein_id'] = b_cell_epitope['parent_protein_id'].cat.codes

b_cell_epitope['protein_seq'] = b_cell_epitope['protein_seq'].astype(
    'category')
b_cell_epitope['protein_seq'] = b_cell_epitope['protein_seq'].cat.codes

b_cell_epitope['peptide_seq'] = b_cell_epitope['peptide_seq'].astype(
    'category')
b_cell_epitope['peptide_seq'] = b_cell_epitope['peptide_seq'].cat.codes


minmax_b_cell_epitope = b_cell_epitope.drop('target', axis=1)
col_name = b_cell_epitope.drop(['target'], axis=1).columns[:]

minmax_scaler = preprocessing.MinMaxScaler()
minmax_b_cell_epitope = minmax_scaler.fit_transform(minmax_b_cell_epitope)
minmax_b_cell_epitope = pd.DataFrame(minmax_b_cell_epitope, columns=col_name)
minmax_b_cell_epitope['target'] = b_cell_epitope['target']

X = minmax_b_cell_epitope.drop('target', axis=1)
y = minmax_b_cell_epitope['target']

strat_shuffledsplit = StratifiedShuffleSplit(
    n_splits=1, test_size=0.2, random_state=5)
for train_index, test_index in strat_shuffledsplit.split(X, y):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X.loc[train_index], X.loc[test_index]
    y_train, y_test = y.loc[train_index], y.loc[test_index]

etc = ExtraTreesClassifier(
    n_estimators=250, criterion='entropy', random_state=5)
etc.fit(X_train, y_train)

extra_tree_pkl_filename = 'extra_tree_classifier.pkl'
# Open the file to save as pkl file
extra_tree_model_pkl = open(extra_tree_pkl_filename, 'wb')
pickle.dump(etc, extra_tree_model_pkl)
# Close the pickle instances
extra_tree_model_pkl.close()
