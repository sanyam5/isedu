import pickle
import json

data_dict = pickle.load(open("outputs/data_dict.pickle"))

for number in data_dict:
    print "doing ", number
    for attr in ['text', 'title']:
        data_dict[number][attr] = ''.join([i if ord(i) < 128 else ' ' for i in data_dict[number][attr]])
        data_dict[number][attr] = ' '.join(data_dict[number][attr].split())

json.dump(data_dict, open("outputs/data.json", "wb"))
