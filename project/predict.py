import pandas as pd
import numpy as np
import cPickle as pkl
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.preprocessing import MultiLabelBinarizer
# from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import easydict
import utilities
from utilities import predict
import sys
import os
import gc
import random
import pdb; pdb.set_trace()
def main():
	model_file = sys.argv[1]
	test_data_root = sys.argv[2]
	test_label_root = sys.argv[3]

	## Load the config file (if necessary)
	_cfg = utilities.load_cfg_from_file('cfg_file.yml')
	# print _cfg	

	## Load all the data
	## and convert the data to a unified Dict of eq classes
	print "Loading data .."
	print "Creating unified set of equivalence classes .."
	all_eq_classes = utilities.create_master_set(test_data_root)

	print "All equivalence classes created .."
	print ""



	# ## Make the Train dataframe
	print "Making the train dataframe with best features for multi-task prediction .."
	folder_names = utilities.get_folder_names(test_data_root)
	with open(_cfg.multi_features) as f:
		multi_features = pkl.load(f)
	train = pd.DataFrame(np.zeros( (len(folder_names), _cfg.cutoff) ), index=folder_names,columns=multi_features)

	# count =1
	for feature in multi_features:
		# print count
		# count+=1
		for folder in folder_names:
			if int(feature) in all_eq_classes[folder]:
				train.loc[folder,feature] = all_eq_classes[folder][int(feature)]
			

	# for folder in folder_names:
	#     acc = all_eq_classes[folder]
	    
	#     classes = pd.Series(acc)
	#     train.loc[folder] = classes

	train.fillna(0, inplace=True)
	# train = train.astype('int16')

	print "Train dataframe ready .."
	print ""


	# ## Some recycling
	# # del master_set
	# # del all_eq_c
	# # gc.collect()


	# ## Read the labels data
	print "Reading test labels .."
	labels = pd.read_csv(test_label_root, index_col=0)
	train = train.merge(labels, left_index=True, right_index=True)

	print "Reading Complete .."
	print ""


	## Load the models
	with open(model_file) as f:
		model = pkl.load(f)
	
	with open(_cfg.all_scalers) as f:
		scalers = pkl.load(f)	

	X = train.drop(['population', 'sequencing_center'], axis=1)
	Y = train[['population', 'sequencing_center']]
	with open(_cfg.binarizer) as f:
		mlb = pkl.load(f)
	y = mlb.transform(Y.as_matrix())
	Y = pd.DataFrame(y)
	# X = scalers['multi_scaler'].transform(X)
	# ## Loading models from the files
	predict(X, Y, model['joint_model'])


	del X
	del Y
	del y
	del train
	gc.collect()





	## Make the Train dataframe
	print "Making the train dataframe with best features for population prediction .."
	# folder_names = utilities.get_folder_names(test_data_root)
	with open(_cfg.pop_features) as f:
		pop_features = pkl.load(f)
	train = pd.DataFrame(np.zeros( (len(folder_names), _cfg.cutoff) ), index=folder_names,columns=pop_features)

	for feature in pop_features:
		for folder in folder_names:
			if int(feature) in all_eq_classes[folder]:
				train.loc[folder,feature] = all_eq_classes[folder][int(feature)]

	train.fillna(0, inplace=True)
	train = train.astype('int16')
	train = train.merge(labels, left_index=True, right_index=True)
	print "Train dataframe ready .."
	print ""


	X = train.drop(['population', 'sequencing_center'], axis=1)
	Y = train['population']
	# X = scalers['pop_scaler'].transform(X)
	# mlb = MultiLabelBinarizer()
	# y = mlb.fit_transform(Y.as_matrix())
	# Y = pd.DataFrame(y)
	## Loading models from the files
	predict(X, Y, model['population'])
	

	del X
	del Y
	del train
	gc.collect()

	

	## Make the Train dataframe
	print "Making the train dataframe with best features for sequencing center prediction .."
	# folder_names = utilities.get_folder_names(test_data_root)
	with open(_cfg.seq_features) as f:
		seq_features = pkl.load(f)
	train = pd.DataFrame(np.zeros( (len(folder_names), _cfg.cutoff) ), index=folder_names,columns=seq_features)

	for feature in seq_features:
		for folder in folder_names:
			if int(feature) in all_eq_classes[folder]:
				train.loc[folder,feature] = all_eq_classes[folder][int(feature)]

	train.fillna(0, inplace=True)
	train = train.astype('int16')
	train = train.merge(labels, left_index=True, right_index=True)
	print "Train dataframe ready .."
	print ""


	X = train.drop(['population', 'sequencing_center'], axis=1)
	Y = train['sequencing_center']
	# X = scalers['seq_scaler'].transform(X)
	## Loading models from the files
	predict(X, Y, model['sequencing_center'])

	## Use Extra trees classifier and extract important features	
	# print "Finding Feature importance for predicting BOTH Sequencing Center and Population .."
	# X = train.drop(['population', 'sequencing_center'], axis=1)
	# # Y = train[['population', 'sequencing_center']]
	# Y = train[['population', 'sequencing_center']]

	# important_indices = feature_importance(X, Y, _cfg.feature_importance_params)
	# cutoff = importances[importances > _cfg.importance_threshold].shape[0]

	# X_reduced = X.iloc[:, indices[:cutoff]]

	# ## Loading models from the files
	# predict(X, Y, model['joint_model'])


	# ## 


if __name__ == '__main__':
	main()