import os
import pandas as pd
import numpy as np
import pickle as pkl

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


def get_feature_vector(trans_name='',feature_name='TPM'):
    file_name = os.path.join(trans_name, "bias/quant.sf")
    df = pd.read_csv(file_name,sep='\t')
    tpm = df[feature_name]
    return tpm.tolist()


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
		row.extend(labels.values[0])
		features.append(row)

	features = np.array(features)

	print features.shape
	with open("tpm_train.pkl", 'wb') as dump_file:
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


if __name__ == "__main__":
	load_train_data('./train')
