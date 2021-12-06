import nltk
import pandas as pd
import numpy

class Correction:
	def __init__(self):
		self.village = pd.read_csv('app/static/csv/vil_list.csv')
		self.district = pd.read_csv('app/static/csv/dis_list.csv')
		self.regencies = pd.read_csv('app/static/csv/reg_list.csv')

	def find_result(self,label,string_kec):
		edit_value = []
		list_data = []

		if label == 'kel':
			list_data = self.village['village']

		elif label == 'kec':
			list_data = self.district['district']

		elif label == 'tempat':
			list_data = self.regencies['regency']

		mistake = string_kec
		for word in list_data:
			ed = nltk.edit_distance(mistake,str(word))
			edit_value.append(ed)

		_min = numpy.partition(edit_value, 3)[:3]
		_min = set(_min)
		_min = list(_min)

		result = []
		for item in _min:
			indices = [i for i, x in enumerate(edit_value) if x == item]
			for item in indices:
				result.append(list_data[item])

		return result

	def correct(self,label,string):
		corrected = []
		print(corrected)
		for item in string.split(' '):
			res = self.find_result(label,str(item))
			if len(res) > 0:
				corrected.append(res[0])

		return " ".join(str(x) for x in corrected)

