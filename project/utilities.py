import os
import pandas as pd
import numpy as np
import pickle as pkl
import gc
from easydict import EasyDict as edict


#import pdb; pdb.set_trace()
class fasta(object):
	"""docstring for fasta"""

	def __init__(self, fasta_id, value):
		super(fasta, self).__init__()
		self.fasta_id = fasta_id
		self.value = value
		

# inplement properly
def fasta_read(filename):
	read_data = []

	with open(filename, 'r') as file:
		data = file.read()
	
	data = data.split('>')[1:]

	for line in data:
		words = line.split()
		fasta_id = words[0]
		value = ''.join(words[1:])
		# print value
		read_data.append(fasta(fasta_id, value))
		# read_data.append(value)

	return read_data


def get_folder_names(path):
	list_of_files = {}
	for (dirpath, dirnames, filenames) in os.walk(path):
		return  dirnames
		# if dirpath.count(os.path.sep) >= 1:
		# 	break

def load_cfg_from_file(filename):
	"""Load a config file and merge it into the default options."""
	import yaml

	with open(filename, 'r') as f:
		yaml_cfg = edict(yaml.load(f))

	return yaml_cfg

def get_feature_vector(trans_name='',feature_name='TPM'):
	if feature_name == 'TPM':

		file_name = os.path.join(trans_name, "bias/quant.sf")
		df = pd.read_csv(file_name,sep='\t')
		tpm = df[feature_name]
		return tpm.tolist()
	elif feature_name == 'EQC':
		file_name = os.path.join(trans_name,"bias/aux_info/eq_classes.txt")
		with open(file_name) as file:
			data = file.read()

		data = data.strip().split('\r\n')
		data = data[199326:]
		avg_num_transcripts = 0.0
		avg_reads_mapped = 0.0
		for row in data:
			d = row.split('\t')
			avg_num_transcripts+=int(d[0])
			avg_reads_mapped += int(d[-1])
		avg_num_transcripts/=len(data)
		avg_reads_mapped /= len(data)
		return [avg_num_transcripts,avg_reads_mapped]


def load_train_data(path):
	list_of_files = get_folder_names(path)
	# for i in list_of_files:
	# 	print i

	train_data = pd.read_csv("p1_train.csv")	
	# print train_data
	features = []
	i = 0

	for file in list_of_files:
		print i
		i+= 1
		labels = train_data[train_data['accession']==file][['population','sequencing_center']]
		row = []

		row.append(file)
		row.extend(get_feature_vector(os.path.join(path, file)))
		row.extend(get_feature_vector(os.path.join(path, file),feature_name='EQC'))
		row.extend(labels.values[0])
		features.append(row)

	features = np.array(features)

	print features.shape
	with open("tpm_train_with_eqc.pkl", 'wb') as dump_file:
		pkl.dump(features,  dump_file)

	# print features[:10]

def equi_classes_feature(accession):
	
	feature_vec = []
	for acc in accessions:
		filename = './train/' + acc + '/bias/aux_info/eq_classes.txt' 
		with open(path) as filename:
			eq_classes = filename.read()
		eq_classes = eq_classes.split('\n')
		num_classes = int(eq_classes[1])
		classes_start_index = 199326
		avg_feature = 0
		for i in range(classes_start_index,classes_start_index+num_classes):
			equi_class = eq_classes[i].split(" ")
			avg_feature +=float(equi_class[-1])/equi_class[0]
		
		feature_vec.append(avg_feature/num_classes)

	return np.array(feature_vec)


## TODO : remove the hardcoded path
def create_master_set(path="./train/", path_to_eq_classes="/bias/aux_info/eq_classes.txt"):
	folder_names = utilities.get_folder_names(path)

	master_set = set()
	all_eq_c = {}
	count = 0
	classes_start_index = 199326

	for f in folder_names:
		with open(path + f + path_to_eq_classes) as eq_file:
			eq_c = eq_file.read()

		eq_c = eq_c.strip()
		eq_c = eq_c.split("\n")
		eq_c = eq_c[classes_start_index:]
		
		eq_c = np.array(eq_c)

		acc_folder = {}
		
		try:
			for i in range(len(eq_c)):
				e = eq_c[i].split('\t')
				key = int(''.join(e[:-1]))
				acc_folder[key] = int(e[-1])
				master_set.add(key)

		except Exception as err:
			print err
			print f,i
		
		all_eq_c[f] = acc_folder
		count+=1
		print count
		gc.collect()

	return all_eq_c, master_set

def reindex(path='./train', master_set={}, all_eq_classes={}, eq_classes_root='./eq_classes', save_files=False):

	folder_names = utilities.get_folder_names(path)
	master_set = list(master_set)

	if save_files:
		if not os.path.exists(eq_classes_root):
			os.makedirs(eq_classes_root)

	for count, folder in enumerate(folder_names):
		if count%50 == 0:
			print "Reindexing accession folder ", count+1
		
		for i in range(len(master_set)):
			cur = master_set[i]

			if cur in all_eq_classes[folder]:
				all_eq_classes[folder][i] = all_eq_classes[folder][cur]
				del all_eq_classes[folder][cur]

		if save_files:
			with open(eq_classes_root + folder + '.pkl', 'wb') as out_file:
				pkl.dump(all_eq_classes[folder], out_file)

		gc.collect()

	return all_eq_classes

def feature_importance(X, Y, params):

	# Build a forest and compute the feature importances
	forest = ExtraTreesClassifier(n_estimators=params.n_estimators, n_jobs=params.n_jobs, bootstrap=params.bootstrap, 
									oob_score=params.oob_score, verbose=params.verbose, random_state=params.random_state)

	# using out-of-bag samples for testing generalization accuracy

	forest.fit(X, Y)
	importances = forest.feature_importances_

	indices = np.argsort(importances)[::-1]

	# Print the feature ranking
	print("Feature ranking:")

	for f in range(X.shape[1])[:15]:
		print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

	return indices


def predict(X_test, Y_test, model):
	y_pred = model.predict(X_test)
	print f1_score(y_test, y_pred, average='macro')


if __name__ == "__main__":
	load_train_data('./train')
