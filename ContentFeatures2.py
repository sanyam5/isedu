import Utilities
import numpy as np
import json
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from collections import defaultdict
import math


def get_user_features():
    user_features = {}
    with open('annotation_data.json') as data_file:
        user_features = json.load(data_file)
    return user_features


def get_html_data():
    with open('data.json') as data_file:
        html_data = json.load(data_file)
    return html_data


def removeunwanted(string):
    string = string.lower()
    if string == "":
        return ""
    stop_words = []
    stop_words = set(stopwords.words('english'))
    # stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    list_of_words = [i.lower() for i in wordpunct_tokenize(string) if i.lower() not in stop_words]
    final = "" + list_of_words[0]
    for i in range(1, len(list_of_words)):
        final += " " + list_of_words[i]
    return final


def get_html_features(html_data, user_features):
    X = []
    Y = []
    z = []
    for key, val in html_data.iteritems():
        if key not in ["142", "200", "986", "321", "259", "305", "807", ] and user_features.has_key(key):
            # print val,key
            # break
            X.append(removeunwanted(val["text"]))
            y_array = np.asarray(user_features[key]).astype(int)
            # print y_array
            # break
            Y.append(y_array[1:-3].tolist())
            z.append(y_array[-1].tolist())
    return X, Y, z


def write_vocab_json(X):
    dic = {}
    k1 = 0
    for string in X:
        k1 = max(k1,len(string.split()))
        # break
        for word in string.split():
            dic[word] = 1
    vocab_list = []
    for key, val in dic.iteritems():
        vocab_list.append(key)
    print len(vocab_list), " no. of words in vocab."
    with open('vocab_list.json', 'w') as fp:
        json.dump(vocab_list, fp)
    print "stored"


def get_vocab():
    vocab = []
    with open('vocab_list.json', 'r') as data_file:
        vocab = json.load(data_file)import Utilities
import numpy as np
import json
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from collections import defaultdict
import math

def get_user_features():
    user_features = {}
    with open('annotation_data.json') as data_file:
        user_features = json.load(data_file)
    return user_features


def get_html_data():
    with open('data.json') as data_file:
        html_data = json.load(data_file)
    return html_data


def removeunwanted(string):
    string = string.lower()
    if string == "":
        return ""
    stop_words = []
    stop_words = set(stopwords.words('english'))
    # stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    list_of_words = [i.lower() for i in wordpunct_tokenize(string) if i.lower() not in stop_words]
    final = "" + list_of_words[0]
    for i in range(1, len(list_of_words)):
        final += " " + list_of_words[i]
    return final


def get_html_features(html_data, user_features):
    X = []
    Y = []
    z = []
    for key, val in html_data.iteritems():
        if key not in ["142", "200", "986", "321", "259", "305", "807", ] and user_features.has_key(key):
            # print val,key
            # break
            X.append(removeunwanted(val["text"]))
            y_array = np.asarray(user_features[key]).astype(int)
            # print y_array
            # break
            Y.append(y_array[1:-3].tolist())
            z.append(y_array[-1].tolist())
    return X, Y, z


def write_vocab_json(X):
    dic = {}
    k1 = 0
    for string in X:
        k1 = max(k1,len(string.split()))
        # break
        for word in string.split():
            dic[word] = 1
    vocab_list = []
    for key, val in dic.iteritems():
        vocab_list.append(key)
    print len(vocab_list), " no. of words in vocab."
    with open('vocab_list.json', 'w') as fp:
        json.dump(vocab_list, fp)
    print "stored"


def get_vocab():
    vocab = []
    with open('vocab_list.json', 'r') as data_file:
        vocab = json.load(data_file)
    return vocab


def get_features(X, inv_map, size_vocab):
    # print inv_map
    features = np.zeros((len(X), size_vocab))
    N = 0.0+len(X)
    invdoc = {}
    for i in range(len(X)):
        mark = {}
        for w in X[i].split():
            if w not in mark:
                mark[w] = 1
                invdoc[w] = invdoc.get(w,0.0)+1.0

    print "hi"

    for i in range(len(X)):
        # kk = 0
        for w in X[i].split():
            # print w
            if w in inv_map:
                # kk += 1
                features[i, inv_map[w]] += (1.0 * math.log(N/invdoc[w]))
            # print kk
            # break
    # print kk
    return features.tolist()


def main():
    html_data = get_html_data()
    user_features = get_user_features()
    X, Y, z = get_html_features(html_data, user_features)
    # print X.keys()
    write_vocab_json(X)
    vocab = get_vocab()
    inv_map = defaultdict()
    # print vocab
    for i in range(len(vocab)):
        inv_map[vocab[i]] = i
    # print inv_map
    X = get_features(X, inv_map, len(vocab))
    json.dump(X,open('X.json','wb'))
    json.dump(z,open('y.json','wb'))
    json.dump(Y,open('X_manual.json','wb'))

if __name__ == '__main__':
    main()

    return vocab


def get_features2(X, inv_map, size_vocab, vocab):
    # print inv_map
    invdoc = dict()
    features = np.zeros((len(X), size_vocab))
    for key in vocab:
        print key
        c = 0.0    
        for x in X:
            u = x.split()
            if key in u:
                c+=1.0
        invdoc[key] = math.log(len(X)/c)

    for i in range(len(X)):
        # kk = 0
        for w in X[i].split():
            # print w
            if w in inv_map:
                # kk += 1
                features[i, inv_map[w]] += (1.0*invdoc[w])
            # print kk
            # break
    return features.tolist()


def main():
    html_data = get_html_data()
    user_features = get_user_features()
    X, Y, z = get_html_features(html_data, user_features)
    # print X.keys()
    write_vocab_json(X)
    vocab = get_vocab()
    inv_map = defaultdict()
    print vocab
    for i in range(len(vocab)):
        inv_map[vocab[i]] = i
    print inv_map
    X = get_features2(X, inv_map, len(vocab),vocab)

    json.dump(X,open('X.json','wb'))
    json.dump(z,open('y.json','wb'))
    json.dump(Y,open('X_manual.json','wb'))

if __name__ == '__main__':
    main()