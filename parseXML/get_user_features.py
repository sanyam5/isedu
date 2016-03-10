import xml.etree.ElementTree as ET
import json

# returns dictionary of key,val
# key is docID
# val is array of user features, order of features/columns specified in annotation_desc.txt
def get_user_features():
	tree = ET.parse('Annotation.xml')
	root = tree.getroot()
	data = {}
	for child in root:
		temp_arr = []
		now = False
		DocID = ""
		new_ele = True
		for child_of_child in child:
			if child_of_child.tag == "DocID":
				now = True
				DocID = child_of_child.text
				if data.has_key(child_of_child.text):
					new_ele = False
			elif now and (child_of_child.tag != "SearchQuery"):
				temp_arr.append(child_of_child.text)
		if new_ele:
			data[DocID]=[temp_arr]
		else:
			data[DocID].append(temp_arr)
	final_data={}
	for key,val in data.iteritems():
		temp_arr = []
		for i in range(len(val[0])):
			temp_arr2 = []	
			for j in range(3):
				temp_arr2.append(val[j][i])
			max_element = max(set(temp_arr2), key=temp_arr2.count)
			temp_arr.append(max_element)
		final_data[key]=temp_arr
	return final_data

def main():
	data = get_user_features()
	with open('annotation_data.json', 'w') as fp:
		json.dump(data, fp)


if __name__ == '__main__':
	main()