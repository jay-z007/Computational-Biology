import pandas as pd
import numpy as np
import cPickle as pkl
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import easydict
import utilities
import sys
import os
import gc
import random

def main():
	model_file = sys.argv[1]
	test_data_root = sys.argv[2]
	test_label_root = sys.argv[3]
	# print "model", model_file
	# print "test_root", test_root
	# print "test_labels", test_labels

	## Load the config file (if necessary)
	_cfg = utilities.load_cfg_from_file('cfg_file.yml')
	# print _cfg	

	## Load all the data
	## and convert the data to a unified Dict of eq classes
	print "Loading data .."
	print "Creating unified set of equivalence classes .."
	all_eq_classes, master_set = utilities.create_master_set(test_data_root)

	print "Master set created .."
	print ""


	## Reindex the keys
	print "Reindexing the equivalence class keys .."
	all_eq_classes = utilities.reindex(test_data_root, master_set, all_eq_classes, _cfg.eq_classes_root, save_files=False)
	
	print "Reindexing Complete .."
	print ""


	## Make the Train dataframe
	print "Making the train dataframe .."
	folder_names = utilities.get_folder_names(test_data_root)
	train = pd.DataFrame(np.zeros( (len(folder_names), len(master_set)) ), index=folder_names, dtype='int32')

	for folder in folder_names:
	    acc = all_eq_classes[folder]
	    
	    for classes in acc:
	        train.loc[folder][classes] = acc[classes]

	print "Train dataframe ready .."
	print ""


	## Some recycling
	del master_set
	del all_eq_c
	gc.collect()


	## Read the labels data
	print "Reading test labels .."
	labels = pd.read_csv(test_label_root, index_col=0)
	train = train.merge(labels, left_index=True, right_index=True)

	print "Reading Complete .."
	print ""


	## Use Extra trees classifier and extract important features	
	print "Finding Feature importance for predicting Population .."
	X = train.drop(['population', 'sequencing_center'], axis=1)
	# Y = train[['population', 'sequencing_center']]
	Y = train['population']

	important_indices = feature_importance(X, Y, _cfg.feature_importance_params)
	cutoff = importances[importances > _cfg.importance_threshold].shape[0]

	X_reduced = X.iloc[:, indices[:cutoff]]


	## Loading models from the files
	

	predict(X, Y, _cfg.population_classifier_params)
	

	# ## 


if __name__ == '__main__':
	main()